import xml.etree.ElementTree as ET

class ComprehensiveDrawIOBuilder:
    def __init__(self, filename):
        self.filename = filename
        self.root = ET.Element("mxfile", {
            "host": "app.diagrams.net",
            "modified": "2026-10-31T15:00:00.000Z",
            "agent": "Pilahin-Detailed-Process-Agent",
            "version": "21.6.8",
            "type": "device"
        })

    def create_canvas(self, name="Userflow Pilah.in (End-to-End)", width=2400, height=4200):
        diagram = ET.SubElement(self.root, "diagram", {"id": "pilahin-complete-flow", "name": name})
        model = ET.SubElement(diagram, "mxGraphModel", {
            "dx": "2000",
            "dy": "1200",
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": str(width),
            "pageHeight": str(height),
            "math": "0",
            "shadow": "0"
        })
        root_cell = ET.SubElement(model, "root")
        ET.SubElement(root_cell, "mxCell", {"id": "0"})
        ET.SubElement(root_cell, "mxCell", {"id": "1", "parent": "0"})
        return root_cell

    def add_section_banner(self, root, cell_id, text, x, y, width=1200, height=40, fill="#0f172a", font="#38bdf8"):
        val = f"<b>{text}</b>"
        style = f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor=#334155;strokeWidth=1.5;fontColor={font};fontSize=13;fontStyle=1;align=left;spacingLeft=16;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_process(self, root, cell_id, title, detail, x, y, width=220, height=65, fill="#ffffff", stroke="#0284c7"):
        val = f"<b>{title}</b><br><span style='font-size:10px;color:#334155;'>{detail}</span>"
        style = f"rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor={fill};strokeColor={stroke};strokeWidth=1.5;fontColor=#0f172a;fontSize=11;spacing=4;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_decision(self, root, cell_id, question, x, y, width=150, height=70):
        style = "rhombus;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=1.5;fontColor=#92400e;fontSize=10;fontStyle=1;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": question, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_happy(self, root, cell_id, title, detail, x, y, width=220, height=65):
        val = f"<b style='color:#14532d;'>✅ {title}</b><br><span style='font-size:10px;color:#166534;'>{detail}</span>"
        style = "rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#dcfce7;strokeColor=#16a34a;strokeWidth=2;fontColor=#14532d;fontSize=11;spacing=4;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_sad(self, root, cell_id, title, detail, x, y, width=220, height=65):
        val = f"<b style='color:#9f1239;'>❌ {title}</b><br><span style='font-size:10px;color:#881337;'>{detail}</span>"
        style = "rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#ffe4e6;strokeColor=#e11d48;strokeWidth=1.5;fontColor=#9f1239;fontSize=10;spacing=4;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_screen_badge(self, root, cell_id, text, x, y, width=200, height=35):
        val = f"📱 <b>Layar:</b> {text}"
        style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#e0e7ff;strokeColor=#4338ca;strokeWidth=1.5;fontColor=#1e1b4b;fontSize=10;fontStyle=1;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_pill(self, root, cell_id, text, x, y, width=160, height=40, fill="#16a34a", font="#ffffff"):
        style = f"rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor={fill};strokeColor=#334155;strokeWidth=1.5;fontColor={font};fontSize=11;fontStyle=1;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": text, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_connector(self, root, edge_id, src, tgt, label="", color="#059669", dashed=False, width=2):
        style = f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor={color};strokeWidth={width};fontSize=10;fontColor={color};fontStyle=1;endArrow=classic;endFill=1;"
        if dashed:
            style += "dashed=1;"
        cell = ET.SubElement(root, "mxCell", {"id": edge_id, "value": label, "style": style, "edge": "1", "source": src, "target": tgt, "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})

    def save(self):
        tree = ET.ElementTree(self.root)
        ET.indent(tree, space="  ")
        tree.write(self.filename, encoding="utf-8", xml_declaration=True)
        print(f"Generated Comprehensive Userflow at: {self.filename}")


def generate_long_flowchart(output_path):
    builder = ComprehensiveDrawIOBuilder(output_path)
    root = builder.create_canvas("Userflow Lengkap Pilah.in (End-to-End)", width=2200, height=4400)

    # Global Legend Box
    style_leg = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#94a3b8;strokeWidth=1.5;fontColor=#0f172a;fontSize=11;align=left;spacingLeft=12;"
    leg = ET.SubElement(root, "mxCell", {
        "id": "legend",
        "value": "<b>LEGENDA ELEMEN USERFLOW:</b><br>"
                 "• Kotak Persegi Panjang = <b>Process / Langkah Operasional Tunggal</b><br>"
                 "• Kotak Belah Ketupat = <b>Decision Point / Pengecekan Logika</b><br>"
                 "• Kotak Hijau = <b>Happy Path (Alur Sukses Utama)</b><br>"
                 "• Kotak Merah = <b>Sad Path (Validasi Error & Alur Alternatif)</b><br>"
                 "• Kotak Ungu = <b>Konteks Layar UI yang Sedang Aktif</b>",
        "style": style_leg, "vertex": "1", "parent": "1"
    })
    ET.SubElement(leg, "mxGeometry", {"x": "60", "y": "20", "width": "400", "height": "90", "as": "geometry"})

    # Main Header
    style_hdr = "text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=20;fontStyle=1;fontColor=#065f46;"
    hdr = ET.SubElement(root, "mxCell", {
        "id": "hdr",
        "value": "<b>PILAH.IN — USERFLOW END-TO-END LENGKAP (SINGLE CONNECTED FLOW)</b><br>"
                 "<span style='font-size:12px;font-weight:normal;color:#64748b;'>"
                 "Alur Granular: 1 Kotak = 1 Process Nyata, Lengkap dengan Decision, Happy Path & Sad Path"
                 "</span>",
        "style": style_hdr, "vertex": "1", "parent": "1"
    })
    ET.SubElement(hdr, "mxGeometry", {"x": "550", "y": "30", "width": "750", "height": "60", "as": "geometry"})

    # =========================================================================
    # FASE 1: ONBOARDING & AUTENTIKASI (Y: 140 - 850)
    # =========================================================================
    builder.add_section_banner(root, "sec1", "FASE 1: ONBOARDING, REGISTRASI, OTP & AUTENTIKASI PENGGUNA", 60, 140, 1400)

    # Start
    builder.add_pill(root, "start", "MULAI: Buka Pilah.in", 650, 200, 180, 40, fill="#0f172a")

    # Landing
    builder.add_screen_badge(root, "scr_landing", "LandingScreen.jsx", 640, 260)
    builder.add_connector(root, "e1", "start", "scr_landing")

    builder.add_process(root, "p_read_landing", "Baca Deskripsi & Visi Sirkular", "Pelajari 4 alur sirkular, masalah vs solusi uang asli, & cek harga sampah", 630, 310, 220, 60)
    builder.add_connector(root, "e2", "scr_landing", "p_read_landing")

    # Decision 1: Has account?
    builder.add_decision(root, "dec_has_account", "Sudah Punya<br>Akun Terdaftar?", 665, 395, 150, 70)
    builder.add_connector(root, "e3", "p_read_landing", "dec_has_account")

    # ------------------ CABANG REGISTRASI (BELUM PUNYA AKUN) ------------------
    builder.add_screen_badge(root, "scr_register", "RegisterScreen.jsx", 200, 480)
    builder.add_connector(root, "e4", "dec_has_account", "scr_register", label="BELUM (Daftar)", color="#0284c7")

    builder.add_process(root, "p_reg_role", "Pilih Peran Akun", "Klik [Warga Penyetor] atau [Mitra Bank Sampah]", 190, 530, 220, 50)
    builder.add_connector(root, "e5", "scr_register", "p_reg_role")

    builder.add_process(root, "p_reg_data", "Input Data Diri & Akun", "Ketik Nama, No WhatsApp, Kata Sandi, & Email (opsional)", 190, 600, 220, 60)
    builder.add_connector(root, "e6", "p_reg_role", "p_reg_data")

    builder.add_decision(root, "dec_reg_valid", "Format Data Valid?<br>(WA >= 10 digit,<br>Pass >= 6 char)", 225, 680, 150, 70)
    builder.add_connector(root, "e7", "p_reg_data", "dec_reg_valid")

    # Sad Path Reg 1
    builder.add_sad(root, "sad_reg_data", "Validasi Input Gagal", "Toast: 'Lengkapi nama, WA, dan password minimal 6 karakter!'", 30, 770, 210, 60)
    builder.add_connector(root, "e8", "dec_reg_valid", "sad_reg_data", label="TIDAK", color="#e11d48")
    builder.add_connector(root, "e8_loop", "sad_reg_data", "p_reg_data", label="Perbaiki", color="#e11d48", dashed=True)

    # Process OTP Verification
    builder.add_process(root, "p_send_otp", "Kirim Kode Verifikasi OTP", "Sistem kirim 6 digit OTP ke WhatsApp pendaftar", 270, 770, 210, 55)
    builder.add_connector(root, "e9", "dec_reg_valid", "p_send_otp", label="YA / LENGKAP", color="#16a34a")

    builder.add_process(root, "p_input_otp", "Input Kode OTP 6 Digit", "Pengguna mengetik kode OTP yang diterima", 270, 845, 210, 50)
    builder.add_connector(root, "e10", "p_send_otp", "p_input_otp")

    builder.add_decision(root, "dec_otp_match", "Kode OTP Cocok?", 300, 915, 150, 65)
    builder.add_connector(root, "e11", "p_input_otp", "dec_otp_match")

    builder.add_sad(root, "sad_otp_err", "Kode OTP Salah", "Toast: 'Kode OTP tidak cocok! Minta kirim ulang kode'", 70, 995, 210, 60)
    builder.add_connector(root, "e12", "dec_otp_match", "sad_otp_err", label="SALAH", color="#e11d48")
    builder.add_connector(root, "e12_loop", "sad_otp_err", "p_send_otp", label="Kirim Ulang", color="#e11d48", dashed=True)

    builder.add_process(root, "p_reg_addr", "Input Alamat Utama & Patokan", "Isi jalan, RT/RW, dan patokan rumah (akses motor Tossa)", 300, 995, 220, 60)
    builder.add_connector(root, "e13", "dec_otp_match", "p_reg_addr", label="COCOK", color="#16a34a")

    builder.add_process(root, "p_reg_pin", "Buat 6 Digit PIN Transaksi", "PIN untuk verifikasi belanja & pencairan tunai dompet", 300, 1075, 220, 55)
    builder.add_connector(root, "e14", "p_reg_addr", "p_reg_pin")

    builder.add_happy(root, "hp_reg_success", "Registrasi Berhasil Selesai", "Akun terbit, alamat tersimpan, PIN aktif, sesi terverifikasi", 300, 1150, 220, 60)
    builder.add_connector(root, "e15", "p_reg_pin", "hp_reg_success", color="#16a34a")

    # ------------------ CABANG LOGIN & LUPA PASSWORD ------------------
    builder.add_screen_badge(root, "scr_login", "LoginScreen.jsx", 950, 480)
    builder.add_connector(root, "e16", "dec_has_account", "scr_login", label="SUDAH (Masuk)", color="#0284c7")

    builder.add_decision(root, "dec_login_method", "Metode Masuk?", 985, 535, 130, 65)
    builder.add_connector(root, "e17", "scr_login", "dec_login_method")

    # Fast Demo Branch
    builder.add_happy(root, "hp_demo_login", "1-Click Fast Demo Login", "Klik [Warga Raka] atau [Mitra Sri] ➔ Langsung bypass ke dasbor", 1150, 600, 210, 60)
    builder.add_connector(root, "e18", "dec_login_method", "hp_demo_login", label="Fast Demo", color="#16a34a")

    # Manual Login Branch
    builder.add_process(root, "p_login_id", "Input No. WA / Email", "Ketik nomor WhatsApp terdaftar", 880, 610, 210, 50)
    builder.add_connector(root, "e19", "dec_login_method", "p_login_id", label="Manual")

    builder.add_decision(root, "dec_forgot_pass", "Lupa Kata Sandi?", 910, 680, 150, 65)
    builder.add_connector(root, "e20", "p_login_id", "dec_forgot_pass")

    # Sub-branch: Lupa Password
    builder.add_process(root, "p_req_reset", "Klik 'Lupa Password'", "Sistem kirim tautan/kode reset via WhatsApp", 1140, 745, 210, 50)
    builder.add_connector(root, "e21", "dec_forgot_pass", "p_req_reset", label="YA (Lupa)", color="#d97706")

    builder.add_process(root, "p_verify_reset_otp", "Verifikasi Kode Reset", "Input kode OTP reset yang masuk ke WA", 1140, 815, 210, 50)
    builder.add_connector(root, "e22", "p_req_reset", "p_verify_reset_otp")

    builder.add_process(root, "p_new_pass", "Input Kata Sandi Baru", "Ketik password baru & simpan perubahan", 1140, 885, 210, 50)
    builder.add_connector(root, "e23", "p_verify_reset_otp", "p_new_pass")

    # Return to login with new password
    builder.add_connector(root, "e24", "p_new_pass", "p_login_id", label="Login Password Baru", color="#0284c7", dashed=True)

    # Normal Password Input
    builder.add_process(root, "p_input_pass", "Input Kata Sandi", "Ketik password akun terdaftar", 880, 775, 210, 50)
    builder.add_connector(root, "e25", "dec_forgot_pass", "p_input_pass", label="INGAT", color="#16a34a")

    builder.add_decision(root, "dec_login_auth", "Kredensial Cocok?", 910, 855, 150, 65)
    builder.add_connector(root, "e26", "p_input_pass", "dec_login_auth")

    builder.add_sad(root, "sad_login_fail", "Kredensial Tidak Cocok", "Toast: 'Email/No WhatsApp atau kata sandi tidak cocok!'", 700, 925, 200, 60)
    builder.add_connector(root, "e27", "dec_login_auth", "sad_login_fail", label="SALAH", color="#e11d48")
    builder.add_connector(root, "e27_loop", "sad_login_fail", "p_input_pass", label="Ulangi", color="#e11d48", dashed=True)

    builder.add_happy(root, "hp_login_success", "Login Berhasil Masuk", "Sesi terbit, toast 'Selamat datang kembali!', redirect dasbor", 930, 955, 220, 60)
    builder.add_connector(root, "e28", "dec_login_auth", "hp_login_success", label="COCOK", color="#16a34a")

    # =========================================================================
    # FASE 2: BERANDA & DETEKSI SAMPAH SNAPSORT AI (Y: 1240 - 1650)
    # =========================================================================
    builder.add_section_banner(root, "sec2", "FASE 2: DASBOR BERANDA WARGA & DETEKSI SAMPAH (SNAPSORT AI)", 60, 1240, 1400)

    builder.add_screen_badge(root, "scr_home", "Beranda Utama Warga (Home Feed)", 640, 1300)
    builder.add_connector(root, "e29", "hp_reg_success", "scr_home", color="#16a34a")
    builder.add_connector(root, "e30", "hp_login_success", "scr_home", color="#16a34a")
    builder.add_connector(root, "e31", "hp_demo_login", "scr_home", color="#16a34a")

    builder.add_process(root, "p_view_home", "Cek Saldo Mengendap & Panduan", "Lihat saldo riil siap tarik, info visi sirkular & kartu Tinder lacak sampah", 630, 1355, 220, 60)
    builder.add_connector(root, "e32", "scr_home", "p_view_home")

    builder.add_decision(root, "dec_use_ai", "Gunakan SnapSort AI<br>untuk Pindai Sampah?", 665, 1435, 150, 70)
    builder.add_connector(root, "e33", "p_view_home", "dec_use_ai")

    # SnapSort AI Sub-flow
    builder.add_screen_badge(root, "scr_snapsort", "Tab SnapSort AI Scanner", 1000, 1450)
    builder.add_connector(root, "e34", "dec_use_ai", "scr_snapsort", label="YA (Buka AI)", color="#0284c7")

    builder.add_process(root, "p_camera_snap", "Pindai Sampah dengan Kamera", "Arahkan lensa ke botol/kardus & klik 'Pindai Sampah Sekarang'", 990, 1505, 220, 55)
    builder.add_connector(root, "e35", "scr_snapsort", "p_camera_snap")

    builder.add_decision(root, "dec_ai_detect", "Kondisi Material<br>Hasil Deteksi AI?", 1025, 1585, 150, 70)
    builder.add_connector(root, "e36", "p_camera_snap", "dec_ai_detect")

    builder.add_sad(root, "sad_ai_b3", "Terdeteksi Limbah B3", "Peringatan Merah: 'Tercemar oli/B3! Dilarang disetor, buang ke TPS B3'", 1240, 1590, 220, 60)
    builder.add_connector(root, "e37", "dec_ai_detect", "sad_ai_b3", label="B3 / Tercemar", color="#e11d48")

    builder.add_sad(root, "sad_ai_blur", "Foto Buram / Tidak Dikenali", "Pesan: 'Objek tidak terdeteksi. Pastikan pencahayaan cukup & foto lebih dekat'", 1240, 1665, 220, 60)
    builder.add_connector(root, "e38", "dec_ai_detect", "sad_ai_blur", label="Buram", color="#e11d48")
    builder.add_connector(root, "e38_loop", "sad_ai_blur", "p_camera_snap", label="Foto Ulang", color="#e11d48", dashed=True)

    builder.add_happy(root, "hp_ai_success", "Deteksi AI Berhasil", "Material PET 96%, Rp 3.500/kg. Klik 'Langsung Setor' ➔ Auto-centang di Tab Setor", 990, 1690, 220, 65)
    builder.add_connector(root, "e39", "dec_ai_detect", "hp_ai_success", label="Bersih & Layak", color="#16a34a")

    # =========================================================================
    # FASE 3: PENGAJUAN SETOR SAMPAH (Y: 1780 - 2350)
    # =========================================================================
    builder.add_section_banner(root, "sec3", "FASE 3: PENGAJUAN SETOR SAMPAH (JEMPUT ARMADA TOSSA VS DROP-OFF MANDIRI)", 60, 1780, 1400)

    builder.add_screen_badge(root, "scr_setor", "Tab 'Setor Sampah'", 640, 1840)
    builder.add_connector(root, "e40", "dec_use_ai", "scr_setor", label="TIDAK (Setor Manual)")
    builder.add_connector(root, "e41", "hp_ai_success", "scr_setor", label="Auto-Prefill", color="#16a34a")

    builder.add_process(root, "p_select_waste", "Pilih Kategori & Atur Berat", "Centang Kardus, Botol PET, Jelantah, atau Organik & naik-turunkan stepper kg", 630, 1895, 220, 60)
    builder.add_connector(root, "e42", "scr_setor", "p_select_waste")

    builder.add_decision(root, "dec_waste_picked", "Minimal 1 Kategori<br>Dipilih & Berat > 0?", 665, 1975, 150, 70)
    builder.add_connector(root, "e43", "p_select_waste", "dec_waste_picked")

    builder.add_sad(root, "sad_no_waste", "Belum Memilih Sampah", "Toast: 'Pilih minimal satu kategori sampah dan tentukan beratnya!'", 400, 1980, 210, 60)
    builder.add_connector(root, "e44", "dec_waste_picked", "sad_no_waste", label="TIDAK", color="#e11d48")
    builder.add_connector(root, "e44_loop", "sad_no_waste", "p_select_waste", label="Pilih Sampah", color="#e11d48", dashed=True)

    builder.add_decision(root, "dec_setor_method", "Metode Setor?", 675, 2075, 130, 65)
    builder.add_connector(root, "e45", "dec_waste_picked", "dec_setor_method", label="YA", color="#16a34a")

    # ------------------ OPSI A: JEMPUT ARMADA TOSSA ------------------
    builder.add_process(root, "p_calc_tossa", "Kalkulasi Ongkir Jemput 10%", "Gross Total - 10% Ongkir Bensin Tossa = Estimasi Saldo Bersih", 460, 2165, 220, 55)
    builder.add_connector(root, "e46", "dec_setor_method", "p_calc_tossa", label="Jemput Tossa", color="#0284c7")

    builder.add_process(root, "p_pick_address", "Pilih Alamat & Cek Patokan", "Pilih chip [Rumah], pastikan No WA aktif & patokan teras terisi", 460, 2240, 220, 60)
    builder.add_connector(root, "e47", "p_calc_tossa", "p_pick_address")

    builder.add_decision(root, "dec_addr_ok", "Alamat Lengkap &<br>Bisa Masuk Tossa?", 495, 2320, 150, 65)
    builder.add_connector(root, "e48", "p_pick_address", "dec_addr_ok")

    builder.add_process(root, "p_edit_addr", "Ubah / Tambah Alamat", "Ketik alamat jalan baru, nomor rumah, dan patokan samping warung", 230, 2322, 210, 60)
    builder.add_connector(root, "e49", "dec_addr_ok", "p_edit_addr", label="Ubah / Kosong", color="#d97706")
    builder.add_connector(root, "e49_done", "p_edit_addr", "p_pick_address", label="Simpan", color="#16a34a")

    builder.add_process(root, "p_btn_tossa", "Klik 'Ajukan Penjemputan'", "Kirim pengajuan tiket jemput ke server", 460, 2410, 220, 50)
    builder.add_connector(root, "e50", "dec_addr_ok", "p_btn_tossa", label="LENGKAP", color="#16a34a")

    # ------------------ OPSI B: ANTAR SENDIRI (DROP-OFF) ------------------
    builder.add_process(root, "p_calc_dropoff", "Kalkulasi Drop-off 0% Ongkir", "Ongkir = Rp 0. Nilai Bersih = 100% Saldo Utuh Tanpa Potongan", 800, 2165, 220, 55)
    builder.add_connector(root, "e51", "dec_setor_method", "p_calc_dropoff", label="Antar Sendiri", color="#0284c7")

    builder.add_process(root, "p_pick_pos", "Pilih Pos Bank Sampah RW", "Pilih Pos RW 05 (Jarak: 650m, Jam operasional: 13.00 - 16.00 WIB)", 800, 2240, 220, 60)
    builder.add_connector(root, "e52", "p_calc_dropoff", "p_pick_pos")

    builder.add_process(root, "p_btn_dropoff", "Klik 'Buat Tiket Mandiri'", "Terbitkan tiket penyetoran langsung ke pos", 800, 2325, 220, 50)
    builder.add_connector(root, "e53", "p_pick_pos", "p_btn_dropoff")

    # Generate Ticket Result
    builder.add_happy(root, "hp_ticket_gen", "Tiket Digital QR Terbit", "ID Tiket: PLH-XXXXXX, QR Code aktif, status 'Menunggu Penjemputan / Drop-off'", 630, 2490, 220, 65)
    builder.add_connector(root, "e54", "p_btn_tossa", "hp_ticket_gen", color="#16a34a")
    builder.add_connector(root, "e55", "p_btn_dropoff", "hp_ticket_gen", color="#16a34a")

    # =========================================================================
    # FASE 4: PENIMBANGAN DIGITAL LAPANGAN & VERIFIKASI MITRA (Y: 2600 - 3050)
    # =========================================================================
    builder.add_section_banner(root, "sec4", "FASE 4: PENIMBANGAN DIGITAL LAPANGAN & VERIFIKASI TIKET MITRA", 60, 2600, 1400)

    builder.add_decision(root, "dec_field_method", "Jenis Penyetoran?", 675, 2660, 130, 65)
    builder.add_connector(root, "e56", "hp_ticket_gen", "dec_field_method")

    # Jemput Tossa Execution
    builder.add_process(root, "p_tossa_arrive", "Motor Tossa Tiba di Alamat", "Kurir cek patokan rumah & hubungi WhatsApp warga", 450, 2740, 220, 55)
    builder.add_connector(root, "e57", "dec_field_method", "p_tossa_arrive", label="Jemput Tossa", color="#0284c7")

    builder.add_decision(root, "dec_citizen_home", "Warga Ada di Rumah?", 485, 2815, 150, 65)
    builder.add_connector(root, "e58", "p_tossa_arrive", "dec_citizen_home")

    builder.add_sad(root, "sad_not_home", "Warga Tidak Ada di Lokasi", "WA tidak dibalas. Kurir ubah status: 'Jadwalkan Ulang'. Tiket tidak hangus", 200, 2817, 220, 60)
    builder.add_connector(root, "e59", "dec_citizen_home", "sad_not_home", label="TIDAK ADA", color="#e11d48")

    builder.add_process(root, "p_digital_weigh", "Timbang Digital di Teras", "Karung digantung di timbangan digital kurir, angka disaksikan bersama", 450, 2900, 220, 60)
    builder.add_connector(root, "e60", "dec_citizen_home", "p_digital_weigh", label="ADA & SIAP", color="#16a34a")

    # Drop-off Execution
    builder.add_process(root, "p_dropoff_arrive", "Warga Bawa Sampah ke Pos RW", "Tiba di Bank Sampah Berkah Lestari RW 05", 810, 2740, 220, 55)
    builder.add_connector(root, "e61", "dec_field_method", "p_dropoff_arrive", label="Antar Sendiri", color="#0284c7")

    builder.add_decision(root, "dec_pos_open", "Tiba Saat Jam Buka?<br>(13.00 - 16.00 WIB)", 845, 2815, 150, 65)
    builder.add_connector(root, "e62", "p_dropoff_arrive", "dec_pos_open")

    builder.add_sad(root, "sad_pos_closed", "Pos RW Tutup", "Tiba jam 18.00. Tiket tetap tersimpan aman, warga kembali esok hari", 1080, 2817, 220, 60)
    builder.add_connector(root, "e63", "dec_pos_open", "sad_pos_closed", label="TUTUP", color="#e11d48")

    builder.add_process(root, "p_pos_weigh", "Petugas Pos Timbang di Tempat", "Gunakan timbangan digital pos bank sampah RW", 810, 2900, 220, 55)
    builder.add_connector(root, "e64", "dec_pos_open", "p_pos_weigh", label="BUKA", color="#16a34a")

    # Partner Portal Verification
    builder.add_screen_badge(root, "scr_mitra", "Portal Mitra Pengelola RW 05", 640, 2985)
    builder.add_connector(root, "e65", "p_digital_weigh", "scr_mitra")
    builder.add_connector(root, "e66", "p_pos_weigh", "scr_mitra")

    builder.add_process(root, "p_mitra_verify", "Input Kode Tiket & Bobot Riil", "Ketik PLH-XXXXXX, ketik bobot timbangan (11 kg), & klik 'Verifikasi'", 630, 3040, 220, 60)
    builder.add_connector(root, "e67", "scr_mitra", "p_mitra_verify")

    builder.add_happy(root, "hp_balance_credit", "Saldo Tunai Masuk Dompet!", "Saldo mengendap bertambah detik itu juga (+Rp 22.410), total kg naik, tiket selesai", 630, 3120, 220, 65)
    builder.add_connector(root, "e68", "p_mitra_verify", "hp_balance_credit", color="#16a34a")

    # =========================================================================
    # FASE 5: PEMANFAATAN SALDO — BELANJA VS TARIK TUNAI (Y: 3230 - 3900)
    # =========================================================================
    builder.add_section_banner(root, "sec5", "FASE 5: PEMANFAATAN SALDO LIKUID (BELANJA SIRKULAR VS TARIK TUNAI E-WALLET)", 60, 3230, 1400)

    builder.add_decision(root, "dec_wallet_use", "Pilihan Penggunaan<br>Saldo Mengendap?", 675, 3290, 130, 65)
    builder.add_connector(root, "e69", "hp_balance_credit", "dec_wallet_use")

    # ------------------ CABANG A: BELANJA TOKO SIRKULAR ------------------
    builder.add_screen_badge(root, "scr_toko", "Tab 'Toko Sirkular Mitra'", 400, 3370)
    builder.add_connector(root, "e70", "dec_wallet_use", "scr_toko", label="Belanja Produk Upcycle", color="#0284c7")

    builder.add_process(root, "p_pick_prod", "Pilih Pupuk Kompos (Rp 18k)", "Pilih Pupuk Kompos Super 5kg olahan sampah warga & klik 'Beli'", 390, 3425, 220, 55)
    builder.add_connector(root, "e71", "scr_toko", "p_pick_prod")

    builder.add_decision(root, "dec_balance_prod", "Saldo Mengendap >=<br>Rp 18.000?", 425, 3500, 150, 65)
    builder.add_connector(root, "e72", "p_pick_prod", "dec_balance_prod")

    builder.add_sad(root, "sad_no_money_store", "Saldo Tidak Cukup", "Toast: 'Saldo tidak mencukupi untuk pembelian ini!' ➔ Transaksi batal", 150, 3502, 220, 60)
    builder.add_connector(root, "e73", "dec_balance_prod", "sad_no_money_store", label="TIDAK CUKUP", color="#e11d48")

    builder.add_process(root, "p_input_pin_store", "Input PIN Transaksi 6 Digit", "Verifikasi keamanan pemotongan saldo", 390, 3585, 220, 50)
    builder.add_connector(root, "e74", "dec_balance_prod", "p_input_pin_store", label="CUKUP", color="#16a34a")

    builder.add_happy(root, "hp_store_success", "Pembelian Berhasil Selesai!", "Saldo dipotong -Rp 18.000. Kompos diserahkan ke warga. LOOP SIRKULAR TERTUTUP!", 390, 3655, 220, 65)
    builder.add_connector(root, "e75", "p_input_pin_store", "hp_store_success", color="#16a34a")

    # ------------------ CABANG B: TARIK TUNAI KE E-WALLET ------------------
    builder.add_screen_badge(root, "scr_dompet", "Tab 'Dompet' (Tarik Tunai)", 880, 3370)
    builder.add_connector(root, "e76", "dec_wallet_use", "scr_dompet", label="Tarik Tunai Rupiah", color="#0284c7")

    builder.add_process(root, "p_input_cashout", "Pilih E-Wallet & Nominal", "Pilih [GoPay] / [DANA], pilih nominal Rp 50.000, ketik nomor HP", 870, 3425, 220, 55)
    builder.add_connector(root, "e77", "scr_dompet", "p_input_cashout")

    builder.add_decision(root, "dec_cashout_min", "Nominal >= 10k &<br>No HP Valid?", 905, 3500, 150, 65)
    builder.add_connector(root, "e78", "p_input_cashout", "dec_cashout_min")

    builder.add_sad(root, "sad_cashout_invalid", "Format Salah / &lt; 10k", "Toast: 'Minimal penarikan Rp 10.000 & nomor HP minimal 10 digit!'", 1140, 3502, 220, 60)
    builder.add_connector(root, "e79", "dec_cashout_min", "sad_cashout_invalid", label="TIDAK VALID", color="#e11d48")

    builder.add_decision(root, "dec_cashout_balance", "Saldo Mengendap >=<br>Rp 50.000?", 905, 3585, 150, 65)
    builder.add_connector(root, "e80", "dec_cashout_min", "dec_cashout_balance", label="VALID", color="#16a34a")

    builder.add_sad(root, "sad_cashout_short", "Saldo Kurang", "Toast: 'Saldo mengendap Anda tidak mencukupi untuk penarikan ini!'", 1140, 3587, 220, 60)
    builder.add_connector(root, "e81", "dec_cashout_balance", "sad_cashout_short", label="KURANG", color="#e11d48")

    builder.add_process(root, "p_input_pin_cashout", "Input PIN Transaksi 6 Digit", "Verifikasi keamanan pencairan dana", 870, 3670, 220, 50)
    builder.add_connector(root, "e82", "dec_cashout_balance", "p_input_pin_cashout", label="CUKUP", color="#16a34a")

    builder.add_happy(root, "hp_cashout_success", "Uang Cair ke GoPay/DANA!", "Saldo dipotong -Rp 50.000 (0% biaya admin). Uang tunai langsung cair ke e-wallet warga!", 870, 3740, 220, 65)
    builder.add_connector(root, "e83", "p_input_pin_cashout", "hp_cashout_success", color="#16a34a")

    # =========================================================================
    # END STATE
    # =========================================================================
    builder.add_pill(root, "flow_end", "SELESAI: Nilai Ekonomi Nyata Tercipta!", 630, 3850, 240, 45, fill="#0f172a")
    builder.add_connector(root, "e84", "hp_store_success", "flow_end", color="#16a34a")
    builder.add_connector(root, "e85", "hp_cashout_success", "flow_end", color="#16a34a")

    builder.save()

if __name__ == "__main__":
    generate_long_flowchart("/home/jansky/pilahin-app/userflow_pilahin.drawio")
    generate_long_flowchart("/home/jansky/userflow_pilahin.drawio")
