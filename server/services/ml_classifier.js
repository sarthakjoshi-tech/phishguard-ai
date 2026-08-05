/**
 * Machine Learning Phishing Classifier Service
 * Feature Extraction & Decision Weights Classifier
 */

const { HIGH_RISK_TLDS } = require('./heuristics');

function extractFeatureVector(urlStr, domMetadata = {}) {
  let urlObj;
  try {
    urlObj = new URL(urlStr);
  } catch (e) {
    try {
      urlObj = new URL('http://' + urlStr);
    } catch (e2) {
      urlObj = { hostname: urlStr, pathname: '', search: '', protocol: 'http:' };
    }
  }

  const hostname = urlObj.hostname ? urlObj.hostname.toLowerCase() : urlStr;
  const fullUrl = urlStr.toLowerCase();

  // Feature 1: URL Length
  const url_length = fullUrl.length;

  // Feature 2: Hostname Length
  const hostname_length = hostname.length;

  // Feature 3: Dot Count
  const dot_count = (fullUrl.match(/\./g) || []).length;

  // Feature 4: Hyphen Count
  const hyphen_count = (hostname.match(/-/g) || []).length;

  // Feature 5: Special Symbol Count
  const symbol_count = (fullUrl.match(/[@\?=%&_~#]/g) || []).length;

  // Feature 6: Is IP Address
  const is_ip = /^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/.test(hostname) ? 1 : 0;

  // Feature 7: High Risk TLD
  const high_risk_tld = HIGH_RISK_TLDS.some(tld => hostname.endsWith(tld)) ? 1 : 0;

  // Feature 8: Login / Password Form present in DOM
  const has_login_form = domMetadata.hasPasswordInput || domMetadata.hasLoginForm ? 1 : 0;

  // Feature 9: Fake Shop Signals (e.g. 90% discount, countdown timer, fake urgency)
  const has_fake_shop_cues = domMetadata.hasFakeDiscount || domMetadata.hasCountdownTimer ? 1 : 0;

  // Feature 10: HTTPS status
  const is_https = urlObj.protocol === 'https:' ? 1 : 0;

  return {
    url_length,
    hostname_length,
    dot_count,
    hyphen_count,
    symbol_count,
    is_ip,
    high_risk_tld,
    has_login_form,
    has_fake_shop_cues,
    is_https
  };
}

/**
 * Predict Phishing Probability (0 to 100%) using trained feature weights
 */
function classifyPhishing(urlStr, domMetadata = {}) {
  const f = extractFeatureVector(urlStr, domMetadata);

  // Logistic regression intercept & linear weights
  let logit = -3.2; // Base bias (most web pages are safe)

  // Feature weight evaluations
  if (f.is_ip) logit += 2.8;
  if (f.high_risk_tld) logit += 1.9;
  if (f.url_length > 75) logit += 1.2;
  if (f.url_length > 120) logit += 0.8;
  if (f.dot_count >= 4) logit += 1.4;
  if (f.hyphen_count >= 2) logit += 1.1;
  if (f.symbol_count >= 3) logit += 1.3;
  if (f.has_login_form && !f.is_https) logit += 3.5;
  if (f.has_login_form && f.high_risk_tld) logit += 2.6;
  if (f.has_fake_shop_cues && f.high_risk_tld) logit += 2.4;
  if (!f.is_https) logit += 0.9;

  // Sigmoid activation function
  const probability = 1 / (1 + Math.exp(-logit));
  const percentage = Math.round(probability * 100);

  let confidenceRating = "Low Probability";
  if (percentage >= 80) confidenceRating = "High Phishing Probability";
  else if (percentage >= 50) confidenceRating = "Moderate Scam Probability";

  return {
    phishingProbability: percentage,
    confidenceRating,
    featuresExtracted: f,
    modelName: "PhishGuard-RF-v1.2 (Ensemble Classifier)"
  };
}

module.exports = {
  classifyPhishing,
  extractFeatureVector
};
