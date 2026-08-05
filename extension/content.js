/**
 * Content Script for Real-Time On-Page DOM Security Auditing & Link Scanning
 */

(function () {
  const KNOWN_BRANDS = [
    { name: 'facebook', official: ['facebook.com', 'fb.com'] },
    { name: 'google', official: ['google.com', 'accounts.google.com'] },
    { name: 'amazon', official: ['amazon.com', 'amazon.in', 'amazon.co.uk'] },
    { name: 'paypal', official: ['paypal.com'] },
    { name: 'netflix', official: ['netflix.com'] },
    { name: 'microsoft', official: ['microsoft.com', 'live.com', 'outlook.com'] }
  ];

  const HIGH_RISK_EXTENSIONS = ['.exe', '.scr', '.bat', '.cmd', '.vbs', '.zip', '.apk'];
  const HIGH_RISK_TLDS = ['.xyz', '.top', '.tk', '.click', '.site', '.gq', '.online', '.download'];

  /**
   * Audit DOM elements on active page
   */
  function auditDOM() {
    const hostname = window.location.hostname.toLowerCase();
    
    // Check password fields & login forms
    const passwordInputs = document.querySelectorAll('input[type="password"]');
    const hasPasswordInput = passwordInputs.length > 0;
    const loginForms = document.querySelectorAll('form');
    const hasLoginForm = loginForms.length > 0;

    // Check Brand Mismatch on Login Pages
    const pageText = (document.title + " " + document.body.innerText).toLowerCase();
    let isFormMismatch = false;
    let spoofedBrand = null;

    if (hasPasswordInput || hasLoginForm) {
      for (let brand of KNOWN_BRANDS) {
        if (pageText.includes(brand.name)) {
          const isOfficial = brand.official.some(domain => hostname.endsWith(domain));
          if (!isOfficial) {
            isFormMismatch = true;
            spoofedBrand = brand.name;
            break;
          }
        }
      }
    }

    // Check Fake Discount & Urgent Countdown Indicators
    const bodyText = document.body.innerText || "";
    const hasDiscountKeyword = /90%\s*off|80%\s*off|95%\s*off|free\s*iphone|claims?\s*gift|claim\s*prize/i.test(bodyText);
    const hasTimer = !!document.querySelector('[id*="timer"], [class*="timer"], [id*="countdown"], [class*="countdown"]');
    const hasFakeDiscount = hasDiscountKeyword && hasTimer;

    return {
      hostname,
      hasPasswordInput,
      hasLoginForm,
      isFormMismatch,
      spoofedBrand,
      hasFakeDiscount,
      hasCountdownTimer: hasTimer,
      linksCount: document.querySelectorAll('a').length
    };
  }

  /**
   * Highlight dangerous links on the web page
   */
  function highlightDangerousLinks() {
    const links = document.querySelectorAll('a[href]');
    let highlightedCount = 0;

    links.forEach(link => {
      const href = link.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('javascript:')) return;

      let linkUrl;
      try {
        linkUrl = new URL(href, window.location.href);
      } catch (e) {
        return;
      }

      const linkHost = linkUrl.hostname.toLowerCase();
      const linkPath = linkUrl.pathname.toLowerCase();

      let isDangerous = false;
      let reason = "";

      // 1. IP address in link
      if (/^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/.test(linkHost)) {
        isDangerous = true;
        reason = "Direct IP Address Link";
      }

      // 2. High-risk TLD
      if (!isDangerous && HIGH_RISK_TLDS.some(tld => linkHost.endsWith(tld))) {
        isDangerous = true;
        reason = "High-Risk Scam TLD";
      }

      // 3. Executable download
      if (!isDangerous && HIGH_RISK_EXTENSIONS.some(ext => linkPath.endsWith(ext))) {
        isDangerous = true;
        reason = "Executable Download File";
      }

      // 4. Typosquatting substring link
      if (!isDangerous) {
        for (let brand of KNOWN_BRANDS) {
          if (linkHost.includes(brand.name)) {
            const isOfficial = brand.official.some(d => linkHost.endsWith(d));
            if (!isOfficial) {
              isDangerous = true;
              reason = `Fake ${brand.name.toUpperCase()} Link`;
              break;
            }
          }
        }
      }

      if (isDangerous) {
        highlightedCount++;
        link.classList.add('phishguard-danger-link');
        link.setAttribute('data-phishguard-reason', reason);

        // Append visual danger badge if not already present
        if (!link.querySelector('.phishguard-badge')) {
          const badge = document.createElement('span');
          badge.className = 'phishguard-badge';
          badge.innerHTML = ` 🔴 <b>${reason}</b>`;
          link.appendChild(badge);
        }
      }
    });

    return highlightedCount;
  }

  /**
   * Display floating top security warning banner on critical threat pages
   */
  function showWarningBanner(aiSummary) {
    if (document.getElementById('phishguard-top-banner')) return;

    const banner = document.createElement('div');
    banner.id = 'phishguard-top-banner';
    banner.className = 'phishguard-banner-danger';
    banner.innerHTML = `
      <div class="pg-banner-content">
        <span class="pg-icon">🚨</span>
        <div class="pg-text">
          <strong>PhishGuard AI Warning:</strong> ${aiSummary || "This website has been identified as a high-risk scam or phishing page."}
        </div>
        <button id="pg-banner-close" class="pg-btn">Proceed Anyway</button>
      </div>
    `;

    document.body.prepend(banner);
    document.getElementById('pg-banner-close').addEventListener('click', () => {
      banner.remove();
    });
  }

  // Listen for messages from extension popup or background worker
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "AUDIT_DOM") {
      const audit = auditDOM();
      sendResponse(audit);
    } else if (request.action === "HIGHLIGHT_LINKS") {
      const count = highlightDangerousLinks();
      sendResponse({ count });
    } else if (request.action === "SHOW_WARNING_BANNER") {
      showWarningBanner(request.summary);
      sendResponse({ status: "BANNER_SHOWN" });
    }
    return true;
  });

})();
