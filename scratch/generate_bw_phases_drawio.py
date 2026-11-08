import xml.etree.ElementTree as ET
import os
import shutil

class MonochromeDrawIOBuilder:
    def __init__(self, filename):
        self.filename = filename
        self.root = ET.Element("mxfile", {
            "host": "app.diagrams.net",
            "modified": "2026-11-08T14:00:00.000Z",
            "agent": "Pilahin-Monochrome-Agent",
            "version": "21.6.8",
            "type": "device"
        })

    def add_page(self, page_id, page_name, width=1200, height=900):
        diagram = ET.SubElement(self.root, "diagram", {"id": page_id, "name": page_name})
        model = ET.SubElement(diagram, "mxGraphModel", {
            "dx": "1400",
            "dy": "900",
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

    def add_header(self, root, cell_id, title, subtitle, x=50, y=20, width=800, height=45):
        val = f"<b style='font-size:15px;'>{title}</b><br><span style='font-size:11px;color:#333333;'>{subtitle}</span>"
        style = "text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];strokeColor=none;fillColor=none;fontColor=#000000;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_pill(self, root, cell_id, text, x, y, width=180, height=35):
        style = "rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11;fontStyle=1;align=center;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": text, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_process(self, root, cell_id, title, detail="", x=0, y=0, width=200, height=45, is_sad=False):
        if detail:
            val = f"<b>{title}</b><br><span style='font-size:10px;color:#333333;'>{detail}</span>"
        else:
            val = f"<b>{title}</b>"
        if is_sad:
            style = "rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=10;align=center;spacing=3;strokePattern=dashed;"
        else:
            style = "rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.2;fontColor=#000000;fontSize=11;align=center;spacing=4;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_decision(self, root, cell_id, question, x, y, width=140, height=55):
        style = "rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.2;fontColor=#000000;fontSize=10;fontStyle=1;align=center;"
        cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": question, "style": style, "vertex": "1", "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

    def add_connector(self, root, edge_id, src, tgt, label="", dashed=False):
        style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=1.2;fontSize=10;fontColor=#000000;endArrow=classic;endFill=1;"
        if dashed:
            style += "dashed=1;"
        cell = ET.SubElement(root, "mxCell", {"id": edge_id, "value": label, "style": style, "edge": "1", "source": src, "target": tgt, "parent": "1"})
        ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})

    def save(self):
        tree = ET.ElementTree(self.root)
        ET.indent(tree, space="  ")
        tree.write(self.filename, encoding="utf-8", xml_declaration=True)
        print(f"Saved: {self.filename}")


