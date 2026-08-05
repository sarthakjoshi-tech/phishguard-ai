/**
 * Background Service Worker for PhishGuard AI Extension (Manifest V3)
 * Monitors tab navigation, runs automated backend scans, & manages extension badges.
 */

const API_ENDPOINT = "http://localhost:5000/api/scan";

// Cache recent scan results by URL
const scanCache = new Map();

/**
 * Perform background scan for active tab
 */
async function scanTab(tabId, url) {
  if (!url || !url.startsWith("http")) return;

  try {
    let domain = "";
    try {
      domain = new URL(url).hostname;
    } catch (e) {
      return;
    }

    // Ignore localhost or extension pages
    if (domain === "localhost" || domain === "127.0.0.1") return;

    // Check cache
    if (scanCache.has(url)) {
      updateBadge(tabId, scanCache.get(url));
      return;
    }

    // Fetch scan from API
    const response = await fetch(API_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    if (!response.ok) return;
    const scanData = await response.json();
    scanCache.set(url, scanData);

    updateBadge(tabId, scanData);

    // If critical threat, trigger top warning banner
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
