/**
 * Background Service Worker for PhishGuard AI Extension (Manifest V3)
 * Monitors tab navigation, runs automated backend scans, manages badges,
 * and intercepts mistyped / typosquatted phishing URLs BEFORE visiting.
 */

const API_ENDPOINT = "http://localhost:5000/api/scan";

// Cache recent scan results by URL
const scanCache = new Map();

// Temporarily bypassed URLs by user choice ("Proceed Anyway")
const bypassSet = new Set();

const PROTECTED_BRANDS = [
  { name: 'amazon', official: ['amazon.com', 'amazon.in', 'amazon.co.uk', 'amazon.de', 'amazon.fr'] },
  { name: 'paypal', official: ['paypal.com'] },
  { name: 'facebook', official: ['facebook.com', 'fb.com'] },
  { name: 'google', official: ['google.com', 'accounts.google.com'] },
  { name: 'apple', official: ['apple.com', 'icloud.com'] },
  { name: 'microsoft', official: ['microsoft.com', 'live.com', 'outlook.com', 'office.com'] },
  { name: 'netflix', official: ['netflix.com'] },
  { name: 'instagram', official: ['instagram.com'] },
  { name: 'twitter', official: ['twitter.com', 'x.com'] },
  { name: 'linkedin', official: ['linkedin.com'] },
  { name: 'binance', official: ['binance.com'] },
  { name: 'bankofamerica', official: ['bankofamerica.com'] },
  { name: 'wellsfargo', official: ['wellsfargo.com'] },
  { name: 'chase', official: ['chase.com'] }
];

const HIGH_RISK_TLDS = ['.xyz', '.top', '.tk', '.click', '.site', '.gq', '.online', '.download', '.live', '.icu', '.club', '.vip'];

/**
 * Pre-visit URL inspection: checks if a URL typed/visited is a typosquatted brand or suspicious destination
 */
function inspectPreVisitUrl(urlStr) {
  if (!urlStr || !urlStr.startsWith("http")) return null;

  let urlObj;
  try {
    urlObj = new URL(urlStr);
  } catch (e) {
    return null;
  }

  const hostname = urlObj.hostname.toLowerCase();
  if (hostname === "localhost" || hostname === "127.0.0.1") return null;

  // If user already clicked "Proceed Anyway", allow navigation
  if (bypassSet.has(hostname) || bypassSet.has(urlStr)) return null;

  // 1. Typosquatting / Brand Spoofing Check
  for (let brand of PROTECTED_BRANDS) {
    const isOfficial = brand.official.some(officialDomain => hostname === officialDomain || hostname.endsWith("." + officialDomain));
    if (isOfficial) continue;

    // Check substring brand spoofing (e.g. amazon-sale.xyz, paypal-security.top)
    if (hostname.includes(brand.name)) {
      return {
        brand: brand.name,
        reason: `Domain contains protected brand keyword "${brand.name}" on an unofficial domain (${hostname}).`
      };
    }

    // Check leetspeak typosquatting (e.g. amaz0n, paypa1, facebo0k, g00gle)
    const normalized = hostname.replace(/0/g, 'o').replace(/1/g, 'l').replace(/3/g, 'e').replace(/5/g, 's');
    if (normalized.includes(brand.name)) {
      return {
        brand: brand.name,
        reason: `Typosquatting/Homograph detected: Misspelled URL mimicking official "${brand.name}".`
      };
    }
  }

  // 2. High risk disposable scam TLD with phishing/urgency keyword
  const hasHighRiskTLD = HIGH_RISK_TLDS.some(tld => hostname.endsWith(tld));
  if (hasHighRiskTLD) {
    const fullUrlLower = urlStr.toLowerCase();
    const scamKeywords = ['login', 'verify', 'account', 'secure', 'banking', 'update', 'claim', 'discount', 'free', 'reward', 'sale'];
    const matchedKeyword = scamKeywords.find(kw => fullUrlLower.includes(kw));
    if (matchedKeyword) {
      return {
        brand: null,
        reason: `High-risk disposable domain (${hostname}) targeting "${matchedKeyword}" keywords.`
      };
    }
  }

  return null;
}