def build_phase_1(builder, root):
    """FASE 1: Registrasi, OTP & Login (Granular, Sad Paths & Happy Paths)"""
    builder.add_header(root, "p1_hdr", "FASE 1: REGISTRASI, VERIFIKASI OTP & LOGIN", "Alur Lengkap Pembuatan Akun, Verifikasi WhatsApp, PIN, dan Sad Path Sistem Menolak", 100, 15, 850)

    # Start & Landing
    builder.add_pill(root, "p1_start", "Mulai: Buka Pilah.in", 410, 75, 180, 35)
    builder.add_process(root, "p1_landing", "Buka Halaman Utama (Landing Page)", "Pelajari sistem ekonomi sirkular & harga beli sampah", 390, 130, 220, 42)
    builder.add_connector(root, "p1_e1", "p1_start", "p1_landing")

    builder.add_decision(root, "p1_dec_has_acc", "Sudah Punya<br>Akun Terdaftar?", 430, 195, 140, 55)
    builder.add_connector(root, "p1_e2", "p1_landing", "p1_dec_has_acc")

    # ----------------- REGISTRASI (BELUM PUNYA AKUN) -----------------
    builder.add_process(root, "p1_reg_role", "Pilih Peran Akun", "Klik Warga Penyetor atau Mitra Bank Sampah", 130, 280, 200, 42)
    builder.add_connector(root, "p1_e3", "p1_dec_has_acc", "p1_reg_role", label="Belum (Daftar)")

    builder.add_process(root, "p1_reg_data", "Input Data Diri & Akun", "Ketik Nama Lengkap, Nomor WhatsApp, Kata Sandi", 130, 345, 200, 42)
    builder.add_connector(root, "p1_e4", "p1_reg_role", "p1_reg_data")

    builder.add_decision(root, "p1_dec_data_valid", "Format Data<br>Valid?", 160, 410, 140, 50)
    builder.add_connector(root, "p1_e5", "p1_reg_data", "p1_dec_data_valid")

    # Sad Path 1: Format Eror
    builder.add_process(root, "p1_err_data", "SISTEM MENOLAK (SAD PATH)", "Format No WA / Sandi Salah. Wajib min 10 digit", 10, 415, 130, 42, is_sad=True)
    builder.add_connector(root, "p1_e6", "p1_dec_data_valid", "p1_err_data", label="Tidak")
    builder.add_connector(root, "p1_e6_loop", "p1_err_data", "p1_reg_data", label="Perbaiki", dashed=True)

    builder.add_process(root, "p1_send_otp", "Kirim Kode OTP ke WhatsApp", "Sistem mengirim 6 digit kode verifikasi resmi", 130, 485, 200, 42)
    builder.add_connector(root, "p1_e7", "p1_dec_data_valid", "p1_send_otp", label="Ya")

    builder.add_process(root, "p1_input_otp", "Input Kode OTP 6 Digit", "Pengguna mengetik kode verifikasi dari WhatsApp", 130, 545, 200, 42)
    builder.add_connector(root, "p1_e8", "p1_send_otp", "p1_input_otp")

    builder.add_decision(root, "p1_dec_otp_match", "Kode OTP<br>Cocok?", 160, 605, 140, 50)
    builder.add_connector(root, "p1_e9", "p1_input_otp", "p1_dec_otp_match")

    # Sad Path 2: OTP Salah
    builder.add_process(root, "p1_err_otp", "SISTEM MENOLAK (SAD PATH)", "Kode OTP Salah / Kedaluwarsa. Minta kirim baru", 10, 610, 130, 42, is_sad=True)
    builder.add_connector(root, "p1_e10", "p1_dec_otp_match", "p1_err_otp", label="Salah")
    builder.add_connector(root, "p1_e10_loop", "p1_err_otp", "p1_send_otp", label="Kirim Ulang", dashed=True)

    builder.add_process(root, "p1_reg_addr", "Input Alamat & Titik Jemput", "Isi nama jalan, RT/RW, dan patokan teras warga", 130, 680, 200, 42)
    builder.add_connector(root, "p1_e11", "p1_dec_otp_match", "p1_reg_addr", label="Cocok")

    builder.add_process(root, "p1_reg_pin", "Buat 6 Digit PIN Transaksi", "PIN keamanan belanja sirkular & pencairan dana", 130, 740, 200, 42)
    builder.add_connector(root, "p1_e12", "p1_reg_addr", "p1_reg_pin")

    builder.add_process(root, "p1_reg_done", "Registrasi Berhasil", "Akun terbit, alamat tersimpan, & PIN siap dipakai", 130, 800, 200, 42)
    builder.add_connector(root, "p1_e13", "p1_reg_pin", "p1_reg_done")

    # ----------------- LOGIN (SUDAH PUNYA AKUN) -----------------
    builder.add_process(root, "p1_login_id", "Input No. WhatsApp / Email", "Ketik nomor akun terdaftar di Pilah.in", 670, 280, 200, 42)
    builder.add_connector(root, "p1_e14", "p1_dec_has_acc", "p1_login_id", label="Sudah (Masuk)")

    builder.add_decision(root, "p1_dec_forgot", "Lupa Kata<br>Sandi?", 700, 345, 140, 55)
    builder.add_connector(root, "p1_e15", "p1_login_id", "p1_dec_forgot")

    # Sub-alur Lupa Password
    builder.add_process(root, "p1_forgot_btn", "Klik 'Lupa Password'", "Sistem kirim token pemulihan via WhatsApp", 850, 410, 140, 42)
    builder.add_connector(root, "p1_e16", "p1_dec_forgot", "p1_forgot_btn", label="Ya (Lupa)")

    builder.add_process(root, "p1_forgot_otp", "Input OTP Reset", "Verifikasi identitas nomor WhatsApp aktif", 850, 475, 140, 42)
    builder.add_connector(root, "p1_e17", "p1_forgot_btn", "p1_forgot_otp")

    builder.add_process(root, "p1_forgot_newpass", "Input Kata Sandi Baru", "Ketik & simpan kata sandi pengganti", 850, 540, 140, 42)
    builder.add_connector(root, "p1_e18", "p1_forgot_otp", "p1_forgot_newpass")
    builder.add_connector(root, "p1_e18_loop", "p1_forgot_newpass", "p1_login_id", label="Login Sandi Baru", dashed=True)

    # Sub-alur Login Normal
    builder.add_process(root, "p1_login_pass", "Input Kata Sandi Akun", "Ketik kata sandi akun terdaftar", 670, 425, 160, 42)
    builder.add_connector(root, "p1_e19", "p1_dec_forgot", "p1_login_pass", label="Ingat")

    builder.add_decision(root, "p1_dec_auth", "Kredensial<br>Cocok?", 680, 495, 140, 55)
    builder.add_connector(root, "p1_e20", "p1_login_pass", "p1_dec_auth")

    # Sad Path 3: Kredensial Salah
    builder.add_process(root, "p1_err_auth", "SISTEM MENOLAK (SAD PATH)", "Kredensial Salah. Cek nomor WA & kata sandi", 520, 502, 140, 42, is_sad=True)
    builder.add_connector(root, "p1_e21", "p1_dec_auth", "p1_err_auth", label="Salah")
    builder.add_connector(root, "p1_e21_loop", "p1_err_auth", "p1_login_pass", label="Ulangi", dashed=True)

    builder.add_process(root, "p1_login_done", "Login Berhasil", "Sesi masuk terbit & token autentikasi aktif", 660, 580, 180, 42)
    builder.add_connector(root, "p1_e22", "p1_dec_auth", "p1_login_done", label="Cocok")

    # Convergence End
    builder.add_pill(root, "p1_end", "Selesai: Masuk ke Beranda Warga", 400, 860, 200, 35)
    builder.add_connector(root, "p1_e23", "p1_reg_done", "p1_end")
    builder.add_connector(root, "p1_e24", "p1_login_done", "p1_end")


