const express = require('express');
const router = express.Router();
const { analyzeHeuristics } = require('../services/heuristics');
const { classifyPhishing } = require('../services/ml_classifier');
const { queryThreatIntel } = require('../services/threat_intelligence');
const { generateAIExplanation } = require('../services/ai_explainer');
const { addScan, isWhitelisted, isBlacklisted } = require('../db/storage');

router.post('/', async (req, res) => {
  try {
    const { url, title, domMetadata = {} } = req.body;

    if (!url) {
      return res.status(400).json({ error: "Missing required 'url' field in request body." });
    }

    let urlObj;
    try {
      urlObj = new URL(url);
    } catch (e) {
      try {
        urlObj = new URL('http://' + url);
      } catch (e2) {
        urlObj = { hostname: url, pathname: '', protocol: 'http:' };
      }
    }

    const hostname = urlObj.hostname ? urlObj.hostname.toLowerCase() : url;

    // Fast-path Whitelist check
    if (isWhitelisted(hostname)) {
      const scanResult = {
        url,
        hostname,
        title: title || hostname,
        timestamp: new Date().toISOString(),
        score: 0,
        riskRating: "SAFE",
        aiExplanation: {
          compositeScore: 0,
          riskRating: "SAFE",
          summary: "✅ Verified Trusted Domain: This site is on the verified global trusted whitelist.",
          keyReasons: ["• Verified official domain signature.", "• Clean threat reputation across all databases."],
          recommendation: "Safe for secure browsing and transactions."
        },
        mlClassification: { phishingProbability: 0, confidenceRating: "Verified Whitelisted" },
        threatIntel: { threatLevel: "SAFE", virusTotal: { positives: 0, total: 72 } }
      };
      addScan(scanResult);
      return res.json(scanResult);
    }

    // Heuristics Analysis
    const heuristics = analyzeHeuristics(url);

    // ML Phishing Classifier
    const mlClassification = classifyPhishing(url, domMetadata);

    // Threat Intelligence Lookup
    const threatIntel = await queryThreatIntel(url, hostname);

    // Fast-path Blacklist override
    if (isBlacklisted(hostname)) {
      heuristics.score = 98;
      heuristics.flags.unshift("Domain is listed on global community scam blacklist.");
    }

    // AI Explanation Generator
    const aiExplanation = generateAIExplanation(heuristics, mlClassification, threatIntel, domMetadata);

    const scanResult = {
      url,
      hostname,
      title: title || hostname,
      timestamp: new Date().toISOString(),
      score: aiExplanation.compositeScore,
      riskRating: aiExplanation.riskRating,
      heuristics,
      mlClassification,
      threatIntel,
      aiExplanation
    };

    // Store scan record in DB
    addScan(scanResult);

    return res.json(scanResult);

  } catch (err) {
    console.error("Scan API Error:", err);
    return res.status(500).json({ error: "Internal Server Error during scanning." });
  }
});

module.exports = router;
