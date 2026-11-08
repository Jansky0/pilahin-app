import xml.etree.ElementTree as ET
import html

class DrawIOBuilder:
    def __init__(self, filename):
        self.filename = filename
        self.root = ET.Element("mxfile", {
            "host": "app.diagrams.net",
            "modified": "2026-10-31T14:30:00.000Z",
            "agent": "Pilahin-Architecture-Agent",
            "version": "21.6.8",
            "type": "device"
        })

    def add_page(self, name, page_id):
        diagram = ET.SubElement(self.root, "diagram", {"id": page_id, "name": name})
        model = ET.SubElement(diagram, "mxGraphModel", {
            "dx": "1422",
            "dy": "800",
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": "1654",
            "pageHeight": "1169",
            "math": "0",
            "shadow": "0"
        })
        root_cell = ET.SubElement(model, "root")
        ET.SubElement(root_cell, "mxCell", {"id": "0"})
        ET.SubElement(root_cell, "mxCell", {"id": "1", "parent": "0"})
        return root_cell

    def add_swimlane(self, parent, cell_id, name, x, y, width, height, fill_color, stroke_color):
        style = f"swimlane;whiteSpace=wrap;html=1;startSize=32;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=32;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor={fill_color};strokeColor={stroke_color};fontColor=#0f172a;fontSize=13;"
        cell = ET.SubElement(parent, "mxCell", {
            "id": cell_id,
            "value": name,
            "style": style,
            "vertex": "1",
            "parent": "1"
        })
        ET.SubElement(cell, "mxGeometry", {
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "as": "geometry"
        })
        return cell

    def add_node(self, parent, cell_id, value, x, y, width, height, shape_type="box", fill_color="#ffffff", stroke_color="#059669", font_color="#0f172a"):
        if shape_type == "box":
            style = f"rounded=1;whiteSpace=wrap;html=1;arcSize=14;fillColor={fill_color};strokeColor={stroke_color};strokeWidth=1.5;fontColor={font_color};fontSize=11;fontStyle=0;spacing=6;shadow=0;"
        elif shape_type == "pill":
            style = f"rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor={fill_color};strokeColor={stroke_color};strokeWidth=2;fontColor={font_color};fontSize=12;fontStyle=1;spacing=4;"
        elif shape_type == "rhombus":
            style = f"rhombus;whiteSpace=wrap;html=1;fillColor={fill_color};strokeColor={stroke_color};strokeWidth=1.5;fontColor={font_color};fontSize=11;fontStyle=1;"
        elif shape_type == "database":
            style = f"shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=12;fillColor={fill_color};strokeColor={stroke_color};strokeWidth=1.5;fontColor={font_color};fontSize=11;"
        elif shape_type == "header":
            style = f"text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=18;fontStyle=1;fontColor={font_color};"
        else:
            style = f"whiteSpace=wrap;html=1;fillColor={fill_color};strokeColor={stroke_color};"

        cell = ET.SubElement(parent, "mxCell", {
            "id": cell_id,
            "value": value,
            "style": style,
            "vertex": "1",
            "parent": "1"
        })
        ET.SubElement(cell, "mxGeometry", {
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "as": "geometry"
        })
        return cell

    def add_edge(self, parent, edge_id, source_id, target_id, label="", stroke_color="#059669", dashed=False):
        style = f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor={stroke_color};strokeWidth=1.5;fontSize=10;fontColor=#334155;endArrow=classic;endFill=1;"
        if dashed:
            style += "dashed=1;"
        cell = ET.SubElement(parent, "mxCell", {
            "id": edge_id,
            "value": label,
            "style": style,
            "edge": "1",
            "source": source_id,
            "target": target_id,
            "parent": "1"
        })
        ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
        return cell

    def save(self):
        tree = ET.ElementTree(self.root)
        ET.indent(tree, space="  ")
        tree.write(self.filename, encoding="utf-8", xml_declaration=True)
        print(f"Generated Draw.io diagram at: {self.filename}")