def build_phase_2(builder, root):
    """FASE 2: Beranda Warga & Deteksi Sampah SnapSort AI (Sad Path Limbah B3 & Buram)"""
    builder.add_header(root, "p2_hdr", "FASE 2: BERANDA WARGA & DETEKSI SAMPAH (SNAPSORT AI)", "Alur Pengecekan Saldo Mengendap, Deteksi Kamera AI, dan Penolakan Limbah B3", 100, 15, 800)

    builder.add_pill(root, "p2_start", "Mulai: Beranda Warga", 380, 75, 180, 35)
    builder.add_process(root, "p2_view_home", "Pantau Saldo Mengendap & Riwayat", "Cek rupiah nyata siap cair & tiket penjemputan", 360, 130, 220, 42)
    builder.add_connector(root, "p2_e1", "p2_start", "p2_view_home")

    builder.add_decision(root, "p2_dec_ai", "Gunakan SnapSort AI<br>untuk Pindai?", 395, 195, 150, 55)
    builder.add_connector(root, "p2_e2", "p2_view_home", "p2_dec_ai")

    # Manual branch
    builder.add_process(root, "p2_goto_manual", "Buka Tab 'Setor Sampah'", "Lanjut pemilihan jenis sampah manual", 150, 280, 200, 42)
    builder.add_connector(root, "p2_e3", "p2_dec_ai", "p2_goto_manual", label="Tidak (Manual)")

    # AI branch
    builder.add_process(root, "p2_open_ai", "Buka Tab 'SnapSort AI'", "Akses antarmuka kamera pengenal jenis sampah", 590, 280, 200, 42)
    builder.add_connector(root, "p2_e4", "p2_dec_ai", "p2_open_ai", label="Ya (Buka AI)")

    builder.add_process(root, "p2_snap_cam", "Arahkan Kamera & Ambil Foto", "Posisikan sampah di frame & tekan tombol pindai", 590, 345, 200, 42)
    builder.add_connector(root, "p2_e5", "p2_open_ai", "p2_snap_cam")

    builder.add_decision(root, "p2_dec_material", "Hasil Analisis<br>Material AI?", 615, 410, 150, 55)
    builder.add_connector(root, "p2_e6", "p2_snap_cam", "p2_dec_material")

    # Sad Path 1: Limbah B3 (SISTEM MENOLAK)
    builder.add_process(root, "p2_err_b3", "SISTEM MENOLAK (SAD PATH)", "Limbah B3 (Baterai/Medis). Dilarang masuk sirkular!", 780, 480, 160, 48, is_sad=True)
    builder.add_connector(root, "p2_e7", "p2_dec_material", "p2_err_b3", label="Tercemar / B3")

    # Sad Path 2: Blur (SISTEM MENOLAK)
    builder.add_process(root, "p2_err_blur", "SISTEM MENOLAK (SAD PATH)", "Objek Buram / Gelap. Sistem minta ambil ulang foto", 410, 480, 160, 48, is_sad=True)
    builder.add_connector(root, "p2_e8", "p2_dec_material", "p2_err_blur", label="Buram / Jauh")
    builder.add_connector(root, "p2_e8_loop", "p2_err_blur", "p2_snap_cam", label="Foto Ulang", dashed=True)

    # Happy Path: Valid
    builder.add_process(root, "p2_ai_valid", "Deteksi Material Valid", "Botol PET 96%, estimasi Rp 3.500/kg (Lolos Kurasi)", 600, 485, 180, 42)
    builder.add_connector(root, "p2_e9", "p2_dec_material", "p2_ai_valid", label="Bersih & Layak")

    builder.add_process(root, "p2_ai_prefill", "Klik 'Langsung Setor'", "Sistem otomatis memilih kategori di Tab Setor", 590, 555, 200, 42)
    builder.add_connector(root, "p2_e10", "p2_ai_valid", "p2_ai_prefill")

    # End
    builder.add_pill(root, "p2_end", "Selesai: Menuju Halaman Setor Sampah", 365, 635, 220, 35)
    builder.add_connector(root, "p2_e11", "p2_goto_manual", "p2_end")
    builder.add_connector(root, "p2_e12", "p2_ai_prefill", "p2_end")


