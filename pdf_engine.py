"""
Complete PDF Generator for PhishGuard AI Master Guide
Generates a professional, multi-page PDF covering the entire project from zero.
"""

import sys
import os

class CanvasPDF:
    def __init__(self, filename):
        self.filename = filename
        self.pages = []
        self.current_cmds = []
        self.width = 595.28  # A4 width in points
        self.height = 841.89 # A4 height in points
        self.margin_x = 42.0
        self.margin_top = 45.0
        self.margin_bottom = 45.0
        self.printable_width = self.width - (2 * self.margin_x)
        self.y = self.height - self.margin_top
        self.page_number = 1

    def new_page(self):
        if self.current_cmds:
            self.pages.append((self.page_number, self.current_cmds))
            self.page_number += 1
        self.current_cmds = []
        self.y = self.height - self.margin_top

    def check_space(self, height_needed):
        if self.y - height_needed < self.margin_bottom:
            self.new_page()

    def escape_str(self, text):
        return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

    def draw_rect(self, x, y, w, h, fill_rgb=None, stroke_rgb=None, line_width=1.0):
        cmds = []
        if line_width != 1.0:
            cmds.append(f'{line_width:.2f} w\n')
        if fill_rgb and stroke_rgb:
            cmds.append(f'{fill_rgb[0]:.2f} {fill_rgb[1]:.2f} {fill_rgb[2]:.2f} rg {stroke_rgb[0]:.2f} {stroke_rgb[1]:.2f} {stroke_rgb[2]:.2f} RG {x:.2f} {y:.2f} {w:.2f} {h:.2f} re B\n')
        elif fill_rgb:
            cmds.append(f'{fill_rgb[0]:.2f} {fill_rgb[1]:.2f} {fill_rgb[2]:.2f} rg {x:.2f} {y:.2f} {w:.2f} {h:.2f} re f\n')
        elif stroke_rgb:
            cmds.append(f'{stroke_rgb[0]:.2f} {stroke_rgb[1]:.2f} {stroke_rgb[2]:.2f} RG {x:.2f} {y:.2f} {w:.2f} {h:.2f} re s\n')
        self.current_cmds.append(''.join(cmds))

    def draw_line(self, x1, y1, x2, y2, stroke_rgb=(0.7, 0.7, 0.7), line_width=1.0):
        cmd = f'{line_width:.2f} w {stroke_rgb[0]:.2f} {stroke_rgb[1]:.2f} {stroke_rgb[2]:.2f} RG {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l s\n'
        self.current_cmds.append(cmd)

    def add_text_line(self, x, y, text, font='F1', size=10, rgb=(0.1, 0.1, 0.1)):
        safe = self.escape_str(text)
        cmd = f'BT /{font} {size} Tf {rgb[0]:.2f} {rgb[1]:.2f} {rgb[2]:.2f} rg {x:.2f} {y:.2f} Td ({safe}) Tj ET\n'
        self.current_cmds.append(cmd)

    def wrap_text(self, text, max_chars_per_line=85, max_chars=None):
        if max_chars is not None:
            max_chars_per_line = max_chars
        words = text.split(' ')
        lines = []
        current_line = []
        current_len = 0

        for word in words:
            word_len = len(word)
            if current_len + word_len + (1 if current_line else 0) <= max_chars_per_line:
                current_line.append(word)
                current_len += word_len + (1 if current_len > 0 else 0)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_len = word_len
        if current_line:
            lines.append(' '.join(current_line))
        return lines if lines else ['']

    # High-level components
    def add_title_banner(self, title, subtitle, author="PhishGuard AI Research Team"):
        banner_height = 80
        self.check_space(banner_height + 20)
        # Gradient / dark navy background
        self.draw_rect(self.margin_x, self.y - banner_height, self.printable_width, banner_height, fill_rgb=(0.07, 0.13, 0.26))
        # Accent left stripe (Cyan/Blue)
        self.draw_rect(self.margin_x, self.y - banner_height, 6, banner_height, fill_rgb=(0.12, 0.65, 0.95))

        self.add_text_line(self.margin_x + 18, self.y - 28, title, font='F2', size=18, rgb=(1.0, 1.0, 1.0))
        self.add_text_line(self.margin_x + 18, self.y - 48, subtitle, font='F1', size=10.5, rgb=(0.75, 0.88, 1.0))
        self.add_text_line(self.margin_x + 18, self.y - 68, f"Final Project Evaluation Guide  |  Author: {author}  |  November 2026", font='F1', size=8.5, rgb=(0.55, 0.70, 0.85))

        self.y -= (banner_height + 22)

    def add_heading_1(self, text):
        self.check_space(45)
        self.y -= 10
        self.add_text_line(self.margin_x, self.y, text, font='F2', size=14, rgb=(0.08, 0.18, 0.36))
        self.draw_line(self.margin_x, self.y - 5, self.margin_x + self.printable_width, self.y - 5, stroke_rgb=(0.12, 0.65, 0.95), line_width=1.5)
        self.y -= 18

    def add_heading_2(self, text):
        self.check_space(32)
        self.y -= 6
        self.add_text_line(self.margin_x, self.y, text, font='F2', size=11.5, rgb=(0.12, 0.28, 0.50))
        self.y -= 15

    def add_heading_3(self, text):
        self.check_space(24)
        self.y -= 4
        self.add_text_line(self.margin_x, self.y, text, font='F2', size=10, rgb=(0.15, 0.35, 0.40))
        self.y -= 13

    def add_paragraph(self, text, font='F1', size=9.5, leading=13.5, rgb=(0.15, 0.15, 0.15), max_chars=95):
        lines = self.wrap_text(text, max_chars)
        for line in lines:
            self.check_space(leading)
            self.add_text_line(self.margin_x, self.y, line, font=font, size=size, rgb=rgb)
            self.y -= leading
        self.y -= 3

    def add_bullet(self, bold_prefix, text, max_chars=90):
        full_text = f"{bold_prefix}: {text}" if bold_prefix else text
        lines = self.wrap_text(full_text, max_chars)

        for i, line in enumerate(lines):
            self.check_space(13)
            if i == 0:
                self.add_text_line(self.margin_x + 5, self.y, "*", font='F2', size=11, rgb=(0.12, 0.65, 0.95))
            self.add_text_line(self.margin_x + 18, self.y, line, font='F1', size=9.0, rgb=(0.15, 0.15, 0.15))
            self.y -= 13
        self.y -= 2

    def add_callout(self, title, content, callout_type="info"):
        # colors: info (blue), warning (amber), success (green)
        bg = (0.94, 0.97, 1.0)
        border = (0.12, 0.65, 0.95)
        title_rgb = (0.05, 0.30, 0.65)
        if callout_type == "warning":
            bg = (1.0, 0.97, 0.92)
            border = (0.95, 0.60, 0.10)
            title_rgb = (0.70, 0.35, 0.05)
        elif callout_type == "concept":
            bg = (0.95, 0.98, 0.95)
            border = (0.15, 0.65, 0.30)
            title_rgb = (0.10, 0.45, 0.20)

        lines = self.wrap_text(content, max_chars=88)
        box_height = 24 + (len(lines) * 12.5)
        self.check_space(box_height + 10)

        # Draw box
        self.draw_rect(self.margin_x, self.y - box_height, self.printable_width, box_height, fill_rgb=bg)
        self.draw_rect(self.margin_x, self.y - box_height, 4, box_height, fill_rgb=border)

        # Title
        self.add_text_line(self.margin_x + 12, self.y - 14, title, font='F2', size=9.5, rgb=title_rgb)

        # Content lines
        curr_y = self.y - 27
        for line in lines:
            self.add_text_line(self.margin_x + 12, curr_y, line, font='F1', size=8.5, rgb=(0.18, 0.18, 0.18))
            curr_y -= 12.5

        self.y -= (box_height + 8)

    def add_code_block(self, title, code_lines):
        line_height = 11.5
        box_height = 18 + (len(code_lines) * line_height) + 6
        self.check_space(box_height + 10)

        # Box background (slate light gray)
        self.draw_rect(self.margin_x, self.y - box_height, self.printable_width, box_height, fill_rgb=(0.95, 0.96, 0.98), stroke_rgb=(0.82, 0.85, 0.90))
        # Top title bar
        self.draw_rect(self.margin_x, self.y - 16, self.printable_width, 16, fill_rgb=(0.88, 0.91, 0.95))
        self.add_text_line(self.margin_x + 10, self.y - 12, title, font='F4', size=8.0, rgb=(0.20, 0.25, 0.35))

        curr_y = self.y - 28
        for line in code_lines:
            # Wrap long code lines if needed
            safe_code = line[:90]
            self.add_text_line(self.margin_x + 10, curr_y, safe_code, font='F3', size=7.8, rgb=(0.12, 0.15, 0.20))
            curr_y -= line_height

        self.y -= (box_height + 8)

    def add_table_row(self, col1, col2, is_header=False, col1_w=150):
        row_height = 20 if is_header else 22
        col2_w = self.printable_width - col1_w
        self.check_space(row_height)

        bg = (0.88, 0.92, 0.97) if is_header else None
        if bg:
            self.draw_rect(self.margin_x, self.y - row_height, self.printable_width, row_height, fill_rgb=bg)

        self.draw_line(self.margin_x, self.y - row_height, self.margin_x + self.printable_width, self.y - row_height, stroke_rgb=(0.80, 0.80, 0.80), line_width=0.7)

        f1 = 'F2' if is_header else 'F2'
        f2 = 'F2' if is_header else 'F1'
        s1 = 9.0 if is_header else 8.5
        s2 = 9.0 if is_header else 8.2

        self.add_text_line(self.margin_x + 6, self.y - 14, col1, font=f1, size=s1, rgb=(0.1, 0.2, 0.35) if is_header else (0.1, 0.3, 0.5))
        # col2 might need wrapping
        col2_lines = self.wrap_text(col2, max_chars=65)
        for i, l in enumerate(col2_lines[:2]):
            self.add_text_line(self.margin_x + col1_w + 6, self.y - 13 - (i * 9), l, font=f2, size=s2, rgb=(0.15, 0.15, 0.15))

        self.y -= row_height

    def save(self):
        if self.current_cmds:
            self.pages.append((self.page_number, self.current_cmds))

        total_pages = len(self.pages)
        font_objs = [
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Courier-Bold >>'
        ]

        page_obj_nums = []
        content_obj_nums = []
        start_page_num = 7

        for i in range(total_pages):
            page_obj_nums.append(start_page_num + i * 2)
            content_obj_nums.append(start_page_num + i * 2 + 1)

        kids_refs = ' '.join([f'{p} 0 R' for p in page_obj_nums])
        pages_obj = f'<< /Type /Pages /Kids [{kids_refs}] /Count {total_pages} >>'.encode('ascii')

        all_objs = [
            None,
            b'<< /Type /Catalog /Pages 2 0 R >>',
            pages_obj,
            font_objs[0], # F1: Helvetica
            font_objs[1], # F2: Helvetica-Bold
            font_objs[2], # F3: Courier
            font_objs[3]  # F4: Courier-Bold
        ]

        for i, (p_num, page_cmds) in enumerate(self.pages):
            c_num = content_obj_nums[i]

            # Header running rule
            header_text = f"PhishGuard AI: Real-Time Cybersecurity System Guide"
            safe_header = self.escape_str(header_text)
            header_cmd = f"BT /F1 7.5 Tf 0.55 0.60 0.65 rg {self.margin_x} {self.height - 25} Td ({safe_header}) Tj ET\n"
            header_line = f"0.5 w 0.85 0.88 0.92 RG {self.margin_x} {self.height - 30} m {self.margin_x + self.printable_width} {self.height - 30} l s\n"

            # Footer running rule & page count
            footer_text = f"Final Presentation Master Document  |  Zero-Knowledge to Mastery"
            safe_footer = self.escape_str(footer_text)
            page_str = self.escape_str(f"Page {i+1} of {total_pages}")
            footer_line = f"0.5 w 0.85 0.88 0.92 RG {self.margin_x} 32 m {self.margin_x + self.printable_width} 32 l s\n"
            footer_cmd = f"BT /F1 7.5 Tf 0.50 0.50 0.50 rg {self.margin_x} 20 Td ({safe_footer}) Tj ET\n"
            page_cmd = f"BT /F2 8.0 Tf 0.12 0.45 0.75 rg {self.margin_x + self.printable_width - 55} 20 Td ({page_str}) Tj ET\n"

            full_cmds = [header_cmd, header_line] + page_cmds + [footer_line, footer_cmd, page_cmd]
            stream_data = ''.join(full_cmds).encode('latin-1', errors='replace')

            page_obj = f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.width:.2f} {self.height:.2f}] /Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R /F4 6 0 R >> >> /Contents {c_num} 0 R >>'.encode('ascii')
            content_obj = f'<< /Length {len(stream_data)} >>\nstream\n'.encode('ascii') + stream_data + b'\nendstream'

            all_objs.append(page_obj)
            all_objs.append(content_obj)

        pdf_bytes = bytearray(b'%PDF-1.4\n')
        xref_offsets = [0]

        for idx in range(1, len(all_objs)):
            xref_offsets.append(len(pdf_bytes))
            obj_bytes = f'{idx} 0 obj\n'.encode('ascii') + all_objs[idx] + b'\nendobj\n'
            pdf_bytes.extend(obj_bytes)

        xref_pos = len(pdf_bytes)
        pdf_bytes.extend(f'xref\n0 {len(all_objs)}\n0000000000 65535 f \n'.encode('ascii'))
        for offset in xref_offsets[1:]:
            pdf_bytes.extend(f'{offset:010d} 00000 n \n'.encode('ascii'))

        pdf_bytes.extend(f'trailer\n<< /Size {len(all_objs)} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n'.encode('ascii'))

        with open(self.filename, 'wb') as f:
            f.write(pdf_bytes)

        print(f"Successfully generated {total_pages} page PDF at: {self.filename}")
        return total_pages