def generate_pilahin_diagram(output_path):
    builder = DrawIOBuilder(output_path)

    # -------------------------------------------------------------
    # PAGE 1: USERFLOW ONBOARDING, AUTENTIKASI & STRUKTUR DASBOR
    # -------------------------------------------------------------
    p1 = builder.add_page("1. Onboarding & Autentikasi", "page-auth")
    
    # Title
    builder.add_node(p1, "t1", "<b>PILAH.IN — USERFLOW ONBOARDING & AUTENTIKASI</b><br><span style='font-size:12px;font-weight:normal;color:#64748b;'>Alur Pengguna Baru, Masuk Akun, Deskripsi Platform & Pemisahan Peran</span>", 400, 20, 600, 50, "header", font_color="#065f46")

    # Start
    builder.add_node(p1, "start_app", "MULAI<br>(Buka Aplikasi / Web)", 600, 90, 160, 40, "pill", fill_color="#d1fae5", stroke_color="#059669", font_color="#065f46")

    # Landing Page
    builder.add_node(p1, "landing", "<b>Halaman Landing & Deskripsi</b><br>• Narasi Platform Sirkular<br>• Solusi: Uang Asli vs Masalah Sampah<br>• 4 Langkah Alur Sirkular<br>• Indeks Harga Sampah Real-Time", 570, 160, 220, 90, "box", fill_color="#f0fdf4", stroke_color="#10b981")
    builder.add_edge(p1, "e1", "start_app", "landing")

    # Decision: Punya Akun?
    builder.add_node(p1, "dec_auth", "Punya Akun?", 620, 280, 120, 60, "rhombus", fill_color="#fef3c7", stroke_color="#d97706", font_color="#92400e")
    builder.add_edge(p1, "e2", "landing", "dec_auth")

    # Branch 1: Register Screen
    builder.add_node(p1, "register", "<b>Halaman Pendaftaran (Penuh)</b><br>• Pilih Peran: Warga vs Mitra<br>• Nama Lengkap & No WhatsApp<br>• Password & Email<br>• Alamat Utama & Patokan Rumah", 320, 370, 210, 85, "box", fill_color="#ecfdf5", stroke_color="#059669")
    builder.add_edge(p1, "e3", "dec_auth", "register", "Belum (Daftar)")

    # Branch 2: Login Screen
    builder.add_node(p1, "login", "<b>Halaman Masuk (Penuh)</b><br>• Input Email / No WhatsApp<br>• Input Kata Sandi<br>• <i>Fast Demo Login 1-Klik:</i><br>  - Warga (Raka Pradipta)<br>  - Mitra (Ibu Sri Mulyani)", 830, 370, 210, 85, "box", fill_color="#eff6ff", stroke_color="#3b82f6", font_color="#1e3a8a")
    builder.add_edge(p1, "e4", "dec_auth", "login", "Sudah (Masuk)")

    # Direct Demo/Skip to App
    builder.add_node(p1, "direct_dash", "Akses Langsung Dasbor<br>(Mode Tamu / Eksplorasi)", 585, 390, 190, 45, "box", fill_color="#f1f5f9", stroke_color="#64748b")
    builder.add_edge(p1, "e5", "dec_auth", "direct_dash", "Eksplorasi")

    # Decision Role
    builder.add_node(p1, "dec_role", "Peran Akun?", 620, 490, 120, 60, "rhombus", fill_color="#fef3c7", stroke_color="#d97706", font_color="#92400e")
    builder.add_edge(p1, "e6", "register", "dec_role")
    builder.add_edge(p1, "e7", "login", "dec_role")
    builder.add_edge(p1, "e8", "direct_dash", "dec_role")

    # Warga Dashboard
    builder.add_node(p1, "warga_dash", "<b>DASBOR UTAMA WARGA</b><br>• Kartu Saldo Mengendap Tunai<br>• On-Page Deskripsi Singkat Visi<br>• Quick Action: Setor, Tarik, Toko, Riwayat<br>• SnapSort AI & Tinder Card Lacak Jejak<br>• Bottom Bar: Beranda, Setor, Toko, Dompet", 400, 590, 240, 100, "box", fill_color="#d1fae5", stroke_color="#059669", font_color="#064e3b")
    builder.add_edge(p1, "e9", "dec_role", "warga_dash", "Warga Penyetor")

    # Mitra Dashboard
    builder.add_node(p1, "mitra_dash", "<b>PORTAL MITRA PENGELOLA RW</b><br>• Validasi Tiket & Timbangan Digital<br>• Dasbor Pasokan Sampah Masuk<br>• Manajemen Produk Toko Kompos<br>• Riwayat Penimbangan Selesai", 750, 590, 240, 100, "box", fill_color="#fef3c7", stroke_color="#d97706", font_color="#78350f")
    builder.add_edge(p1, "e10", "dec_role", "mitra_dash", "Pengurus Mitra")

    # Switch Profile
    builder.add_node(p1, "switch_role", "<b>Menu Profil Pengguna</b><br>• Beralih Akun (Warga ↔ Mitra)<br>• Halaman Tentang / Panduan<br>• Sertifikat Dampak Lingkungan<br>• Keluar / Ganti Akun", 585, 730, 210, 80, "box", fill_color="#f8fafc", stroke_color="#94a3b8")
    builder.add_edge(p1, "e11", "warga_dash", "switch_role", "Buka Profil", dashed=True)
    builder.add_edge(p1, "e12", "mitra_dash", "switch_role", "Kembali Warga", dashed=True)

    # -------------------------------------------------------------
    # PAGE 2: ALUR SETOR SAMPAH & PENJEMPUTAN ARMADA TOSSA
    # -------------------------------------------------------------
    p2 = builder.add_page("2. Alur Setor Sampah & Tossa", "page-setor")
    builder.add_node(p2, "t2", "<b>PILAH.IN — ALUR PENYETORAN SAMPAH & PENJEMPUTAN MOTOR TOSSA</b><br><span style='font-size:12px;font-weight:normal;color:#64748b;'>Swimlane Interaction: Warga, Sistem Pilah.in, Armada Tossa & Mitra Bank Sampah</span>", 420, 20, 680, 50, "header", font_color="#065f46")

    # Swimlanes
    builder.add_swimlane(p2, "lane_warga", "WARGA (PENYETOR)", 50, 80, 340, 950, "#f0fdf4", "#10b981")
    builder.add_swimlane(p2, "lane_sistem", "SISTEM APLIKASI PILAH.IN", 410, 80, 340, 950, "#f8fafc", "#64748b")
    builder.add_swimlane(p2, "lane_armada", "ARMADA PENJEMPUT TOSSA", 770, 80, 340, 950, "#fffbeb", "#f59e0b")
    builder.add_swimlane(p2, "lane_mitra", "MITRA BANK SAMPAH / TPS3R", 1130, 80, 340, 950, "#eff6ff", "#3b82f6")

    # Warga actions
    builder.add_node(p2, "s_step1", "<b>Buka Tab Setor</b><br>Pilih 1 atau lebih jenis sampah:<br>• Kardus Box (Rp 1.800/kg)<br>• Botol PET (Rp 3.500/kg)<br>• Minyak Jelantah (Rp 7.000/L)<br>• Sisa Organik Dapur (Rp 800/kg)", 90, 140, 260, 90, "box", fill_color="#ffffff", stroke_color="#059669")
    builder.add_node(p2, "s_step2", "<b>Atur Estimasi Bobot</b><br>Stepper berat (min. 1 kg)", 120, 260, 200, 50, "box")
    builder.add_edge(p2, "se1", "s_step1", "s_step2")

    # Sistem Live Calc
    builder.add_node(p2, "s_calc", "<b>Hitung Estimasi Otomatis</b><br>• Gross Total = Bobot x Harga<br>• Tampilkan Saldo Potensial", 450, 260, 260, 60, "box", fill_color="#ffffff", stroke_color="#64748b")
    builder.add_edge(p2, "se2", "s_step2", "s_calc")

    # Decision Opsi Setor
    builder.add_node(p2, "s_metode", "Metode Setor?", 160, 345, 120, 60, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p2, "se3", "s_calc", "s_metode")

    # Opsi A: Jemput Tossa
    builder.add_node(p2, "s_pickup", "<b>Opsi: Jemput Armada Tossa</b><br>• Pilih Chip Alamat (Rumah/Kantor/Kos)<br>• Cek Kontak & WhatsApp aktif<br>• Isi Patokan Rumah (misal: Pagar hitam)<br>• Sistem terapkan potongan 10% ongkir", 80, 440, 280, 85, "box", fill_color="#ecfdf5", stroke_color="#059669")
    builder.add_edge(p2, "se4", "s_metode", "s_pickup", "Pilih Jemput")

    # Opsi B: Antar Sendiri
    builder.add_node(p2, "s_dropoff", "<b>Opsi: Antar Sendiri</b><br>• Pilih Bank Sampah RW terdekat<br>• 100% Saldo Utuh Tanpa Ongkir", 100, 555, 240, 60, "box", fill_color="#f0fdf4", stroke_color="#10b981")
    builder.add_edge(p2, "se5", "s_metode", "s_dropoff", "Pilih Drop-off")

    # Buat Tiket
    builder.add_node(p2, "s_btn_tiket", "Klik: <b>Buat Tiket Penyetoran</b>", 130, 645, 180, 40, "pill", fill_color="#059669", stroke_color="#047857", font_color="#ffffff")
    builder.add_edge(p2, "se6", "s_pickup", "s_btn_tiket")
    builder.add_edge(p2, "se7", "s_dropoff", "s_btn_tiket")

    # Sistem Generate Tiket
    builder.add_node(p2, "s_gen_tiket", "<b>Terbitkan Tiket Digital</b><br>• Kode Tiket (cth: PLH-386477)<br>• QR Code Tiket Penyetoran<br>• Status: Menunggu Penjemputan", 450, 635, 260, 65, "box", fill_color="#e0e7ff", stroke_color="#4f46e5", font_color="#1e1b4b")
    builder.add_edge(p2, "se8", "s_btn_tiket", "s_gen_tiket")

    # Armada Tossa Dispatched
    builder.add_node(p2, "armada_dispatch", "<b>Terima Tugas Jemput</b><br>• Terima alamat & patokan rumah<br>• Hubungi warga via WhatsApp<br>• Armada Motor Tossa meluncur", 810, 635, 260, 65, "box", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p2, "se9", "s_gen_tiket", "armada_dispatch")

    # On site digital weighing
    builder.add_node(p2, "armada_weigh", "<b>Penimbangan di Lokasi</b><br>• Timbang digital gantung di teras<br>• Tunjukkan bobot riil ke warga<br>• Bawa sampah ke TPS3R", 810, 735, 260, 65, "box", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p2, "se10", "armada_dispatch", "armada_weigh")

    # Mitra Input Verification
    builder.add_node(p2, "mitra_input", "<b>Verifikasi Tiket di Portal</b><br>• Masukkan Kode Tiket (PLH-xxx)<br>• Input bobot riil timbangan<br>• Klik 'Verifikasi & Timbang'", 1170, 735, 260, 70, "box", fill_color="#dbeafe", stroke_color="#2563eb", font_color="#1e3a8a")
    builder.add_edge(p2, "se11", "armada_weigh", "mitra_input")

    # Sistem Crediting
    builder.add_node(p2, "s_credit", "<b>Kredit Saldo Mengendap</b><br>• Update Saldo Tunai Warga detik itu juga<br>• Tambah total kg daur ulang warga<br>• Catat transaksi kredit ke riwayat<br>• Kirim notifikasi toast", 450, 835, 260, 85, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p2, "se12", "mitra_input", "s_credit")

    # Warga receives balance
    builder.add_node(p2, "warga_done", "<b>Saldo Tunai Bertambah</b><br>Siap dicairkan atau dibelanjakan!", 110, 855, 220, 50, "pill", fill_color="#22c55e", stroke_color="#15803d", font_color="#ffffff")
    builder.add_edge(p2, "se13", "s_credit", "warga_done")

    # -------------------------------------------------------------
    # PAGE 3: EKONOMI SIRKULAR — PEMANFAATAN SALDO LIKUID
    # -------------------------------------------------------------
    p3 = builder.add_page("3. Pemanfaatan Saldo Sirkular", "page-wallet")
    builder.add_node(p3, "t3", "<b>PILAH.IN — ALUR PEMANFAATAN SALDO & EKONOMI SIRKULAR</b><br><span style='font-size:12px;font-weight:normal;color:#64748b;'>Loop Tertutup: Belanja Produk Olahan Bank Sampah vs Pencairan Tunai ke E-Wallet</span>", 400, 20, 700, 50, "header", font_color="#065f46")

    # Starting balance
    builder.add_node(p3, "w_balance", "<b>Saldo Mengendap Warga</b><br>(Rupiah Asli Hasil Penyetoran Sampah)", 600, 90, 280, 50, "box", fill_color="#d1fae5", stroke_color="#059669", font_color="#064e3b")

    # Decision Loop
    builder.add_node(p3, "w_choice", "Pilihan Penggunaan Saldo?", 650, 175, 180, 60, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p3, "we1", "w_balance", "w_choice")

    # BRANCH 1: BELANJA TOKO SIRKULAR MITRA
    builder.add_node(p3, "store_browse", "<b>Buka Toko Sirkular Mitra</b><br>Pilih produk hasil binaan bank sampah:<br>• Pupuk Kompos Organik Super (Rp 18.000)<br>• Pot Bunga Daur Ulang Plastik (Rp 12.500)<br>• Eco-Enzyme Pembersih Alami (Rp 15.000)", 280, 260, 260, 85, "box", fill_color="#f0fdf4", stroke_color="#10b981")
    builder.add_edge(p3, "we2", "w_choice", "store_browse", "Belanja Produk Upcycle")

    # Check store balance
    builder.add_node(p3, "store_check", "Saldo >= Harga Produk?", 330, 375, 160, 60, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p3, "we3", "store_browse", "store_check")

    builder.add_node(p3, "store_reject", "Tolak: Saldo Tidak Cukup<br>(Toast Error)", 120, 385, 170, 40, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#881337")
    builder.add_edge(p3, "we4", "store_check", "store_reject", "Tidak Cukup")

    builder.add_node(p3, "store_success", "<b>Pembelian Berhasil</b><br>• Saldo terpotong langsung<br>• Tercatat di riwayat mutasi debit<br>• Pesanan masuk ke dasbor mitra<br>• Warga terima produk kompos/pot", 280, 475, 260, 80, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p3, "we5", "store_check", "store_success", "Saldo Cukup")

    # Circular loop feedback
    builder.add_node(p3, "loop_close", "<b>SIKLUS SIRKULAR TERTUTUP</b><br>Sampah warga ➔ Diolah Bank Sampah RW ➔ Kembali jadi produk bermanfaat di kebun/rumah warga", 280, 595, 260, 75, "pill", fill_color="#059669", stroke_color="#047857", font_color="#ffffff")
    builder.add_edge(p3, "we6", "store_success", "loop_close")

    # BRANCH 2: TARIK TUNAI KE E-WALLET
    builder.add_node(p3, "cashout_form", "<b>Buka Tab Dompet & Tarik Tunai</b><br>• Pilih E-Wallet: GoPay / DANA<br>• Input Nominal (Preset: 25k, 50k, 100k)<br>• Input Nomor HP Akun E-Wallet", 940, 260, 260, 85, "box", fill_color="#eff6ff", stroke_color="#3b82f6", font_color="#1e3a8a")
    builder.add_edge(p3, "we7", "w_choice", "cashout_form", "Tarik Tunai Rupiah")

    # Validate Cashout
    builder.add_node(p3, "cashout_val1", "Nominal >= Rp 10.000<br>& Valid Phone?", 990, 375, 160, 60, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p3, "we8", "cashout_form", "cashout_val1")

    builder.add_node(p3, "cashout_err1", "Tolak: Di bawah Rp 10.000<br>atau format no HP salah", 1200, 385, 180, 40, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#881337")
    builder.add_edge(p3, "we9", "cashout_val1", "cashout_err1", "Tidak Valid")

    builder.add_node(p3, "cashout_val2", "Saldo Mengendap >= Nominal?", 990, 475, 160, 60, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p3, "we10", "cashout_val1", "cashout_val2", "Valid")

    builder.add_node(p3, "cashout_err2", "Tolak: Saldo Mengendap<br>Tidak Mencukupi", 1200, 485, 180, 40, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#881337")
    builder.add_edge(p3, "we11", "cashout_val2", "cashout_err2", "Tidak Cukup")

    builder.add_node(p3, "cashout_exec", "<b>Pencairan Berhasil Diproses</b><br>• Saldo dipotong seketika<br>• Uang tunai ditransfer ke GoPay/DANA<br>• 0% Biaya Admin<br>• Tercatat di buku besar mutasi", 940, 580, 260, 80, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p3, "we12", "cashout_val2", "cashout_exec", "Cukup")

    builder.add_node(p3, "cashout_done", "<b>Uang Tunai Cair ke Dompet Warga</b><br>Insentif ekonomi nyata atas pemilahan", 960, 700, 220, 50, "pill", fill_color="#22c55e", stroke_color="#15803d", font_color="#ffffff")
    builder.add_edge(p3, "we13", "cashout_exec", "cashout_done")

    # -------------------------------------------------------------
    # PAGE 4: FITUR PENDUKUNG — SNAPSORT AI, JEJAK & SERTIFIKAT
    # -------------------------------------------------------------
    p4 = builder.add_page("4. Fitur AI & Lacak Jejak", "page-features")
    builder.add_node(p4, "t4", "<b>PILAH.IN — ALUR FITUR PENDUKUNG</b><br><span style='font-size:12px;font-weight:normal;color:#64748b;'>SnapSort AI Scanner, Tinder-Style Jejak Sampah & Sertifikat Dampak</span>", 400, 20, 650, 50, "header", font_color="#065f46")

    # Feature 1: SnapSort AI
    builder.add_node(p4, "f1_start", "<b>SnapSort AI Detector</b><br>Pindai Sampah dengan Kamera", 120, 100, 240, 50, "pill", fill_color="#e0f2fe", stroke_color="#0284c7", font_color="#0369a1")
    builder.add_node(p4, "f1_proc", "<b>Analisis Citra AI</b><br>Identifikasi material, estimasi berat,<br>dan tingkat kontaminasi kotoran", 120, 180, 240, 65, "box", fill_color="#ffffff", stroke_color="#0284c7")
    builder.add_edge(p4, "fe1", "f1_start", "f1_proc")
    builder.add_node(p4, "f1_out", "<b>Rekomendasi Pintar</b><br>• Tampilkan Kategori & Harga/kg<br>• Panduan Pembersihan Awal<br>• Shortcut Langsung Masuk ke Tab Setor", 120, 275, 240, 75, "box", fill_color="#f0fdf4", stroke_color="#10b981")
    builder.add_edge(p4, "fe2", "f1_proc", "f1_out")

    # Feature 2: Lacak Jejak Tinder Card
    builder.add_node(p4, "f2_start", "<b>Lacak Jejak Sampah</b><br>Tinder-Style Interactive Stack Cards", 520, 100, 240, 50, "pill", fill_color="#fef3c7", stroke_color="#d97706", font_color="#92400e")
    builder.add_node(p4, "f2_proc", "<b>Interaksi Swipe Card</b><br>Geser kartu kiri/kanan untuk berpindah<br>antar tiket penyetoran aktif", 520, 180, 240, 65, "box", fill_color="#ffffff", stroke_color="#d97706")
    builder.add_edge(p4, "fe3", "f2_start", "f2_proc")
    builder.add_node(p4, "f2_out", "<b>Informasi Transparan</b><br>• Posisi Armada Tossa & Estimasi Tiba<br>• Tahap Olahan (Pencacahan/Pengomposan)<br>• QR Code Tiket Terlampir", 520, 275, 240, 75, "box", fill_color="#fffbeb", stroke_color="#f59e0b")
    builder.add_edge(p4, "fe4", "f2_proc", "f2_out")

    # Feature 3: Sertifikat Dampak
    builder.add_node(p4, "f3_start", "<b>Sertifikat Dampak Sirkular</b><br>Dapat Diakses via Modal Profil", 920, 100, 240, 50, "pill", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_node(p4, "f3_proc", "<b>Kalkulasi Ekologis Riil</b><br>• Formula Konversi Kg ➔ Pohon<br>• Formula Emisi Karbon Tercegah (CO2e)<br>• Level Pahlawan Hijau Warga", 920, 180, 240, 65, "box", fill_color="#ffffff", stroke_color="#16a34a")
    builder.add_edge(p4, "fe5", "f3_start", "f3_proc")
    builder.add_node(p4, "f3_out", "<b>Sertifikat Digital Resmi</b><br>• Kartu Badge & Piagam Penghargaan<br>• Dapat Dibagikan ke Komunitas RW<br>• Memicu Kebanggaan Memilah", 920, 275, 240, 75, "box", fill_color="#f0fdf4", stroke_color="#059669")
    builder.add_edge(p4, "fe6", "f3_proc", "f3_out")

    builder.save()

if __name__ == "__main__":
    generate_pilahin_diagram("/home/jansky/pilahin-app/userflow_pilahin.drawio")
    generate_pilahin_diagram("/home/jansky/userflow_pilahin.drawio")