def build_phase_3(builder, root):
    """FASE 3: Pengajuan Setor Sampah (Jemput vs Drop-off, Sad Path Di Luar Radius)"""
    builder.add_header(root, "p3_hdr", "FASE 3: PENGAJUAN PENYETORAN SAMPAH", "Pilihan Kategori, Kalkulasi Ongkir Jemput 10% vs Drop-off 0%, dan Sad Path Di Luar Radius", 100, 15, 850)

    builder.add_pill(root, "p3_start", "Mulai: Tab Setor Sampah", 420, 75, 180, 35)

    builder.add_process(root, "p3_select_waste", "Pilih Kategori & Atur Berat (kg)", "Centang sampah (Kardus/PET) & atur kg stepper", 400, 130, 220, 42)
    builder.add_connector(root, "p3_e1", "p3_start", "p3_select_waste")

    builder.add_decision(root, "p3_dec_valid", "Kategori Terpilih &<br>Bobot > 0 kg?", 435, 195, 150, 55)
    builder.add_connector(root, "p3_e2", "p3_select_waste", "p3_dec_valid")

    # Sad Path: No item
    builder.add_process(root, "p3_err_empty", "SISTEM MENOLAK (SAD PATH)", "Pilih minimal satu jenis sampah & isi berat > 0", 170, 202, 180, 42, is_sad=True)
    builder.add_connector(root, "p3_e3", "p3_dec_valid", "p3_err_empty", label="Tidak")
    builder.add_connector(root, "p3_e3_loop", "p3_err_empty", "p3_select_waste", label="Pilih Sampah", dashed=True)

    builder.add_decision(root, "p3_dec_method", "Pilih Metode<br>Penyetoran?", 435, 275, 150, 55)
    builder.add_connector(root, "p3_e4", "p3_dec_valid", "p3_dec_method", label="Ya")

    # ----------------- OPSI JEMPUT ARMADA TOSSA -----------------
    builder.add_process(root, "p3_calc_tossa", "Kalkulasi Ongkir Jemput 10%", "Gross Total dikurangi 10% operasional motor Tossa", 180, 355, 210, 42)
    builder.add_connector(root, "p3_e5", "p3_dec_method", "p3_calc_tossa", label="Jemput Tossa")

    builder.add_process(root, "p3_pick_addr", "Pilih Alamat Jemput & Patokan", "Pilih alamat tersimpan atau ketik titik jemput", 180, 420, 210, 42)
    builder.add_connector(root, "p3_e6", "p3_calc_tossa", "p3_pick_addr")

    # Decision: Radius Check (SAD PATH DI LUAR RADIUS)
    builder.add_decision(root, "p3_dec_radius", "Alamat Dalam<br>Radius <= 3 km?", 210, 485, 150, 50)
    builder.add_connector(root, "p3_e7_rad", "p3_pick_addr", "p3_dec_radius")

    # Sad Path: Di Luar Radius
    builder.add_process(root, "p3_err_radius", "SISTEM MENOLAK (SAD PATH)", "Di Luar Radius Layanan (>3 km). Jemputan diblokir", 10, 489, 160, 42, is_sad=True)
    builder.add_connector(root, "p3_e_rad_no", "p3_dec_radius", "p3_err_radius", label="> 3 km")

    builder.add_process(root, "p3_rec_dropoff", "Arahkan ke Drop-off Mandiri", "Sistem arahkan setor langsung ke Pos Mitra terdekat", 10, 555, 160, 42)
    builder.add_connector(root, "p3_e_rad_rec", "p3_err_radius", "p3_rec_dropoff")
    builder.add_connector(root, "p3_e_rad_switch", "p3_rec_dropoff", "p3_calc_dropoff", label="Beralih Drop-off", dashed=True)

    builder.add_decision(root, "p3_dec_addr_ok", "Patokan Teras<br>Rumah Jelas?", 210, 560, 150, 50)
    builder.add_connector(root, "p3_e7", "p3_dec_radius", "p3_dec_addr_ok", label="<= 3 km")

    builder.add_process(root, "p3_submit_tossa", "Klik 'Ajukan Penjemputan Tossa'", "Terbitkan tiket penjemputan armada roda 3 RW", 180, 635, 210, 42)
    builder.add_connector(root, "p3_e9", "p3_dec_addr_ok", "p3_submit_tossa", label="Jelas")

    # ----------------- OPSI DROP-OFF MANDIRI -----------------
    builder.add_process(root, "p3_calc_dropoff", "Kalkulasi Drop-off (0% Ongkir)", "Ongkos kirim Rp 0, 100% saldo utuh milik warga", 640, 355, 210, 42)
    builder.add_connector(root, "p3_e10", "p3_dec_method", "p3_calc_dropoff", label="Antar Sendiri")

    builder.add_process(root, "p3_pick_pos", "Pilih Drop Point / Pos Mitra", "Pilih TPS3R RW 05 / Bank Sampah & cek jam buka", 640, 425, 210, 42)
    builder.add_connector(root, "p3_e11", "p3_calc_dropoff", "p3_pick_pos")

    builder.add_process(root, "p3_submit_dropoff", "Klik 'Buat Tiket Mandiri'", "Terbitkan tiket penyetoran langsung ke pos mitra", 640, 495, 210, 42)
    builder.add_connector(root, "p3_e12", "p3_pick_pos", "p3_submit_dropoff")

    # Convergence
    builder.add_process(root, "p3_ticket_gen", "Tiket Digital QR Terbit", "ID Tiket: PLH-XXXXXX, QR Code siap ditimbang", 410, 715, 210, 42)
    builder.add_connector(root, "p3_e13", "p3_submit_tossa", "p3_ticket_gen")
    builder.add_connector(root, "p3_e14", "p3_submit_dropoff", "p3_ticket_gen")

    builder.add_pill(root, "p3_end", "Selesai: Menunggu Penimbangan Lapangan", 405, 785, 220, 35)
    builder.add_connector(root, "p3_e15", "p3_ticket_gen", "p3_end")


