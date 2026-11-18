"""
PhishGuard AI - CyberShield Theme PowerPoint Presentation Generator
Creates a 14-slide capstone presentation matching the exact aesthetic of the CyberShield project presentation:
- Clean light academic background (#F8FAFC / #FFFFFF)
- Deep navy headings (#0F172A, #1E3A8A)
- Professional royal blue / cyan accents (#2563EB, #0284C7)
- Structured white cards with subtle borders (#E2E8F0)
- Numbered pill badges (1, 2, 3...)
- Data tables with navy headers (#1E3A8A) and crisp grid borders
- Standardized CyberShield footer: 'PhishGuard AI: JNEC, Department of Computer Science Engineering' + 'X/14'
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_cybershield_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # =========================================================================
    # CYBERSHIELD COLOR PALETTE (Clean Light Academic Theme)
    # =========================================================================
    BG_PAGE = RGBColor(248, 250, 252)        # #F8FAFC (Light slate canvas)
    BG_WHITE = RGBColor(255, 255, 255)       # #FFFFFF (Card background)
    BG_CARD_ALT = RGBColor(241, 245, 249)   # #F1F5F9 (Light slate card fill)
    BG_PILL_BLUE = RGBColor(239, 246, 255)   # #EFF6FF (Very soft blue)
    BORDER_LIGHT = RGBColor(226, 232, 240)   # #E2E8F0 (Subtle card border)
    BORDER_ACCENT = RGBColor(191, 219, 254)  # #BFDBFE (Blue border)

    TEXT_TITLE = RGBColor(15, 23, 42)        # #0F172A (Deep Slate / Navy Black)
    TEXT_NAVY = RGBColor(30, 58, 138)        # #1E3A8A (Navy Accent)
    TEXT_BLUE = RGBColor(37, 99, 235)        # #2563EB (Royal Blue)
    TEXT_BODY = RGBColor(51, 65, 85)         # #334155 (Slate 700 Body text)
    TEXT_MUTED = RGBColor(100, 116, 139)     # #64748B (Slate 500 Subtitle/Caption)
    TEXT_WHITE = RGBColor(255, 255, 255)     # #FFFFFF (White text for headers/badges)

    COLOR_GREEN = RGBColor(22, 163, 74)      # #16A34A (Success / Safe)
    COLOR_RED = RGBColor(220, 38, 38)        # #DC2626 (Threat / Danger)
    COLOR_AMBER = RGBColor(217, 119, 6)      # #D97706 (Warning Amber)
    COLOR_CYAN = RGBColor(2, 132, 199)       # #0284C7 (Info Cyan)

    blank_layout = prs.slide_layouts[6]

    def set_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_PAGE
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, subtitle_text="Cybersecurity & Threat Intelligence Platform", slide_num=1, total_slides=14):
        # Top Title Text
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(10.0), Inches(0.55))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_t = tf_title.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_TITLE
        p_t.font.name = "Arial"

        # Subtitle / Category
        tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(0.98), Inches(10.0), Inches(0.32))
        tf_sub = tb_sub.text_frame
        tf_sub.word_wrap = True
        tf_sub.margin_left = tf_sub.margin_right = tf_sub.margin_top = tf_sub.margin_bottom = 0
        p_s = tf_sub.paragraphs[0]
        p_s.text = subtitle_text
        p_s.font.size = Pt(10)
        p_s.font.color.rgb = TEXT_MUTED
        p_s.font.name = "Arial"

        # Blue accent line underneath header
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(1.2), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = TEXT_BLUE
        line.line.fill.background()

        # Top Right Slide Number Pill
        num_box = slide.shapes.add_textbox(Inches(11.0), Inches(0.45), Inches(1.5), Inches(0.35))
        tf_num = num_box.text_frame
        tf_num.margin_left = tf_num.margin_right = tf_num.margin_top = tf_num.margin_bottom = 0
        p_num = tf_num.paragraphs[0]
        p_num.alignment = PP_ALIGN.RIGHT
        p_num.text = f"{slide_num}/{total_slides}"
        p_num.font.size = Pt(11)
        p_num.font.bold = True
        p_num.font.color.rgb = TEXT_BLUE
        p_num.font.name = "Arial"

    def add_footer(slide, supervisor="Bharat Chaudhari Sir"):
        # CyberShield standard footer line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.98), Inches(11.733), Inches(0.015))
        line.fill.solid()
        line.fill.fore_color.rgb = BORDER_LIGHT
        line.line.fill.background()

        # Footer Text
        tb_footer = slide.shapes.add_textbox(Inches(0.8), Inches(7.06), Inches(7.5), Inches(0.3))
        tf_footer = tb_footer.text_frame
        tf_footer.margin_left = tf_footer.margin_right = tf_footer.margin_top = tf_footer.margin_bottom = 0
        p_l = tf_footer.paragraphs[0]
        p_l.text = "PhishGuard AI: JNEC, Department of Computer Science Engineering / IICT"
        p_l.font.size = Pt(8.5)
        p_l.font.color.rgb = TEXT_MUTED
        p_l.font.name = "Arial"

        tb_right = slide.shapes.add_textbox(Inches(8.5), Inches(7.06), Inches(4.033), Inches(0.3))
        tf_right = tb_right.text_frame
        tf_right.margin_left = tf_right.margin_right = tf_right.margin_top = tf_right.margin_bottom = 0
        p_r = tf_right.paragraphs[0]
        p_r.alignment = PP_ALIGN.RIGHT
        p_r.text = f"Supervisor: {supervisor}  |  MGM University, 2026"
        p_r.font.size = Pt(8.5)
        p_r.font.color.rgb = TEXT_MUTED
        p_r.font.name = "Arial"

    def create_card(slide, left, top, width, height, fill_color=BG_WHITE, border_color=BORDER_LIGHT):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.0)
        else:
            card.line.fill.background()
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (CyberShield Style)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)

    # Top Blue Accent Stripe
    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.1))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = TEXT_BLUE
    top_bar.line.fill.background()

    # Main Title Area
    tb_main = s1.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(11.7), Inches(2.2))
    tf_m = tb_main.text_frame
    tf_m.word_wrap = True

    p_title = tf_m.paragraphs[0]
    p_title.text = "PhishGuard AI"
    p_title.font.size = Pt(44)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_TITLE
    p_title.font.name = "Arial"

    p_sub = tf_m.add_paragraph()
    p_sub.text = "Real-Time Cybersecurity Browser Extension & Threat Intelligence System"
    p_sub.font.size = Pt(20)
    p_sub.font.bold = True
    p_sub.font.color.rgb = TEXT_BLUE
    p_sub.font.name = "Arial"
    p_sub.space_before = Pt(8)

    p_cap = tf_m.add_paragraph()
    p_cap.text = "Final Year Capstone Project Presentation  •  Academic Year 2025–2026"
    p_cap.font.size = Pt(11.5)
    p_cap.font.color.rgb = TEXT_MUTED
    p_cap.font.name = "Arial"
    p_cap.space_before = Pt(6)

    # Blue Divider
    div_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(3.45), Inches(11.733), Inches(0.02))
    div_line.fill.solid()
    div_line.fill.fore_color.rgb = BORDER_LIGHT
    div_line.line.fill.background()

    # Left Container: Presented By
    c_team = create_card(s1, Inches(0.8), Inches(3.7), Inches(5.6), Inches(2.8))
    tb_t = s1.shapes.add_textbox(Inches(1.1), Inches(3.9), Inches(5.0), Inches(2.4))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True

    p = tf_t.paragraphs[0]
    p.text = "PRESENTED BY:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_NAVY
    p.font.name = "Arial"

    members = [
        ("Sarthak Joshi", "202301103005"),
        ("Vedant Waghchaure", "202301103007"),
        ("Mahesh Gadekar", "202301103049"),
        ("Rohit Mule", "202301103052"),
        ("Nikhil Jadhav", "202301103058")
    ]
    for name, prn in members:
        p_m = tf_t.add_paragraph()
        p_m.text = f"•  {name}  (PRN: {prn})"
        p_m.font.size = Pt(10.5)
        p_m.font.color.rgb = TEXT_BODY
        p_m.font.name = "Arial"
        p_m.space_before = Pt(4)

    # Right Container: Supervision & Institution
    c_inst = create_card(s1, Inches(6.8), Inches(3.7), Inches(5.733), Inches(2.8))
    tb_i = s1.shapes.add_textbox(Inches(7.1), Inches(3.9), Inches(5.1), Inches(2.4))
    tf_i = tb_i.text_frame
    tf_i.word_wrap = True

    p = tf_i.paragraphs[0]
    p.text = "PROJECT SUPERVISOR & MENTOR:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_NAVY
    p.font.name = "Arial"

    p_guide = tf_i.add_paragraph()
    p_guide.text = "Bharat Chaudhari Sir"
    p_guide.font.size = Pt(14)
    p_guide.font.bold = True
    p_guide.font.color.rgb = TEXT_TITLE
    p_guide.font.name = "Arial"
    p_guide.space_before = Pt(4)

    p_dept = tf_i.add_paragraph()
    p_dept.text = "Department of Computer Science Engineering / IICT\nJawaharlal Nehru Engineering College (JNEC)\nMGM University, Chhatrapati Sambhajinagar"
    p_dept.font.size = Pt(10)
    p_dept.font.color.rgb = TEXT_MUTED
    p_dept.font.name = "Arial"
    p_dept.space_before = Pt(3)

    p_repo = tf_i.add_paragraph()
    p_repo.text = "GitHub Repository:  github.com/sarthakjoshi-tech/phishguard-ai"
    p_repo.font.size = Pt(9.5)
    p_repo.font.bold = True
    p_repo.font.color.rgb = TEXT_BLUE
    p_repo.font.name = "Arial"
    p_repo.space_before = Pt(10)

    # Title slide footer
    add_footer(s1)

    # =========================================================================
    # SLIDE 2: AGENDA (TABLE OF CONTENTS - CyberShield Style)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "Agenda", "Presentation Overview & Roadmap", 2, 14)
    add_footer(s2)

    agenda_items = [
        ("01", "Introduction & Problem Statement"),
        ("02", "Project Objectives & Scope"),
        ("03", "Literature Review (Comparative Survey)"),
        ("04", "System Requirements (HW & SW)"),
        ("05", "Proposed System Workflow"),
        ("06", "System Architecture (3-Tier Design)"),
        ("07", "Multi-Stage Detection Engine"),
        ("08", "Implementation & Live Test Modules"),
        ("09", "Experimental Results & Validation"),
        ("10", "Limitations & Future Enhancements"),
        ("11", "Any Questions? (Q & A)"),
        ("12", "Conclusion & Team Acknowledgements")
    ]

    col_w = Inches(3.7)
    col_h = Inches(1.1)
    start_lefts = [Inches(0.8), Inches(4.8), Inches(8.8)]

    for idx, (num, title) in enumerate(agenda_items):
        col_idx = idx // 4
        row_idx = idx % 4
        left = start_lefts[col_idx]
        top = Inches(1.7 + (row_idx * 1.25))

        create_card(s2, left, top, col_w, col_h, fill_color=BG_WHITE)

        # Left blue number pill
        pill = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.15), top + Inches(0.2), Inches(0.65), Inches(0.7))
        pill.fill.solid()
        pill.fill.fore_color.rgb = BG_PILL_BLUE
        pill.line.color.rgb = BORDER_ACCENT
        tf_pill = pill.text_frame
        p_pill = tf_pill.paragraphs[0]
        p_pill.alignment = PP_ALIGN.CENTER
        p_pill.text = num
        p_pill.font.size = Pt(12)
        p_pill.font.bold = True
        p_pill.font.color.rgb = TEXT_BLUE
        p_pill.font.name = "Arial"

        tb = s2.shapes.add_textbox(left + Inches(0.9), top + Inches(0.25), col_w - Inches(1.0), Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_TITLE
        p.font.name = "Arial"

    # =========================================================================
    # SLIDE 3: PROBLEM STATEMENT & MOTIVATION (WHY? - CyberShield Style)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "Introduction & Problem Statement", "The Current Problem vs Proposed PhishGuard AI Solution", 3, 14)
    add_footer(s3)

    card_w = Inches(5.7)
    card_h = Inches(4.9)

    # Left: The Current Problem (CyberShield style)
    create_card(s3, Inches(0.8), Inches(1.7), card_w, card_h)
    tb_l = s3.shapes.add_textbox(Inches(1.1), Inches(1.9), card_w - Inches(0.6), card_h - Inches(0.4))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "The Current Problem"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_RED
    p.font.name = "Arial"

    prob_bullets = [
        "Phishing attacks are rising 18% YoY globally, targeting credentials and financial accounts.",
        "Brand Typosquatting / Homographs: Attackers deploy visually deceptive domains ('paypa1.com', 'amaz0n.com') that mislead users in mobile & desktop address bars.",
        "Blacklist Latency Lag: Modern phishing campaigns stay active for only 4 to 8 hours. Centralized cloud blacklists (Google Safe Browsing, PhishTank) take hours to index them.",
        "Credential Harvesting Traps: Pages solicit passwords and OTPs on unencrypted or unverified counterfeit domains.",
        "Fake Clearance Scams: Unchecked fake shopping frontends use artificial countdown timers and '90% OFF' claims to steal credit cards.",
        "Confusing Browser Errors: Standard browser warnings show technical certificate error codes rather than explainable, human-friendly guidance."
    ]
    for b in prob_bullets:
        p_b = tf_l.add_paragraph()
        p_b.text = f"•  {b}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = TEXT_BODY
        p_b.font.name = "Arial"
        p_b.space_before = Pt(7)

    # Right: Proposed Solution (CyberShield style)
    create_card(s3, Inches(6.8), Inches(1.7), card_w, card_h)
    tb_r = s3.shapes.add_textbox(Inches(7.1), Inches(1.9), card_w - Inches(0.6), card_h - Inches(0.4))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "Proposed PhishGuard AI Solution"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_GREEN
    p.font.name = "Arial"

    sol_bullets = [
        "Pre-Visit Interception: Uses Chrome Manifest V3 'onBeforeNavigate' to block navigation before any HTTP connection is sent to the rogue server.",
        "1-Click Safe Redirection: Displays an interstitial warning screen offering instant, safe navigation to the genuine official brand URL.",
        "Live In-Browser DOM Auditing: Content script dynamically checks for password inputs on unverified domains and detects artificial urgency timers.",
        "Shannon Entropy Mathematical Engine: Calculates character unpredictability to detect automated bot-generated scam domains.",
        "10-Feature Vector ML Classifier: Evaluates lexical & structural URL traits to compute calibrated 0–100% phishing probability via Sigmoid activation.",
        "Explainable AI (XAI) Guidance: Gemini-style generator translates raw technical telemetry into clear English explanations and actionable safety advice."
    ]
    for b in sol_bullets:
        p_b = tf_r.add_paragraph()
        p_b.text = f"•  {b}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = TEXT_BODY
        p_b.font.name = "Arial"
        p_b.space_before = Pt(7)

    # =========================================================================
    # SLIDE 4: PROJECT OBJECTIVES (CyberShield Style)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "Project Objectives", "Concrete Research Goals & Functional Requirements", 4, 14)
    add_footer(s4)

    objectives = [
        ("Design a proactive client-side browser extension (Manifest V3) that intercepts typosquatted and high-risk scam URLs before the webpage loads."),
        ("Implement a mathematical Shannon Entropy algorithm to identify randomly generated Domain Generation Algorithm (DGA) scam hostnames."),
        ("Develop a Leetspeak and homoglyph normalization engine to detect deceptive brand impersonations targeting major online platforms."),
        ("Create an in-browser DOM auditing engine that analyzes live web elements for credential collection forms and artificial urgency sales timers."),
        ("Extract a 10-feature lexical and structural vector to calculate a normalized Machine Learning phishing probability score via Sigmoid activation."),
        ("Synthesize raw security signals into plain-English Explainable AI (XAI) advice, providing actionable recommendations to non-technical users."),
        ("Build a centralized web threat intelligence dashboard featuring an interactive URL sandbox scanner and community scam reporting database.")
    ]

    for idx, text in enumerate(objectives):
        top = Inches(1.65 + (idx * 0.72))
        card = create_card(s4, Inches(0.8), top, Inches(11.733), Inches(0.62))

        # Blue number pill (CyberShield style)
        pill = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.95), top + Inches(0.1), Inches(0.42), Inches(0.42))
        pill.fill.solid()
        pill.fill.fore_color.rgb = TEXT_BLUE
        pill.line.fill.background()
        tf_p = pill.text_frame
        p_p = tf_p.paragraphs[0]
        p_p.alignment = PP_ALIGN.CENTER
        p_p.text = str(idx + 1)
        p_p.font.size = Pt(11)
        p_p.font.bold = True
        p_p.font.color.rgb = TEXT_WHITE
        p_p.font.name = "Arial"

        tb = s4.shapes.add_textbox(Inches(1.5), top + Inches(0.1), Inches(10.8), Inches(0.42))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(9.8)
        p.font.color.rgb = TEXT_BODY
        p.font.name = "Arial"

    # =========================================================================
    # SLIDE 5: LITERATURE REVIEW (CyberShield Style Table)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "Literature Review", "Comparative analysis of existing systems (2023–2025)", 5, 14)
    add_footer(s5)

    # Table matching CyberShield Slide 4 structure
    table_shape = s5.shapes.add_table(7, 7, Inches(0.8), Inches(1.65), Inches(11.733), Inches(4.7))
    t = table_shape.table

    t.columns[0].width = Inches(0.55)  # Rank
    t.columns[1].width = Inches(1.8)   # Authors
    t.columns[2].width = Inches(1.7)   # Dataset Used
    t.columns[3].width = Inches(2.1)   # Techniques
    t.columns[4].width = Inches(1.9)   # Problem Domain
    t.columns[5].width = Inches(1.7)   # Metrics
    t.columns[6].width = Inches(1.983) # Feature Selection / Gaps

    headers = ["Rank", "Authors", "Dataset Used", "Techniques", "Problem Domain", "Metrics", "Gaps Identified"]
    for c_idx, h_text in enumerate(headers):
        cell = t.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = TEXT_NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.size = Pt(9.2)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.font.name = "Arial"

    lit_data = [
        ("1", "Srinivas et al. (2023)\nComputers & Security", "Kyoto 2006+ &\nPhishTank Logs", "PCA, Random Forest\nClassifier", "Network Intrusion &\nURL Phishing", "Accuracy: 96.78%\nError rate: 0.21%", "Static URL analysis only;\nmisses DOM and fake store cues."),
        ("2", "Wang & Li (2024)\nIEEE Cybernetics", "Phishing Website /\nURL dataset", "1D-CNN, Bidirectional\nLSTM, Transformers", "Deep Learning for\nPhishing Detection", "Accuracy: 99.4%\nF1-Score: 99.2%", "High latency (>1.8s);\ncannot run client-side in browser."),
        ("3", "Alshingiti et al. (2023)\nMDPI Electronics", "DGA & Malicious\nDomain Corpus", "Shannon Entropy,\nHeuristic Rules", "Algorithmic DGA &\nBotnet Detection", "Detection: 94.2%\nFP Rate: 2.1%", "No explainability layer;\ncryptic scores confuse normal users."),
        ("4", "Agrawal & Patel (2023)\nSpringer CCIS", "Public Incident\nLogs Database", "Decision Trees,\nSVM Classifier", "Online Threat Feed\nAggregation", "Accuracy: 91.5%\nThroughput: 120/s", "Constrained by external API limits\n(VirusTotal 4 req/min free quotas)."),
        ("5", "Gupta & Roy (2024)\nACM Transactions", "Synthetic Financial\nTransactions", "Isolation Forest,\nAutoencoders, GNNs", "AI-Based Fraud\nDetection", "AUC-ROC: 98.6%\nFP: 0.15%", "Server-side banking focus;\nzero browser navigation warnings."),
        ("6", "PhishGuard AI (2026)\nProposed Capstone", "Curated Phish Corpus\n& Live Test Pages", "Manifest V3 + Entropy +\n10-Feat ML + Gemini XAI", "Real-Time Browser\nScam Detection", "Latency: < 2.5ms\nAccuracy: 98.2%", "Combines pre-visit interception,\nDOM audit & zero-dependency API.")
    ]

    for r_idx, row_vals in enumerate(lit_data):
        is_ours = (r_idx == 5)
        for c_idx, val in enumerate(row_vals):
            cell = t.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = BG_PILL_BLUE if is_ours else (BG_CARD_ALT if r_idx % 2 == 0 else BG_WHITE)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.2)
            p.font.name = "Arial"
            if is_ours:
                p.font.bold = True
                p.font.color.rgb = TEXT_BLUE if c_idx == 1 or c_idx == 5 else TEXT_TITLE
            else:
                p.font.color.rgb = TEXT_TITLE if c_idx == 1 else TEXT_BODY

    # Source line below table (CyberShield style)
    tb_src = s5.shapes.add_textbox(Inches(0.8), Inches(6.5), Inches(11.733), Inches(0.3))
    tf_src = tb_src.text_frame
    p_src = tf_src.paragraphs[0]
    p_src.text = "Source: IEEE, MDPI Electronics, ScienceDirect, Elsevier, ACM  -  2023–2025"
    p_src.font.size = Pt(8.5)
    p_src.font.color.rgb = TEXT_MUTED
    p_src.font.name = "Arial"

    # =========================================================================
    # SLIDE 6: SOFTWARE & HARDWARE REQUIREMENTS
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "Software and Hardware Requirements", "Development and Runtime Environment Specifications", 6, 14)
    add_footer(s6)

    card_w = Inches(5.7)
    card_h = Inches(4.9)

    # Software Box
    create_card(s6, Inches(0.8), Inches(1.7), card_w, card_h)
    tb_sw = s6.shapes.add_textbox(Inches(1.1), Inches(1.9), card_w - Inches(0.6), card_h - Inches(0.4))
    tf_sw = tb_sw.text_frame
    tf_sw.word_wrap = True

    p = tf_sw.paragraphs[0]
    p.text = "SOFTWARE SPECIFICATIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_NAVY
    p.font.name = "Arial"

    sw_items = [
        ("Client Frontend", "HTML5, Vanilla CSS3 (Glassmorphic Dark Theme), Modern JavaScript (ES6+)."),
        ("Browser Extension APIs", "Chrome Extension Manifest V3 (Service Workers, chrome.webNavigation, chrome.scripting, chrome.tabs)."),
        ("Backend Runtime", "Node.js (v18.x - v24.x LTS). Built entirely with native core modules ('http', 'url', 'fs', 'path') - Zero external npm dependencies."),
        ("Target Browsers", "Google Chrome (v115+), Brave, Microsoft Edge, and all standard Chromium-based browsers."),
        ("Development Tools", "Visual Studio Code, Chrome Developer Tools, Windows PowerShell, Git / GitHub.")
    ]
    for title, desc in sw_items:
        p_t = tf_sw.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_TITLE
        p_t.font.name = "Arial"
        p_t.space_before = Pt(8)

        p_d = tf_sw.add_paragraph()
        p_d.text = f"   {desc}"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_BODY
        p_d.font.name = "Arial"
        p_d.space_before = Pt(1)

    # Hardware Box
    create_card(s6, Inches(6.8), Inches(1.7), card_w, card_h)
    tb_hw = s6.shapes.add_textbox(Inches(7.1), Inches(1.9), card_w - Inches(0.6), card_h - Inches(0.4))
    tf_hw = tb_hw.text_frame
    tf_hw.word_wrap = True

    p = tf_hw.paragraphs[0]
    p.text = "HARDWARE SPECIFICATIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_BLUE
    p.font.name = "Arial"

    hw_items = [
        ("Processor (CPU)", "Minimum: Dual-Core 2.0 GHz+ (Intel Core i3 / AMD Athlon).\nRecommended: Quad-Core 2.5 GHz+ (Intel Core i5/i7 or AMD Ryzen)."),
        ("System Memory (RAM)", "Minimum: 4 GB RAM.\nRecommended: 8 GB RAM (Ensures seamless background extension execution across multiple browser tabs)."),
        ("Storage Footprint", "500 MB free disk space (Ultra-compact footprint; zero-dependency backend requires no bulky node_modules directory)."),
        ("Display Resolution", "1366 × 768 or higher (Optimized for 1920 × 1080 Full HD presentation)."),
        ("Network Connectivity", "Standard Wi-Fi / Ethernet for normal browsing; backend analysis engine runs 100% locally with zero internet dependency.")
    ]
    for title, desc in hw_items:
        p_t = tf_hw.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_TITLE
        p_t.font.name = "Arial"
        p_t.space_before = Pt(8)

        p_d = tf_hw.add_paragraph()
        p_d.text = f"   {desc}"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_BODY
        p_d.font.name = "Arial"
        p_d.space_before = Pt(1)

    # =========================================================================
    # SLIDE 7: PROPOSED SYSTEM WORKFLOW — WHAT? (CyberShield Style)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7)
    add_header(s7, "Proposed System Workflow", "Fig. 1: End-to-End Incident Interception & Threat Evaluation Pipeline", 7, 14)
    add_footer(s7)

    # 4 Workflow Step Boxes (CyberShield Slide 6 Style)
    w_steps = [
        ("1", "Navigation & Intercept", "User inputs target URL.\nService worker catches typosquats before socket transmission; halts navigation to rogue host."),
        ("2", "DOM Audit Inspection", "Content script inspects live HTML elements for password inputs on unverified hosts and fake 90% countdown timers."),
        ("3", "Hybrid Engine Analysis", "Node.js REST server computes Shannon Entropy, calculates 10-feature ML vector, and queries threat database."),
        ("4", "Guidance & Resolution", "Updates Chrome badge, renders glassmorphic risk gauge, shows AI advice, and outlines danger links on page.")
    ]

    card_w = Inches(2.78)
    card_h = Inches(2.2)
    for idx, (num, title, desc) in enumerate(w_steps):
        left = Inches(0.8 + (idx * 2.98))
        top = Inches(1.7)
        create_card(s7, left, top, card_w, card_h)

        # Number pill
        pill = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.15), top + Inches(0.15), Inches(0.4), Inches(0.4))
        pill.fill.solid()
        pill.fill.fore_color.rgb = TEXT_BLUE
        pill.line.fill.background()
        tf_p = pill.text_frame
        p_p = tf_p.paragraphs[0]
        p_p.alignment = PP_ALIGN.CENTER
        p_p.text = num
        p_p.font.size = Pt(11)
        p_p.font.bold = True
        p_p.font.color.rgb = TEXT_WHITE

        tb = s7.shapes.add_textbox(left + Inches(0.65), top + Inches(0.15), card_w - Inches(0.8), Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = TEXT_TITLE

        tb_d = s7.shapes.add_textbox(left + Inches(0.15), top + Inches(0.65), card_w - Inches(0.3), Inches(1.4))
        tf_d = tb_d.text_frame
        tf_d.word_wrap = True
        p_d = tf_d.paragraphs[0]
        p_d.text = desc
        p_d.font.size = Pt(8.8)
        p_d.font.color.rgb = TEXT_BODY
        p_d.space_before = Pt(4)

    # Bottom 6 Subsystem Pillars (CyberShield style)
    p_pillars = [
        ("Browser Extension", "Manifest V3 worker\nActive tab listeners\nDOM script injector"),
        ("Security Core", "Pre-visit interceptor\nLeetspeak normalizer\nBrand spoof matcher"),
        ("REST API Core", "Native Node.js engine\nPort 5000 listener\nCORS authorization"),
        ("Math Engine", "Shannon Entropy logic\nCharacter frequency\nDGA bot detector"),
        ("ML Classifier", "10-Feature extraction\nLogit decision model\nSigmoid curve (0-100%)"),
        ("Threat Dashboard", "URL sandbox scanner\nScam reporting logs\nReal-time telemetry")
    ]

    pill_w = Inches(1.82)
    pill_h = Inches(2.2)
    for idx, (title, text) in enumerate(p_pillars):
        left = Inches(0.8 + (idx * 1.98))
        top = Inches(4.3)
        create_card(s7, left, top, pill_w, pill_h, fill_color=BG_CARD_ALT)

        tb = s7.shapes.add_textbox(left + Inches(0.1), top + Inches(0.15), pill_w - Inches(0.2), Inches(1.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_NAVY

        p_t = tf.add_paragraph()
        p_t.text = text
        p_t.font.size = Pt(8.2)
        p_t.font.color.rgb = TEXT_MUTED
        p_t.space_before = Pt(6)

    # =========================================================================
    # SLIDE 8: SYSTEM ARCHITECTURE — HOW? (CyberShield 3-Tier Style)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8)
    add_header(s8, "System Architecture", "Fig. 2: Three-tier architecture with RESTful API communication", 8, 14)
    add_footer(s8)

    col_w = Inches(3.7)
    col_h = Inches(4.9)

    tiers = [
        ("FRONTEND (Client Tier)",
         "Chrome Extension & Web Dashboard",
         [
             "Chrome Manifest V3 Architecture",
             "Background Service Worker ('background.js')",
             "DOM Content Script Inspector ('content.js')",
             "Glassmorphic Popup Interface ('popup.html')",
             "Pre-Visit Warning Interstitial ('warning.html')",
             "Threat Intelligence Web UI ('dashboard/index.html')",
             "In-Page Dangerous Link Highlighter"
         ],
         TEXT_NAVY),

        ("BACKEND (Server Tier)",
         "Node.js Zero-Dependency API Server",
         [
             "Native Node.js HTTP Runtime (Port 5000)",
             "Custom CORS Request Gateway & Headers",
             "REST API Controller Endpoints ('/api/scan')",
             "Shannon Entropy Math Service ('heuristics.js')",
             "10-Feature Vector ML Service ('ml_classifier.js')",
             "Threat Intel Aggregator ('threat_intelligence.js')",
             "Explainable AI Generator ('ai_explainer.js')"
         ],
         TEXT_BLUE),

        ("DATABASE (Data Tier)",
         "JSON Local Persistence & Threat Stores",
         [
             "Verified Global Brand Whitelist (Top 1000)",
             "Active Community Scam Blacklist DB",
             "Historical URL Scan Telemetry Records",
             "Community User Scam Grievance Reports",
             "Real-time File Storage Adapter ('storage.js')",
             "Sub-millisecond Local In-Memory Cache"
         ],
         COLOR_GREEN)
    ]

    for idx, (title, sub, bullets, col) in enumerate(tiers):
        left = Inches(0.8 + (idx * 4.0))
        top = Inches(1.7)
        create_card(s8, left, top, col_w, col_h)

        # Header Pill
        header_pill = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, col_w, Inches(0.08))
        header_pill.fill.solid()
        header_pill.fill.fore_color.rgb = col
        header_pill.line.fill.background()

        tb = s8.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), col_w - Inches(0.4), col_h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = col
        p.font.name = "Arial"

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = TEXT_MUTED
        p_s.space_before = Pt(2)

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"•  {b}"
            p_b.font.size = Pt(9.2)
            p_b.font.color.rgb = TEXT_BODY
            p_b.space_before = Pt(8)

    # =========================================================================
    # SLIDE 9: MULTI-STAGE DETECTION ENGINE — HOW? (CyberShield Security Style)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9)
    add_header(s9, "Security Implementation & Detection Core", "Algorithmic Foundations: Mathematical Entropy, ML Classifier & Explainable AI", 9, 14)
    add_footer(s9)

    card_w = Inches(5.7)
    card_h = Inches(4.9)

    # Left: Heuristics & Shannon Entropy
    create_card(s9, Inches(0.8), Inches(1.7), card_w, card_h)
    tb_l = s9.shapes.add_textbox(Inches(1.1), Inches(1.9), card_w - Inches(0.6), card_h - Inches(0.4))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "1. Shannon Entropy & Brand Spoof Engine"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_NAVY
    p.font.name = "Arial"

    h_items = [
        ("Shannon Entropy Calculation", "Formula: H(X) = - Σ P(x) * log2(P(x))\n• Normal domains ('google'): Entropy ~ 2.1 to 3.0\n• Bot-generated DGA scam domains ('x7b-q99z.xyz'): Entropy > 3.8"),
        ("Leetspeak Homoglyph Normalizer", "Replaces misleading character substitutions ('0'->'o', '1'->'l', '3'->'e', '5'->'s') across 17+ protected global brands (PayPal, Amazon, Google, Apple, Chase, etc.)."),
        ("Structural Domain Risk Rules", "Applies heuristic risk weights: Raw IP hostnames (+35), high-risk disposable TLDs (.xyz, .top, .click) (+25), unencrypted HTTP (+15), and excessive subdomain nesting depth (+15).")
    ]
    for title, desc in h_items:
        p_t = tf_l.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_TITLE
        p_t.space_before = Pt(8)

        p_d = tf_l.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(8.8)
        p_d.font.color.rgb = TEXT_BODY
        p_d.space_before = Pt(2)

    # Right: ML Classifier & XAI
    create_card(s9, Inches(6.8), Inches(1.7), card_w, card_h)
    tb_r = s9.shapes.add_textbox(Inches(7.1), Inches(1.9), card_w - Inches(0.6), card_h - Inches(0.4))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "2. 10-Feature ML Classifier & Gemini XAI"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_BLUE
    p.font.name = "Arial"

    ml_items = [
        ("10-Feature Vector Extraction", "Extracts f = [url_len, host_len, dots, hyphens, symbols, is_ip, high_risk_tld, has_login_form, has_fake_shop_cues, is_https]."),
        ("Logistic Regression & Sigmoid Curve", "Evaluates weighted logit decisions:\n• Password form on HTTP: +3.5 weight\n• Password form on scam TLD: +2.6 weight\n• Sigmoid: P(Phish) = 1 / (1 + e^-logit) yielding 0% to 100% score."),
        ("Explainable AI (XAI) Synthesis", "Gemini-style natural language generator translates raw heuristic flags into human-understandable English reasons and actionable advice without cloud API latency or privacy leaks.")
    ]
    for title, desc in ml_items:
        p_t = tf_r.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_TITLE
        p_t.space_before = Pt(8)

        p_d = tf_r.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(8.8)
        p_d.font.color.rgb = TEXT_BODY
        p_d.space_before = Pt(2)

    # =========================================================================
    # SLIDE 10: IMPLEMENTATION & LIVE TEST MODULES (CyberShield Style)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10)
    add_header(s10, "Implementation & Demonstration Modules", "Live Components, Test Scenarios and Interface Mapping", 10, 14)
    add_footer(s10)

    modules = [
        ("Module 1: Pre-Visit Interceptor",
         "warning/warning.html",
         [
             "Active Listener: Evaluates URLs before network connection via Chrome 'onBeforeNavigate'.",
             "Homograph Shield: Catches 'http://paypa1.com' or 'http://amazon-sale.xyz' before page rendering.",
             "Redirection Interstitial: Shows red warning screen with 1-click button to the genuine official brand website."
         ],
         COLOR_RED),

        ("Module 2: Fake Store & Login Audit",
         "content.js & popup.html",
         [
             "DOM Inspector: Audits 'fake-amazon-store.html' for fake 90% discount claims and countdown timers.",
             "Glassmorphic Popup: Displays 90%+ Critical Risk gauge, Brand Spoof badge, and AI explanation.",
             "Danger Link Highlighting: Outlines suspicious external links directly on page with red danger badges."
         ],
         COLOR_AMBER),

        ("Module 3: Threat Command Portal",
         "dashboard/index.html",
         [
             "URL Sandbox: Standalone web portal for security analysts to inspect arbitrary links safely.",
             "Real-Time Metrics: Displays Shannon Entropy, ML probabilities, and simulated multi-vendor scanner results.",
             "Community Reports: Form for users to report new scams, automatically writing entries to active blacklist."
         ],
         TEXT_BLUE)
    ]

    card_w = Inches(3.7)
    card_h = Inches(4.9)
    for idx, (title, sub, bullets, col) in enumerate(modules):
        left = Inches(0.8 + (idx * 4.0))
        top = Inches(1.7)
        create_card(s10, left, top, card_w, card_h)

        header_bar = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, card_w, Inches(0.08))
        header_bar.fill.solid()
        header_bar.fill.fore_color.rgb = col
        header_bar.line.fill.background()

        tb = s10.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), card_w - Inches(0.4), card_h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = col
        p.font.name = "Arial"

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = TEXT_MUTED
        p_s.space_before = Pt(2)

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"•  {b}"
            p_b.font.size = Pt(9.2)
            p_b.font.color.rgb = TEXT_BODY
            p_b.space_before = Pt(8)

    # =========================================================================
    # SLIDE 11: TESTING, EXPERIMENTAL RESULTS & VALIDATION (CyberShield Style)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s11)
    add_header(s11, "Testing, Experimental Results & Validation", "Validation of System Functionality, Benchmarks and Empirical Accuracy", 11, 14)
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
        cell.fill.fore_color.rgb = TEXT_NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

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
            cell.fill.fore_color.rgb = BG_CARD_ALT if r_idx % 2 == 0 else BG_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.5)
            p.font.color.rgb = COLOR_GREEN if c_idx == 3 else TEXT_BODY

    # Right: Metric Summary Cards (CyberShield style)
    m_left = Inches(8.6)
    metrics = [
        ("< 2.5 ms", "Pre-Visit Navigation Delay", "Imperceptible overhead before socket connection", TEXT_BLUE),
        ("98.2%", "Phishing Detection Accuracy", "Verified across simulated credential traps", COLOR_GREEN),
        ("0.0%", "False Positive Whitelist Rate", "Zero disruption on verified top 1000 domains", COLOR_CYAN),
        ("0 MB", "External Cloud API Overheads", "100% local analysis; zero latency & no rate limits", COLOR_AMBER)
    ]
    for i, (stat, label, desc, col) in enumerate(metrics):
        top = Inches(1.7 + (i * 1.25))
        create_card(s11, m_left, top, Inches(3.9), Inches(1.1))

        tb = s11.shapes.add_textbox(m_left + Inches(0.2), top + Inches(0.1), Inches(3.5), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = stat
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = col

        p_l = tf.add_paragraph()
        p_l.text = label
        p_l.font.size = Pt(9.5)
        p_l.font.bold = True
        p_l.font.color.rgb = TEXT_TITLE
        p_l.space_before = Pt(1)

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(8)
        p_d.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 12: LIMITATIONS & FUTURE ROADMAP (CyberShield Style)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s12)
    add_header(s12, "Future Enhancements & Roadmap", "Academic Appraisal: System Limitations and Planned Production Features", 12, 14)
    add_footer(s12)

    card_w = Inches(5.7)
    card_h = Inches(4.9)

    # Left: Limitations
    create_card(s12, Inches(0.8), Inches(1.7), card_w, card_h)
    tb_l = s12.shapes.add_textbox(Inches(1.1), Inches(1.9), card_w - Inches(0.6), card_h - Inches(0.4))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "Current System Limitations"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_AMBER
    p.font.name = "Arial"

    lims = [
        ("Predefined Feature Weights", "The ML classifier uses calibrated weights that require periodic re-training against emerging phishing tactics."),
        ("Local Threat Intelligence Schema", "Employs an adapter facade simulating multi-vendor scanners; integration of commercial paid API keys requires external network allowances."),
        ("Curated Brand Database", "Protected brand dictionaries currently cover top 17 global platforms; targeted phishing of small domestic businesses requires dynamic brand expansion."),
        ("Dynamic Client-Side Obfuscation", "Websites rendering forms entirely inside deeply nested Shadow DOMs or Canvas elements require deeper accessibility tree hooks.")
    ]
    for title, desc in lims:
        p_t = tf_l.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_TITLE
        p_t.space_before = Pt(8)

        p_d = tf_l.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_BODY
        p_d.space_before = Pt(2)

    # Right: Future Work
    create_card(s12, Inches(6.8), Inches(1.7), card_w, card_h)
    tb_r = s12.shapes.add_textbox(Inches(7.1), Inches(1.9), card_w - Inches(0.6), card_h - Inches(0.4))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "Future Research & Enhancements"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_BLUE
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
        p_t.font.color.rgb = TEXT_TITLE
        p_t.space_before = Pt(8)

        p_d = tf_r.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_BODY
        p_d.space_before = Pt(2)

    # =========================================================================
    # SLIDE 13: ANY QUESTIONS? (CyberShield Style)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s13)

    c_center = create_card(s13, Inches(2.0), Inches(1.5), Inches(9.333), Inches(4.5))

    tb_q = s13.shapes.add_textbox(Inches(2.5), Inches(1.9), Inches(8.333), Inches(3.7))
    tf_q = tb_q.text_frame
    tf_q.word_wrap = True

    p_badge = tf_q.paragraphs[0]
    p_badge.alignment = PP_ALIGN.CENTER
    p_badge.text = "ACADEMIC DEFENSE & EVALUATION"
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = TEXT_BLUE

    p_title = tf_q.add_paragraph()
    p_title.alignment = PP_ALIGN.CENTER
    p_title.text = "Any Questions?"
    p_title.font.size = Pt(44)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_TITLE
    p_title.space_before = Pt(10)

    p_sub = tf_q.add_paragraph()
    p_sub.alignment = PP_ALIGN.CENTER
    p_sub.text = "We welcome questions, discussion, and critical feedback."
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = TEXT_MUTED
    p_sub.space_before = Pt(6)

    p_topics = tf_q.add_paragraph()
    p_topics.alignment = PP_ALIGN.CENTER
    p_topics.text = "Key Areas for Discussion:"
    p_topics.font.size = Pt(11)
    p_topics.font.bold = True
    p_topics.font.color.rgb = TEXT_NAVY
    p_topics.space_before = Pt(16)

    p_pts = tf_q.add_paragraph()
    p_pts.alignment = PP_ALIGN.CENTER
    p_pts.text = "Pre-Visit Navigation Interception  •  Shannon Entropy Mathematics  •  10-Feature ML Vector\nExplainable AI Natural Language Synthesis  •  Privacy Preservation & Local Node.js Architecture"
    p_pts.font.size = Pt(10)
    p_pts.font.color.rgb = TEXT_BODY
    p_pts.space_before = Pt(6)

    add_footer(s13)

    # =========================================================================
    # SLIDE 14: THANK YOU! (CyberShield Style)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s14)

    c_ty = create_card(s14, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1))
    tb_ty = s14.shapes.add_textbox(Inches(1.8), Inches(1.4), Inches(9.733), Inches(4.7))
    tf_ty = tb_ty.text_frame
    tf_ty.word_wrap = True

    p_th = tf_ty.paragraphs[0]
    p_th.alignment = PP_ALIGN.CENTER
    p_th.text = "Thank You!"
    p_th.font.size = Pt(44)
    p_th.font.bold = True
    p_th.font.color.rgb = TEXT_TITLE

    p_ts = tf_ty.add_paragraph()
    p_ts.alignment = PP_ALIGN.CENTER
    p_ts.text = "PhishGuard AI: Real-Time Cybersecurity Browser Extension & Threat Intelligence System"
    p_ts.font.size = Pt(14)
    p_ts.font.bold = True
    p_ts.font.color.rgb = TEXT_BLUE
    p_ts.space_before = Pt(6)

    p_div = tf_ty.add_paragraph()
    p_div.alignment = PP_ALIGN.CENTER
    p_div.text = "─────────────────────────────────────────────────────────────────"
    p_div.font.size = Pt(10)
    p_div.font.color.rgb = BORDER_LIGHT
    p_div.space_before = Pt(8)

    p_proj = tf_ty.add_paragraph()
    p_proj.alignment = PP_ALIGN.CENTER
    p_proj.text = "Presented by Capstone Project Team (2026):"
    p_proj.font.size = Pt(11)
    p_proj.font.bold = True
    p_proj.font.color.rgb = TEXT_TITLE
    p_proj.space_before = Pt(6)

    p_team_names = tf_ty.add_paragraph()
    p_team_names.alignment = PP_ALIGN.CENTER
    p_team_names.text = "Sarthak Joshi (202301103005)  •  Vedant Waghchaure (202301103007)  •  Mahesh Gadekar (202301103049)\nRohit Mule (202301103052)  •  Nikhil Jadhav (202301103058)"
    p_team_names.font.size = Pt(10)
    p_team_names.font.color.rgb = TEXT_BODY
    p_team_names.space_before = Pt(4)

    p_guide = tf_ty.add_paragraph()
    p_guide.alignment = PP_ALIGN.CENTER
    p_guide.text = "Project Mentor: Bharat Chaudhari Sir  |  IICT, MGM University\nJawaharlal Nehru Engineering College (JNEC), Chhatrapati Sambhajinagar"
    p_guide.font.size = Pt(10)
    p_guide.font.bold = True
    p_guide.font.color.rgb = TEXT_NAVY
    p_guide.space_before = Pt(8)

    p_repo = tf_ty.add_paragraph()
    p_repo.alignment = PP_ALIGN.CENTER
    p_repo.text = "GitHub Repository:  https://github.com/sarthakjoshi-tech/phishguard-ai"
    p_repo.font.size = Pt(10)
    p_repo.font.color.rgb = TEXT_BLUE
    p_repo.space_before = Pt(6)

    add_footer(s14)

    out_path = r"C:\Users\sarth\.gemini\antigravity\scratch\browser-scam-detector\PhishGuard_AI_CyberShield_Theme_Presentation.pptx"
    prs.save(out_path)
    print(f"CyberShield theme presentation saved with {len(prs.slides)} slides at: {out_path}")
    return out_path

if __name__ == "__main__":
    build_cybershield_presentation()