/**
 * Intercept navigation BEFORE page loads if suspicious URL pattern is detected
 */
chrome.webNavigation.onBeforeNavigate.addListener(details => {
  // Only intercept main frame top-level user navigations
  if (details.frameId !== 0) return;

  const url = details.url;
  // Ignore chrome:// or extension internal pages
  if (!url || url.startsWith("chrome") || url.includes("warning/warning.html")) return;

  const threat = inspectPreVisitUrl(url);
  if (threat) {
    const warningPageUrl = chrome.runtime.getURL("warning/warning.html") +
      `?target=${encodeURIComponent(url)}` +
      `&brand=${encodeURIComponent(threat.brand || '')}` +
      `&reason=${encodeURIComponent(threat.reason)}`;

    chrome.tabs.update(details.tabId, { url: warningPageUrl });
  }
});

/**
 * Perform background scan for active tab
 */
async function scanTab(tabId, url) {
  if (!url || !url.startsWith("http")) return;
  if (url.includes("warning/warning.html")) return;

  try {
    let domain = "";
    try {
      domain = new URL(url).hostname;
    } catch (e) {
      return;
    }

    if (domain === "localhost" || domain === "127.0.0.1") return;

    if (scanCache.has(url)) {
      updateBadge(tabId, scanCache.get(url));
      return;
    }

    const response = await fetch(API_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    if (!response.ok) return;
    const scanData = await response.json();
    scanCache.set(url, scanData);

    updateBadge(tabId, scanData);

    // If critical threat and page loaded, trigger warning banner as secondary safeguard
    if (scanData.riskRating === "CRITICAL" || scanData.score >= 80) {
      chrome.tabs.sendMessage(tabId, {
        action: "SHOW_WARNING_BANNER",
        summary: scanData.aiExplanation ? scanData.aiExplanation.summary : "Critical Scam Page"
      }, () => {
        if (chrome.runtime.lastError) {
          // Content script might not be injected yet
        }
      });
    }

  } catch (err) {
    console.warn("PhishGuard Background Scan Error:", err);
  }
}

/**
 * Update Extension Icon Badge & Background Color
 */
function updateBadge(tabId, scanData) {
  const rating = scanData.riskRating || "SAFE";
  const score = scanData.score || 0;

  if (rating === "CRITICAL" || score >= 80) {
    chrome.action.setBadgeText({ tabId, text: `${score}%` });
    chrome.action.setBadgeBackgroundColor({ tabId, color: "#dc2626" }); // Red
  } else if (rating === "MEDIUM" || score >= 45) {
    chrome.action.setBadgeText({ tabId, text: "WARN" });
    chrome.action.setBadgeBackgroundColor({ tabId, color: "#d97706" }); // Amber
  } else {
    chrome.action.setBadgeText({ tabId, text: "SAFE" });
    chrome.action.setBadgeBackgroundColor({ tabId, color: "#059669" }); // Green
  }
}

// Allow user bypass message from warning page
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "ALLOW_TEMPORARY_BYPASS" && request.url) {
    try {
      const hostname = new URL(request.url).hostname.toLowerCase();
      bypassSet.add(hostname);
      bypassSet.add(request.url);
    } catch (e) {
      bypassSet.add(request.url);
    }
    sendResponse({ status: "ALLOWED" });
  }
  return true;
});

// Tab navigation listeners
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url) {
    scanTab(tabId, tab.url);
  }
});

chrome.tabs.onActivated.addListener(activeInfo => {
  chrome.tabs.get(activeInfo.tabId, tab => {
    if (tab && tab.url) {
      scanTab(activeInfo.tabId, tab.url);
    }
  });
});
