/**
 * Domain & URL Heuristic Analysis Engine
 */

const HIGH_RISK_TLDS = [
  '.xyz', '.top', '.tk', '.click', '.site', '.gq', '.online', '.download', 
  '.work', '.info', '.live', '.space', '.icu', '.club', '.vip', '.rest'
];

const PROTECTED_BRANDS = [
  'amazon', 'paypal', 'facebook', 'google', 'apple', 'microsoft', 
  'netflix', 'instagram', 'twitter', 'linkedin', 'bankofamerica', 
  'wellsfargo', 'chase', 'binance', 'coinbase', 'stripe', 'steam'
];

const SUSPICIOUS_KEYWORDS = [
  'login', 'signin', 'verify', 'verification', 'account', 'security', 
  'update', 'banking', 'secure', 'confirm', 'password', 'credential',
  'free', 'reward', 'claim', 'discount', '90-off', 'sale', 'prize',
  'winner', 'bonus', 'wallet', 'crypto', 'support', 'customer-service'
];

/**
 * Calculate Shannon Entropy of a string to detect randomized/generated domains
 */
function calculateEntropy(str) {
  if (!str) return 0;
  const len = str.length;
  const frequencies = {};
  for (let char of str) {
    frequencies[char] = (frequencies[char] || 0) + 1;
  }
  let entropy = 0;
  for (let char in frequencies) {
    const p = frequencies[char] / len;
    entropy -= p * Math.log2(p);
  }
  return entropy;
}

/**
 * Perform comprehensive heuristic scan on a URL string
 */
function analyzeHeuristics(urlStr) {
  let urlObj;
  try {
    urlObj = new URL(urlStr);
  } catch (e) {
    // If protocol missing, assume http://
    try {
      urlObj = new URL('http://' + urlStr);
    } catch (e2) {
      return { score: 90, flags: ["Malformed or invalid URL string"], entropy: 0 };
    }
  }

  const hostname = urlObj.hostname.toLowerCase();
  const fullPath = urlObj.pathname.toLowerCase() + urlObj.search.toLowerCase();
  const flags = [];
  let riskScore = 0;

  // 1. IP Address Host Check
  const ipRegex = /^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/;
  if (ipRegex.test(hostname)) {
    riskScore += 35;
    flags.push("IP address used as hostname instead of a domain name.");
  }

  // 2. Protocol Check
  if (urlObj.protocol === 'http:') {
    riskScore += 15;
    flags.push("Unencrypted connection (HTTP instead of HTTPS).");
  }

  // 3. TLD Risk Check
  const hasHighRiskTLD = HIGH_RISK_TLDS.some(tld => hostname.endsWith(tld));
  if (hasHighRiskTLD) {
    riskScore += 25;
    flags.push(`Uses high-risk Top-Level Domain (TLD) commonly associated with disposable scam sites.`);
  }

  // 4. Domain Entropy
  const domainParts = hostname.split('.');
  const sld = domainParts.length >= 2 ? domainParts[domainParts.length - 2] : hostname;
  const entropy = calculateEntropy(sld);
  if (entropy > 3.8 && sld.length > 8) {
    riskScore += 20;
    flags.push(`Domain name has high character entropy (${entropy.toFixed(2)}), suggesting auto-generated strings.`);
  }

  // 5. Typosquatting / Brand Spoofing
  let brandSpoofed = null;
  for (let brand of PROTECTED_BRANDS) {
    // Check if domain contains brand name but is not official domain (e.g., amazon-sale.xyz or amaz0n.com)
    const isExactBrandDomain = hostname === `${brand}.com` || hostname === `www.${brand}.com`;
    if (!isExactBrandDomain) {
      // Check for exact substring match (e.g., amazon-verify)
      if (hostname.includes(brand)) {
        brandSpoofed = brand;
        riskScore += 40;
        flags.push(`Brand spoofing detected: Domain contains brand keyword "${brand}" on an unofficial domain.`);
        break;
      }
      // Check for common leetspeak typos (e.g. amaz0n, paypa1, facebo0k, g00gle)
      const leetReplaced = hostname.replace(/0/g, 'o').replace(/1/g, 'l').replace(/3/g, 'e').replace(/5/g, 's');
      if (leetReplaced.includes(brand) && !hostname.includes(brand)) {
        brandSpoofed = brand;
        riskScore += 45;
        flags.push(`Typosquatting/Homograph attack detected: Domain uses visually misleading characters for "${brand}".`);
        break;
      }
    }
  }

  // 6. Subdomain Depth (Deep subdomains like login.paypal.com.scam.com)
  if (domainParts.length > 3) {
    riskScore += 15;
    flags.push(`Excessive subdomain depth (${domainParts.length} levels), often used to hide true domain identity.`);
  }

  // 7. Suspicious Keywords in URL
  const matchedKeywords = SUSPICIOUS_KEYWORDS.filter(kw => fullPath.includes(kw) || sld.includes(kw));
  if (matchedKeywords.length > 0) {
    const kwWeight = Math.min(matchedKeywords.length * 10, 25);
    riskScore += kwWeight;
    flags.push(`URL contains security/phishing high-risk keywords: [${matchedKeywords.join(', ')}].`);
  }

  // 8. Hyphen count in SLD
  const hyphenCount = (sld.match(/-/g) || []).length;
  if (hyphenCount >= 2) {
    riskScore += 15;
    flags.push(`Domain contains multiple hyphens (${hyphenCount}), a common tactic in counterfeit domains.`);
  }

  return {
    score: Math.min(riskScore, 100),
    flags,
    entropy: Number(entropy.toFixed(2)),
    hostname,
    brandSpoofed
  };
}

module.exports = {
  analyzeHeuristics,
  HIGH_RISK_TLDS,
  PROTECTED_BRANDS
};