def build_phase_4(builder, root):
    """FASE 4: Operasional Timbang Lapangan & Sad Path Penolakan Kurasi Fisik"""
    builder.add_header(root, "p4_hdr", "FASE 4: OPERASIONAL TIMBANG LAPANGAN & VERIFIKASI MITRA", "Alur Timbang Digital, Validasi Tiket Mitra, dan Sad Path Sistem Menolak Kurasi Gagal", 100, 15, 850)

    builder.add_pill(root, "p4_start", "Mulai: Tiket Digital Aktif", 420, 75, 180, 35)

    builder.add_decision(root, "p4_dec_type", "Jenis Penyetoran<br>Lapangan?", 435, 135, 150, 55)
    builder.add_connector(root, "p4_e1", "p4_start", "p4_dec_type")

    # ----------------- JEMPUT TOSSA -----------------
    builder.add_process(root, "p4_tossa_arrive", "Armada Tossa Tiba di Alamat Warga", "Kurir cek patokan rumah & hubungi WhatsApp warga", 180, 215, 210, 42)
    builder.add_connector(root, "p4_e2", "p4_dec_type", "p4_tossa_arrive", label="Jemput Tossa")

    builder.add_decision(root, "p4_dec_citizen", "Warga Ada<br>di Rumah?", 210, 280, 150, 50)
    builder.add_connector(root, "p4_e3", "p4_tossa_arrive", "p4_dec_citizen")

    builder.add_process(root, "p4_sad_not_home", "Jadwalkan Ulang Jemputan", "Warga tidak ada di lokasi. Tiket tetap aktif", 20, 285, 150, 42, is_sad=True)
    builder.add_connector(root, "p4_e4", "p4_dec_citizen", "p4_sad_not_home", label="Tidak")

    builder.add_process(root, "p4_tossa_weigh", "Timbang Digital di Teras Rumah", "Karung digantung di timbangan kurir & disaksikan", 180, 355, 210, 42)
    builder.add_connector(root, "p4_e5", "p4_dec_citizen", "p4_tossa_weigh", label="Ada")

    # ----------------- DROP-OFF MANDIRI -----------------
    builder.add_process(root, "p4_dropoff_arrive", "Warga Bawa Sampah ke Pos Mitra", "Tiba di lokasi Bank Sampah / TPS3R RW 05", 640, 215, 210, 42)
    builder.add_connector(root, "p4_e6", "p4_dec_type", "p4_dropoff_arrive", label="Antar Sendiri")

    builder.add_decision(root, "p4_dec_pos_open", "Pos Sedang Buka?<br>(13.00 - 16.00 WIB)", 670, 280, 150, 50)
    builder.add_connector(root, "p4_e7", "p4_dropoff_arrive", "p4_dec_pos_open")

    builder.add_process(root, "p4_sad_closed", "Pos Tutup (Di Luar Jam Buka)", "Tiket aman tersimpan, warga datang kembali esok", 850, 285, 150, 42, is_sad=True)
    builder.add_connector(root, "p4_e8", "p4_dec_pos_open", "p4_sad_closed", label="Tutup")

    builder.add_process(root, "p4_pos_weigh", "Petugas Timbang di Pos Mitra", "Sampah ditimbang menggunakan timbangan pos", 640, 355, 210, 42)
    builder.add_connector(root, "p4_e9", "p4_dec_pos_open", "p4_pos_weigh", label="Buka")

    # ----------------- PORTAL MITRA & KURASI FISIK -----------------
    builder.add_process(root, "p4_open_mitra", "Buka Portal Mitra Pengelola", "Petugas masuk ke dasbor operasional timbangan", 405, 430, 210, 42)
    builder.add_connector(root, "p4_e10", "p4_tossa_weigh", "p4_open_mitra")
    builder.add_connector(root, "p4_e11", "p4_pos_weigh", "p4_open_mitra")

    builder.add_process(root, "p4_input_weight", "Input Nomor Tiket & Bobot Riil", "Ketik ID tiket PLH-XXXXXX & angka timbangan nyata", 405, 495, 210, 42)
    builder.add_connector(root, "p4_e12", "p4_open_mitra", "p4_input_weight")

    # DECISION: KURASI FISIK LOLOS STANDAR?
    builder.add_decision(root, "p4_dec_kurasi", "Kurasi Fisik Lolos<br>Standar Pilah?", 435, 560, 150, 55)
    builder.add_connector(root, "p4_e13_k", "p4_input_weight", "p4_dec_kurasi")

    # SAD PATH: KURASI FISIK GAGAL (SISTEM MENOLAK)
    builder.add_process(root, "p4_err_kurasi", "SISTEM MENOLAK (SAD PATH)", "Sampah Basah Kuyup / Tercemar Minyak / B3", 120, 565, 180, 45, is_sad=True)
    builder.add_connector(root, "p4_e_kurasi_no", "p4_dec_kurasi", "p4_err_kurasi", label="Tolak (Gagal)")

    builder.add_process(root, "p4_reject_action", "Tiket Ditolak & Saldo Rp 0", "Petugas klik 'Tolak Sampah', catatan audit tersimpan", 120, 635, 180, 42)
    builder.add_connector(root, "p4_e_rej_act", "p4_err_kurasi", "p4_reject_action")

    builder.add_process(root, "p4_warga_edu", "Kirim Tips Edukasi ke Warga", "Banner merah di aplikasi warga & opsi setor ulang", 120, 705, 180, 42)
    builder.add_connector(root, "p4_e_edu", "p4_reject_action", "p4_warga_edu")

    # HAPPY PATH: LOLOS KURASI
    builder.add_process(root, "p4_verify_ticket", "Verifikasi Data Penimbangan", "Sistem kalkulasi total rupiah bersih sesuai bobot", 560, 635, 210, 42)
    builder.add_connector(root, "p4_e13", "p4_dec_kurasi", "p4_verify_ticket", label="Lolos (Bersih)")

    builder.add_process(root, "p4_balance_credit", "Saldo Tunai Masuk ke Dompet Warga", "Kredit rupiah cair instan & status tiket selesai", 550, 705, 230, 45)
    builder.add_connector(root, "p4_e14", "p4_verify_ticket", "p4_balance_credit")

    builder.add_pill(root, "p4_end", "Selesai: Saldo Siap Dibelanjakan / Ditarik", 555, 780, 220, 35)
    builder.add_connector(root, "p4_e15", "p4_balance_credit", "p4_end")


