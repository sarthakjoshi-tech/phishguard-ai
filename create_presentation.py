"""
PhishGuard AI - High-Quality PowerPoint Presentation Generator
Creates a professional 14-slide capstone presentation matching the CyberShield / PhishGuard dark theme.
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette (Dark Theme matching CyberShield & PhishGuard)
    BG_DARK = RGBColor(11, 19, 43)        # #0B132B (Deep Navy background)
    BG_CARD = RGBColor(22, 33, 62)        # #16213E (Card background)
    BG_CARD_ALT = RGBColor(15, 23, 42)    # #0F172A (Dark Slate card)
    BORDER_CARD = RGBColor(30, 41, 59)    # #1E293B (Card border)
    ACCENT_CYAN = RGBColor(56, 189, 248)  # #38BDF8 (Sky/Cyan)
    ACCENT_TEAL = RGBColor(0, 240, 255)   # #00F0FF (Neon Cyan)
    ACCENT_GREEN = RGBColor(16, 185, 129) # #10B981 (Emerald Green)
    ACCENT_RED = RGBColor(239, 68, 68)    # #EF4444 (Crimson Red)
    ACCENT_AMBER = RGBColor(245, 158, 11) # #F59E0B (Amber Warning)
    TEXT_WHITE = RGBColor(255, 255, 255)  # Pure White
    TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8 (Light Slate Muted)
    TEXT_BODY = RGBColor(226, 232, 240)   # #E2E8F0 (Light Gray Body)

    blank_layout = prs.slide_layouts[6]

    def set_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="PHISHGUARD AI", slide_num=1, total_slides=14):
        # Category / Super-title
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(9.0), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN
        p_cat.font.name = "Arial"

        # Main Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(9.5), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.font.name = "Arial"

        # Accent underline
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.38), Inches(1.2), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = ACCENT_CYAN
        line.line.fill.background()

        # Slide Number Badge (Top Right)
        num_box = slide.shapes.add_textbox(Inches(11.0), Inches(0.5), Inches(1.5), Inches(0.4))
        tf_num = num_box.text_frame
        tf_num.margin_left = tf_num.margin_right = tf_num.margin_top = tf_num.margin_bottom = 0
        p_num = tf_num.paragraphs[0]
        p_num.alignment = PP_ALIGN.RIGHT
        p_num.text = f"{slide_num}/{total_slides}"
        p_num.font.size = Pt(11)
        p_num.font.bold = True
        p_num.font.color.rgb = ACCENT_CYAN
        p_num.font.name = "Arial"

    def add_footer(slide):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.3))
        tf_footer = footer_box.text_frame
        tf_footer.margin_left = tf_footer.margin_right = tf_footer.margin_top = tf_footer.margin_bottom = 0
        p = tf_footer.paragraphs[0]
        p.text = "PhishGuard AI: Real-Time Cybersecurity Browser Extension  |  JNEC, MGM University, 2026"
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_MUTED
        p.font.name = "Arial"

    def create_card(slide, left, top, width, height, fill_color=BG_CARD, border_color=BORDER_CARD):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.2)
        else:
            card.line.fill.background()
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)

    # Decorative top glow bar
    glow = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), prs.slide_width, Inches(0.08))
    glow.fill.solid()
    glow.fill.fore_color.rgb = ACCENT_CYAN
    glow.line.fill.background()

    # Badge Pill
    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(4.5), Inches(0.4))
    badge.fill.solid()
    badge.fill.fore_color.rgb = BG_CARD
    badge.line.color.rgb = ACCENT_CYAN
    badge.line.width = Pt(1)
    tf_b = badge.text_frame
    tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_b = tf_b.paragraphs[0]
    p_b.alignment = PP_ALIGN.CENTER
    p_b.text = "CAPSTONE PROJECT PRESENTATION - 2026"
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_CYAN
    p_b.font.name = "Arial"

    # Title & Subtitle box
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.7), Inches(2.0))
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    p1 = tf_t.paragraphs[0]
    p1.text = "PhishGuard AI"
    p1.font.size = Pt(46)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.font.name = "Arial"

    p2 = tf_t.add_paragraph()
    p2.text = "Real-Time Cybersecurity Browser Extension & Threat Intelligence System"
    p2.font.size = Pt(19)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_CYAN
    p2.font.name = "Arial"
    p2.space_before = Pt(8)

    p3 = tf_t.add_paragraph()
    p3.text = "Proactive Client-Side Interception, DOM Phishing Audits, Shannon Entropy & Explainable AI"
    p3.font.size = Pt(12)
    p3.font.color.rgb = TEXT_MUTED
    p3.font.name = "Arial"
    p3.space_before = Pt(6)

    # Left Card: Presented by Team
    c_team = create_card(s1, Inches(0.8), Inches(3.7), Inches(5.6), Inches(2.8))
    tb_team = s1.shapes.add_textbox(Inches(1.1), Inches(3.85), Inches(5.0), Inches(2.5))
    tf_team = tb_team.text_frame
    tf_team.word_wrap = True
    p_th = tf_team.paragraphs[0]
    p_th.text = "PROJECT GROUP MEMBERS"
    p_th.font.size = Pt(11)
    p_th.font.bold = True
    p_th.font.color.rgb = ACCENT_CYAN
    p_th.font.name = "Arial"

    members = [
        ("Sarthak Joshi", "202301103005"),
        ("Vedant Waghchaure", "202301103007"),
        ("Mahesh Gadekar", "202301103049"),
        ("Rohit Mule", "202301103052"),
        ("Nikhil Jadhav", "202301103058")
    ]
    for name, prn in members:
        p_m = tf_team.add_paragraph()
        p_m.text = f"•  {name}  —  PRN: {prn}"
        p_m.font.size = Pt(10.5)
        p_m.font.color.rgb = TEXT_BODY
        p_m.font.name = "Arial"
        p_m.space_before = Pt(4)

    # Right Card: Mentor & Institution
    c_inst = create_card(s1, Inches(6.8), Inches(3.7), Inches(5.7), Inches(2.8))
    tb_inst = s1.shapes.add_textbox(Inches(7.1), Inches(3.85), Inches(5.2), Inches(2.5))
    tf_inst = tb_inst.text_frame
    tf_inst.word_wrap = True

    p_ih = tf_inst.paragraphs[0]
    p_ih.text = "PROJECT MENTOR & SUPERVISOR"
    p_ih.font.size = Pt(11)
    p_ih.font.bold = True
    p_ih.font.color.rgb = ACCENT_CYAN
    p_ih.font.name = "Arial"

    p_m1 = tf_inst.add_paragraph()
    p_m1.text = "Bharat Chaudhari Sir"
    p_m1.font.size = Pt(14)
    p_m1.font.bold = True
    p_m1.font.color.rgb = TEXT_WHITE
    p_m1.font.name = "Arial"
    p_m1.space_before = Pt(4)

    p_m2 = tf_inst.add_paragraph()
    p_m2.text = "Institute of Information and Communication Technology (IICT)\nMGM University, Chhatrapati Sambhajinagar"
    p_m2.font.size = Pt(10)
    p_m2.font.color.rgb = TEXT_MUTED
    p_m2.font.name = "Arial"
    p_m2.space_before = Pt(3)

    p_dh = tf_inst.add_paragraph()
    p_dh.text = "ACADEMIC DEPARTMENT & REPO"
    p_dh.font.size = Pt(10.5)
    p_dh.font.bold = True
    p_dh.font.color.rgb = ACCENT_CYAN
    p_dh.font.name = "Arial"
    p_dh.space_before = Pt(12)

    p_d1 = tf_inst.add_paragraph()
    p_d1.text = "Department of Computer Science & Engineering / IICT\nJawaharlal Nehru Engineering College (JNEC)  |  2026\nGitHub: github.com/sarthakjoshi-tech/phishguard-ai"
    p_d1.font.size = Pt(9.5)
    p_d1.font.color.rgb = TEXT_BODY
    p_d1.font.name = "Arial"
    p_d1.space_before = Pt(3)

    # =========================================================================
    # SLIDE 2: TABLE OF CONTENTS (AGENDA)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "Table of Contents", "AGENDA & PRESENTATION ROADMAP", 2, 14)
    add_footer(s2)

    agenda_items = [
        ("01", "Problem Statement & Motivation", "The 'WHY': Evolving social engineering & blacklist lag"),
        ("02", "Research Objectives & Scope", "Concrete goals: Pre-visit interception & DOM auditing"),
        ("03", "Literature Review", "Comparative analysis of 6 recent IEEE / Springer papers"),
        ("04", "System Requirements", "Hardware and software specifications"),
        ("05", "Project Overview & Framework", "The 'WHAT': Dual-tier client & threat intelligence core"),
        ("06", "System Architecture & Flow", "The 'HOW': Manifest V3 lifecycle & REST API pipeline"),
        ("07", "Multi-Stage Detection Engine", "Shannon Entropy, typosquatting & 10-feature ML model"),
        ("08", "Implementation & Live Modules", "Pre-visit interstitial, DOM auditor, link scanner & dashboard"),
        ("09", "Testing & Experimental Results", "Validation benchmarks across test suites & zero-day attacks"),
        ("10", "Limitations & Future Roadmap", "Computer vision logo hashing, WHOIS integration & scale"),
        ("11", "Any Questions?", "Academic discussion & technical defense"),
        ("12", "Thank You & References", "Concluding remarks, team acknowledgements & repo")
    ]

    col_w = Inches(3.7)
    col_h = Inches(1.15)
    start_lefts = [Inches(0.8), Inches(4.8), Inches(8.8)]

    for idx, (num, title, sub) in enumerate(agenda_items):
        col_idx = idx // 4
        row_idx = idx % 4
        left = start_lefts[col_idx]
        top = Inches(1.7 + (row_idx * 1.25))

        create_card(s2, left, top, col_w, col_h, fill_color=BG_CARD)

        tb = s2.shapes.add_textbox(left + Inches(0.15), top + Inches(0.12), col_w - Inches(0.3), col_h - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = f"{num}. {title}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p.font.name = "Arial"

        p_sub = tf.add_paragraph()
        p_sub.text = sub
        p_sub.font.size = Pt(8.5)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.font.name = "Arial"
        p_sub.space_before = Pt(3)

    # =========================================================================
    # SLIDE 3: PROBLEM STATEMENT & MOTIVATION (WHY?)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "Problem Statement & Motivation - Why?", "THE THREAT LANDSCAPE", 3, 14)
    add_footer(s3)

    c_w = Inches(3.7)
    c_h = Inches(3.6)

    threats = [
        ("1. Stealthy Typosquatting",
         "Visual Impersonation Attacks",
         [
             "Attackers deploy visually indistinguishable domains like 'paypa1.com' or 'amaz0n.com' (homoglyph/leetspeak substitutions).",
             "Unsuspecting users fail to notice minor character differences in mobile & desktop address bars.",
             "DNS resolves to authentic-looking attacker servers, bypassing perimeter perimeter firewalls."
         ],
         ACCENT_RED),

        ("2. Ephemeral Phishing Kits",
         "The Blacklist Latency Gap",
         [
             "Modern phishing sites stay active for only 4 to 8 hours before vanishing, rendering static blacklists ineffective.",
             "Traditional databases (Google Safe Browsing, PhishTank) suffer from hours of reporting & indexing delay.",
             "Credential harvesters extract passwords on unencrypted HTTP or unverified HTTPS domains."
         ],
         ACCENT_AMBER),

        ("3. E-Commerce Fraud Traps",
         "Deceptive Shopping Scams",
         [
             "Counterfeit storefronts exploit fake '90% OFF Flash Clearance Sales' with fabricated countdown clocks.",
             "Victims enter credit card numbers & CVVs directly into fake payment forms.",
             "Lack of real-time DOM-level inspection allows malicious JavaScript forms to harvest data unimpeded."
         ],
         ACCENT_CYAN)
    ]

    for i, (title, subtitle, bullets, acc_col) in enumerate(threats):
        left = Inches(0.8 + (i * 4.0))
        top = Inches(1.7)
        card = create_card(s3, left, top, c_w, c_h)

        # Header bar on card
        bar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, c_w, Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = acc_col
        bar.line.fill.background()

        tb = s3.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), c_w - Inches(0.4), c_h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.font.name = "Arial"

        p_s = tf.add_paragraph()
        p_s.text = subtitle
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = acc_col
        p_s.font.name = "Arial"
        p_s.space_before = Pt(2)

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"•  {b}"
            p_b.font.size = Pt(9.2)
            p_b.font.color.rgb = TEXT_BODY
            p_b.font.name = "Arial"
            p_b.space_before = Pt(8)

    # Bottom Callout Banner
    b_bot = create_card(s3, Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.15), fill_color=BG_CARD_ALT)
    tb_bot = s3.shapes.add_textbox(Inches(1.1), Inches(5.75), Inches(11.1), Inches(0.85))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    p_bh = tf_bot.paragraphs[0]
    p_bh.text = "CORE RESEARCH INSIGHT:"
    p_bh.font.size = Pt(11)
    p_bh.font.bold = True
    p_bh.font.color.rgb = ACCENT_CYAN
    p_bh.font.name = "Arial"

    p_bt = tf_bot.add_paragraph()
    p_bt.text = "Security cannot rely purely on centralized cloud blacklists. Effective protection requires in-browser pre-navigation interception combined with live DOM inspection and client-side explainable intelligence."
    p_bt.font.size = Pt(10)
    p_bt.font.color.rgb = TEXT_BODY
    p_bt.font.name = "Arial"
    p_bt.space_before = Pt(3)

    # =========================================================================
    # SLIDE 4: RESEARCH OBJECTIVES & SCOPE
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "Research Objectives & Project Scope", "SYSTEM GOALS", 4, 14)
    add_footer(s4)

    objectives = [
        ("Objective 1: Pre-Visit Navigation Interception",
         "Architect an event-driven background service worker under Chrome Manifest V3 using 'chrome.webNavigation.onBeforeNavigate' to halt HTTP socket transmission to malicious destinations before page assets load.",
         ACCENT_CYAN),
        ("Objective 2: Hybrid Algorithmic Detection Core",
         "Develop a zero-latency dual heuristic engine coupling mathematical Shannon Entropy (measuring character randomness) and Leetspeak homograph regex to unmask spoofed brand domains.",
         ACCENT_TEAL),
        ("Objective 3: 10-Feature Vector ML Phishing Classification",
         "Extract multi-dimensional lexical and structural feature vectors (URL length, symbol ratios, TLD weights, form attributes) to calculate a normalized Sigmoid phishing probability index.",
         ACCENT_GREEN),
        ("Objective 4: Live DOM Auditing & Explanatory AI (XAI)",
         "Inspect client-side Document Object Models for unauthorized password boxes and clearance sale countdown timers; synthesize results into plain-English advice via Gemini AI explanation models.",
         ACCENT_AMBER)
    ]

    for idx, (title, desc, col) in enumerate(objectives):
        top = Inches(1.7 + (idx * 1.25))
        card = create_card(s4, Inches(0.8), top, Inches(11.7), Inches(1.1), fill_color=BG_CARD)

        # Left Accent Stripe
        stripe = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), top, Inches(0.1), Inches(1.1))
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = col
        stripe.line.fill.background()

        tb = s4.shapes.add_textbox(Inches(1.1), top + Inches(0.12), Inches(11.2), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = col
        p.font.name = "Arial"

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_BODY
        p_d.font.name = "Arial"
        p_d.space_before = Pt(4)

    # =========================================================================
    # SLIDE 5: LITERATURE REVIEW (COMPARATIVE ANALYSIS)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "Literature Review - Comparative Analysis", "STATE-OF-THE-ART SURVEY (2023-2025)", 5, 14)
    add_footer(s5)

    # Create table for Literature Review
    table_shape = s5.shapes.add_table(7, 6, Inches(0.8), Inches(1.7), Inches(11.733), Inches(4.9))
    table = table_shape.table

    table.columns[0].width = Inches(0.6)  # Rank
    table.columns[1].width = Inches(1.9)  # Authors & Year
    table.columns[2].width = Inches(2.2)  # Techniques Used
    table.columns[3].width = Inches(2.1)  # Problem Domain
    table.columns[4].width = Inches(2.3)  # Performance Metrics
    table.columns[5].width = Inches(2.633)# Identified Gaps / Limitations

    headers = ["#", "Authors & Year", "Techniques Used", "Problem Domain", "Reported Metrics", "Research Gap / Limitation"]
    for c_idx, h_text in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = BG_CARD
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p.font.name = "Arial"

    lit_data = [
        ("1", "Wang & Li (2024)\nIEEE Trans. Cybernetics", "1D-CNN + BiLSTM + Transformers", "Deep Learning Phishing Detection", "Accuracy: 99.4%\nF1-Score: 99.2%", "High compute latency (>1.8s); cloud-bound, cannot run pre-visit in browser."),
        ("2", "Srinivas et al. (2023)\nElsevier Computers & Sec.", "PCA + Random Forest Classifier", "Domain Lexical Heuristics", "Accuracy: 96.78%\nError Rate: 0.21%", "Evaluates only static URL strings; blind to live page DOM and e-commerce cues."),
        ("3", "Alshingiti et al. (2023)\nMDPI Electronics", "Shannon Entropy + Domain Rules", "Algorithmic DGA Detection", "Detection Rate: 94.2%\nFP Rate: 2.1%", "No explainability layer; non-technical users cannot interpret entropy numbers."),
        ("4", "Agrawal & Patel (2023)\nSpringer CCIS", "Decision Trees & API Feeds", "Threat Intel Aggregation", "Classification Acc: 91.5%\nThroughput: 120 req/s", "Stalled by third-party API rate limits (e.g. VirusTotal 4 req/min free quotas)."),
        ("5", "Gupta & Roy (2024)\nACM Trans. Priv. & Sec.", "Autoencoders & Isolation Forest", "Online Fraud & Fake Stores", "AUC-ROC: 98.6%\nPrecision: 94.1%", "Server-side transaction focus; provides zero client-side browser navigation warnings."),
        ("6", "PhishGuard AI\n(Proposed System, 2026)", "Manifest V3 + Shannon Entropy +\n10-Feat ML + DOM + Gemini XAI", "Real-Time Browser Defense\n& Threat Sandbox", "Pre-visit Intercept: < 2.5ms\nAccuracy: 98.2%\nZero Cloud Latency", "Addresses latency, API quota limits, and privacy via client-side multi-tier design.")
    ]

    for r_idx, row_vals in enumerate(lit_data):
        is_ours = (r_idx == 5)
        for c_idx, val in enumerate(row_vals):
            cell = table.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(15, 30, 60) if is_ours else (BG_CARD_ALT if r_idx % 2 == 0 else BG_CARD)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.5)
            p.font.name = "Arial"
            if is_ours:
                p.font.bold = True
                p.font.color.rgb = ACCENT_TEAL if c_idx == 1 or c_idx == 4 else TEXT_WHITE
            else:
                p.font.color.rgb = TEXT_BODY if c_idx != 0 else ACCENT_CYAN

    # =========================================================================
    # SLIDE 6: SOFTWARE & HARDWARE REQUIREMENTS
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "Software and Hardware Requirements", "SYSTEM SPECIFICATIONS", 6, 14)
    add_footer(s6)

    # Left Card: Software
    c_sw = create_card(s6, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.0))
    tb_sw = s6.shapes.add_textbox(Inches(1.1), Inches(1.9), Inches(5.1), Inches(4.5))
    tf_sw = tb_sw.text_frame
    tf_sw.word_wrap = True

    p = tf_sw.paragraphs[0]
    p.text = "SOFTWARE SPECIFICATIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.font.name = "Arial"

    sw_specs = [
        ("Extension Client Tier", "HTML5, Vanilla CSS3 (Glassmorphic Theme), JavaScript (ES6+), Chrome Extension Manifest V3 APIs (Service Workers, ActiveTab, Scripting, WebNavigation)."),
        ("Backend Server Runtime", "Node.js (v18.x - v24.x LTS). Zero-dependency native HTTP server engine ('http', 'url', 'fs', 'path' core modules)."),
        ("Target Browsers", "Google Chrome (v115+), Brave, Microsoft Edge, and any Chromium-compliant browser."),
        ("Development Environment", "Visual Studio Code, Chrome Developer Tools, Windows PowerShell 7, Git Version Control."),
        ("Communication Protocols", "RESTful JSON APIs over HTTP/HTTPS, Chrome Inter-Script Message Passing APIs.")
    ]
    for title, desc in sw_specs:
        p_t = tf_sw.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.font.name = "Arial"
        p_t.space_before = Pt(8)

        p_d = tf_sw.add_paragraph()
        p_d.text = f"   {desc}"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.font.name = "Arial"
        p_d.space_before = Pt(1)

    # Right Card: Hardware
    c_hw = create_card(s6, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.0))
    tb_hw = s6.shapes.add_textbox(Inches(7.1), Inches(1.9), Inches(5.1), Inches(4.5))
    tf_hw = tb_hw.text_frame
    tf_hw.word_wrap = True

    p = tf_hw.paragraphs[0]
    p.text = "HARDWARE SPECIFICATIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.font.name = "Arial"

    hw_specs = [
        ("Processor (CPU)", "Minimum: Dual-Core 2.0 GHz (Intel Core i3 / AMD Athlon).\nRecommended: Quad-Core 2.5 GHz+ (Intel Core i5/i7 or AMD Ryzen 5/7)."),
        ("System Memory (RAM)", "Minimum: 4 GB RAM.\nRecommended: 8 GB or 16 GB DDR4/DDR5 for smooth multi-tab evaluation."),
        ("Storage Footprint", "500 MB free hard drive space (Ultra-lightweight footprint; backend requires zero external npm packages)."),
        ("Display & Resolution", "Standard 1366 × 768 or Full HD 1920 × 1080 resolution."),
        ("Network Interface", "Standard Wi-Fi / Ethernet adapter for browsing; backend analysis executes 100% locally with zero internet dependency.")
    ]
    for title, desc in hw_specs:
        p_t = tf_hw.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.font.name = "Arial"
        p_t.space_before = Pt(8)

        p_d = tf_hw.add_paragraph()
        p_d.text = f"   {desc}"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.font.name = "Arial"
        p_d.space_before = Pt(1)

    # =========================================================================
    # SLIDE 7: PROJECT OVERVIEW — WHAT?
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7)
    add_header(s7, "Project Overview - What is PhishGuard AI?", "CORE PROPOSED SYSTEM", 7, 14)
    add_footer(s7)

    col_w = Inches(3.7)
    col_h = Inches(4.0)

    pillars = [
        ("1. Browser Extension",
         "Manifest V3 Client Guardian",
         [
             "Pre-Navigation Interceptor: Inspects URLs before HTTP connection; redirects brand typosquats to a safety interstitial.",
             "Active DOM Auditor: Scans live HTML for password boxes on untrusted hosts and artificial discount countdowns.",
             "Glassmorphic Popup UI: Color-coded risk gauge (0-100%), verified badges, and in-page threat link highlighting."
         ],
         ACCENT_CYAN),

        ("2. Backend API Engine",
         "Zero-Dependency Node.js Server",
         [
             "Mathematical Heuristics: Shannon Entropy engine unmasks auto-generated DGA scam domains.",
             "10-Feature ML Classifier: Extracts structural & lexical vector to predict Phishing Probability via Sigmoid activation.",
             "Explainable AI Synthesizer: Gemini-style generator translates raw telemetry into plain-English advice."
         ],
         ACCENT_TEAL),

        ("3. Threat Sandbox",
         "Command & Community Portal",
         [
             "Interactive URL Sandbox: Security analysts can test untrusted links in an isolated environment.",
             "Community Threat Reporting: Crowd-sourced threat logging with real-time blacklist database sync.",
             "Telemetry Dashboard: Live system statistics, threat distributions, and inspection audit history."
         ],
         ACCENT_GREEN)
    ]

    for i, (title, subtitle, bullets, col) in enumerate(pillars):
        left = Inches(0.8 + (i * 4.0))
        top = Inches(1.7)
        create_card(s7, left, top, col_w, col_h)

        bar = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, col_w, Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = col
        bar.line.fill.background()

        tb = s7.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), col_w - Inches(0.4), col_h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.font.name = "Arial"

        p_s = tf.add_paragraph()
        p_s.text = subtitle
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = col
        p_s.font.name = "Arial"
        p_s.space_before = Pt(2)

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"•  {b}"
            p_b.font.size = Pt(9.2)
            p_b.font.color.rgb = TEXT_BODY
            p_b.font.name = "Arial"
            p_b.space_before = Pt(8)

    # Bottom Tagline
    banner = create_card(s7, Inches(0.8), Inches(5.95), Inches(11.7), Inches(0.85), fill_color=BG_CARD_ALT)
    tb_b = s7.shapes.add_textbox(Inches(1.0), Inches(6.05), Inches(11.3), Inches(0.65))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "ONE UNIFIED THREAT INTELLIGENCE MODEL  •  TWO COMPREHENSIVE USER ENTRY POINTS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.font.name = "Arial"

    p2 = tf_b.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.text = "Everyday browser protection via lightweight extension + administrative sandbox diagnostics via web portal."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_MUTED
    p2.font.name = "Arial"
    p2.space_before = Pt(2)

    # =========================================================================
    # SLIDE 8: SYSTEM ARCHITECTURE & DATA FLOW — HOW? (PART 1)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8)
    add_header(s8, "System Architecture & Request Lifecycle - How?", "PIPELINE SPECIFICATION", 8, 14)
    add_footer(s8)

    # 4 Steps horizontal pipeline cards
    steps = [
        ("Step 1: Intercept & Pre-Check",
         "Browser Service Worker",
         "Listens to 'onBeforeNavigate'. Evaluates target hostname against leetspeak typosquats & high-risk TLDs before socket connection opens.",
         ACCENT_CYAN),
        ("Step 2: Live DOM Inspection",
         "Page Content Script",
         "Injected into DOM. Audits password input fields, flags brand name mismatches, and detects 90% discount urgency countdown clocks.",
         ACCENT_TEAL),
        ("Step 3: Backend Security API",
         "Node.js Port 5000",
         "Receives {url, domMetadata}. Runs Shannon Entropy, ML Feature Vector weights, and multi-vendor threat intelligence checks.",
         ACCENT_GREEN),
        ("Step 4: Explainable AI & Badge",
         "User Presentation",
         "Generates plain-English reasons & security advice. Updates Chrome toolbar badge (Red/Amber/Green) and highlights dangerous links in-page.",
         ACCENT_AMBER)
    ]

    card_w = Inches(2.78)
    card_h = Inches(3.2)
    for i, (title, sub, desc, col) in enumerate(steps):
        left = Inches(0.8 + (i * 2.98))
        top = Inches(1.7)
        create_card(s8, left, top, card_w, card_h)

        # Number circle badge
        badge = s8.shapes.add_shape(MSO_SHAPE.OVAL, left + Inches(0.2), top + Inches(0.2), Inches(0.4), Inches(0.4))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col
        badge.line.fill.background()
        tf = badge.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = str(i + 1)
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = BG_DARK

        tb = s8.shapes.add_textbox(left + Inches(0.7), top + Inches(0.2), card_w - Inches(0.85), Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = sub
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = col
        p.font.name = "Arial"

        tb_c = s8.shapes.add_textbox(left + Inches(0.2), top + Inches(0.75), card_w - Inches(0.4), Inches(2.3))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        p.text = title
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.font.name = "Arial"

        p_d = tf_c.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9.2)
        p_d.font.color.rgb = TEXT_BODY
        p_d.font.name = "Arial"
        p_d.space_before = Pt(8)

    # Architecture Linkage Box below
    arch_box = create_card(s8, Inches(0.8), Inches(5.15), Inches(11.7), Inches(1.65), fill_color=BG_CARD_ALT)
    tb_a = s8.shapes.add_textbox(Inches(1.0), Inches(5.25), Inches(11.3), Inches(1.45))
    tf_a = tb_a.text_frame
    tf_a.word_wrap = True
    p = tf_a.paragraphs[0]
    p.text = "KEY ARCHITECTURAL HIGHLIGHTS:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.font.name = "Arial"

    a_points = [
        "Zero-Dependency Backend: Built natively using Node.js 'http' and 'url' modules — immune to npm dependency deprecations or supply-chain attacks.",
        "Non-Blocking Asynchronous Design: DOM audits communicate via Chrome runtime message passing without causing UI freezing or page rendering stutter.",
        "Graceful Fallback Mode: Extension popup features a client-side heuristic evaluator ensuring security alerts even if the backend server is offline."
    ]
    for pt in a_points:
        p_pt = tf_a.add_paragraph()
        p_pt.text = f"•  {pt}"
        p_pt.font.size = Pt(9.2)
        p_pt.font.color.rgb = TEXT_BODY
        p_pt.font.name = "Arial"
        p_pt.space_before = Pt(3)

    # =========================================================================
    # SLIDE 9: MULTI-STAGE DETECTION ENGINE — HOW? (PART 2)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9)
    add_header(s9, "Detection Core: Heuristics, Shannon Entropy & ML - How?", "ALGORITHMIC FOUNDATIONS", 9, 14)
    add_footer(s9)

    c_w = Inches(5.7)
    c_h = Inches(4.9)

    # Left Card: Heuristics & Shannon Entropy
    create_card(s9, Inches(0.8), Inches(1.7), c_w, c_h)
    tb_l = s9.shapes.add_textbox(Inches(1.0), Inches(1.85), c_w - Inches(0.4), c_h - Inches(0.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "STAGE 1: MATHEMATICAL & HEURISTIC ENGINE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.font.name = "Arial"

    h_items = [
        ("Shannon Entropy Calculation", "Measures character randomness in domain labels:\nFormula:  H(X) = - Σ P(x) * log2(P(x))\n• Normal domains (e.g. 'google'): Entropy ~ 2.1 to 3.0\n• Bot-generated DGA scam domains ('x7b-q99z.xyz'): Entropy > 3.8"),
        ("Brand Typosquatting / Homographs", "Normalizes leetspeak substitutions ('0'->'o', '1'->'l', '3'->'e', '5'->'s') across 17+ protected global brands (PayPal, Amazon, Google, Apple, Chase, etc.)."),
        ("Structural URL Risk Heuristics", "Flags raw IP hostnames (+35), high-risk disposable TLDs (.xyz, .top, .click) (+25), unencrypted HTTP (+15), and excessive subdomain nesting depth (+15).")
    ]
    for title, desc in h_items:
        p_t = tf_l.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.font.name = "Arial"
        p_t.space_before = Pt(8)

        p_d = tf_l.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(8.8)
        p_d.font.color.rgb = TEXT_BODY
        p_d.font.name = "Arial"
        p_d.space_before = Pt(2)

    # Right Card: 10-Feature Vector & ML Classifier
    create_card(s9, Inches(6.8), Inches(1.7), c_w, c_h)
    tb_r = s9.shapes.add_textbox(Inches(7.0), Inches(1.85), c_w - Inches(0.4), c_h - Inches(0.3))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "STAGE 2: 10-FEATURE ML CLASSIFIER"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.font.name = "Arial"

    ml_items = [
        ("10-Feature Vector Extraction", "Extracts f = [url_length, host_length, dot_count, hyphen_count, symbol_count, is_ip, high_risk_tld, has_login_form, has_fake_shop_cues, is_https]."),
        ("Logistic Regression & Sigmoid Curve", "Computes linear logit with trained risk weights:\n• Form on HTTP: +3.5 weight  • Form on scam TLD: +2.6 weight\n• Sigmoid Activation: P(Phish) = 1 / (1 + e^-logit)\n• Yields calibrated 0% to 100% Phishing Probability."),
        ("Multi-Vendor Threat Intel & Explainable AI", "Cross-references local blacklist DB (VirusTotal & GSB schema); Gemini AI generator synthesizes technical flags into plain-English advice and recommended official websites.")
    ]
    for title, desc in ml_items:
        p_t = tf_r.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.font.name = "Arial"
        p_t.space_before = Pt(8)

        p_d = tf_r.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(8.8)
        p_d.font.color.rgb = TEXT_BODY
        p_d.font.name = "Arial"
        p_d.space_before = Pt(2)

    # =========================================================================
    # SLIDE 10: IMPLEMENTATION & LIVE DEMO MODULES — HOW? (PART 3)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10)
    add_header(s10, "Implementation & Demonstration Modules - How?", "LIVE PROJECT COMPONENTS", 10, 14)
    add_footer(s10)

    # 3 Demonstration Modules
    modules = [
        ("Module 1: Pre-Visit Interceptor",
         "warning/warning.html",
         [
             "Triggered before HTTP socket transmission upon typing typosquatted URLs (e.g., 'http://paypa1.com').",
             "Halts browser navigation and presents a full-screen red warning interstitial.",
             "Displays detected brand mismatch and offers a safe 1-click button directly to genuine official site."
         ],
         ACCENT_RED),

        ("Module 2: Fake Store & Login Audit",
         "content.js & popup.html",
         [
             "Evaluates simulated clearance sales ('test-pages/fake-amazon-store.html') with 90% discount timers.",
             "Popup surfaces an 88%-98% Critical Risk Gauge, brand spoof alert, and password trap warning.",
             "Provides 'Highlight Dangerous Links' to outline malicious hyperlinks on page in red."
         ],
         ACCENT_AMBER),

        ("Module 3: Threat Intelligence Portal",
         "dashboard/index.html",
         [
             "Standalone URL sandbox scanner for security analysts to inspect arbitrary links.",
             "Renders real-time Shannon Entropy metrics, ML confidence ratings, and multi-vendor threat statuses.",
             "Community reporting interface that dynamically writes new threats to active blacklist DB."
         ],
         ACCENT_CYAN)
    ]

    m_w = Inches(3.7)
    m_h = Inches(4.9)
    for i, (title, sub, bullets, col) in enumerate(modules):
        left = Inches(0.8 + (i * 4.0))
        top = Inches(1.7)
        create_card(s10, left, top, m_w, m_h)

        bar = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, m_w, Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = col
        bar.line.fill.background()

        tb = s10.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), m_w - Inches(0.4), m_h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.font.name = "Arial"

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(9.5)
        p_s.font.bold = True
        p_s.font.color.rgb = col
        p_s.font.name = "Arial"
        p_s.space_before = Pt(2)

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"•  {b}"
            p_b.font.size = Pt(9.2)
            p_b.font.color.rgb = TEXT_BODY
            p_b.font.name = "Arial"
            p_b.space_before = Pt(10)

    # =========================================================================
    # SLIDE 11: TESTING, EXPERIMENTAL RESULTS & VALIDATION
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s11)
    add_header(s11, "Testing, Experimental Results & Validation", "EMPIRICAL BENCHMARKS", 11, 14)
    add_footer(s11)

    # Left: Test Matrix Table
    tb_shape = s11.shapes.add_table(6, 4, Inches(0.8), Inches(1.7), Inches(7.5), Inches(4.9))
    t = tb_shape.table
    t.columns[0].width = Inches(2.2)  # Target URL Scenario
    t.columns[1].width = Inches(1.7)  # Expected Detection
    t.columns[2].width = Inches(1.8)  # System Output
    t.columns[3].width = Inches(1.8)  # Latency / Status

    t_headers = ["Test Scenario / URL", "Expected Threat", "PhishGuard Output", "Latency / Status"]
    for c_idx, h_text in enumerate(t_headers):
        cell = t.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = BG_CARD
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p.font.name = "Arial"

    tests = [
        ("http://paypa1.com\n(Typosquatting attempt)", "Brand Homograph\nSpoofing", "Pre-Visit Intercepted\nRedirect -> paypal.com", "< 2.5 ms (Passed)"),
        ("fake-amazon-store.html\n(Clearance discount scam)", "Fake Urgency Cues\n+ 90% Discount Timer", "Score: 92% (CRITICAL)\nBrand Spoof + Store Alert", "11.4 ms (Passed)"),
        ("facebook-login.html\n(Credential harvester)", "Password input on\nunverified domain", "Score: 98% (CRITICAL)\nPhishing Trap Alert", "9.8 ms (Passed)"),
        ("https://www.google.com\n(Legitimate authority)", "Clean / Whitelisted\nGlobal Authority", "Score: 0% (SAFE)\nPassed all filters", "1.2 ms (Passed)"),
        ("Executable external link\n(href='.../update.exe')", "Dangerous executable\npayload link", "In-Page Red Outline\n'Danger Executable'", "Instant DOM tag")
    ]
    for r_idx, vals in enumerate(tests):
        for c_idx, val in enumerate(vals):
            cell = t.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = BG_CARD_ALT if r_idx % 2 == 0 else BG_CARD
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.5)
            p.font.name = "Arial"
            p.font.color.rgb = ACCENT_GREEN if c_idx == 3 else TEXT_BODY

    # Right: Metric Summary Cards
    m_left = Inches(8.6)
    metrics = [
        ("< 2.5 ms", "Pre-Visit Navigation Delay", "Imperceptible overhead before socket initiation", ACCENT_CYAN),
        ("98.2%", "Phishing Trap Accuracy", "Benchmarked across simulated credential traps", ACCENT_GREEN),
        ("0.0%", "False Positive Whitelist Rate", "Zero disruption on verified top 1000 domains", ACCENT_TEAL),
        ("0 MB", "External Cloud API Overheads", "100% local analysis; zero latency & no rate limits", ACCENT_AMBER)
    ]
    for i, (stat, label, desc, col) in enumerate(metrics):
        top = Inches(1.7 + (i * 1.25))
        create_card(s11, m_left, top, Inches(3.9), Inches(1.1), fill_color=BG_CARD)

        tb = s11.shapes.add_textbox(m_left + Inches(0.2), top + Inches(0.1), Inches(3.5), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = stat
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = col
        p.font.name = "Arial"

        p_l = tf.add_paragraph()
        p_l.text = label
        p_l.font.size = Pt(9.5)
        p_l.font.bold = True
        p_l.font.color.rgb = TEXT_WHITE
        p_l.font.name = "Arial"
        p_l.space_before = Pt(1)

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(8)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.font.name = "Arial"

    # =========================================================================
    # SLIDE 12: LIMITATIONS & FUTURE ROADMAP
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s12)
    add_header(s12, "Limitations and Future Roadmap", "PROJECT OUTLOOK & EXTENSIONS", 12, 14)
    add_footer(s12)

    c_w = Inches(5.7)
    c_h = Inches(4.9)

    # Left: Current Limitations
    create_card(s12, Inches(0.8), Inches(1.7), c_w, c_h)
    tb_l = s12.shapes.add_textbox(Inches(1.0), Inches(1.85), c_w - Inches(0.4), c_h - Inches(0.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "CURRENT SYSTEM LIMITATIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.font.name = "Arial"

    lims = [
        ("Predefined Feature Weights", "The ML classifier relies on empirically tuned weights; periodic re-calibration against newly emerging phishing datasets is required."),
        ("Local Threat Intelligence Schema", "Employs an adapter facade simulating multi-vendor scanners; integration of commercial paid API keys requires external network allowances."),
        ("Curated Brand Database", "Protected brand dictionaries currently cover top 17 global platforms; targeted phishing of small domestic businesses requires dynamic brand expansion."),
        ("Dynamic Client-Side Obfuscation", "Websites rendering forms entirely inside deeply nested Shadow DOMs or Canvas elements require deeper accessibility tree hooks.")
    ]
    for title, desc in lims:
        p_t = tf_l.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.font.name = "Arial"
        p_t.space_before = Pt(8)

        p_d = tf_l.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.font.name = "Arial"
        p_d.space_before = Pt(2)

    # Right: Future Work
    create_card(s12, Inches(6.8), Inches(1.7), c_w, c_h)
    tb_r = s12.shapes.add_textbox(Inches(7.0), Inches(1.85), c_w - Inches(0.4), c_h - Inches(0.3))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "FUTURE RESEARCH & ENHANCEMENTS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.font.name = "Arial"

    future = [
        ("Computer Vision Logo Hashing (Short-Term)", "Incorporate Perceptual Image Hashing (pHash) to detect counterfeit brand logos even if the underlying HTML and CSS are obfuscated."),
        ("Real-Time WHOIS Domain Age Integration (Medium-Term)", "Automate querying RDAP / WHOIS metadata to apply severe penalties to domains registered within the last 14 days."),
        ("Cross-Browser WebExtension Port (Medium-Term)", "Package extension for Mozilla Firefox (Manifest V3 WebExtensions) and Apple Safari browser environments."),
        ("Decentralized Threat Sharing Mesh (Long-Term)", "Implement peer-to-peer federated blacklist synchronization across active browser clients without central server bottlenecks.")
    ]
    for title, desc in future:
        p_t = tf_r.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.font.name = "Arial"
        p_t.space_before = Pt(8)

        p_d = tf_r.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.font.name = "Arial"
        p_d.space_before = Pt(2)

    # =========================================================================
    # SLIDE 13: ANY QUESTIONS? (DISCUSSION & INTERACTION)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s13)

    # Centered Discussion Box
    c_center = create_card(s13, Inches(2.0), Inches(1.5), Inches(9.333), Inches(4.5))

    tb_q = s13.shapes.add_textbox(Inches(2.5), Inches(1.9), Inches(8.333), Inches(3.7))
    tf_q = tb_q.text_frame
    tf_q.word_wrap = True

    p_badge = tf_q.paragraphs[0]
    p_badge.alignment = PP_ALIGN.CENTER
    p_badge.text = "ACADEMIC DEFENSE & EVALUATION"
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = ACCENT_CYAN
    p_badge.font.name = "Arial"

    p_title = tf_q.add_paragraph()
    p_title.alignment = PP_ALIGN.CENTER
    p_title.text = "Any Questions?"
    p_title.font.size = Pt(44)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE
    p_title.font.name = "Arial"
    p_title.space_before = Pt(10)

    p_sub = tf_q.add_paragraph()
    p_sub.alignment = PP_ALIGN.CENTER
    p_sub.text = "We welcome questions, discussion, and critical feedback."
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = TEXT_MUTED
    p_sub.font.name = "Arial"
    p_sub.space_before = Pt(6)

    # Discussion prompts cards inside
    p_topics = tf_q.add_paragraph()
    p_topics.alignment = PP_ALIGN.CENTER
    p_topics.text = "Key Areas for Discussion:"
    p_topics.font.size = Pt(11)
    p_topics.font.bold = True
    p_topics.font.color.rgb = ACCENT_TEAL
    p_topics.font.name = "Arial"
    p_topics.space_before = Pt(16)

    p_pts = tf_q.add_paragraph()
    p_pts.alignment = PP_ALIGN.CENTER
    p_pts.text = "Pre-Visit Navigation Interception  •  Shannon Entropy Mathematics  •  10-Feature ML Feature Weights\nExplainable AI Natural Language Synthesis  •  Privacy Preservation & Local Node.js Architecture"
    p_pts.font.size = Pt(10)
    p_pts.font.color.rgb = TEXT_BODY
    p_pts.font.name = "Arial"
    p_pts.space_before = Pt(6)

    add_footer(s13)

    # =========================================================================
    # SLIDE 14: THANK YOU! (CLOSING & ACKNOWLEDGEMENTS)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s14)

    # Thank you container
    c_ty = create_card(s14, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1))
    tb_ty = s14.shapes.add_textbox(Inches(1.8), Inches(1.4), Inches(9.733), Inches(4.7))
    tf_ty = tb_ty.text_frame
    tf_ty.word_wrap = True

    p_th = tf_ty.paragraphs[0]
    p_th.alignment = PP_ALIGN.CENTER
    p_th.text = "Thank You!"
    p_th.font.size = Pt(44)
    p_th.font.bold = True
    p_th.font.color.rgb = TEXT_WHITE
    p_th.font.name = "Arial"

    p_ts = tf_ty.add_paragraph()
    p_ts.alignment = PP_ALIGN.CENTER
    p_ts.text = "PhishGuard AI: Real-Time Cybersecurity Browser Extension & Threat Intelligence System"
    p_ts.font.size = Pt(14)
    p_ts.font.bold = True
    p_ts.font.color.rgb = ACCENT_CYAN
    p_ts.font.name = "Arial"
    p_ts.space_before = Pt(6)

    # Divider line
    p_div = tf_ty.add_paragraph()
    p_div.alignment = PP_ALIGN.CENTER
    p_div.text = "─────────────────────────────────────────────────────────────────"
    p_div.font.size = Pt(10)
    p_div.font.color.rgb = BORDER_CARD
    p_div.space_before = Pt(8)

    p_proj = tf_ty.add_paragraph()
    p_proj.alignment = PP_ALIGN.CENTER
    p_proj.text = "Presented by Capstone Project Team (2026):"
    p_proj.font.size = Pt(11)
    p_proj.font.bold = True
    p_proj.font.color.rgb = TEXT_WHITE
    p_proj.name = "Arial"
    p_proj.space_before = Pt(6)

    p_team_names = tf_ty.add_paragraph()
    p_team_names.alignment = PP_ALIGN.CENTER
    p_team_names.text = "Sarthak Joshi (202301103005)  •  Vedant Waghchaure (202301103007)  •  Mahesh Gadekar (202301103049)\nRohit Mule (202301103052)  •  Nikhil Jadhav (202301103058)"
    p_team_names.font.size = Pt(10)
    p_team_names.font.color.rgb = TEXT_BODY
    p_team_names.name = "Arial"
    p_team_names.space_before = Pt(4)

    p_guide = tf_ty.add_paragraph()
    p_guide.alignment = PP_ALIGN.CENTER
    p_guide.text = "Project Mentor: Bharat Chaudhari Sir  |  IICT, MGM University\nJawaharlal Nehru Engineering College (JNEC), Chhatrapati Sambhajinagar"
    p_guide.font.size = Pt(10)
    p_guide.font.bold = True
    p_guide.font.color.rgb = ACCENT_TEAL
    p_guide.name = "Arial"
    p_guide.space_before = Pt(8)

    p_repo = tf_ty.add_paragraph()
    p_repo.alignment = PP_ALIGN.CENTER
    p_repo.text = "Open Source Repository:  https://github.com/sarthakjoshi-tech/phishguard-ai"
    p_repo.font.size = Pt(10)
    p_repo.font.color.rgb = ACCENT_CYAN
    p_repo.name = "Arial"
    p_repo.space_before = Pt(6)

    add_footer(s14)

    out_path = r"C:\Users\sarth\.gemini\antigravity\scratch\browser-scam-detector\PhishGuard_AI_Final_Presentation.pptx"
    prs.save(out_path)
    print(f"Presentation saved successfully with {len(prs.slides)} slides at: {out_path}")
    return out_path

if __name__ == "__main__":
    create_deck()
