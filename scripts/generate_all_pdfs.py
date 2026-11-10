import os
import re
import subprocess
import markdown

DOCS_DIR = "/home/jansky/pilahin-app/docs"
USER_DOCS_DIR = "/home/jansky/Documents/Pilahin_PDFs"
os.makedirs(USER_DOCS_DIR, exist_ok=True)

CSS_STYLES = """
<style>
@page {
  size: A4 portrait;
  margin: 18mm 14mm 18mm 14mm;
}

* {
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #1e293b;
  line-height: 1.6;
  font-size: 10pt;
  margin: 0;
  padding: 0;
  background-color: #ffffff;
}

/* Header Banner */
.doc-header {
  background: linear-gradient(135deg, #064e3b 0%, #047857 50%, #059669 100%);
  color: #ffffff;
  padding: 22px 24px;
  border-radius: 10px;
  margin-bottom: 24px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.doc-header .badge {
  display: inline-block;
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.35);
  padding: 3px 10px;
  border-radius: 9999px;
  font-size: 8.5pt;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 10px;
}

.doc-header h1 {
  font-size: 18pt;
  font-weight: 800;
  margin: 0 0 6px 0;
  color: #ffffff;
  line-height: 1.3;
  border: none;
  padding: 0;
}

.doc-header p {
  margin: 4px 0;
  font-size: 9.5pt;
  color: #d1fae5;
}

.meta-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 9pt;
}

.meta-item strong {
  color: #ffffff;
}

/* Typography */
h1 {
  font-size: 16pt;
  color: #064e3b;
  border-bottom: 2px solid #10b981;
  padding-bottom: 6px;
  margin-top: 24px;
  margin-bottom: 14px;
  page-break-after: avoid;
}

h2 {
  font-size: 13pt;
  color: #0f766e;
  border-left: 4px solid #0d9488;
  padding-left: 10px;
  margin-top: 20px;
  margin-bottom: 10px;
  page-break-after: avoid;
}

h3 {
  font-size: 11pt;
  color: #047857;
  margin-top: 16px;
  margin-bottom: 8px;
  page-break-after: avoid;
}

h4 {
  font-size: 10pt;
  color: #334155;
  margin-top: 12px;
  margin-bottom: 6px;
  font-weight: 700;
  page-break-after: avoid;
}

p, li {
  color: #334155;
  margin-bottom: 8px;
}

ul, ol {
  padding-left: 20px;
  margin-bottom: 12px;
}

li {
  margin-bottom: 4px;
}

hr {
  border: none;
  height: 1px;
  background: #e2e8f0;
  margin: 20px 0;
}

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0 18px 0;
  font-size: 9pt;
  page-break-inside: avoid;
}

th {
  background: #0f766e;
  color: #ffffff;
  font-weight: 600;
  text-align: left;
  padding: 8px 10px;
  border: 1px solid #0f766e;
}

td {
  padding: 7px 10px;
  border: 1px solid #cbd5e1;
  vertical-align: top;
  color: #334155;
}

tr:nth-child(even) td {
  background: #f8fafc;
}

/* Blockquotes / Speeches */
blockquote {
  border-left: 4px solid #10b981;
  background: #f0fdf4;
  margin: 10px 0;
  padding: 10px 14px;
  border-radius: 0 6px 6px 0;
  color: #065f46;
  font-size: 9.5pt;
  page-break-inside: avoid;
}

blockquote p {
  margin: 0;
  color: #065f46;
}

/* Speaker Badges */
.badge-haris {
  display: inline-block;
  background: #dcfce7;
  color: #166534;
  border: 1px solid #86efac;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 8.5pt;
}

.badge-amrin {
  display: inline-block;
  background: #cffafe;
  color: #155e75;
  border: 1px solid #67e8f9;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 8.5pt;
}

.badge-andika {
  display: inline-block;
  background: #e0e7ff;
  color: #3730a3;
  border: 1px solid #a5b4fc;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 8.5pt;
}

.timecode-pill {
  display: inline-block;
  background: #0f172a;
  color: #f8fafc;
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 700;
  font-size: 8.5pt;
  margin-right: 6px;
}

.visual-box {
  background: #f8fafc;
  border: 1px dashed #94a3b8;
  border-radius: 6px;
  padding: 8px 12px;
  margin: 8px 0;
  font-size: 8.5pt;
  color: #475569;
}

/* Footer note */
.doc-footer {
  margin-top: 30px;
  padding-top: 10px;
  border-top: 1px solid #cbd5e1;
  font-size: 8pt;
  color: #64748b;
  text-align: center;
}
</style>
"""

def enhance_pitching_script_html(html):
  # Replace speaker mentions
  html = re.sub(
    r'\(Pembicara:\s*Haris([^\)]*)\)',
    r'<span class="badge-haris">🎤 Haris\1</span>',
    html
  )
  html = re.sub(
    r'\(Pembicara:\s*Amrin([^\)]*)\)',
    r'<span class="badge-amrin">🎤 Amrin\1</span>',
    html
  )
  html = re.sub(
    r'\(Pembicara:\s*Andika([^\)]*)\)',
    r'<span class="badge-andika">🎤 Andika\1</span>',
    html
  )
  return html

