import xml.etree.ElementTree as ET
import os
import subprocess

def generate_ia_drawio(output_path):
    root = ET.Element("mxfile", {
        "host": "app.diagrams.net",
        "modified": "2026-11-01T13:00:00.000Z",
        "agent": "Pilahin-IA-Agent",
        "version": "21.6.8",
        "type": "device"
    })

    diagram = ET.SubElement(root, "diagram", {"id": "ia-pilahin", "name": "Information Architecture Pilah.in"})
    model = ET.SubElement(diagram, "mxGraphModel", {
        "dx": "1600",
        "dy": "1000",
        "grid": "1",
        "gridSize": "10",
        "guides": "1",
        "tooltips": "1",
        "connect": "1",
        "arrows": "1",
        "fold": "1",
        "page": "1",
        "pageScale": "1",
        "pageWidth": "1600",
        "pageHeight": "950",
        "math": "0",
        "shadow": "0"
    })
    root_cell = ET.SubElement(model, "root")
    ET.SubElement(root_cell, "mxCell", {"id": "0"})
    ET.SubElement(root_cell, "mxCell", {"id": "1", "parent": "0"})

    def add_node(cid, val, x, y, w, h, style):
        c = ET.SubElement(root_cell, "mxCell", {"id": cid, "value": val, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(c, "mxGeometry", {"x": str(x), "y": str(y), "width": str(w), "height": str(h), "as": "geometry"})

    def add_edge(eid, src, tgt, style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=1.2;endArrow=classic;endFill=1;"):
        c = ET.SubElement(root_cell, "mxCell", {"id": eid, "style": style, "edge": "1", "source": src, "target": tgt, "parent": "1"})
        ET.SubElement(c, "mxGeometry", {"relative": "1", "as": "geometry"})

    # Styles (Clean Monochrome)
    st_title = "text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];strokeColor=none;fillColor=none;fontColor=#000000;"
    st_root = "rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=13;fontStyle=1;align=center;"
    st_l1 = "rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=11;fontStyle=1;align=center;"
    st_l2 = "rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.2;fontColor=#000000;fontSize=10;fontStyle=1;align=center;"
    st_l3 = "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#333333;strokeWidth=1;fontColor=#222222;fontSize=9;align=left;spacingLeft=8;"

    # Header Title
    add_node("hdr", "<b>ARSITEKTUR INFORMASI (INFORMATION ARCHITECTURE) — PILAH.IN</b><br><span style='font-size:11px;color:#444444;'>Struktur Hierarki Halaman, Navigasi Menu, dan Pengorganisasian Fitur Sistem</span>", 400, 15, 800, 45, st_title)

    # Level 0: Root Platform
    add_node("root_app", "<b>PLATFORM PILAH.IN</b><br><span style='font-size:10px;color:#444444;'>Web Application (Mobile-First)</span>", 680, 75, 240, 45, st_root)

    # Level 1: 3 Pillars
    # 1. Public & Onboarding (x=70)
    add_node("l1_public", "<b>1. AREA PUBLIK &amp; TAMU</b><br><span style='font-size:9px;color:#444444;'>Landing Page &amp; Autentikasi</span>", 110, 160, 240, 45, st_l1)
    add_edge("e_r_pub", "root_app", "l1_public")

    # 2. Citizen Core App (x=400..1180, center at 790)
    add_node("l1_citizen", "<b>2. APLIKASI UTAMA WARGA</b><br><span style='font-size:9px;color:#444444;'>Navigasi 5 Tab Pengguna Penyetor</span>", 680, 160, 240, 45, st_l1)
    add_edge("e_r_cit", "root_app", "l1_citizen")

    # 3. Partner Portal (x=1240) - MITRA PENGELOLA SAMPAH (Bank Sampah, TPS3R, Pengepul, Unit Daur Ulang)
    add_node("l1_mitra", "<b>3. PORTAL MITRA PENGELOLA</b><br><span style='font-size:9px;color:#444444;'>Bank Sampah, TPS3R &amp; Unit Daur Ulang</span>", 1250, 160, 250, 45, st_l1)
    add_edge("e_r_mit", "root_app", "l1_mitra")

    # ================= LEVEL 2 & 3: PUBLIC AREA =================
    add_node("pub_landing", "Halaman Landing<br>&amp; Visi Sirkular", 60, 250, 160, 40, st_l2)
    add_node("pub_reg", "Formulir Registrasi<br>&amp; Verifikasi OTP", 60, 390, 160, 40, st_l2)
    add_node("pub_login", "Formulir Login &amp;<br>Lupa Kata Sandi", 60, 560, 160, 40, st_l2)

    add_edge("e_p1", "l1_public", "pub_landing")
    add_edge("e_p2", "l1_public", "pub_reg")
    add_edge("e_p3", "l1_public", "pub_login")

    # Sub-items under Landing
    add_node("sub_l1", "• 4 Alur Sirkular (Pilah-Jemput-Uang)<br>• Perbandingan Solusi Nilai Nyata<br>• Daftar Harga Komoditas Sampah<br>• Call-to-Action Daftar Warga", 60, 295, 160, 75, st_l3)

    # Sub-items under Register
    add_node("sub_r1", "• Pilihan Peran (Warga / Mitra)<br>• Input Nama, WhatsApp, Kata Sandi<br>• Input 6 Digit OTP WhatsApp<br>• Input Alamat &amp; Patokan Rumah<br>• Pembuatan 6 Digit PIN Transaksi", 60, 435, 160, 95, st_l3)

    # Sub-items under Login
    add_node("sub_lg1", "• Input No. WhatsApp / Email<br>• Input Kata Sandi Akun<br>• Fitur Pemulihan Lupa Sandi<br>• Verifikasi OTP Reset Sandi<br>• Input Kata Sandi Baru", 60, 605, 160, 95, st_l3)

    # ================= LEVEL 2 & 3: CITIZEN APP (5 TABS) =================
    tabs = [
        ("tab_home", "Tab Beranda<br>(Home Feed)", 280, 250, 170, 40, [
            "• Saldo Mengendap Siap Tarik",
            "• Banner Visi Ekonomi Sirkular",
            "• Lacak Status Tiket Penjemputan",
            "• Kartu Tinder Edukasi Sampah",
            "• Info Jadwal Mitra Terdekat"
        ], 85),
        ("tab_ai", "Tab SnapSort AI<br>(Scanner Kamera)", 470, 250, 170, 40, [
            "• Antarmuka Kamera Realtime",
            "• Tombol Pindai Sampah",
            "• Deteksi Jenis (PET, Kardus, dll)",
            "• Peringatan Limbah B3 / Oli",
            "• Tombol Auto-Prefill ke Setor"
        ], 85),
        ("tab_setor", "Tab Setor Sampah<br>(Formulir Tiket)", 660, 250, 170, 40, [
            "• Katalog Jenis Sampah (PET, Jelantah)",
            "• Stepper Berat Realtime (kg)",
            "• Pilihan: Jemput Armada (Ongkir 10%)",
            "• Pilihan: Drop-off Mandiri (0%)",
            "• Pilih Alamat Jemput & Patokan",
            "• Penerbitan Tiket QR PLH-XXXXXX"
        ], 105),
        ("tab_toko", "Tab Toko Sirkular<br>(Produk Upcycle)", 850, 250, 170, 40, [
            "• Katalog Pupuk Kompos Olahan",
            "• Produk Upcycle & Daur Ulang",
            "• Detail Harga & Stok Kompos",
            "• Pembayaran Potong Saldo Dompet",
            "• Otorisasi PIN Transaksi 6 Digit"
        ], 85),
        ("tab_dompet", "Tab Dompet<br>(Pencairan Tunai)", 1040, 250, 170, 40, [
            "• Total Saldo Mengendap (Rupiah)",
            "• Pilihan E-Wallet (GoPay / DANA)",
            "• Input Nominal Tarik (Min 10k)",
            "• Verifikasi PIN Transaksi 6 Digit",
            "• 0% Biaya Admin Pencairan",
            "• Riwayat Mutasi Kredit & Debit"
        ], 105),
    ]

    for tid, tname, x, y, w, h, items, item_h in tabs:
        add_node(tid, tname, x, y, w, h, st_l2)
        add_edge(f"e_c_{tid}", "l1_citizen", tid)
        sub_text = "<br>".join(items)
        add_node(f"sub_{tid}", sub_text, x, y + 45, w, item_h, st_l3)

    # ================= LEVEL 2 & 3: PARTNER PORTAL (GENERAL MITRA) =================
    add_node("mit_weigh", "Portal Penimbangan<br>&amp; Verifikasi Tiket", 1250, 250, 190, 40, st_l2)
    add_edge("e_m1", "l1_mitra", "mit_weigh")

    add_node("sub_m1", "• Input Nomor Tiket PLH-XXXXXX<br>• Input Bobot Timbangan Riil (kg)<br>• Verifikasi Kesesuaian Sampah<br>• Otomasi Kredit Saldo ke Warga<br>• Pembaruan Status Tiket Selesai", 1250, 295, 190, 95, st_l3)

    add_node("mit_rekap", "Dasbor Operasional<br>&amp; Logistik Mitra", 1250, 420, 190, 40, st_l2)
    add_edge("e_m2", "l1_mitra", "mit_rekap")

    add_node("sub_m2", "• Total Volume Sampah Diterima<br>• Kas Operasional Armada Jemput (10%)<br>• Inventaris Pupuk Kompos Daur Ulang<br>• Rekapitulasi Penyetoran Warga", 1250, 465, 190, 85, st_l3)

    # Save Draw.io XML
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated IA Draw.io at: {output_path}")


def generate_ia_svg(output_path):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1560 760" width="1560" height="760" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="780" y="32" text-anchor="middle" font-size="18" font-weight="bold" fill="#000000">ARSITEKTUR INFORMASI (INFORMATION ARCHITECTURE) — PLATFORM PILAH.IN</text>
  <text x="780" y="52" text-anchor="middle" font-size="11" fill="#444444">Struktur Hierarki Halaman, Pengorganisasian Fitur, dan Navigasi Menu — Format Monochrome</text>

  <!-- Level 0: Root -->
  <rect x="650" y="70" width="260" height="42" rx="21" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="780" y="88" text-anchor="middle" font-size="13" font-weight="bold" fill="#000000">PLATFORM PILAH.IN</text>
  <text x="780" y="102" text-anchor="middle" font-size="10" fill="#444444">Web Application (Mobile-First)</text>

  <!-- Connector from Root to 3 Pillars -->
  <path d="M 780 112 L 780 135 L 200 135 L 200 158" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <line x1="780" y1="112" x2="780" y2="158" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 780 112 L 780 135 L 1360 135 L 1360 158" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- ================= PILLAR 1: PUBLIC ================= -->
  <rect x="90" y="160" width="220" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="200" y="178" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">1. AREA PUBLIK &amp; TAMU</text>
  <text x="200" y="192" text-anchor="middle" font-size="9" fill="#444444">Landing Page &amp; Autentikasi</text>

  <!-- Public items -->
  <line x1="200" y1="202" x2="200" y2="238" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="90" y="240" width="220" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="200" y="260" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Halaman Landing &amp; Visi</text>
  <rect x="90" y="275" width="220" height="70" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="100" y="292" font-size="9" fill="#222222">• 4 Alur Sirkular (Pilah-Jemput-Uang)</text>
  <text x="100" y="307" font-size="9" fill="#222222">• Perbandingan Solusi Nilai Nyata</text>
  <text x="100" y="322" font-size="9" fill="#222222">• Daftar Harga Komoditas Terkini</text>
  <text x="100" y="337" font-size="9" fill="#222222">• Call-to-Action Daftar Warga</text>

  <rect x="90" y="365" width="220" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="200" y="385" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Formulir Registrasi &amp; OTP</text>
  <rect x="90" y="400" width="220" height="85" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="100" y="417" font-size="9" fill="#222222">• Pilih Peran (Warga / Mitra)</text>
  <text x="100" y="432" font-size="9" fill="#222222">• Input Nama, WhatsApp, Kata Sandi</text>
  <text x="100" y="447" font-size="9" fill="#222222">• Verifikasi 6 Digit OTP WhatsApp</text>
  <text x="100" y="462" font-size="9" fill="#222222">• Input Alamat &amp; Patokan Rumah</text>
  <text x="100" y="477" font-size="9" fill="#222222">• Pembuatan 6 Digit PIN Transaksi</text>

  <rect x="90" y="505" width="220" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="200" y="525" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Formulir Login &amp; Lupa Sandi</text>
  <rect x="90" y="540" width="220" height="85" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="100" y="557" font-size="9" fill="#222222">• Input No WhatsApp / Email</text>
  <text x="100" y="572" font-size="9" fill="#222222">• Input Kata Sandi Akun</text>
  <text x="100" y="587" font-size="9" fill="#222222">• Fitur Pemulihan Lupa Kata Sandi</text>
  <text x="100" y="602" font-size="9" fill="#222222">• Verifikasi OTP Reset Sandi</text>
  <text x="100" y="617" font-size="9" fill="#222222">• Pembaruan Kata Sandi Baru</text>


  <!-- ================= PILLAR 2: CITIZEN APP ================= -->
  <rect x="660" y="160" width="240" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="780" y="178" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">2. APLIKASI UTAMA WARGA</text>
  <text x="780" y="192" text-anchor="middle" font-size="9" fill="#444444">Navigasi 5 Tab Pengguna Penyetor</text>

  <!-- Connectors to 5 Tabs -->
  <path d="M 780 202 L 780 220 L 410 220 L 410 238" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 780 202 L 780 220 L 595 220 L 595 238" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <line x1="780" y1="202" x2="780" y2="238" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 780 202 L 780 220 L 965 220 L 965 238" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 780 202 L 780 220 L 1150 220 L 1150 238" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Tab 1: Beranda -->
  <rect x="330" y="240" width="160" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="410" y="260" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Tab Beranda</text>
  <rect x="330" y="275" width="160" height="85" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="338" y="292" font-size="8.5" fill="#222222">• Saldo Mengendap Siap Tarik</text>
  <text x="338" y="307" font-size="8.5" fill="#222222">• Banner Visi Ekonomi Sirkular</text>
  <text x="338" y="322" font-size="8.5" fill="#222222">• Lacak Status Tiket Penjemputan</text>
  <text x="338" y="337" font-size="8.5" fill="#222222">• Kartu Swipe Edukasi Sampah</text>
  <text x="338" y="352" font-size="8.5" fill="#222222">• Info Jam Buka Mitra Terdekat</text>

  <!-- Tab 2: SnapSort AI -->
  <rect x="515" y="240" width="160" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="595" y="260" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Tab SnapSort AI</text>
  <rect x="515" y="275" width="160" height="85" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="523" y="292" font-size="8.5" fill="#222222">• Viewfinder Kamera Realtime</text>
  <text x="523" y="307" font-size="8.5" fill="#222222">• Tombol Pindai Sampah</text>
  <text x="523" y="322" font-size="8.5" fill="#222222">• Deteksi Objek &amp; Akurasi</text>
  <text x="523" y="337" font-size="8.5" fill="#222222">• Peringatan Bahaya B3 / Oli</text>
  <text x="523" y="352" font-size="8.5" fill="#222222">• Tombol Auto-Prefill ke Setor</text>

  <!-- Tab 3: Setor Sampah -->
  <rect x="700" y="240" width="160" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="780" y="260" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Tab Setor Sampah</text>
  <rect x="700" y="275" width="160" height="100" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="708" y="292" font-size="8.5" fill="#222222">• Pilihan Kardus, PET, Jelantah</text>
  <text x="708" y="307" font-size="8.5" fill="#222222">• Stepper Berat Realtime (kg)</text>
  <text x="708" y="322" font-size="8.5" fill="#222222">• Jemput Armada (Ongkir 10%)</text>
  <text x="708" y="337" font-size="8.5" fill="#222222">• Drop-off Mandiri (0% Ongkir)</text>
  <text x="708" y="352" font-size="8.5" fill="#222222">• Pilih Alamat &amp; Patokan Rumah</text>
  <text x="708" y="367" font-size="8.5" fill="#222222">• Terbitkan Tiket QR PLH-XXXX</text>

  <!-- Tab 4: Toko Sirkular -->
  <rect x="885" y="240" width="160" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="965" y="260" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Tab Toko Sirkular</text>
  <rect x="885" y="275" width="160" height="85" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="893" y="292" font-size="8.5" fill="#222222">• Katalog Pupuk Kompos Olahan</text>
  <text x="893" y="307" font-size="8.5" fill="#222222">• Kerajinan Upcycle Mitra</text>
  <text x="893" y="322" font-size="8.5" fill="#222222">• Detail Harga &amp; Stok Produk</text>
  <text x="893" y="337" font-size="8.5" fill="#222222">• Checkout Potong Saldo</text>
  <text x="893" y="352" font-size="8.5" fill="#222222">• Otorisasi PIN Transaksi</text>

  <!-- Tab 5: Dompet -->
  <rect x="1070" y="240" width="160" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="1150" y="260" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Tab Dompet</text>
  <rect x="1070" y="275" width="160" height="100" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="1078" y="292" font-size="8.5" fill="#222222">• Total Saldo Mengendap</text>
  <text x="1078" y="307" font-size="8.5" fill="#222222">• Pilihan GoPay / DANA</text>
  <text x="1078" y="322" font-size="8.5" fill="#222222">• Input Nominal (Min 10k)</text>
  <text x="1078" y="337" font-size="8.5" fill="#222222">• Validasi PIN Transaksi</text>
  <text x="1078" y="352" font-size="8.5" fill="#222222">• 0% Admin Fee Pencairan</text>
  <text x="1078" y="367" font-size="8.5" fill="#222222">• Mutasi Riwayat Kredit/Debit</text>


  <!-- ================= PILLAR 3: PARTNER PORTAL (GENERAL MITRA) ================= -->
  <rect x="1260" y="160" width="210" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="1365" y="178" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">3. PORTAL MITRA PENGELOLA</text>
  <text x="1365" y="192" text-anchor="middle" font-size="9" fill="#444444">Bank Sampah, TPS3R &amp; Daur Ulang</text>

  <line x1="1365" y1="202" x2="1365" y2="238" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="1260" y="240" width="210" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="1365" y="260" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Portal Verifikasi Tiket</text>
  <rect x="1260" y="275" width="210" height="85" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="1270" y="292" font-size="8.5" fill="#222222">• Input ID Tiket PLH-XXXXXX</text>
  <text x="1270" y="307" font-size="8.5" fill="#222222">• Input Bobot Timbangan Riil (kg)</text>
  <text x="1270" y="322" font-size="8.5" fill="#222222">• Verifikasi Kesesuaian Fisik</text>
  <text x="1270" y="337" font-size="8.5" fill="#222222">• Kredit Saldo Instan ke Warga</text>
  <text x="1270" y="352" font-size="8.5" fill="#222222">• Pembaruan Status Tiket Selesai</text>

  <rect x="1260" y="380" width="210" height="32" rx="3" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="1365" y="400" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Dasbor Operasional &amp; Kas</text>
  <rect x="1260" y="415" width="210" height="85" fill="#ffffff" stroke="#444444" stroke-width="0.8"/>
  <text x="1270" y="432" font-size="8.5" fill="#222222">• Total Tonase Sampah Diterima</text>
  <text x="1270" y="447" font-size="8.5" fill="#222222">• Kas Biaya Armada Jemput (10%)</text>
  <text x="1270" y="462" font-size="8.5" fill="#222222">• Inventaris Pupuk Kompos Siap Jual</text>
  <text x="1270" y="477" font-size="8.5" fill="#222222">• Rekapitulasi Penyetoran Warga</text>
  <text x="1270" y="492" font-size="8.5" fill="#222222">• Ekspor Laporan Bulanan Mitra</text>
</svg>'''
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated IA SVG at: {output_path}")

def render_ia_png():
    svg_file = "/home/jansky/pilahin-app/flow_screenshots/information_architecture_pilahin.svg"
    html_file = "/home/jansky/pilahin-app/flow_screenshots/information_architecture_pilahin.html"
    png_file = "/home/jansky/pilahin-app/flow_screenshots/information_architecture_pilahin.png"

    generate_ia_svg(svg_file)

    with open(svg_file, "r", encoding="utf-8") as f:
        svg_content = f.read()

    html_content = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Information Architecture Pilah.in</title>
  <style>
    body {{
      margin: 0;
      padding: 24px;
      background: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
  </style>
</head>
<body>
  {svg_content}
</body>
</html>'''

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    cmd = [
        "/home/jansky/.local/bin/google-chrome",
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--window-size=1640,820",
        f"--screenshot={png_file}",
        html_file
    ]
    subprocess.run(cmd, check=True)
    print(f"Generated IA PNG screenshot at: {png_file}")

    # Copy to Screenshots_Userflow and root
    import shutil
    shutil.copy(png_file, "/home/jansky/Screenshots_Userflow/information_architecture_pilahin.png")
    shutil.copy(png_file, "/home/jansky/.gemini/antigravity-cli/brain/aee97e02-8282-4ad4-be88-03497eee84f2/information_architecture_pilahin.png")
    shutil.copy(png_file, "/home/jansky/pilahin-app/public/flow_screenshots/information_architecture_pilahin.png")
    shutil.copy(png_file, "/home/jansky/pilahin-app/dist/flow_screenshots/information_architecture_pilahin.png")
    print("Copied updated IA PNG to all required directories!")

if __name__ == "__main__":
    generate_ia_drawio("/home/jansky/pilahin-app/information_architecture_pilahin.drawio")
    import shutil
    shutil.copy("/home/jansky/pilahin-app/information_architecture_pilahin.drawio", "/home/jansky/information_architecture_pilahin.drawio")
    render_ia_png()
