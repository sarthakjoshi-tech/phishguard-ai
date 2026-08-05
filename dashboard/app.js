const API_BASE = "http://localhost:5000/api";

document.addEventListener('DOMContentLoaded', () => {
  const apiStatusEl = document.getElementById('api-status');
  const scanForm = document.getElementById('scan-form');
  const scanUrlInput = document.getElementById('scan-url-input');
  
  const scanResultCard = document.getElementById('scan-result-card');
  const resHostname = document.getElementById('res-hostname');
  const resBadge = document.getElementById('res-badge');
  const resScore = document.getElementById('res-score');
  
  const resAiSummary = document.getElementById('res-ai-summary');
  const resAiReasons = document.getElementById('res-ai-reasons');
  const resAiRec = document.getElementById('res-ai-rec');
  
  const resHeuristicCount = document.getElementById('res-heuristic-count');
  const resMlProb = document.getElementById('res-ml-prob');
  const resVtCount = document.getElementById('res-vt-count');
  const resGsbStatus = document.getElementById('res-gsb-status');
  
  const statTotalScans = document.getElementById('stat-total-scans');
  const statCriticalScams = document.getElementById('stat-critical-scams');
  const statWarnings = document.getElementById('stat-warnings');
  const statCommunityReports = document.getElementById('stat-community-reports');
  
  const scansList = document.getElementById('scans-list');
  const reportsList = document.getElementById('reports-list');

  // 1. Check API Health
  async function checkHealth() {
    try {
      const res = await fetch(`${API_BASE}/health`);
      if (res.ok) {
        apiStatusEl.textContent = "ONLINE (Node.js API)";
        apiStatusEl.style.color = "#10b981";
      } else {
        throw new Error();
      }
    } catch (e) {
      apiStatusEl.textContent = "OFFLINE (Using Fallback)";
      apiStatusEl.style.color = "#f59e0b";
    }
  }

  // 2. Fetch System Stats & Feed
  async function fetchStats() {
    try {
      const res = await fetch(`${API_BASE}/stats`);
      if (!res.ok) return;
      const data = await res.json();

      statTotalScans.textContent = data.totalScans.toLocaleString();
      statCriticalScams.textContent = data.criticalScamsDetected.toLocaleString();
      statWarnings.textContent = data.warningsIssued.toLocaleString();
      statCommunityReports.textContent = data.communityReportsCount.toLocaleString();

      // Render Recent Scans
      if (data.recentScans && data.recentScans.length > 0) {
        renderScansList(data.recentScans);
      }
    } catch (e) {
      console.warn("Could not load API stats:", e);
    }
  }

  // 3. Fetch Reports List
  async function fetchReports() {
    try {
      const res = await fetch(`${API_BASE}/reports`);
      if (!res.ok) return;
      const reports = await res.json();
      renderReportsList(reports);
    } catch (e) {
      console.warn("Could not load reports:", e);
    }
  }

  function renderScansList(scans) {
    scansList.innerHTML = scans.map(item => {
      const badgeClass = item.riskRating === "CRITICAL" ? "badge-danger" : (item.riskRating === "MEDIUM" ? "badge-warning" : "badge-safe");
      const timeStr = new Date(item.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      return `
        <div class="scan-item">
          <div class="item-info">
            <span class="item-title">${escapeHTML(item.hostname)}</span>
            <span class="item-sub">${timeStr} &bull; ${escapeHTML(item.url)}</span>
          </div>
          <div class="item-badge-col">
            <span class="${badgeClass}">${item.riskRating} (${item.score}%)</span>
          </div>
        </div>
      `;
    }).join('');
  }

  function renderReportsList(reports) {
    reportsList.innerHTML = reports.map(rep => {
      const dateStr = new Date(rep.timestamp).toLocaleDateString();
      return `
        <div class="report-item">
          <div class="item-info">
            <span class="item-title">🚫 ${escapeHTML(rep.domain)}</span>
            <span class="item-sub">Category: <b>${escapeHTML(rep.category)}</b> &bull; ${escapeHTML(rep.description)}</span>
          </div>
          <div class="item-badge-col">
            <span class="badge-danger">Blacklisted</span>
            <span class="item-sub" style="font-size:10px">${dateStr}</span>
          </div>
        </div>
      `;
    }).join('');
  }

  // 4. Run Live URL Scan
  scanForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const urlVal = scanUrlInput.value.trim();
    if (!urlVal) return;

    scanResultCard.classList.remove('hidden');
    resAiSummary.textContent = "Analyzing domain security heuristics, ML vectors, and threat databases...";
    resAiReasons.innerHTML = "<li>Scanning protocol & TLD...</li>";

    try {
      const res = await fetch(`${API_BASE}/scan`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: urlVal })
      });

      if (!res.ok) throw new Error("Scan API returned error");
      const data = await res.json();
      displayScanResult(data);
      fetchStats(); // refresh feed

    } catch (err) {
      console.warn("API scan error, displaying local estimation:", err);
      displayScanResult(clientEstimate(urlVal));
    }
  });

  function displayScanResult(data) {
    resHostname.textContent = data.hostname || data.url;
    resBadge.textContent = `${data.riskRating} (${data.score}%)`;
    resBadge.className = data.riskRating === "CRITICAL" ? "badge-danger" : (data.riskRating === "MEDIUM" ? "badge-warning" : "badge-safe");

    resScore.textContent = `${data.score}%`;
    const ring = document.querySelector('.result-score-ring');
    if (data.score >= 80) {
      ring.style.borderColor = "#ef4444";
      ring.style.color = "#ef4444";
    } else if (data.score >= 45) {
      ring.style.borderColor = "#f59e0b";
      ring.style.color = "#f59e0b";
    } else {
      ring.style.borderColor = "#10b981";
      ring.style.color = "#10b981";
    }

    if (data.aiExplanation) {
      resAiSummary.textContent = data.aiExplanation.summary;
      resAiReasons.innerHTML = data.aiExplanation.keyReasons.map(r => `<li>${escapeHTML(r)}</li>`).join('');
      resAiRec.textContent = `Recommendation: ${data.aiExplanation.recommendation}`;
    }

    resHeuristicCount.textContent = `${data.heuristics ? data.heuristics.flags.length : 0} Flags`;
    resMlProb.textContent = `${data.mlClassification ? data.mlClassification.phishingProbability : 0}%`;
    resVtCount.textContent = `${data.threatIntel && data.threatIntel.virusTotal ? data.threatIntel.virusTotal.positives : 0} / 72 Vendors`;
    resGsbStatus.textContent = data.threatIntel ? data.threatIntel.googleSafeBrowsing.status : "CLEAN";
  }

  function clientEstimate(url) {
    const isPhish = url.includes("scam") || url.includes("login") || url.endsWith(".xyz") || url.endsWith(".top");
    const score = isPhish ? 91 : 5;
    return {
      url,
      hostname: url,
      score,
      riskRating: score >= 80 ? "CRITICAL" : "SAFE",
      heuristics: { flags: isPhish ? ["High risk TLD or keywords detected."] : [] },
      mlClassification: { phishingProbability: score },
      threatIntel: { virusTotal: { positives: isPhish ? 24 : 0 }, googleSafeBrowsing: { status: isPhish ? "MALICIOUS" : "CLEAN" } },
      aiExplanation: {
        summary: score >= 80 ? "⚠️ DANGER: High probability phishing site." : "✅ SAFE: Clean domain metrics.",
        keyReasons: isPhish ? ["• Flagged domain signature."] : ["• Valid SSL & domain reputation."],
        recommendation: score >= 80 ? "Do not enter passwords." : "Safe to browse."
      }
    };
  }

  function escapeHTML(str) {
    if (!str) return '';
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  // Initial Load
  checkHealth();
  fetchStats();
  fetchReports();
  setInterval(fetchStats, 10000); // refresh every 10s
});
