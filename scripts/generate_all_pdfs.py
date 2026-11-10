import os
import re
import subprocess
import markdown
import shutil

DOCS_DIR = "/home/jansky/pilahin-app/docs"
USER_DOCS_DIR = "/home/jansky/Documents/Pilahin_PDFs"
os.makedirs(USER_DOCS_DIR, exist_ok=True)

# Formal, clean, minimalist print styling — NO highlights, NO colorful gradient banners, NO pill badges
CSS_STYLES = """
<style>
@page {
  size: A4 portrait;
  margin: 18mm 16mm 18mm 16mm;
  @bottom-right {
    content: counter(page);
    font-size: 8.5pt;
    color: #475569;
  }
}

* {
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  color: #0f172a;
  line-height: 1.65;
  font-size: 9.5pt;
  margin: 0;
  padding: 0;
  background-color: #ffffff;
}

/* Formal Header - Clean, No color highlights */
.doc-header {
  border-bottom: 2px solid #0f172a;
  padding-bottom: 12px;
  margin-bottom: 20px;
}

.doc-header .doc-category {
  font-size: 8.5pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #475569;
  margin-bottom: 4px;
}

.doc-header h1 {
  font-size: 16pt;
  font-weight: 800;
  margin: 0 0 6px 0;
  color: #0f172a;
  line-height: 1.3;
  border: none;
  padding: 0;
}

.doc-header .doc-subtitle {
  margin: 2px 0 10px 0;
  font-size: 9.5pt;
  color: #475569;
}

.doc-header .meta-table {
  width: 100%;
  margin-top: 8px;
  border-collapse: collapse;
  font-size: 8.5pt;
}

.doc-header .meta-table td {
  padding: 2px 4px;
  border: none;
  vertical-align: top;
  color: #1e293b;
}

.doc-header .meta-table td.label {
  width: 18%;
  font-weight: 600;
  color: #0f172a;
  padding-left: 0;
}

/* Headings */
h1 {
  font-size: 14pt;
  font-weight: 700;
  color: #0f172a;
  border-bottom: 1px solid #cbd5e1;
  padding-bottom: 4px;
  margin-top: 22px;
  margin-bottom: 10px;
  page-break-after: avoid;
}

h2 {
  font-size: 12pt;
  font-weight: 700;
  color: #0f172a;
  margin-top: 18px;
  margin-bottom: 8px;
  border: none;
  padding: 0;
  page-break-after: avoid;
}

h3 {
  font-size: 10.5pt;
  font-weight: 700;
  color: #1e293b;
  margin-top: 14px;
  margin-bottom: 6px;
  page-break-after: avoid;
}

h4 {
  font-size: 9.5pt;
  font-weight: 700;
  color: #334155;
  margin-top: 10px;
  margin-bottom: 4px;
  page-break-after: avoid;
}

p, li {
  color: #1f2937;
  margin-bottom: 8px;
}

ul, ol {
  padding-left: 20px;
  margin-bottom: 10px;
}

li {
  margin-bottom: 4px;
}

hr {
  border: none;
  height: 1px;
  background: #e2e8f0;
  margin: 16px 0;
}

/* Formal Clean Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0 16px 0;
  font-size: 8.5pt;
  page-break-inside: avoid;
}

th {
  background: #f1f5f9;
  color: #0f172a;
  font-weight: 700;
  text-align: left;
  padding: 7px 9px;
  border: 1px solid #cbd5e1;
}

td {
  padding: 6px 9px;
  border: 1px solid #cbd5e1;
  vertical-align: top;
  color: #1e293b;
}

tr:nth-child(even) td {
  background: #f8fafc;
}

/* Dialogue & Spoken Text */
blockquote {
  border-left: 3px solid #64748b;
  background: #f8fafc;
  margin: 8px 0;
  padding: 8px 12px;
  color: #0f172a;
  font-size: 9.5pt;
  page-break-inside: avoid;
}

blockquote p {
  margin: 0;
  color: #0f172a;
}

/* Clean Footer */
.doc-footer {
  margin-top: 24px;
  padding-top: 8px;
  border-top: 1px solid #cbd5e1;
  font-size: 8pt;
  color: #64748b;
  text-align: center;
}
</style>
"""

def clean_markdown_body(text):
  lines = text.splitlines()
  filtered = []
  skip_header = True
  for line in lines:
    # Skip topmost title/metadata lines already handled in the doc header
    if skip_header:
      if line.startswith("# ") or line.startswith("### ") or line.startswith("**Tema") or line.startswith("**Subtema") or line.startswith("**Karya"):
        continue
      if line.strip() == "---":
        skip_header = False
        continue
    filtered.append(line)
  return "\n".join(filtered)

