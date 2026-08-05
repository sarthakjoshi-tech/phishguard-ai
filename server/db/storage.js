const fs = require('fs');
const path = require('path');

const DB_FILE = path.join(__dirname, 'data.json');

const defaultData = {
  scans: [],
  reports: [
    {
      id: "rep-101",
      domain: "amazon-shop-sale.xyz",
      url: "http://amazon-shop-sale.xyz/deal-90-off",
      category: "Fake E-Commerce Store",
      description: "Claims to sell electronics at 90% off, steals credit card details.",
      timestamp: new Date(Date.now() - 86400000 * 2).toISOString(),
      votes: 14
    },
    {
      id: "rep-102",
      domain: "facebook-login-verify.top",
      url: "http://facebook-login-verify.top/auth/login.php",
      category: "Credential Harvesting / Phishing",
      description: "Fake Facebook login form asking for password and 2FA code.",
      timestamp: new Date(Date.now() - 86400000).toISOString(),
      votes: 28
    }
  ],
  blacklist: [
    "amazon-shop-sale.xyz",
    "facebook-login-verify.top",
    "free-iphone-claim.click",
    "paypal-account-update.info",
    "bankofamerica-secure-verify.site"
  ],
  whitelist: [
    "google.com",
    "facebook.com",
    "amazon.com",
    "paypal.com",
    "github.com",
    "microsoft.com",
    "apple.com",
    "youtube.com",
    "wikipedia.org"
  ]
};

function readDB() {
  try {
    if (!fs.existsSync(DB_FILE)) {
      fs.writeFileSync(DB_FILE, JSON.stringify(defaultData, null, 2), 'utf-8');
      return defaultData;
    }
    const raw = fs.readFileSync(DB_FILE, 'utf-8');
    return JSON.parse(raw);
  } catch (err) {
    console.error("Error reading database file, using fallback data:", err);
    return defaultData;
  }
}

function writeDB(data) {
  try {
    fs.writeFileSync(DB_FILE, JSON.stringify(data, null, 2), 'utf-8');
  } catch (err) {
    console.error("Error writing to database file:", err);
  }
}

module.exports = {
  getScans: () => readDB().scans,
  addScan: (scanRecord) => {
    const data = readDB();
    data.scans.unshift(scanRecord);
    // Keep max 100 recent scans
    if (data.scans.length > 100) data.scans.pop();
    writeDB(data);
  },
  getReports: () => readDB().reports,
  addReport: (report) => {
    const data = readDB();
    report.id = "rep-" + Date.now();
    report.timestamp = new Date().toISOString();
    report.votes = 1;
    data.reports.unshift(report);
    if (!data.blacklist.includes(report.domain)) {
      data.blacklist.push(report.domain);
    }
    writeDB(data);
    return report;
  },
  getBlacklist: () => readDB().blacklist,
  getWhitelist: () => readDB().whitelist,
  isBlacklisted: (domain) => readDB().blacklist.includes(domain.toLowerCase()),
  isWhitelisted: (domain) => readDB().whitelist.includes(domain.toLowerCase())
};
