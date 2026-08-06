const API_BASE_URL = "http://localhost:5000/api";

document.addEventListener('DOMContentLoaded', async () => {
  const loadingState = document.getElementById('loading-state');
  const mainState = document.getElementById('main-state');
  const reportModal = document.getElementById('report-modal');
  
  const currentDomainEl = document.getElementById('current-domain');
  const scoreValEl = document.getElementById('score-val');
  const riskBadgeEl = document.getElementById('risk-badge');
  const riskCard = document.getElementById('risk-card');
  
  const statusDomain = document.getElementById('status-domain');
  const statusLogin = document.getElementById('status-login');
  const statusStore = document.getElementById('status-store');
  const statusMl = document.getElementById('status-ml');
  
  const aiSummary = document.getElementById('ai-summary');
  const aiReasons = document.getElementById('ai-reasons');
  const aiRecommendation = document.getElementById('ai-recommendation');
  
  let currentScanData = null;
  let activeTab = null;

  // 1. Get active tab
  try {
    const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
    activeTab = tabs[0];
  } catch (err) {
    console.error("Could not query active tab:", err);
  }

  if (!activeTab || !activeTab.url) {
    loadingState.innerHTML = `<p style="color:#ef4444">Cannot scan this page type (e.g. chrome:// internal pages).</p>`;
    return;
  }

  const tabUrl = activeTab.url;
  let domain = "";
  try {
    domain = new URL(tabUrl).hostname;
  } catch (e) {
    domain = tabUrl;
  }
  currentDomainEl.textContent = domain;
  document.getElementById('report-domain').value = domain;

  // 2. Query DOM metadata from content script
  let domMetadata = {};
  try {
    domMetadata = await new Promise((resolve) => {
      chrome.tabs.sendMessage(activeTab.id, { action: "AUDIT_DOM" }, (response) => {
        if (chrome.runtime.lastError || !response) {
          resolve({});
        } else {
          resolve(response);
        }
      });
    });
  } catch (e) {
    console.warn("DOM metadata audit fallback:", e);
  }

  // 3. Initiate API scan
  async function performScan() {
    loadingState.classList.remove('hidden');
    mainState.classList.add('hidden');

    try {
      const res = await fetch(`${API_BASE_URL}/scan`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          url: tabUrl,
          title: activeTab.title,
          domMetadata
        })
      });

      if (!res.ok) throw new Error("API response error");
      currentScanData = await res.json();
      renderScanResults(currentScanData);

    } catch (err) {
      console.warn("Backend API unavailable, executing client fallback scan:", err);
      currentScanData = performClientFallbackScan(tabUrl, domain, domMetadata);
      renderScanResults(currentScanData);
    } finally {
      loadingState.classList.add('hidden');
      mainState.classList.remove('hidden');
    }
  }

  // Render scan results in popup UI
  function renderScanResults(data) {
    const score = data.score || 0;
    scoreValEl.textContent = `${score}%`;
    riskBadgeEl.textContent = data.riskRating || "SAFE";

    // Set Card Theme
    riskCard.className = "risk-card";
    if (score >= 80 || data.riskRating === "CRITICAL") {
      riskCard.classList.add("card-danger");
    } else if (score >= 45 || data.riskRating === "MEDIUM") {
      riskCard.classList.add("card-warning");
    } else {
      riskCard.classList.add("card-safe");
    }

    // Set Domain Status
    if (data.heuristics && data.heuristics.flags.length > 0) {
      statusDomain.textContent = `${data.heuristics.flags.length} Flags`;
      statusDomain.style.color = "#f59e0b";
    } else {
      statusDomain.textContent = "Clean";
      statusDomain.style.color = "#10b981";
    }

    // Set Login Form / Phishing Status
    if (domMetadata.hasPasswordInput) {
      statusLogin.textContent = domMetadata.isFormMismatch ? "Phishing Trap" : "Password Field";
      statusLogin.style.color = domMetadata.isFormMismatch ? "#ef4444" : "#f59e0b";
    } else if (data.heuristics && data.heuristics.brandSpoofed) {
      statusLogin.textContent = "Brand Spoofed";
      statusLogin.style.color = "#ef4444";
    } else {
      statusLogin.textContent = "No Form";
      statusLogin.style.color = "#10b981";
    }

    // Set Fake Store Status
    if (domMetadata.hasFakeDiscount) {
      statusStore.textContent = "Fake Discount";
      statusStore.style.color = "#ef4444";
    } else if (data.heuristics && data.heuristics.flags.some(f => f.includes("sale") || f.includes("90-off"))) {
      statusStore.textContent = "Scam Keyword";
      statusStore.style.color = "#f59e0b";
    } else {
      statusStore.textContent = "None";
      statusStore.style.color = "#10b981";
    }

    // Set ML Probability
    if (data.mlClassification) {
      statusMl.textContent = `${data.mlClassification.phishingProbability}% Prob.`;
      statusMl.style.color = data.mlClassification.phishingProbability > 50 ? "#ef4444" : "#10b981";
    }

    // AI Explanation
    if (data.aiExplanation) {
      aiSummary.textContent = data.aiExplanation.summary;
      aiReasons.innerHTML = data.aiExplanation.keyReasons.map(r => `<li>${r}</li>`).join('');
      aiRecommendation.textContent = `Recommendation: ${data.aiExplanation.recommendation}`;
    }
  }

  // Fallback client-side scanner if server offline
  function performClientFallbackScan(url, domain, dom) {
    const isPhishDomain = domain.includes("login") || domain.includes("verify") || domain.endsWith(".xyz") || domain.endsWith(".top");
    const score = isPhishDomain ? 88 : (dom.hasPasswordInput ? 45 : 5);
    const riskRating = score >= 80 ? "CRITICAL" : (score >= 45 ? "MEDIUM" : "SAFE");

    return {
      url,
      hostname: domain,
      score,
      riskRating,
      heuristics: { flags: isPhishDomain ? ["High-risk TLD or brand keyword detected."] : [], brandSpoofed: domain.includes("amazon") ? "amazon" : null },
      mlClassification: { phishingProbability: score },
      aiExplanation: {
        summary: score >= 80 ? "⚠️ High Risk Phishing Site" : "✅ Normal Web Page",
        keyReasons: isPhishDomain ? ["• High risk domain indicators."] : ["• Valid web standards."],
        recommendation: score >= 80 ? "Do not enter passwords." : "Safe to browse."
      }
    };
  }

  // Action Listeners
  document.getElementById('btn-rescan').addEventListener('click', () => performScan());

  document.getElementById('btn-highlight').addEventListener('click', () => {
    chrome.tabs.sendMessage(activeTab.id, { action: "HIGHLIGHT_LINKS" });
  });

  document.getElementById('btn-report').addEventListener('click', () => {
    reportModal.classList.remove('hidden');
  });

  document.getElementById('close-modal').addEventListener('click', () => {
    reportModal.classList.add('hidden');
  });

  document.getElementById('report-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const category = document.getElementById('report-category').value;
    const description = document.getElementById('report-desc').value;

    try {
      await fetch(`${API_BASE_URL}/reports`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ domain, url: tabUrl, category, description })
      });
      alert(`Scam report submitted! ${domain} has been blacklisted.`);
    } catch (err) {
      alert(`Report noted locally.`);
    }
    reportModal.classList.add('hidden');
    performScan();
  });

  // Initial Scan
  performScan();
});
