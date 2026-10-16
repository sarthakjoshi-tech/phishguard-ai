/**
 * Warning Interstitial Script
 * Reads scan data from URL query params or API and displays AI explanations
 */

const PROTECTED_OFFICIAL_SITES = {
  'amazon': 'https://www.amazon.com',
  'paypal': 'https://www.paypal.com',
  'facebook': 'https://www.facebook.com',
  'google': 'https://www.google.com',
  'apple': 'https://www.apple.com',
  'microsoft': 'https://www.microsoft.com',
  'netflix': 'https://www.netflix.com',
  'instagram': 'https://www.instagram.com',
  'twitter': 'https://www.twitter.com',
  'linkedin': 'https://www.linkedin.com',
  'bankofamerica': 'https://www.bankofamerica.com',
  'chase': 'https://www.chase.com',
  'binance': 'https://www.binance.com'
};

document.addEventListener('DOMContentLoaded', async () => {
  const urlParams = new URLSearchParams(window.location.search);
  const targetUrl = urlParams.get('target') || '';
  const reason = urlParams.get('reason') || 'Suspicious domain pattern';
  const brand = urlParams.get('brand') || '';

  const targetUrlEl = document.getElementById('target-url');
  const aiSummaryEl = document.getElementById('ai-summary');
  const aiReasonsEl = document.getElementById('ai-reasons');
  const aiRecEl = document.getElementById('ai-rec');
  const officialBox = document.getElementById('official-box');
  const officialText = document.getElementById('official-text');
  const btnOfficial = document.getElementById('btn-official');
  const btnBack = document.getElementById('btn-back');
  const btnProceed = document.getElementById('btn-proceed');

  targetUrlEl.textContent = targetUrl || 'Unknown Destination';

  // 1. Show Official Brand Recommendation if Typosquatting / Brand Spoofed
  if (brand && PROTECTED_OFFICIAL_SITES[brand.toLowerCase()]) {
    const officialUrl = PROTECTED_OFFICIAL_SITES[brand.toLowerCase()];
    officialBox.style.display = 'flex';
    officialText.innerHTML = `You may have mistyped the address. The genuine website is <b>${officialUrl}</b>.`;
    btnOfficial.href = officialUrl;
  }

  // 2. Fetch AI Explanation from Backend or synthesize locally
  try {
    const res = await fetch("http://localhost:5000/api/scan", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url: targetUrl })
    });

    if (res.ok) {
      const data = await res.json();
      if (data.aiExplanation) {
        aiSummaryEl.textContent = data.aiExplanation.summary;
        aiReasonsEl.innerHTML = data.aiExplanation.keyReasons.map(r => `<li>${r}</li>`).join('');
        aiRecEl.textContent = `Recommendation: ${data.aiExplanation.recommendation}`;
        if (data.riskRating) {
          document.getElementById('risk-badge').textContent = `${data.riskRating} (${data.score}%)`;
        }
      }
    } else {
      throw new Error("Backend offline");
    }
  } catch (err) {
    // Fallback if backend offline
    aiSummaryEl.textContent = `⚠️ DANGER: Pre-navigation threat interception. The URL "${targetUrl}" displays distinct scam and phishing markers.`;
    aiReasonsEl.innerHTML = `
      <li>• Brand Spoofing / Typosquatting: Domain resembles protected brand "${brand || 'well-known service'}" but points to an unverified server.</li>
      <li>• Suspicious High-Risk Indicators: ${reason}</li>
      <li>• High Probability Phishing: Potential credential theft or counterfeit store frontend.</li>
    `;
    aiRecEl.textContent = "Recommendation: Do not open this website. Your personal credentials and data may be stolen.";
  }

  // Button actions
  btnBack.addEventListener('click', () => {
    if (window.history.length > 1) {
      window.history.back();
    } else {
      window.location.href = 'https://www.google.com';
    }
  });

  btnProceed.addEventListener('click', () => {
    // Notify background worker to temporarily allow this domain so it won't loop
    chrome.runtime.sendMessage({
      action: "ALLOW_TEMPORARY_BYPASS",
      url: targetUrl
    }, () => {
      window.location.href = targetUrl;
    });
  });
});