def build_phase_5(builder, root):
    """FASE 5: Pemanfaatan Saldo (Belanja Produk Upcycle vs Tarik Tunai E-Wallet & Sad Paths)"""
    builder.add_header(root, "p5_hdr", "FASE 5: PEMANFAATAN SALDO LIKUID WARGA", "Belanja Upcycle Kompos atau Pencairan E-Wallet beserta Sad Path PIN & Saldo Kurang", 100, 15, 850)

    builder.add_pill(root, "p5_start", "Mulai: Saldo Mengendap di Dompet", 410, 75, 200, 35)

    builder.add_decision(root, "p5_dec_use", "Pilihan Pemanfaatan<br>Saldo Mengendap?", 435, 135, 150, 55)
    builder.add_connector(root, "p5_e1", "p5_start", "p5_dec_use")

    # ----------------- CABANG A: BELANJA TOKO SIRKULAR -----------------
    builder.add_process(root, "p5_open_store", "Buka Tab 'Toko Sirkular'", "Lihat katalog pupuk kompos & paving block daur ulang", 180, 215, 210, 42)
    builder.add_connector(root, "p5_e2", "p5_dec_use", "p5_open_store", label="Belanja Produk")

    builder.add_process(root, "p5_pick_item", "Pilih Pupuk Kompos (Rp 18.000)", "Pilih pupuk olahan organik warga & klik beli", 180, 280, 210, 42)
    builder.add_connector(root, "p5_e3", "p5_open_store", "p5_pick_item")

    builder.add_decision(root, "p5_dec_store_bal", "Saldo Mengendap<br>>= Rp 18.000?", 210, 345, 150, 50)
    builder.add_connector(root, "p5_e4", "p5_pick_item", "p5_dec_store_bal")

    # Sad Path Belanja: Saldo Kurang
    builder.add_process(root, "p5_err_store_bal", "SISTEM MENOLAK (SAD PATH)", "Saldo Tidak Cukup. Transaksi dibatalkan", 10, 349, 160, 42, is_sad=True)
    builder.add_connector(root, "p5_e5", "p5_dec_store_bal", "p5_err_store_bal", label="Tidak")

    builder.add_process(root, "p5_pin_store", "Input PIN Transaksi 6 Digit", "Verifikasi keamanan otorisasi pemotongan saldo", 180, 420, 210, 42)
    builder.add_connector(root, "p5_e6", "p5_dec_store_bal", "p5_pin_store", label="Cukup")

    # Decision PIN Belanja
    builder.add_decision(root, "p5_dec_pin_store", "PIN Transaksi<br>Valid?", 210, 485, 150, 50)
    builder.add_connector(root, "p5_e_pinstore", "p5_pin_store", "p5_dec_pin_store")

    # Sad Path PIN Salah
    builder.add_process(root, "p5_err_pin_store", "SISTEM MENOLAK (SAD PATH)", "PIN Salah >= 3x. Akun Dikunci Sementara 15 mnt", 10, 489, 160, 42, is_sad=True)
    builder.add_connector(root, "p5_e_pinstore_no", "p5_dec_pin_store", "p5_err_pin_store", label="Salah 3x")

    builder.add_process(root, "p5_store_success", "Pembelian Selesai (Sirkular)", "Saldo terpotong Rp 18.000 & produk kompos diterima", 180, 560, 210, 45)
    builder.add_connector(root, "p5_e7", "p5_dec_pin_store", "p5_store_success", label="Benar")

    # ----------------- CABANG B: TARIK TUNAI E-WALLET -----------------
    builder.add_process(root, "p5_open_wallet", "Buka Tab 'Dompet' (Tarik Tunai)", "Akses formulir pencairan dana ke e-wallet", 640, 215, 210, 42)
    builder.add_connector(root, "p5_e8", "p5_dec_use", "p5_open_wallet", label="Tarik Tunai")

    builder.add_process(root, "p5_input_cashout", "Pilih E-Wallet & Nominal", "Pilih GoPay/DANA, nominal Rp 50.000, & ketik nomor HP", 640, 280, 210, 42)
    builder.add_connector(root, "p5_e9", "p5_open_wallet", "p5_input_cashout")

    builder.add_decision(root, "p5_dec_min", "Nominal >= 10k &<br>No HP Valid?", 670, 345, 150, 50)
    builder.add_connector(root, "p5_e10", "p5_input_cashout", "p5_dec_min")

    builder.add_process(root, "p5_err_min", "SISTEM MENOLAK (SAD PATH)", "Minimal Penarikan Rp 10.000 / Format HP Salah", 860, 349, 160, 42, is_sad=True)
    builder.add_connector(root, "p5_e11", "p5_dec_min", "p5_err_min", label="Tidak")
    builder.add_connector(root, "p5_e11_loop", "p5_err_min", "p5_input_cashout", label="Perbaiki", dashed=True)

    builder.add_decision(root, "p5_dec_cash_bal", "Saldo Mengendap<br>>= Rp 50.000?", 670, 420, 150, 50)
    builder.add_connector(root, "p5_e12", "p5_dec_min", "p5_dec_cash_bal", label="Valid")

    builder.add_process(root, "p5_err_cash_bal", "SISTEM MENOLAK (SAD PATH)", "Saldo Tidak Cukup. Nominal tarik > saldo aktif", 860, 424, 160, 42, is_sad=True)
    builder.add_connector(root, "p5_e13", "p5_dec_cash_bal", "p5_err_cash_bal", label="Kurang")

    builder.add_process(root, "p5_pin_cash", "Input PIN Transaksi 6 Digit", "Verifikasi keamanan pencairan dana e-wallet", 640, 495, 210, 42)
    builder.add_connector(root, "p5_e14", "p5_dec_cash_bal", "p5_pin_cash", label="Cukup")

    builder.add_decision(root, "p5_dec_pin_cash", "PIN Transaksi<br>Valid?", 670, 560, 150, 50)
    builder.add_connector(root, "p5_e_pincash", "p5_pin_cash", "p5_dec_pin_cash")

    builder.add_process(root, "p5_err_pin_cash", "SISTEM MENOLAK (SAD PATH)", "PIN Salah >= 3x. Akun Dikunci Sementara 15 mnt", 860, 564, 160, 42, is_sad=True)
    builder.add_connector(root, "p5_e_pincash_no", "p5_dec_pin_cash", "p5_err_pin_cash", label="Salah 3x")

    builder.add_process(root, "p5_cash_success", "Uang Cair ke E-Wallet Warga", "Saldo terpotong Rp 50.000 (0% biaya admin/gratis)", 640, 635, 210, 45)
    builder.add_connector(root, "p5_e15", "p5_dec_pin_cash", "p5_cash_success", label="Benar")

    # Convergence
    builder.add_pill(root, "p5_end", "Selesai: Dampak Ekologi & Finansial Nyata", 410, 715, 230, 35)
    builder.add_connector(root, "p5_e16", "p5_store_success", "p5_end")
    builder.add_connector(root, "p5_e17", "p5_cash_success", "p5_end")


