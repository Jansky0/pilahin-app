import xml.etree.ElementTree as ET

class DrawIOBuilder:
    def __init__(self, filename):
        self.filename = filename
        self.root = ET.Element("mxfile", {
            "host": "app.diagrams.net",
            "modified": "2026-10-31T14:40:00.000Z",
            "agent": "Pilahin-Architecture-Agent-v2",
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

    def add_node(self, parent, cell_id, value, x, y, width, height, shape_type="box", fill_color="#ffffff", stroke_color="#059669", font_color="#0f172a", font_size=11):
        if shape_type == "box":
            style = f"rounded=1;whiteSpace=wrap;html=1;arcSize=14;fillColor={fill_color};strokeColor={stroke_color};strokeWidth=1.5;fontColor={font_color};fontSize={font_size};fontStyle=0;spacing=6;shadow=0;"
        elif shape_type == "pill":
            style = f"rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor={fill_color};strokeColor={stroke_color};strokeWidth=2;fontColor={font_color};fontSize={font_size};fontStyle=1;spacing=4;"
        elif shape_type == "rhombus":
            style = f"rhombus;whiteSpace=wrap;html=1;fillColor={fill_color};strokeColor={stroke_color};strokeWidth=1.5;fontColor={font_color};fontSize={font_size};fontStyle=1;"
        elif shape_type == "screen_header":
            style = f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill_color};strokeColor={stroke_color};strokeWidth=2;fontColor={font_color};fontSize=12;fontStyle=1;spacing=4;"
        elif shape_type == "header":
            style = f"text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=16;fontStyle=1;fontColor={font_color};"
        elif shape_type == "note":
            style = f"shape=note;whiteSpace=wrap;html=1;size=14;verticalAlign=top;align=left;spacing=6;fillColor={fill_color};strokeColor={stroke_color};fontColor={font_color};fontSize=10;"
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

    def add_edge(self, parent, edge_id, source_id, target_id, label="", stroke_color="#059669", dashed=False, stroke_width=2):
        style = f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor={stroke_color};strokeWidth={stroke_width};fontSize=10;fontColor={stroke_color};fontStyle=1;endArrow=classic;endFill=1;"
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
        print(f"Generated Detailed Multi-Page Draw.io diagram at: {self.filename}")


def generate_all_flows(output_path):
    builder = DrawIOBuilder(output_path)

    # =========================================================================
    # PAGE 1: PROSES 1 - REGISTRASI AKUN PENGGUNA (WARGA / MITRA)
    # =========================================================================
    p1 = builder.add_page("P1. Registrasi Akun", "p1-register")
    builder.add_node(p1, "p1_title", "<b>PROSES 1: REGISTRASI AKUN PENGGUNA (WARGA / MITRA)</b><br><span style='font-size:11px;font-weight:normal;color:#64748b;'>Detail Layar: RegisterScreen.jsx | Happy Path vs Sad Paths</span>", 400, 20, 600, 45, "header", font_color="#065f46")

    # Legend
    builder.add_node(p1, "p1_leg", "<b>LEGENDA:</b><br><span style='color:#16a34a;'>━━━ Jalur Berhasil (Happy Path)</span><br><span style='color:#e11d48;'>━━━ Jalur Gagal / Validasi (Sad Path)</span>", 50, 20, 220, 50, "note", fill_color="#f8fafc", stroke_color="#cbd5e1", font_color="#334155")

    # Step 1: Open Screen
    builder.add_node(p1, "p1_scr", "<b>Layar Terbuka: RegisterScreen.jsx</b><br>(Halaman Penuh / Bukan Modal Pop-up)", 480, 80, 260, 45, "screen_header", fill_color="#ecfdf5", stroke_color="#059669", font_color="#065f46")

    # Step 2: User Inputs
    builder.add_node(p1, "p1_in", "<b>Pengguna Mengisi Formulir:</b><br>1. Pilih Peran: [Warga Penyetor] atau [Mitra RW]<br>2. Input Nama Lengkap (cth: 'Raka Pradipta')<br>3. Input Nomor WhatsApp Aktif (cth: '081234567890')<br>4. Input Kata Sandi & Email (Opsional)<br>5. Input Alamat Penjemputan Utama & Patokan", 460, 150, 300, 100, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p1, "p1_e1", "p1_scr", "p1_in")

    # User clicks Submit
    builder.add_node(p1, "p1_clk", "Klik Tombol:<br><b>'Daftar Akun Pilah.in'</b>", 520, 275, 180, 40, "pill", fill_color="#059669", stroke_color="#047857", font_color="#ffffff")
    builder.add_edge(p1, "p1_e2", "p1_in", "p1_clk")

    # Validation 1: Required Fields
    builder.add_node(p1, "p1_val1", "Apakah Nama, No WA,<br>& Password Terisi?", 530, 345, 160, 70, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p1, "p1_e3", "p1_clk", "p1_val1")

    # Sad Path 1.1: Missing fields
    builder.add_node(p1, "p1_sad1", "<b>SAD PATH 1.1: Field Kosong</b><br>• Muncul Toast Error:<br>  <i>'Mohon lengkapi nama, nomor WhatsApp, dan password!'</i><br>• Form tidak dikirim, tetap di halaman pendaftaran", 140, 350, 270, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p1, "p1_e4", "p1_val1", "p1_sad1", "TIDAK", stroke_color="#e11d48")

    # Validation 2: Phone Format
    builder.add_node(p1, "p1_val2", "No. WhatsApp Valid?<br>(10 - 13 digit angka)", 530, 455, 160, 70, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p1, "p1_e5", "p1_val1", "p1_val2", "YA", stroke_color="#16a34a")

    # Sad Path 1.2: Invalid Phone
    builder.add_node(p1, "p1_sad2", "<b>SAD PATH 1.2: Format HP Tidak Sesuai</b><br>• Validasi inline error:<br>  <i>'Nomor WhatsApp minimal 10 digit angka!'</i><br>• Field WhatsApp disorot merah", 140, 460, 270, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p1, "p1_e6", "p1_val2", "p1_sad2", "TIDAK", stroke_color="#e11d48")

    # Validation 3: Password Length
    builder.add_node(p1, "p1_val3", "Password Minimal<br>6 Karakter?", 530, 565, 160, 70, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p1, "p1_e7", "p1_val2", "p1_val3", "YA", stroke_color="#16a34a")

    # Sad Path 1.3: Short password
    builder.add_node(p1, "p1_sad3", "<b>SAD PATH 1.3: Password Terlalu Pendek</b><br>• Validasi inline error:<br>  <i>'Kata sandi minimal 6 karakter!'</i><br>• Field password diminta diulang", 140, 570, 270, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p1, "p1_e8", "p1_val3", "p1_sad3", "TIDAK", stroke_color="#e11d48")

    # Happy Path Outcome
    builder.add_node(p1, "p1_happy", "<b>HAPPY PATH: Registrasi Berhasil</b><br>1. Objek pengguna dibuat (Role, ID, Alamat & Patokan)<br>2. State currentUser & isAuthenticated = true<br>3. Toast: <i>'Pendaftaran berhasil! Selamat datang, {Nama}!'</i><br>4. Layar diarahkan otomatis ke Dasbor Aplikasi (currentScreen = 'app')", 460, 680, 300, 90, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p1, "p1_e9", "p1_val3", "p1_happy", "YA", stroke_color="#16a34a")

    # Sad Path 1.4: User Cancel / Return
    builder.add_node(p1, "p1_cancel", "<b>SAD PATH 1.4: Pembatalan Pendaftaran</b><br>Pengguna klik '← Kembali' atau 'Sudah memiliki akun? Masuk'<br>➔ Dibatalkan tanpa menyimpan data ➔ Pindah ke Login/Landing", 850, 270, 270, 60, "box", fill_color="#f1f5f9", stroke_color="#64748b", font_color="#334155")
    builder.add_edge(p1, "p1_e10", "p1_in", "p1_cancel", "Batal / Balik", stroke_color="#64748b", dashed=True)

    # End State
    builder.add_node(p1, "p1_end", "SELESAI: Masuk Dasbor Pengguna", 510, 805, 200, 40, "pill", fill_color="#16a34a", stroke_color="#15803d", font_color="#ffffff")
    builder.add_edge(p1, "p1_e11", "p1_happy", "p1_end", stroke_color="#16a34a")


    # =========================================================================
    # PAGE 2: PROSES 2 - LOGIN & AUTENTIKASI PENGGUNA
    # =========================================================================
    p2 = builder.add_page("P2. Login & Autentikasi", "p2-login")
    builder.add_node(p2, "p2_title", "<b>PROSES 2: LOGIN & AUTENTIKASI PENGGUNA</b><br><span style='font-size:11px;font-weight:normal;color:#64748b;'>Detail Layar: LoginScreen.jsx | Kredensial vs 1-Click Demo Access</span>", 400, 20, 600, 45, "header", font_color="#065f46")

    builder.add_node(p2, "p2_leg", "<b>LEGENDA:</b><br><span style='color:#16a34a;'>━━━ Jalur Berhasil (Happy Path)</span><br><span style='color:#e11d48;'>━━━ Jalur Gagal / Validasi (Sad Path)</span>", 50, 20, 220, 50, "note", fill_color="#f8fafc", stroke_color="#cbd5e1", font_color="#334155")

    builder.add_node(p2, "p2_scr", "<b>Layar Terbuka: LoginScreen.jsx</b><br>(Halaman Penuh / Bebas Pop-up)", 480, 80, 260, 45, "screen_header", fill_color="#eff6ff", stroke_color="#3b82f6", font_color="#1e3a8a")

    builder.add_node(p2, "p2_opt", "Pengguna Memilih Metode Masuk:", 510, 150, 200, 40, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p2, "p2_e1", "p2_scr", "p2_opt")

    # Branch A: 1-Click Fast Demo Login
    builder.add_node(p2, "p2_demo", "<b>HAPPY PATH A: Masuk Cepat Demo 1-Klik</b><br>• Klik [Warga Penyetor (Raka Pradipta)] ATAU<br>• Klik [Mitra Bank Sampah (Ibu Sri Mulyani RW 05)]<br>➔ Langsung terautentikasi otomatis tanpa input kata sandi", 150, 240, 280, 80, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p2, "p2_e2", "p2_opt", "p2_demo", "Pilih Fast Demo", stroke_color="#16a34a")

    # Branch B: Standard Credential Login
    builder.add_node(p2, "p2_cred", "<b>Metode Input Kredensial Manual:</b><br>1. Input Email atau No. WhatsApp<br>2. Input Kata Sandi<br>3. Klik 'Masuk ke Akun'", 500, 240, 220, 80, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p2, "p2_e3", "p2_opt", "p2_cred", "Input Manual")

    # Validation: Empty fields?
    builder.add_node(p2, "p2_val1", "Apakah Email/No WA<br>& Password Diisi?", 530, 360, 160, 70, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p2, "p2_e4", "p2_cred", "p2_val1")

    # Sad Path 2.1: Empty Inputs
    builder.add_node(p2, "p2_sad1", "<b>SAD PATH 2.1: Input Kosong</b><br>• Toast Error: <i>'Mohon masukkan email/no HP dan password!'</i><br>• Tetap di halaman login", 830, 365, 270, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p2, "p2_e5", "p2_val1", "p2_sad1", "KOSONG", stroke_color="#e11d48")

    # Validation: Credentials Match?
    builder.add_node(p2, "p2_val2", "Kredensial Sesuai<br>dengan Database?", 530, 470, 160, 70, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p2, "p2_e6", "p2_val1", "p2_val2", "LENGKAP", stroke_color="#16a34a")

    # Sad Path 2.2: Wrong Password / Not Found
    builder.add_node(p2, "p2_sad2", "<b>SAD PATH 2.2: Kredensial Salah</b><br>• Toast Error: <i>'Email/No WhatsApp atau kata sandi tidak cocok!'</i><br>• Pengguna diarahkan mencoba kembali atau reset", 830, 475, 270, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p2, "p2_e7", "p2_val2", "p2_sad2", "SALAH", stroke_color="#e11d48")

    # Happy Path B Outcome
    builder.add_node(p2, "p2_happy", "<b>HAPPY PATH B: Login Manual Sukses</b><br>1. Sesi diverifikasi ➔ currentUser diset<br>2. Toast: <i>'Selamat datang kembali, {Nama}!'</i><br>3. Pindah ke Layar Dasbor Utama (currentScreen = 'app')", 460, 580, 300, 80, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p2, "p2_e8", "p2_val2", "p2_happy", "COCOK", stroke_color="#16a34a")
    builder.add_edge(p2, "p2_e9", "p2_demo", "p2_happy", "Bypass", stroke_color="#16a34a")

    # Role Router
    builder.add_node(p2, "p2_route", "Router Peran Pengguna?", 530, 690, 160, 60, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p2, "p2_e10", "p2_happy", "p2_route")

    builder.add_node(p2, "p2_warga", "Masuk: <b>Dasbor Warga</b><br>(Saldo, Setor, Toko, Dompet)", 380, 780, 200, 50, "pill", fill_color="#10b981", stroke_color="#059669", font_color="#ffffff")
    builder.add_edge(p2, "p2_e11", "p2_route", "p2_warga", "Warga", stroke_color="#10b981")

    builder.add_node(p2, "p2_mitra", "Masuk: <b>Portal Mitra RW 05</b><br>(Timbangan Digital & Toko)", 640, 780, 200, 50, "pill", fill_color="#f59e0b", stroke_color="#d97706", font_color="#ffffff")
    builder.add_edge(p2, "p2_e12", "p2_route", "p2_mitra", "Mitra", stroke_color="#f59e0b")


    # =========================================================================
    # PAGE 3: PROSES 3 - PENGAJUAN SETOR SAMPAH (JEMPUT ARMADA TOSSA)
    # =========================================================================
    p3 = builder.add_page("P3. Setor Sampah (Jemput Tossa)", "p3-setor-tossa")
    builder.add_node(p3, "p3_title", "<b>PROSES 3: PENGAJUAN SETOR SAMPAH (JEMPUT ARMADA TOSSA)</b><br><span style='font-size:11px;font-weight:normal;color:#64748b;'>Detail Layar: Tab Setor (App.jsx) & AddressSection.jsx | Happy Path vs Sad Paths</span>", 400, 20, 650, 45, "header", font_color="#065f46")

    builder.add_node(p3, "p3_leg", "<b>LEGENDA:</b><br><span style='color:#16a34a;'>━━━ Jalur Berhasil (Happy Path)</span><br><span style='color:#e11d48;'>━━━ Jalur Gagal / Validasi (Sad Path)</span>", 50, 20, 220, 50, "note", fill_color="#f8fafc", stroke_color="#cbd5e1", font_color="#334155")

    # Step 1: Open Tab
    builder.add_node(p3, "p3_scr", "<b>Layar Aktif: Tab 'Setor'</b><br>Pengguna memilih tab: <b>[Jemput Mitra (Pickup)]</b>", 480, 80, 260, 45, "screen_header", fill_color="#ecfdf5", stroke_color="#059669", font_color="#065f46")

    # Step 2: Choose categories & weights
    builder.add_node(p3, "p3_cat", "<b>1. Memilih Kategori Sampah & Atur Bobot:</b><br>• Kardus Box (Rp 1.800/kg) [Stepper: 8 kg]<br>• Botol Plastik PET (Rp 3.500/kg) [Stepper: 3 kg]<br>• Minyak Jelantah / Organik Dapur", 460, 150, 300, 80, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p3, "p3_e1", "p3_scr", "p3_cat")

    # Validation: Any category selected?
    builder.add_node(p3, "p3_val1", "Apakah Minimal 1 Kategori<br>Terpilih dengan Bobot > 0?", 520, 255, 180, 70, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p3, "p3_e2", "p3_cat", "p3_val1")

    # Sad Path 3.1: No category
    builder.add_node(p3, "p3_sad1", "<b>SAD PATH 3.1: Belum Memilih Sampah</b><br>• Toast Error: <i>'Pilih minimal satu kategori sampah dan tentukan beratnya!'</i><br>• Pembuatan tiket diblokir", 140, 260, 270, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p3, "p3_e3", "p3_val1", "p3_sad1", "TIDAK", stroke_color="#e11d48")

    # Step 3: Address & Landmark
    builder.add_node(p3, "p3_addr", "<b>2. Memilih Alamat & Detail Patokan Rumah:</b><br>• Pilih Chip Alamat: [Rumah] / [Kantor] / [Kos]<br>• Atau klik '+ Tambah Baru' / 'Ubah Alamat'<br>• Pastikan Nomor WhatsApp aktif terisi<br>• Isi Patokan: 'Pagar hitam depan warung Bu Titin'", 460, 360, 300, 90, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p3, "p3_e4", "p3_val1", "p3_addr", "YA", stroke_color="#16a34a")

    # Validation: Address valid?
    builder.add_node(p3, "p3_val2", "Alamat & No. HP<br>Tersedia Lengkap?", 530, 480, 160, 65, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p3, "p3_e5", "p3_addr", "p3_val2")

    # Sad Path 3.2: Empty Address
    builder.add_node(p3, "p3_sad2", "<b>SAD PATH 3.2: Alamat Penjemputan Kosong</b><br>• Toast Error: <i>'Alamat penjemputan belum ditentukan!'</i><br>• Form meminta pengguna memilih atau menambah alamat", 140, 485, 270, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p3, "p3_e6", "p3_val2", "p3_sad2", "KOSONG", stroke_color="#e11d48")

    # Auto Calculation
    builder.add_node(p3, "p3_calc", "<b>Sistem Menghitung Kalkulasi Otomatis:</b><br>• Total Berat: 11 kg<br>• Nilai Kotor Sampah: Rp 24.900<br>• <i>Potongan Ongkir Armada Tossa 10%:</i> -Rp 2.490<br>• <b>Estimasi Saldo Mengendap Bersih: +Rp 22.410</b>", 460, 575, 300, 85, "box", fill_color="#f0fdf4", stroke_color="#10b981")
    builder.add_edge(p3, "p3_e7", "p3_val2", "p3_calc", "LENGKAP", stroke_color="#16a34a")

    # Click Create Ticket
    builder.add_node(p3, "p3_clk", "Klik Tombol:<br><b>'Ajukan Penjemputan & Buat Tiket'</b>", 510, 690, 200, 40, "pill", fill_color="#059669", stroke_color="#047857", font_color="#ffffff")
    builder.add_edge(p3, "p3_e8", "p3_calc", "p3_clk")

    # Happy Path Result
    builder.add_node(p3, "p3_happy", "<b>HAPPY PATH: Tiket Penjemputan Terbit</b><br>1. Tiket Digital dibuat (ID: PLH-386477) + QR Code<br>2. Status Tiket: <i>'Menunggu Penjemputan Armada'</i><br>3. Modal konfirmasi tiket & estimasi timbangan terbuka<br>4. Notifikasi penjemputan dikirim ke armada motor Tossa", 460, 760, 300, 90, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p3, "p3_e9", "p3_clk", "p3_happy", stroke_color="#16a34a")

    # Sad Path 3.3: Inaccessible alley
    builder.add_node(p3, "p3_sad3", "<b>SAD PATH 3.3: Akses Jalan Terlalu Sempit (&lt; 1.5m)</b><br>Catatan patokan mengindikasikan gang buntu sangat sempit<br>➔ Kurir mengabari warga via WA untuk taruh di ujung gang<br>➔ Atau warga mengubah opsi ke 'Antar Sendiri (Drop-off)'", 840, 485, 290, 75, "box", fill_color="#fffbeb", stroke_color="#f59e0b", font_color="#78350f")
    builder.add_edge(p3, "p3_e10", "p3_addr", "p3_sad3", "Gang Sempit", stroke_color="#f59e0b", dashed=True)


    # =========================================================================
    # PAGE 4: PROSES 4 - PENGAJUAN SETOR SAMPAH (ANTAR SENDIRI DROP-OFF)
    # =========================================================================
    p4 = builder.add_page("P4. Setor Antar Sendiri", "p4-setor-dropoff")
    builder.add_node(p4, "p4_title", "<b>PROSES 4: PENGAJUAN SETOR SAMPAH (ANTAR SENDIRI / DROP-OFF)</b><br><span style='font-size:11px;font-weight:normal;color:#64748b;'>Detail Layar: Tab Setor Mode Drop-Off | 100% Saldo Utuh Tanpa Potongan Ongkir</span>", 400, 20, 680, 45, "header", font_color="#065f46")

    builder.add_node(p4, "p4_leg", "<b>LEGENDA:</b><br><span style='color:#16a34a;'>━━━ Jalur Berhasil (Happy Path)</span><br><span style='color:#e11d48;'>━━━ Jalur Gagal / Validasi (Sad Path)</span>", 50, 20, 220, 50, "note", fill_color="#f8fafc", stroke_color="#cbd5e1", font_color="#334155")

    builder.add_node(p4, "p4_scr", "<b>Layar Aktif: Tab 'Setor'</b><br>Pengguna memilih tab: <b>[Antar Sendiri (Drop-off)]</b>", 480, 80, 260, 45, "screen_header", fill_color="#ecfdf5", stroke_color="#059669", font_color="#065f46")

    builder.add_node(p4, "p4_input", "<b>1. Pilih Kategori & Bobot Sampah:</b><br>• Kardus / Botol PET / Jelantah / Organik<br>• Sistem set Potongan Ongkir = Rp 0<br>• <b>Saldo Bersih = 100% Saldo Kotor Utuh</b>", 460, 150, 300, 75, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p4, "p4_e1", "p4_scr", "p4_input")

    builder.add_node(p4, "p4_pos", "<b>2. Memilih Pos Bank Sampah RW Tujuan:</b><br>• Default: 'Bank Sampah Berkah Lestari (RW 05)'<br>• Jam Operasional: 13.00 - 16.00 WIB (Jarak: 650 m)<br>• Atau klik 'Pilih Lokasi Lain'", 460, 255, 300, 75, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p4, "p4_e2", "p4_input", "p4_pos")

    builder.add_node(p4, "p4_clk", "Klik Tombol:<br><b>'Buat Tiket Antar Mandiri'</b>", 510, 360, 200, 40, "pill", fill_color="#059669", stroke_color="#047857", font_color="#ffffff")
    builder.add_edge(p4, "p4_e3", "p4_pos", "p4_clk")

    # Happy Path
    builder.add_node(p4, "p4_happy", "<b>HAPPY PATH: Tiket Drop-Off Terbit</b><br>1. Tiket Digital QR dibuat dengan label 'Drop-Off Mandiri'<br>2. Nilai saldo 100% utuh tanpa potongan bensin armada<br>3. Warga membawa sampah langsung ke Bank Sampah RW<br>4. Petugas menimbang di tempat & scan QR", 460, 435, 300, 85, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p4, "p4_e4", "p4_clk", "p4_happy", stroke_color="#16a34a")

    # Sad Path 4.1: Outside operating hours
    builder.add_node(p4, "p4_sad1", "<b>SAD PATH 4.1: Datang di Luar Jam Buka</b><br>Warga tiba di pos Bank Sampah pukul 18.00 (Pos tutup)<br>➔ Tiket tetap tersimpan aman di aplikasi (tidak hangus)<br>➔ Warga dapat kembali besok jam 13.00 - 16.00 WIB", 830, 435, 290, 75, "box", fill_color="#fffbeb", stroke_color="#f59e0b", font_color="#78350f")
    builder.add_edge(p4, "p4_e5", "p4_happy", "p4_sad1", "Pos Tutup", stroke_color="#f59e0b", dashed=True)


    # =========================================================================
    # PAGE 5: PROSES 5 - PENIMBANGAN LAPANGAN & VALIDASI PORTAL MITRA
    # =========================================================================
    p5 = builder.add_page("P5. Timbangan Lapangan & Mitra", "p5-weighing")
    builder.add_node(p5, "p5_title", "<b>PROSES 5: PENIMBANGAN LAPANGAN & VALIDASI PORTAL MITRA</b><br><span style='font-size:11px;font-weight:normal;color:#64748b;'>Armada Lapangan ➔ Penimbangan Gantung Digital ➔ Portal Mitra Pengelola RW 05</span>", 400, 20, 680, 45, "header", font_color="#065f46")

    builder.add_node(p5, "p5_leg", "<b>LEGENDA:</b><br><span style='color:#16a34a;'>━━━ Jalur Berhasil (Happy Path)</span><br><span style='color:#e11d48;'>━━━ Jalur Gagal / Validasi (Sad Path)</span>", 50, 20, 220, 50, "note", fill_color="#f8fafc", stroke_color="#cbd5e1", font_color="#334155")

    builder.add_node(p5, "p5_step1", "<b>Armada Tossa Tiba di Alamat Penjemputan</b><br>• Kurir mencocokkan patokan rumah di aplikasi<br>• Konfirmasi kehadiran via WhatsApp warga", 460, 80, 300, 55, "box", fill_color="#fffbeb", stroke_color="#f59e0b", font_color="#78350f")

    # Warga present?
    builder.add_node(p5, "p5_val1", "Warga Ada di Rumah<br>& Sampah Siap?", 530, 165, 160, 65, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p5, "p5_e1", "p5_step1", "p5_val1")

    # Sad Path 5.1: Not at home
    builder.add_node(p5, "p5_sad1", "<b>SAD PATH 5.1: Rumah Kosong / WA Tidak Aktif</b><br>• Kurir menunggu 10 menit, WA tidak terbalas<br>• Kurir menandai tiket: <i>'Jadwalkan Ulang Penjemputan'</i><br>• Tiket tidak hangus, dipindah ke slot penjemputan berikutnya", 140, 165, 290, 70, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p5, "p5_e2", "p5_val1", "p5_sad1", "TIDAK ADA", stroke_color="#e11d48")

    # Step 2: Digital Weighing
    builder.add_node(p5, "p5_weigh", "<b>Penimbangan Digital Transparan di Teras:</b><br>• Gantung karung sampah pada timbangan digital kurir<br>• Angka bobot disaksikan bersama antara warga & kurir<br>• Kurir mencatat bobot riil (misal: 11 kg)", 460, 260, 300, 75, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p5, "p5_e3", "p5_val1", "p5_weigh", "ADA & SIAP", stroke_color="#16a34a")

    # Quality check: contaminated?
    builder.add_node(p5, "p5_val2", "Sampah Kering Bersih?<br>(Tidak tercemar B3/Basah)", 530, 365, 160, 65, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p5, "p5_e4", "p5_weigh", "p5_val2")

    # Sad Path 5.2: Contaminated
    builder.add_node(p5, "p5_sad2", "<b>SAD PATH 5.2: Sampah Tercemar / Rusak</b><br>Kardus terendam air hujan atau botol berisi sisa oli mesin<br>➔ Kurir memisahkan bagian yang rusak & tidak dapat didaur ulang<br>➔ Bobot yang dihitung hanya sampah kering yang lolos sortir", 140, 365, 290, 75, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p5, "p5_e5", "p5_val2", "p5_sad2", "TERCEMAR", stroke_color="#e11d48")

    # Step 3: Partner Verification
    builder.add_node(p5, "p5_mitra", "<b>Buka Portal Mitra Pengelola RW 05:</b><br>1. Input Kode Tiket Digital (PLH-386477)<br>2. Input Bobot Riil Hasil Timbangan (11 kg)<br>3. Klik 'Verifikasi & Selesaikan Timbangan'", 460, 465, 300, 80, "box", fill_color="#eff6ff", stroke_color="#3b82f6", font_color="#1e3a8a")
    builder.add_edge(p5, "p5_e6", "p5_val2", "p5_mitra", "LOLOS SORTIR", stroke_color="#16a34a")

    # Happy Path Result
    builder.add_node(p5, "p5_happy", "<b>HAPPY PATH: Saldo Warga Dikreditkan Seketika!</b><br>• Saldo Tunai Warga bertambah +Rp 22.410 (Rupiah Likuid)<br>• Total Kg Terpilah bertambah +11 kg<br>• Riwayat transaksi tercatat otomatis di Dompet Warga<br>• Stok bahan baku terpilah di Bank Sampah RW bertambah", 460, 580, 300, 90, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p5, "p5_e7", "p5_mitra", "p5_happy", stroke_color="#16a34a")

    builder.add_node(p5, "p5_end", "SELESAI: Saldo Siap Dibelanjakan / Dicairkan", 490, 705, 240, 40, "pill", fill_color="#16a34a", stroke_color="#15803d", font_color="#ffffff")
    builder.add_edge(p5, "p5_e8", "p5_happy", "p5_end", stroke_color="#16a34a")


    # =========================================================================
    # PAGE 6: PROSES 6 - BELANJA PRODUK OLAHAN DI TOKO SIRKULAR MITRA
    # =========================================================================
    p6 = builder.add_page("P6. Belanja Toko Sirkular", "p6-store")
    builder.add_node(p6, "p6_title", "<b>PROSES 6: BELANJA PRODUK OLAHAN DI TOKO SIRKULAR MITRA</b><br><span style='font-size:11px;font-weight:normal;color:#64748b;'>Detail Layar: Tab Toko (activeTab === 'toko') | Pemotongan Saldo Mengendap</span>", 400, 20, 680, 45, "header", font_color="#065f46")

    builder.add_node(p6, "p6_leg", "<b>LEGENDA:</b><br><span style='color:#16a34a;'>━━━ Jalur Berhasil (Happy Path)</span><br><span style='color:#e11d48;'>━━━ Jalur Gagal / Validasi (Sad Path)</span>", 50, 20, 220, 50, "note", fill_color="#f8fafc", stroke_color="#cbd5e1", font_color="#334155")

    builder.add_node(p6, "p6_scr", "<b>Layar Aktif: Tab 'Toko' (Toko Sirkular Mitra)</b><br>Menampilkan katalog produk hasil daur ulang Bank Sampah RW", 460, 80, 300, 45, "screen_header", fill_color="#ecfdf5", stroke_color="#059669", font_color="#065f46")

    builder.add_node(p6, "p6_browse", "<b>Warga Memilih Produk:</b><br>• Contoh: Pupuk Kompos Organik Super (5kg) - Rp 18.000<br>• Klik kartu produk untuk membuka modal rincian", 460, 150, 300, 65, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p6, "p6_e1", "p6_scr", "p6_browse")

    builder.add_node(p6, "p6_clk", "Klik Tombol:<br><b>'Beli dengan Saldo Mengendap'</b>", 510, 245, 200, 40, "pill", fill_color="#059669", stroke_color="#047857", font_color="#ffffff")
    builder.add_edge(p6, "p6_e2", "p6_browse", "p6_clk")

    # Validation: Balance Check
    builder.add_node(p6, "p6_val", "Saldo Mengendap >=<br>Harga Produk (Rp 18.000)?", 520, 320, 180, 70, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p6, "p6_e3", "p6_clk", "p6_val")

    # Sad Path 6.1: Insufficient Balance
    builder.add_node(p6, "p6_sad1", "<b>SAD PATH 6.1: Saldo Mengendap Tidak Cukup</b><br>• Toast Error: <i>'Saldo daur ulang tidak mencukupi untuk pembelian ini!'</i><br>• Saldo warga tidak berkurang, transaksi dibatalkan<br>• Warga disarankan menyetor sampah lagi untuk menambah saldo", 140, 325, 300, 75, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p6, "p6_e4", "p6_val", "p6_sad1", "TIDAK CUKUP", stroke_color="#e11d48")

    # Sad Path 6.2: Out of Stock
    builder.add_node(p6, "p6_sad2", "<b>SAD PATH 6.2: Stok Produk Habis</b><br>Stok produk bernilai 0 di database mitra<br>➔ Tombol beli nonaktif (Disabled: 'Stok Habis')<br>➔ Warga dapat memilih produk daur ulang lainnya", 820, 325, 280, 65, "box", fill_color="#fffbeb", stroke_color="#f59e0b", font_color="#78350f")
    builder.add_edge(p6, "p6_e5", "p6_browse", "p6_sad2", "Stok 0", stroke_color="#f59e0b", dashed=True)

    # Happy Path
    builder.add_node(p6, "p6_happy", "<b>HAPPY PATH: Pembelian Berhasil!</b><br>1. Saldo Mengendap warga dipotong seketika (-Rp 18.000)<br>2. Transaksi debit tercatat di buku besar mutasi Dompet Warga<br>3. Pesanan masuk ke dasbor pengurus Bank Sampah RW<br>4. Toast: <i>'Berhasil membeli 1x Pupuk Kompos Super!'</i><br>5. <b>Loop Sirkular Tercapai:</b> Sampah warga kembali jadi pupuk tanaman", 460, 430, 300, 105, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p6, "p6_e6", "p6_val", "p6_happy", "CUKUP", stroke_color="#16a34a")

    builder.add_node(p6, "p6_end", "SELESAI: Barang Disiapkan Mitra RW", 490, 565, 240, 40, "pill", fill_color="#16a34a", stroke_color="#15803d", font_color="#ffffff")
    builder.add_edge(p6, "p6_e7", "p6_happy", "p6_end", stroke_color="#16a34a")


    # =========================================================================
    # PAGE 7: PROSES 7 - PENCAIRAN SALDO TUNAI KE E-WALLET (GOPAY / DANA)
    # =========================================================================
    p7 = builder.add_page("P7. Tarik Tunai E-Wallet", "p7-cashout")
    builder.add_node(p7, "p7_title", "<b>PROSES 7: PENCAIRAN SALDO TUNAI KE E-WALLET (GOPAY / DANA)</b><br><span style='font-size:11px;font-weight:normal;color:#64748b;'>Detail Layar: Tab Dompet (activeTab === 'dompet') | Pencairan Rupiah Likuid 0% Biaya Admin</span>", 400, 20, 680, 45, "header", font_color="#065f46")

    builder.add_node(p7, "p7_leg", "<b>LEGENDA:</b><br><span style='color:#16a34a;'>━━━ Jalur Berhasil (Happy Path)</span><br><span style='color:#e11d48;'>━━━ Jalur Gagal / Validasi (Sad Path)</span>", 50, 20, 220, 50, "note", fill_color="#f8fafc", stroke_color="#cbd5e1", font_color="#334155")

    builder.add_node(p7, "p7_scr", "<b>Layar Aktif: Tab 'Dompet'</b><br>Menampilkan Saldo Mengendap & Formulir Pencairan", 460, 80, 300, 45, "screen_header", fill_color="#eff6ff", stroke_color="#3b82f6", font_color="#1e3a8a")

    builder.add_node(p7, "p7_form", "<b>Warga Mengisi Formulir Penarikan:</b><br>1. Pilih E-Wallet: [GoPay] atau [DANA]<br>2. Pilih Preset: [Rp 25k] / [Rp 50k] / [Rp 100k] atau Kustom<br>3. Input Nomor WhatsApp / HP E-Wallet", 460, 150, 300, 75, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p7, "p7_e1", "p7_scr", "p7_form")

    builder.add_node(p7, "p7_clk", "Klik Tombol:<br><b>'Tarik Tunai Saldo'</b>", 510, 245, 200, 40, "pill", fill_color="#059669", stroke_color="#047857", font_color="#ffffff")
    builder.add_edge(p7, "p7_e2", "p7_form", "p7_clk")

    # Validation 1: Min Rp 10.000
    builder.add_node(p7, "p7_val1", "Nominal Penarikan<br>>= Rp 10.000?", 530, 315, 160, 65, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p7, "p7_e3", "p7_clk", "p7_val1")

    # Sad Path 7.1: Below min
    builder.add_node(p7, "p7_sad1", "<b>SAD PATH 7.1: Di Bawah Batas Minimum</b><br>• Toast Error: <i>'Minimal penarikan saldo adalah Rp 10.000!'</i><br>• Transaksi dibatalkan", 140, 320, 300, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p7, "p7_e4", "p7_val1", "p7_sad1", "TIDAK", stroke_color="#e11d48")

    # Validation 2: Phone Format
    builder.add_node(p7, "p7_val2", "Nomor HP E-Wallet<br>Valid (>= 10 digit)?", 530, 415, 160, 65, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p7, "p7_e5", "p7_val1", "p7_val2", "YA", stroke_color="#16a34a")

    # Sad Path 7.2: Invalid Phone
    builder.add_node(p7, "p7_sad2", "<b>SAD PATH 7.2: Format No. HP E-Wallet Salah</b><br>• Toast Error: <i>'Nomor HP e-wallet tidak valid!'</i><br>• Meminta koreksi nomor tujuan", 140, 420, 300, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p7, "p7_e6", "p7_val2", "p7_sad2", "TIDAK", stroke_color="#e11d48")

    # Validation 3: Balance Enough?
    builder.add_node(p7, "p7_val3", "Saldo Mengendap >=<br>Nominal Penarikan?", 530, 515, 160, 65, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p7, "p7_e7", "p7_val2", "p7_val3", "YA", stroke_color="#16a34a")

    # Sad Path 7.3: Balance not enough
    builder.add_node(p7, "p7_sad3", "<b>SAD PATH 7.3: Saldo Mengendap Kurang</b><br>• Toast Error: <i>'Saldo mengendap Anda tidak mencukupi!'</i><br>• Penarikan diblokir", 140, 520, 300, 60, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p7, "p7_e8", "p7_val3", "p7_sad3", "TIDAK", stroke_color="#e11d48")

    # Happy Path
    builder.add_node(p7, "p7_happy", "<b>HAPPY PATH: Pencairan Tunai Sukses!</b><br>1. Saldo Mengendap dipotong langsung (-Rp 50.000)<br>2. Biaya Admin = 0% (Rp 0)<br>3. Dana langsung cair ke akun GoPay/DANA warga<br>4. Toast: <i>'Pencairan Rp 50.000 ke GoPay berhasil diproses!'</i><br>5. Mutasi debit tercatat di riwayat Dompet", 460, 615, 300, 95, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p7, "p7_e9", "p7_val3", "p7_happy", "YA", stroke_color="#16a34a")

    builder.add_node(p7, "p7_end", "SELESAI: Uang Tunai Diterima Warga", 490, 740, 240, 40, "pill", fill_color="#16a34a", stroke_color="#15803d", font_color="#ffffff")
    builder.add_edge(p7, "p7_e10", "p7_happy", "p7_end", stroke_color="#16a34a")


    # =========================================================================
    # PAGE 8: PROSES 8 - PINDAI SAMPAH DENGAN SNAPSORT AI SCANNER
    # =========================================================================
    p8 = builder.add_page("P8. SnapSort AI Scanner", "p8-snapsort")
    builder.add_node(p8, "p8_title", "<b>PROSES 8: PINDAI SAMPAH DENGAN SNAPSORT AI SCANNER</b><br><span style='font-size:11px;font-weight:normal;color:#64748b;'>Detail Layar: Tab SnapSort (activeTab === 'snapsort') | Computer Vision Klasifikasi Sampah</span>", 400, 20, 680, 45, "header", font_color="#065f46")

    builder.add_node(p8, "p8_leg", "<b>LEGENDA:</b><br><span style='color:#16a34a;'>━━━ Jalur Berhasil (Happy Path)</span><br><span style='color:#e11d48;'>━━━ Jalur Gagal / Validasi (Sad Path)</span>", 50, 20, 220, 50, "note", fill_color="#f8fafc", stroke_color="#cbd5e1", font_color="#334155")

    builder.add_node(p8, "p8_scr", "<b>Layar Aktif: Tab 'SnapSort'</b><br>Viewfinder Kamera AI & Pilihan Sampel Sampah", 460, 80, 300, 45, "screen_header", fill_color="#e0f2fe", stroke_color="#0284c7", font_color="#0369a1")

    builder.add_node(p8, "p8_snap", "<b>Pengguna Mengarahkan Kamera / Pilih Objek:</b><br>• Contoh: Botol Plastik PET Bening<br>• Klik Tombol: 'Pindai Sampah Sekarang'", 460, 150, 300, 60, "box", fill_color="#ffffff", stroke_color="#3b82f6")
    builder.add_edge(p8, "p8_e1", "p8_scr", "p8_snap")

    builder.add_node(p8, "p8_proc", "<b>Proses Analisis Citra AI (1.2 detik):</b><br>• Klasifikasi material polimer & ketebalan<br>• Deteksi tingkat kotoran / residu cairan<br>• Kalkulasi tingkat keyakinan (Confidence Score)", 460, 235, 300, 75, "box", fill_color="#f8fafc", stroke_color="#64748b")
    builder.add_edge(p8, "p8_e2", "p8_snap", "p8_proc")

    # Validation: Recognition & Cleanliness
    builder.add_node(p8, "p8_val", "Material Dikenali &<br>Layak Daur Ulang?", 530, 340, 160, 65, "rhombus", fill_color="#fef3c7", stroke_color="#d97706")
    builder.add_edge(p8, "p8_e3", "p8_proc", "p8_val")

    # Sad Path 8.1: Unrecognized / Blur
    builder.add_node(p8, "p8_sad1", "<b>SAD PATH 8.1: Objek Buram / Tidak Dikenali</b><br>Kamera terlalu gelap atau objek tidak terdefinisi<br>➔ AI menampilkan pesan: <i>'Objek tidak terdeteksi. Harap pastikan pencahayaan cukup dan foto lebih dekat'</i>", 140, 340, 300, 70, "box", fill_color="#ffe4e6", stroke_color="#e11d48", font_color="#9f1239")
    builder.add_edge(p8, "p8_e4", "p8_val", "p8_sad1", "BURAM / GAGAL", stroke_color="#e11d48")

    # Sad Path 8.2: Severe Contamination
    builder.add_node(p8, "p8_sad2", "<b>SAD PATH 8.2: Sampah Terkontaminasi Berbahaya</b><br>AI mendeteksi botol oli bekas / limbah medis B3<br>➔ Peringatan merah: <i>'Material tercemar oli/B3 tidak dapat disetor ke Bank Sampah biasa'</i><br>➔ Diberikan panduan drop ke pos limbah B3 khusus", 820, 340, 300, 75, "box", fill_color="#fffbeb", stroke_color="#f59e0b", font_color="#78350f")
    builder.add_edge(p8, "p8_e5", "p8_val", "p8_sad2", "TERKONTAMINASI", stroke_color="#f59e0b", dashed=True)

    # Happy Path
    builder.add_node(p8, "p8_happy", "<b>HAPPY PATH: Deteksi Berhasil & Terverifikasi</b><br>1. Deteksi: Plastik PET Bening (Confidence 96%)<br>2. Harga beli resmi: Rp 3.500 / kg<br>3. Panduan aksi: Bilas sisa air & remas pipih<br>4. Tombol Shortcut: <b>'Langsung Setor Kategori Ini'</b><br>5. Otomatis redirect ke Tab Setor dengan PET tercentang", 460, 445, 300, 100, "box", fill_color="#dcfce7", stroke_color="#16a34a", font_color="#14532d")
    builder.add_edge(p8, "p8_e6", "p8_val", "p8_happy", "LAYAK & BERSIH", stroke_color="#16a34a")

    builder.add_node(p8, "p8_end", "SELESAI: Pindah ke Tab Setor (Auto-Prefilled)", 480, 580, 260, 40, "pill", fill_color="#16a34a", stroke_color="#15803d", font_color="#ffffff")
    builder.add_edge(p8, "p8_e7", "p8_happy", "p8_end", stroke_color="#16a34a")

    builder.save()

if __name__ == "__main__":
    generate_all_flows("/home/jansky/pilahin-app/userflow_pilahin.drawio")
    generate_all_flows("/home/jansky/userflow_pilahin.drawio")
