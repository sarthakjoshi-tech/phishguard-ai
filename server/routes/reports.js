const express = require('express');
const router = express.Router();
const { getReports, addReport } = require('../db/storage');

// GET /api/reports - Get recent user scam reports
router.get('/', (req, res) => {
  try {
    const reports = getReports();
    return res.json(reports);
  } catch (err) {
    return res.status(500).json({ error: "Failed to retrieve scam reports." });
  }
});

// POST /api/reports - Submit a new scam report
router.post('/', (req, res) => {
  try {
    const { domain, url, category, description } = req.body;

    if (!domain || !category) {
      return res.status(400).json({ error: "Missing required fields: 'domain' and 'category'." });
    }

    let parsedDomain = domain.toLowerCase().trim();
    if (parsedDomain.startsWith("http://") || parsedDomain.startsWith("https://")) {
      try {
        parsedDomain = new URL(parsedDomain).hostname;
      } catch (e) {}
    }

    const newReport = addReport({
      domain: parsedDomain,
      url: url || `http://${parsedDomain}`,
      category,
      description: description || "Reported by community user via extension popup."
    });

    return res.status(201).json({
      message: "Scam report successfully submitted and domain added to blacklist.",
      report: newReport
    });

  } catch (err) {
    return res.status(500).json({ error: "Failed to submit scam report." });
  }
});

module.exports = router;
