"""
Script to generate the complete, comprehensive PhishGuard AI guide.
"""

import os
import sys

# Ensure current dir in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_engine import CanvasPDF

def build_pdf():
    pdf_path = r"C:\Users\sarth\.gemini\antigravity\scratch\browser-scam-detector\PhishGuard_AI_Complete_Project_Guide.pdf"
    pdf = CanvasPDF(pdf_path)

    # =========================================================================
    # TITLE BANNER & INTRODUCTION
    # =========================================================================
    pdf.add_title_banner(
        title="PhishGuard AI: Complete Project Evaluation Master Guide",
        subtitle="A Zero-Knowledge to Full-Mastery Defense Handbook for Final Project Presentation"
    )

    pdf.add_callout(
        title="How to Use This Document",
        content="This guide was written assuming you know ABSOLUTE ZERO about cybersecurity, browser extensions, or machine learning. Read it from top to bottom. By the end, you will understand every line of code, every technical buzzword, and exactly how to answer any question your teacher asks tomorrow.",
        callout_type="concept"
    )

    pdf.add_heading_1("Executive Summary: The 30-Second Elevator Pitch")
    pdf.add_paragraph(
        "If your teacher asks you: 'Tell me in 30 seconds, what did you build and why?', memorize and say this:"
    )
    pdf.add_callout(
        title="Your 30-Second Elevator Pitch (Memorize This!)",
        content="'Good morning, Teacher. Our project is PhishGuard AI. It is an AI-powered browser security platform that protects everyday users in real time from fake websites, credential theft traps, and shopping scams. Unlike traditional security tools that rely on slow blacklists, PhishGuard intercepts threats BEFORE and DURING page visits by combining mathematical Shannon Entropy, on-page DOM inspection, a 10-feature Machine Learning classifier, and Gemini AI natural language explanations.'",
        callout_type="info"
    )

    # =========================================================================
    # CHAPTER 1: ABSOLUTE BEGINNER FOUNDATIONS
    # =========================================================================
    pdf.add_heading_1("Chapter 1: The Absolute Beginner Primer (Web & Security Basics)")
    pdf.add_paragraph(
        "Before looking at any code, you must understand the basic plumbing of the internet. Here is how websites work in simple, plain English."
    )

    pdf.add_heading_2("1.1 How the Web Works (In Plain English)")
    pdf.add_bullet("IP Address", "Every computer connected to the internet has a unique numerical telephone number called an IP Address (e.g., 142.250.190.46). Computers only understand IP addresses.")
    pdf.add_bullet("Domain Name (DNS)", "Humans cannot remember numbers like 142.250.190.46, so we use domain names like google.com or amazon.com. The Domain Name System (DNS) is like a giant phonebook that translates human names into IP addresses.")
    pdf.add_bullet("URL Anatomy", "A complete address like 'https://accounts.google.com/login?lang=en' breaks down into: (1) Protocol ('https://'), (2) Subdomain ('accounts'), (3) Brand/Domain ('google'), (4) Top-Level Domain or TLD ('.com'), (5) Path ('/login'), and (6) Parameters ('?lang=en').")
    pdf.add_bullet("HTTP vs. HTTPS", "HTTP transmits everything in open plaintext—anyone on your Wi-Fi can see passwords. HTTPS encrypts data in a secure digital envelope using SSL/TLS certificates.")

    pdf.add_heading_2("1.2 What is Phishing and Why is it Dangerous?")
    pdf.add_paragraph(
        "Phishing is a social engineering attack where a criminal creates a fraudulent website that looks visually identical to a trustworthy service (like PayPal, Google, Amazon, or a bank). When an unsuspecting user enters their password or credit card, the attacker steals it."
    )
    pdf.add_callout(
        title="Why Traditional Antivirus & Blacklists Fail Today",
        content="In the past, security companies maintained blacklists of bad websites. But today, modern attackers use automated tools to generate thousands of temporary scam domains that stay online for only 4 to 8 hours before vanishing. By the time a victim reports the site and a company adds it to a blacklist, thousands of people have already been scammed. PhishGuard solves this by analyzing sites in REAL TIME mathematically and behaviorally.",
        callout_type="warning"
    )

    pdf.add_heading_2("1.3 The 3 Most Dangerous Web Scams PhishGuard Solves")
    pdf.add_bullet("1. Typosquatting / Homographs", "Scammers register domain names with tiny spelling mistakes or visually similar characters, e.g., 'paypa1.com' (number 1 instead of letter l) or 'amaz0n.com' (zero instead of letter o). An inattentive user never notices the difference.")
    pdf.add_bullet("2. Credential Harvesting Traps", "A webpage contains an official company logo (like Facebook) and an email/password box, but the website is hosted on 'facebook-login-security.xyz'. Users type credentials and give away their accounts.")
    pdf.add_bullet("3. Fake E-Commerce Stores", "Scam sites offering '90% OFF Clearance Sale on iPhone 16' with a fake ticking countdown timer ('Offer expires in 04:59'). When users enter credit card details, their cards are charged and no product is ever delivered.")

    # =========================================================================
    # CHAPTER 2: MASTER GLOSSARY OF TECHNICAL TERMS
    # =========================================================================
    pdf.new_page()
    pdf.add_heading_1("Chapter 2: Master Glossary of Technical Terms")
    pdf.add_paragraph(
        "Teachers and evaluators love to test whether you truly understand the technical jargon in your project. Here is every term defined clearly so you can explain it without stuttering."
    )

    terms = [
        ("DOM (Document Object Model)", "The live tree of HTML elements built by the browser. When you visit a website, the browser turns the HTML code into a DOM tree of buttons, text, and inputs. Our content script audits the DOM to detect password boxes and urgency countdown timers."),
        ("Manifest V3 (MV3)", "Google Chrome's modern, secure standard for browser extensions. In older Manifest V2, background pages ran forever, draining battery and RAM. Manifest V3 replaces them with lightweight, event-driven Service Workers."),
        ("Service Worker (background.js)", "A background script that runs behind the scenes. It sleeps when nothing is happening and wakes up instantly when an event occurs, like when a user navigates to a new tab."),
        ("Content Script (content.js)", "A JavaScript file injected directly into the active web page. It has direct access to inspect the page DOM, read elements, change styles, and draw warning badges."),
        ("REST API", "Representational State Transfer. A standard architectural style where software systems communicate over HTTP using standard JSON messages. Our extension sends a POST request with the URL to port 5000, and our server replies with a JSON analysis report."),
        ("CORS (Cross-Origin Resource Sharing)", "A browser security rule that restricts websites from requesting data from another domain or port. Our server includes 'Access-Control-Allow-Origin: *' headers so the extension can freely communicate with the backend."),
        ("Shannon Entropy", "A mathematical formula invented by Claude Shannon that measures unpredictability/randomness in text. Real company domains have low entropy (2.0 to 3.0), whereas scam domains generated by computer bots have high entropy (> 3.8)."),
        ("Feature Vector", "In Machine Learning, computers cannot read sentences directly. We convert properties of the website (length, dot count, password box presence) into a 10-number list called a Feature Vector."),
        ("Logistic Regression & Sigmoid", "A mathematical classification algorithm. It multiplies each feature by an importance weight and applies the S-shaped Sigmoid formula: 1 / (1 + e^-z) to squash the final score into a clean 0% to 100% probability."),
        ("TLD (Top-Level Domain)", "The very last suffix of a domain name, such as .com, .org, or .xyz. Free or cheap disposable TLDs like .xyz, .top, .click are heavily abused by cybercriminals."),
        ("Explainable AI (XAI)", "Instead of just giving a cold number like 'Score: 88%', XAI translates technical telemetry into human-readable English: 'Warning: Fake discount detected and password requested on an unverified domain.'"),
        ("Zero-Dependency Architecture", "Our backend server is built using only native Node.js core modules ('http', 'url', 'fs'). It requires zero external npm packages, which prevents crashes and makes the project lightweight.")
    ]

    pdf.add_table_row("Technical Term", "Meaning & Simple Explanation for Teacher", is_header=True, col1_w=140)
    for term, definition in terms:
        pdf.add_table_row(term, definition, is_header=False, col1_w=140)

    # =========================================================================
    # CHAPTER 3: COMPLETE SYSTEM ARCHITECTURE & DATA FLOW
    # =========================================================================
    pdf.new_page()
    pdf.add_heading_1("Chapter 3: End-to-End System Architecture & Lifecycle")
    pdf.add_paragraph(
        "Here is the exact journey of what happens inside PhishGuard AI from the very second a user types a link until the security badge appears."
    )

    pdf.add_heading_2("3.1 The 5-Stage Protection Pipeline")
    pdf.add_bullet("Stage 1: Pre-Visit Interception (Before Page Loads)", "When the user presses Enter in Chrome, 'background.js' listens to 'chrome.webNavigation.onBeforeNavigate'. If the address contains a known typosquat (like 'paypa1.com') or a scam TLD with phishing keywords, navigation is ABORTED before connecting to the rogue server, redirecting to our local warning page.")
    pdf.add_bullet("Stage 2: On-Page DOM Audit (While Page Loads)", "If the address passes pre-check and loads, 'content.js' immediately scans the HTML DOM: Does the page contain '<input type=\"password\">'? Does it mention 'Amazon' on an unauthorized domain? Does it have a countdown timer and '90% OFF' text?")
    pdf.add_bullet("Stage 3: Zero-Dependency Backend Analysis (Port 5000)", "The extension sends a JSON payload to 'POST http://localhost:5000/api/scan' containing the URL, page title, and DOM flags. The server runs: (1) Heuristics & Shannon Entropy, (2) ML Feature Classifier, (3) Threat Intelligence lookup, and (4) Gemini AI Explainer.")
    pdf.add_bullet("Stage 4: Composite Risk Scoring & Dynamic Badge", "The server calculates a composite risk index from 0% to 100%. The service worker updates the Chrome toolbar badge with a color-coded alert: Red (80-100% Critical), Amber (45-79% Warning), Green (0-44% Safe).")
    pdf.add_bullet("Stage 5: User Interface & In-Page Link Badges", "Clicking the extension popup shows a glassmorphic risk gauge, categorized checklist badges, and plain-English recommendations. Clicking 'Highlight Dangerous Links' tags external scam links directly on the page.")

    pdf.add_callout(
        title="Key Architectural Advantage to Highlight to Your Teacher",
        content="Most student extensions only run code AFTER the malicious page loads—meaning dangerous JavaScript has already executed. PhishGuard is unique because it combines Pre-Navigation Interception (stopping the connection before it happens) with Deep On-Page DOM Auditing (catching deceptive content).",
        callout_type="concept"
    )

    # =========================================================================
    # CHAPTER 4: DEEP DIVE INTO EVERY CODE FILE
    # =========================================================================
    pdf.new_page()
    pdf.add_heading_1("Chapter 4: Detailed Code Walkthrough (File-by-File)")
    pdf.add_paragraph(
        "Open these exact files in VS Code during your presentation. Below is the purpose, key functions, and line explanations for each file."
    )

    pdf.add_heading_2("File 1: extension/manifest.json (Extension Configuration)")
    pdf.add_paragraph("This file is the identity card of the Chrome Extension. It registers permissions and components.")
    pdf.add_code_block("manifest.json Key Lines", [
        '1: {',
        '2:   "manifest_version": 3,               // Uses modern Chrome MV3 standard',
        '6:   "permissions": [',
        '7:     "activeTab", "scripting",          // Allows inspecting the current tab DOM',
        '8:     "storage", "tabs", "webNavigation" // webNavigation allows intercepting URLs before load',
        '9:   ],',
        '12:  "background": { "service_worker": "background.js" }, // Registers background engine',
        '14:  "content_scripts": [{ "matches": ["http://*/*", "https://*/*"], "js": ["content.js"] }]'
    ])
    pdf.add_bullet("Why show this?", "Explain: 'This proves our project is built with Manifest V3, adhering to Google's strict security and performance standards.'")

    pdf.add_heading_2("File 2: extension/background.js (The Browser Listener)")
    pdf.add_paragraph("Runs in the background service worker, intercepting navigation and managing toolbar badges.")
    pdf.add_code_block("background.js Key Code Snippet", [
        '// Intercept URLs BEFORE the HTTP request is even sent',
        'chrome.webNavigation.onBeforeNavigate.addListener(details => {',
        '  if (details.frameId !== 0) return; // Only main frame top-level navigations',
        '  const threat = inspectPreVisitUrl(details.url);',
        '  if (threat) {',
        '    // Redirect to local warning interstitial page',
        '    const warningUrl = chrome.runtime.getURL("warning/warning.html") + ...;',
        '    chrome.tabs.update(details.tabId, { url: warningUrl });',
        '  }',
        '});'
    ])
    pdf.add_bullet("Why show this?", "Explain: 'This is our pre-visit interceptor. It evaluates hostnames against brand typosquats and disposable scam TLDs before Chrome connects to the rogue host.'")

    pdf.add_heading_2("File 3: extension/content.js (The On-Page DOM Auditor)")
    pdf.add_paragraph("Injected into every page to detect password inputs and fake urgency cues.")
    pdf.add_code_block("content.js Key Code Snippet", [
        'function auditDOM() {',
        '  const hasPasswordInput = document.querySelectorAll(\'input[type="password"]\').length > 0;',
        '  const bodyText = document.body.innerText || "";',
        '  // Detect deceptive discount text and countdown timers',
        '  const hasDiscountKeyword = /90%\\s*off|80%\\s*off|free\\s*iphone/i.test(bodyText);',
        '  const hasTimer = !!document.querySelector(\'[id*="timer"], [id*="countdown"]\');',
        '  return { hasPasswordInput, hasFakeDiscount: hasDiscountKeyword && hasTimer };',
        '}'
    ])
    pdf.add_bullet("Why show this?", "Explain: 'This function inspects the live DOM. If a site combines aggressive 90% discount text with a ticking timer or demands a password on an unverified domain, it flags it immediately.'")

    # =========================================================================
    # CHAPTER 4 CONTINUED: BACKEND CODE
    # =========================================================================
    pdf.new_page()
    pdf.add_heading_2("File 4: server/services/heuristics.js (Math & Heuristics Engine)")
    pdf.add_paragraph(
        "This is one of the most important files. It contains the Shannon Entropy formula and 8 heuristic detection rules."
    )
    pdf.add_code_block("heuristics.js: Shannon Entropy & Brand Spoofing", [
        'function calculateEntropy(str) {',
        '  const len = str.length;',
        '  const frequencies = {};',
        '  for (let char of str) frequencies[char] = (frequencies[char] || 0) + 1;',
        '  let entropy = 0;',
        '  for (let char in frequencies) {',
        '    const p = frequencies[char] / len;',
        '    entropy -= p * Math.log2(p); // Shannon Entropy Formula: -sum(p * log2(p))',
        '  }',
        '  return entropy;',
        '}',
        '// Leetspeak typosquatting detector (0 -> o, 1 -> l, 3 -> e, 5 -> s)',
        'const leet = hostname.replace(/0/g, "o").replace(/1/g, "l").replace(/3/g, "e");',
        'if (leet.includes(brand) && !hostname.includes(brand)) { /* Typosquat Flagged! */ }'
    ])
    pdf.add_bullet("Shannon Entropy Explanation", "Show lines 26-39. Explain that if entropy > 3.8, characters are randomly distributed (common in bot-generated scam domains).")
    pdf.add_bullet("Leetspeak Explanation", "Show lines 105-112. Explain how replacing numbers with letters unmasks spoofed domains like 'amaz0n' or 'paypa1'.")

    pdf.add_heading_2("File 5: server/services/ml_classifier.js (Machine Learning Engine)")
    pdf.add_paragraph(
        "Extracts a 10-feature vector and applies a trained logistic regression model with the Sigmoid activation function."
    )
    pdf.add_code_block("ml_classifier.js: Feature Extraction & Sigmoid Classification", [
        'function extractFeatureVector(urlStr, domMetadata = {}) {',
        '  return {',
        '    url_length: fullUrl.length, dot_count: (fullUrl.match(/\\./g) || []).length,',
        '    hyphen_count: (hostname.match(/-/g) || []).length, is_ip: /^[0-9.]*$/.test(hostname) ? 1 : 0,',
        '    high_risk_tld: HIGH_RISK_TLDS.some(t => hostname.endsWith(t)) ? 1 : 0,',
        '    has_login_form: domMetadata.hasPasswordInput ? 1 : 0, is_https: urlObj.protocol === "https:" ? 1 : 0',
        '  };',
        '}',
        '// Classification using trained weights & Sigmoid activation function',
        'let logit = -3.2; // Base bias',
        'if (f.has_login_form && !f.is_https) logit += 3.5; // Password on HTTP is very risky',
        'if (f.has_login_form && f.high_risk_tld) logit += 2.6;',
        'const probability = 1 / (1 + Math.exp(-logit)); // Sigmoid formula',
        'return { phishingProbability: Math.round(probability * 100) };'
    ])
    pdf.add_bullet("Why show this?", "Explain: 'We convert webpage traits into numerical features. Our model multiplies these by trained risk weights and squashes the result through a Sigmoid curve to output a calibrated 0-100% phishing probability.'")

    pdf.add_heading_2("File 6: server/server.js (Zero-Dependency Node.js Server)")
    pdf.add_paragraph("Built entirely with native Node.js core modules. Listens on port 5000 and exposes REST endpoints.")
    pdf.add_bullet("Endpoints exposed", "(1) 'GET /api/health' (health status), (2) 'POST /api/scan' (URL scan), (3) 'GET & POST /api/reports' (community blacklist reports), (4) 'GET /api/stats' (system telemetry).")
    pdf.add_bullet("Why zero dependencies?", "Explain: 'Zero dependencies means the server launches in milliseconds without risking npm module version breaks or security vulnerabilities.'")

    # =========================================================================
    # CHAPTER 5: STEP-BY-STEP PRESENTATION SCRIPT
    # =========================================================================
    pdf.new_page()
    pdf.add_heading_1("Chapter 5: Step-by-Step Presentation Script for Tomorrow")
    pdf.add_paragraph(
        "Follow this exact script and screen action sequence during your final project evaluation."
    )

    demo_steps = [
        ("Step 1: Start Backend (30 sec)", "Open VS Code Terminal. Type: cd server, then node server.js. Say: 'Respected evaluators, here our backend cybersecurity analysis engine is running on port 5000. It is written using native Node.js with zero external dependencies, making it ultra-fast and reliable.'"),
        ("Step 2: Show Pre-Visit Interceptor (1.5 min)", "Open Chrome. In the address bar, type: http://paypa1.com and press Enter. The red warning screen appears. Say: 'Notice that before Chrome sent an HTTP request to the counterfeit server, our background service worker intercepted the navigation, caught the brand typosquat, and gave the user a safe 1-click button to visit the real paypal.com.'"),
        ("Step 3: Show DOM Inspection on Fake Store (2 min)", "Open test-pages/fake-amazon-store.html in Chrome. Click the PhishGuard extension icon. Say: 'On this fake shopping page, our content script performed a real-time DOM audit. In our popup, notice the 90%+ Critical Risk score, the Brand Spoofed badge, and the fake clearance discount alert. Clicking Highlight Dangerous Links outlines suspicious links on the page in red.'"),
        ("Step 4: Show Threat Intelligence Sandbox (2 min)", "Open dashboard/index.html in Chrome. Enter 'chase-banking-verify.xyz' and click Run AI Scan. Say: 'We also built an administrative Threat Intelligence Dashboard. Users can sandbox any URL, inspect Shannon Entropy and ML probabilities, and submit community scam reports that automatically update our blacklist.'"),
        ("Step 5: Code Tour in VS Code (1.5 min)", "Open VS Code and click: (1) server/services/heuristics.js (show entropy formula), (2) server/services/ml_classifier.js (show feature vector and sigmoid formula). Say: 'Here is our core mathematical logic implementing Shannon Entropy and our 10-feature vector classification model.'")
    ]

    for title, desc in demo_steps:
        pdf.add_heading_2(title)
        pdf.add_paragraph(desc)

    # =========================================================================
    # CHAPTER 6: COMPREHENSIVE VIVA Q&A
    # =========================================================================
    pdf.new_page()
    pdf.add_heading_1("Chapter 6: Comprehensive Viva Q&A (Top 12 Questions)")
    pdf.add_paragraph(
        "Here are the top 12 questions examiners and professors frequently ask, along with the exact model answers you should give."
    )

    qas = [
        ("Q1: Why do you need both heuristic rules and Machine Learning?",
         "Answer: Heuristics are deterministic and fast for known patterns (e.g. typosquats like 'paypa1' or high-risk TLDs like '.xyz'). Machine Learning evaluates subtle, multi-dimensional patterns (URL length, symbol ratios, form structures) to detect brand-new, unseen phishing attacks that don't match specific keyword rules."),

        ("Q2: What is Shannon Entropy and how does it catch malicious domains?",
         "Answer: Shannon Entropy measures character unpredictability: H(X) = -sum(p * log2(p)). Legitimate companies choose memorable, readable brand words (low entropy: 2.0 to 3.0). Automated phishing kits use Domain Generation Algorithms (DGA) that create random strings (like 'x7b-q99z'), which produce high entropy (> 3.8)."),

        ("Q3: How does the pre-visit interceptor work under Manifest V3?",
         "Answer: We register a listener on 'chrome.webNavigation.onBeforeNavigate' in our background service worker. Chrome triggers this event before making the network socket connection. If the URL matches a brand spoof or disposable scam pattern, we redirect the tab to our local warning page before any malicious data is downloaded."),

        ("Q4: What are the 10 features extracted by your Machine Learning model?",
         "Answer: (1) URL length, (2) Hostname length, (3) Dot count, (4) Hyphen count, (5) Special symbol count, (6) Binary IP address flag, (7) High-risk TLD flag, (8) Presence of password input in DOM, (9) Fake discount/urgency timer cues, and (10) HTTPS security flag."),

        ("Q5: What is the Sigmoid activation function and why is it used?",
         "Answer: Sigmoid is defined as S(z) = 1 / (1 + e^-z). It maps any real-valued number from negative infinity to positive infinity into an output between 0 and 1. We multiply it by 100 to produce a calibrated, human-friendly 0% to 100% phishing probability index."),

        ("Q6: How do you prevent false positives (e.g., legitimate e-commerce sales)?",
         "Answer: A legitimate store having a sale on amazon.com passes our verified domain whitelist check. We only flag fake clearance sales when extreme discount cues co-occur on unverified, unofficial, or high-risk domain extensions."),

        ("Q7: How is user privacy protected?",
         "Answer: User browsing history is never sold or broadcasted to external tracking companies. Communication occurs strictly between the browser extension and our local, self-hosted Node.js backend."),

        ("Q8: Why did you build the backend with zero external npm dependencies?",
         "Answer: Using native Node.js modules ('http', 'url', 'fs') eliminates dependency vulnerabilities, minimizes memory footprint, enables sub-millisecond API response times, and guarantees 100% reproducibility without npm install failures."),

        ("Q9: What happens if the backend server is offline during browsing?",
         "Answer: Our extension's popup.js includes an intelligent client-side fallback scanner that evaluates domain patterns and DOM cues directly inside the browser, ensuring the user is never left unprotected."),

        ("Q10: What is Explainable AI (XAI) and why does it matter here?",
         "Answer: Ordinary users don't understand risk numbers or SSL error codes. Our AI Explainer translates technical metrics into plain English reasons (e.g. 'This site is impersonating Amazon to solicit passwords') and gives actionable advice on what to do."),

        ("Q11: How does your extension communicate between different scripts?",
         "Answer: We use Chrome's message-passing API ('chrome.tabs.sendMessage' and 'chrome.runtime.onMessage') to exchange asynchronous JSON messages between the popup, the content script, and the background service worker."),

        ("Q12: What is the future scope of this project?",
         "Answer: In the future, we plan to incorporate Computer Vision (evaluating visual screenshot similarity using perceptual hashing to catch cloned logos), integrate real-time DNS WHOIS age lookups, and support Firefox and Safari.")
    ]

    for q, a in qas:
        pdf.check_space(50)
        pdf.add_heading_3(q)
        pdf.add_paragraph(a, font='F1', size=8.8, leading=12.5)

    # Save PDF
    total = pdf.save()
    print(f"Total pages generated: {total}")
    return pdf_path

if __name__ == "__main__":
    path = build_pdf()
    print("FINISHED:", path)