def generate_all():
    os.makedirs("/home/jansky/pilahin-app/drawio_phases", exist_ok=True)

    # 1. Multi-Sheet Master File
    master_path = "/home/jansky/pilahin-app/userflow_pilahin.drawio"
    master = MonochromeDrawIOBuilder(master_path)
    
    r1 = master.add_page("p1", "Fase 1: Registrasi, OTP & Login", 1050, 920)
    build_phase_1(master, r1)

    r2 = master.add_page("p2", "Fase 2: Beranda & SnapSort AI", 980, 720)
    build_phase_2(master, r2)

    r3 = master.add_page("p3", "Fase 3: Pengajuan Setor Sampah", 1050, 850)
    build_phase_3(master, r3)

    r4 = master.add_page("p4", "Fase 4: Operasional Timbang Lapangan", 1050, 850)
    build_phase_4(master, r4)

    r5 = master.add_page("p5", "Fase 5: Belanja Toko & Tarik Tunai", 1050, 780)
    build_phase_5(master, r5)

    master.save()

    # Also save to root
    shutil.copy(master_path, "/home/jansky/userflow_pilahin.drawio")

    # 2. Individual Files per Phase
    phases = [
        ("fase_1_registrasi_dan_login.drawio", "Fase 1: Registrasi, OTP & Login", build_phase_1, 1050, 920),
        ("fase_2_beranda_dan_snapsort_ai.drawio", "Fase 2: Beranda & SnapSort AI", build_phase_2, 980, 720),
        ("fase_3_pengajuan_setor_sampah.drawio", "Fase 3: Pengajuan Setor Sampah", build_phase_3, 1050, 850),
        ("fase_4_timbang_lapangan_dan_mitra.drawio", "Fase 4: Operasional Timbang Lapangan", build_phase_4, 1050, 850),
        ("fase_5_belanja_toko_dan_tarik_tunai.drawio", "Fase 5: Belanja Toko & Tarik Tunai", build_phase_5, 1050, 780),
    ]

    for fname, name, builder_func, w, h in phases:
        fpath = os.path.join("/home/jansky/pilahin-app/drawio_phases", fname)
        single = MonochromeDrawIOBuilder(fpath)
        r = single.add_page("p", name, w, h)
        builder_func(single, r)
        single.save()

    print("All Phase DrawIO diagrams regenerated successfully with full Sad Paths & Sistem Menolak!")

if __name__ == "__main__":
    generate_all()