def convert_md_to_pdf(md_filename, pdf_filename, category_text, doc_title, doc_subtitle, meta_items):
  md_path = os.path.join(DOCS_DIR, md_filename)
  if not os.path.exists(md_path):
    print(f"File not found: {md_path}")
    return False

  with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

  clean_text = clean_markdown_body(text)

  # Convert Markdown to HTML
  raw_html = markdown.markdown(clean_text, extensions=['extra', 'tables', 'fenced_code', 'toc'])

  meta_rows_html = ""
  for label, value in meta_items:
    meta_rows_html += f"<tr><td class='label'>{label}</td><td>: {value}</td></tr>\n"

  header_html = f"""
  <div class="doc-header">
    <div class="doc-category">{category_text}</div>
    <h1>{doc_title}</h1>
    <div class="doc-subtitle">{doc_subtitle}</div>
    <table class="meta-table">
      {meta_rows_html}
    </table>
  </div>
  """

  footer_html = """
  <div class="doc-footer">
    Pilah.in — Platform Ekonomi Sirkular Sampah Rumah Tangga | UI/UX In Action (UIA) MIA 2026
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

  # Run Chromium print-to-pdf with --no-pdf-header-footer to suppress date/url header
  cmd = [
    "google-chrome",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-pdf-header-footer",
    f"--print-to-pdf={target_pdf_home}",
    temp_html_path
  ]

  print(f"▶ Generating Clean PDF: {pdf_filename}...")
  res = subprocess.run(cmd, capture_output=True, text=True)
  
  if os.path.exists(target_pdf_home):
    shutil.copyfile(target_pdf_home, target_pdf_docs)
    shutil.copyfile(target_pdf_home, target_pdf_user)
    print(f"  ✓ PDF Generated: {pdf_filename} ({os.path.getsize(target_pdf_docs):,} bytes)")
    if os.path.exists(temp_html_path):
      os.remove(temp_html_path)
    return True
  else:
    print(f"❌ Failed to generate PDF {pdf_filename}. Stderr: {res.stderr}")
    return False

# 1. Naskah Pitching (Clean, No Hardcoded Names, No Highlights)
convert_md_to_pdf(
  "NASKAH_PITCHING_MIA2026.md",
  "NASKAH_PITCHING_MIA2026.pdf",
  "UI/UX IN ACTION • MIA 2026",
  "Naskah Narasi Pitching Resmi (Spoken Script)",
  "Panduan Lengkap Penyampaian Presentasi Video Singkat (~4 Menit)",
  [
    ("Karya", "Pilah.in (Platform Ekonomi Sirkular Sampah Rumah Tangga Tertutup)"),
    ("Tema / Subtema", "Designing Digital Futures / Sustainable Environment"),
    ("Pembagian Peran", "Pembicara 1, Pembicara 2, Pembicara 3 (Dapat disesuaikan mandiri)")
  ]
)

# 2. Bab 3.1 Analisis Desain Karya (Clean, No Hardcoded Names, No Highlights)
convert_md_to_pdf(
  "BAB_3_1_ANALISIS_DESAIN_KARYA.md",
  "BAB_3_1_ANALISIS_DESAIN_KARYA.pdf",
  "PROPOSAL KARYA UI/UX • BAB III",
  "Bab III: Analisis Desain Karya (Pilah.in)",
  "3.1 Target Pengguna, Batasan Aplikasi, Platform yang Digunakan, User Persona, & Analisis SWOT",
  [
    ("Karya", "Pilah.in (Platform Ekonomi Sirkular Sampah Rumah Tangga Tertutup)"),
    ("Tema / Subtema", "Designing Digital Futures / Sustainable Environment"),
    ("Kategori", "UI/UX In Action (UIA) MIA 2026")
  ]
)

# 3. Panduan B-Roll
convert_md_to_pdf(
  "PITCHING_BROLL_GUIDE.md",
  "PITCHING_BROLL_GUIDE.pdf",
  "PANDUAN VIDEO B-ROLL",
  "Panduan Video B-Roll Latar Belakang Masalah",
  "Spesifikasi Aset Video 1080p Full HD & Sinkronisasi Narasi Pitching",
  [
    ("Karya", "Pilah.in"),
    ("Kompetisi", "UI/UX In Action (UIA) MIA 2026"),
    ("Format Video", "Full HD 1080p (30fps), Audio Musik Piano Neoklasik BGM")
  ]
)

print("\n🎉 ALL CLEAN FORMAL PDFS GENERATED SUCCESSFULLY!")