def convert_md_to_pdf(md_filename, pdf_filename, doc_title, doc_subtitle, doc_badge):
  md_path = os.path.join(DOCS_DIR, md_filename)
  if not os.path.exists(md_path):
    print(f"File not found: {md_path}")
    return False

  with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

  # Remove the topmost H1 if present, we will render it in header
  lines = text.splitlines()
  filtered_lines = []
  skip_top_h1 = True
  for line in lines:
    if skip_top_h1 and (line.startswith("# ") or line.startswith("### ")):
      continue
    if line.startswith("---") and skip_top_h1:
      skip_top_h1 = False
      continue
    filtered_lines.append(line)
  
  clean_text = "\n".join(filtered_lines)

  # Convert Markdown to HTML
  raw_html = markdown.markdown(clean_text, extensions=['extra', 'tables', 'fenced_code', 'toc'])
  
  if "PITCHING" in md_filename:
    raw_html = enhance_pitching_script_html(raw_html)

  header_html = f"""
  <div class="doc-header">
    <div class="badge">{doc_badge}</div>
    <h1>{doc_title}</h1>
    <p>{doc_subtitle}</p>
    <div class="meta-grid">
      <div class="meta-item">
        <strong>Nama Tim:</strong> Tim NamaYangNormalAjaPliss<br>
        <strong>Institusi:</strong> Telkom University
      </div>
      <div class="meta-item">
        <strong>Anggota Tim:</strong> Ahmad Haris Dawaa’ul Qulub, Amrin Rasyida Utami, Andika Ramadhan Yusuf<br>
        <strong>Kategori:</strong> UI/UX In Action — Subtema Sustainable Environment
      </div>
    </div>
  </div>
  """

  footer_html = """
  <div class="doc-footer">
    Pilah.in — Closed-Loop Circular Waste Platform | UI/UX In Action (UIA) MIA 2026 | Dokumen Resmi Tim NamaYangNormalAjaPliss
  </div>
  """

  full_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>{doc_title}</title>
  {CSS_STYLES}
</head>
<body>
  {header_html}
  <div class="doc-content">
    {raw_html}
  </div>
  {footer_html}
</body>
</html>
"""

  temp_html_path = f"/home/jansky/temp_{os.path.splitext(pdf_filename)[0]}.html"
  with open(temp_html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

  target_pdf_docs = os.path.join(DOCS_DIR, pdf_filename)
  target_pdf_user = os.path.join(USER_DOCS_DIR, pdf_filename)
  target_pdf_home = os.path.join("/home/jansky", pdf_filename)

  # Run Chromium print-to-pdf
  cmd = [
    "google-chrome",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--print-to-pdf-no-header",
    f"--print-to-pdf={target_pdf_home}",
    temp_html_path
  ]

  print(f"▶ Generating PDF: {pdf_filename}...")
  res = subprocess.run(cmd, capture_output=True, text=True)
  
  if os.path.exists(target_pdf_home):
    # Copy to target directories
    import shutil
    shutil.copyfile(target_pdf_home, target_pdf_docs)
    shutil.copyfile(target_pdf_home, target_pdf_user)
    print(f"  ✓ PDF Generated Successfully ({os.path.getsize(target_pdf_docs):,} bytes)")
    print(f"    - In docs:      {target_pdf_docs}")
    print(f"    - In Documents: {target_pdf_user}")
    print(f"    - In Home:      {target_pdf_home}")
    if os.path.exists(temp_html_path):
      os.remove(temp_html_path)
    return True
  else:
    print(f"❌ Failed to generate PDF {pdf_filename}. Stderr: {res.stderr}")
    return False

# 1. Convert Naskah Pitching
convert_md_to_pdf(
  "NASKAH_PITCHING_MIA2026.md",
  "NASKAH_PITCHING_MIA2026.pdf",
  "Naskah Narasi Pitching Resmi (Spoken Script)",
  "Panduan Lengkap Penyampaian Presentasi Video Singkat (~4 Menit) • MIA 2026",
  "MIA 2026 • UI/UX IN ACTION PITCHING SCRIPT"
)

# 2. Convert Bab 3.1 Analisis Desain Karya
convert_md_to_pdf(
  "BAB_3_1_ANALISIS_DESAIN_KARYA.md",
  "BAB_3_1_ANALISIS_DESAIN_KARYA.pdf",
  "Bab III: Analisis Desain Karya (Pilah.in)",
  "3.1 Target Pengguna, Batasan Aplikasi, Platform, User Persona, & Analisis SWOT",
  "MIA 2026 • PROPOSAL KARYA BAB 3.1"
)

# 3. Convert Panduan B-Roll
convert_md_to_pdf(
  "PITCHING_BROLL_GUIDE.md",
  "PITCHING_BROLL_GUIDE.pdf",
  "Panduan Video B-Roll Latar Belakang Masalah",
  "Spesifikasi Aset Video 1080p Full HD, Soundtrack BGM Piano, & Storyboard Visual",
  "MIA 2026 • VIDEO ASSET & STORYBOARD GUIDE"
)

print("\n🎉 ALL PDFS CREATED SUCCESSFULLY!")
