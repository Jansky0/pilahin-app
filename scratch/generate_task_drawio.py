import os
import xml.etree.ElementTree as ET

def create_model():
    model = ET.Element("mxGraphModel", {
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
        "pageWidth": "1600",
        "pageHeight": "900",
        "math": "0",
        "shadow": "0"
    })
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    return model, root

def add_header(root, cell_id, title, subtitle):
    val = f"<b>{title}</b><br><span style='font-size:12px;font-weight:normal;color:#64748b;'>{subtitle}</span>"
    style = "text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=16;fontStyle=1;fontColor=#065f46;"
    cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
    ET.SubElement(cell, "mxGeometry", {"x": "400", "y": "20", "width": "600", "height": "45", "as": "geometry"})

def add_screen_box(root, cell_id, screen_name, x, y, width=220, height=50):
    val = f"<b>LAYAR:</b><br>{screen_name}"
    style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f1f5f9;strokeColor=#475569;strokeWidth=2;fontColor=#0f172a;fontSize=11;fontStyle=0;spacing=4;"
    cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
    ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

def add_action_box(root, cell_id, text, x, y, width=220, height=75, fill="#ffffff", stroke="#0284c7"):
    val = f"<b>AKSI PENGGUNA:</b><br>{text}"
    style = f"rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor={fill};strokeColor={stroke};strokeWidth=1.5;fontColor=#0f172a;fontSize=11;spacing=6;"
    cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
    ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

def add_decision(root, cell_id, text, x, y, width=150, height=70):
    style = "rhombus;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=1.5;fontColor=#92400e;fontSize=10;fontStyle=1;"
    cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": text, "style": style, "vertex": "1", "parent": "1"})
    ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

def add_happy_box(root, cell_id, title, desc, x, y, width=240, height=80):
    val = f"<b style='color:#14532d;'>✅ HAPPY PATH: {title}</b><br><span style='font-size:10px;color:#166534;'>{desc}</span>"
    style = "rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#dcfce7;strokeColor=#16a34a;strokeWidth=2;fontColor=#14532d;fontSize=11;spacing=6;"
    cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
    ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

def add_sad_box(root, cell_id, title, desc, x, y, width=240, height=75):
    val = f"<b style='color:#9f1239;'>❌ SAD PATH: {title}</b><br><span style='font-size:10px;color:#881337;'>{desc}</span>"
    style = "rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#ffe4e6;strokeColor=#e11d48;strokeWidth=2;fontColor=#9f1239;fontSize=11;spacing=6;"
    cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": val, "style": style, "vertex": "1", "parent": "1"})
    ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

def add_pill(root, cell_id, text, x, y, width=160, height=40, fill="#16a34a", stroke="#15803d", font="#ffffff"):
    style = f"rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=2;fontColor={font};fontSize=11;fontStyle=1;"
    cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": text, "style": style, "vertex": "1", "parent": "1"})
    ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"})

def add_connector(root, edge_id, src, tgt, label="", color="#059669", dashed=False, width=2):
    style = f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor={color};strokeWidth={width};fontSize=10;fontColor={color};fontStyle=1;endArrow=classic;endFill=1;"
    if dashed:
        style += "dashed=1;"
    cell = ET.SubElement(root, "mxCell", {"id": edge_id, "value": label, "style": style, "edge": "1", "source": src, "target": tgt, "parent": "1"})
    ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})

# Define the 9 Single Tasks
TASKS = [
    {
        "id": "t1_register",
        "name": "Tugas 1 - Register Warga",
        "title": "TUGAS 1: PENDAFTARAN AKUN WARGA BARU",
        "subtitle": "Tugasan Tunggal: Warga Baru Mendaftar Akun & Mengisi Alamat Penjemputan",
        "screen": "RegisterScreen.jsx (Layar Penuh)",
        "action": "1. Pilih Peran: [Warga Penyetor]<br>2. Ketik Nama Lengkap<br>3. Ketik No. WhatsApp Aktif<br>4. Ketik Kata Sandi<br>5. Ketik Alamat & Patokan Rumah<br>6. Klik 'Daftar Akun Pilah.in'",
        "decision": "Data Lengkap &<br>No WA >= 10 Digit<br>& Pass >= 6 Char?",
        "happy_title": "Registrasi Berhasil",
        "happy_desc": "Akun tersimpan, toast 'Pendaftaran berhasil!', dan langsung dialihkan masuk ke Dasbor Beranda Warga.",
        "sad_title": "Input Tidak Lengkap / Salah",
        "sad_desc": "Toast 'Lengkapi nama, WA, dan password!' / 'WA min 10 digit'. Form ditahan, user memperbaiki input.",
        "end_happy": "Dasbor Beranda Warga",
        "end_sad": "Perbaiki Input Form"
    },
    {
        "id": "t2_login",
        "name": "Tugas 2 - Login Pengguna",
        "title": "TUGAS 2: MASUK KE AKUN (LOGIN)",
        "subtitle": "Tugasan Tunggal: Pengguna Masuk Akun via Kredensial atau Demo 1-Klik",
        "screen": "LoginScreen.jsx (Layar Penuh)",
        "action": "Pilihan A: Ketik No WA / Email & Password ➔ Klik 'Masuk'<br>Pilihan B: Klik 1-Click Fast Demo [Warga Raka] / [Mitra Sri]",
        "decision": "Kredensial Cocok<br>atau Fast Demo?",
        "happy_title": "Login Berhasil",
        "happy_desc": "Sesi terautentikasi, toast 'Selamat datang kembali!', langsung diarahkan ke Dasbor sesuai peran.",
        "sad_title": "Kredensial Tidak Cocok",
        "sad_desc": "Toast 'Email/No WA atau password tidak cocok!'. Layar tetap di Login, user diminta cek ejaan sandi.",
        "end_happy": "Dasbor Sesuai Peran",
        "end_sad": "Ulangi Input Sandi"
    },
    {
        "id": "t3_setor_tossa",
        "name": "Tugas 3 - Setor Jemput Tossa",
        "title": "TUGAS 3: PENGAJUAN PENJEMPUTAN SAMPAH KE RUMAH",
        "subtitle": "Tugasan Tunggal: Warga Memilih Sampah, Atur Berat & Minta Jemput Motor Tossa",
        "screen": "Tab 'Setor' ➔ Opsi 'Jemput Mitra (Pickup)'",
        "action": "1. Centang kategori (Kardus / PET / Jelantah / Organik)<br>2. Atur berat stepper (cth: 11 kg)<br>3. Pilih Chip Alamat [Rumah] & Cek Patokan<br>4. Sistem potong ongkir 10%<br>5. Klik 'Ajukan Penjemputan & Buat Tiket'",
        "decision": "Minimal 1 Kategori<br>Terpilih & Alamat<br>Lengkap?",
        "happy_title": "Tiket Jemput Terbit",
        "happy_desc": "Tiket QR digital PLH-XXXXXX dibuat, notifikasi dikirim ke armada motor Tossa untuk meluncur ke alamat.",
        "sad_title": "Sampah Belum Dipilih",
        "sad_desc": "Toast 'Pilih minimal satu kategori sampah dan tentukan beratnya!'. Tombol tiket diblokir sampai memilih.",
        "end_happy": "Menunggu Motor Tossa",
        "end_sad": "Pilih Kategori Sampah"
    },
    {
        "id": "t4_ubah_alamat",
        "name": "Tugas 4 - Ubah Alamat Jemput",
        "title": "TUGAS 4: MENGUBAH / MENAMBAH ALAMAT PENJEMPUTAN",
        "subtitle": "Tugasan Tunggal: Menyesuaikan Detail Rumah, Nomor WhatsApp & Patokan Kurir Tossa",
        "screen": "Tab 'Setor' ➔ Form 'AddressSection.jsx'",
        "action": "1. Klik tombol 'Ubah Alamat' / '+ Tambah Baru'<br>2. Edit Nama Kontak & No. WhatsApp Kurir<br>3. Edit Alamat Lengkap & Nomor Rumah<br>4. Edit Patokan Rumah (Pagar, warna teras)<br>5. Klik 'Simpan Perubahan'",
        "decision": "Alamat Jalan &<br>No. WhatsApp Diisi?",
        "happy_title": "Alamat Disimpan",
        "happy_desc": "Data alamat aktif diperbarui seketika, chip alamat ter-update, dan rute kurir Tossa disesuaikan.",
        "sad_title": "Alamat Dikosongkan",
        "sad_desc": "Toast 'Alamat tidak boleh kosong!'. Perubahan dibatalkan dan mengembalikan data alamat sebelumnya.",
        "end_happy": "Alamat Aktif Terpasang",
        "end_sad": "Batal / Reset Alamat"
    },
    {
        "id": "t5_setor_dropoff",
        "name": "Tugas 5 - Setor Drop-off",
        "title": "TUGAS 5: MENYETOR MANDIRI KE BANK SAMPAH RW",
        "subtitle": "Tugasan Tunggal: Drop-off Mandiri untuk Menikmati 100% Saldo Utuh Tanpa Ongkir",
        "screen": "Tab 'Setor' ➔ Opsi 'Antar Sendiri (Drop-off)'",
        "action": "1. Pilih tab 'Antar Sendiri'<br>2. Centang kategori sampah & atur berat<br>3. Sistem tetapkan Ongkir = Rp 0 (100% utuh)<br>4. Pilih Pos RW 05 (Jarak 650m, 13.00-16.00 WIB)<br>5. Klik 'Buat Tiket Antar Mandiri'",
        "decision": "Kategori Terpilih &<br>Tiket Terbit?",
        "happy_title": "Tiket Mandiri Terbit",
        "happy_desc": "Tiket QR terbit dengan label 'Drop-off Mandiri'. Warga membawa sampah ke pos RW saat jam buka.",
        "sad_title": "Tiba Saat Pos Tutup",
        "sad_desc": "Warga tiba di luar jam operasional (pos tutup). Tiket tidak hangus, warga kembali esok hari jam buka.",
        "end_happy": "Timbang di Pos Bank Sampah",
        "end_sad": "Tunggu Jam Buka Besok"
    },
    {
        "id": "t6_belanja_toko",
        "name": "Tugas 6 - Belanja Toko Sirkular",
        "title": "TUGAS 6: MEMBELI PUPUK KOMPOS DI TOKO SIRKULAR",
        "subtitle": "Tugasan Tunggal: Menukarkan Saldo Daur Ulang Menjadi Produk Olahan Bank Sampah",
        "screen": "Tab 'Toko' (Toko Sirkular Mitra)",
        "action": "1. Pilih produk: 'Pupuk Kompos Super 5kg (Rp 18.000)'<br>2. Buka modal rincian produk<br>3. Klik tombol 'Beli dengan Saldo Mengendap'",
        "decision": "Saldo Mengendap >=<br>Harga Produk<br>(Rp 18.000)?",
        "happy_title": "Pembelian Berhasil",
        "happy_desc": "Saldo didebit Rp 18.000, pesanan masuk ke mitra RW, loop sirkular tercapai (sampah jadi pupuk).",
        "sad_title": "Saldo Tidak Cukup",
        "sad_desc": "Toast 'Saldo daur ulang tidak mencukupi untuk pembelian ini!'. Saldo tidak berkurang, transaksi batal.",
        "end_happy": "Pupuk Diterima Warga",
        "end_sad": "Setor Sampah Lagi"
    },
    {
        "id": "t7_tarik_tunai",
        "name": "Tugas 7 - Tarik Tunai E-Wallet",
        "title": "TUGAS 7: PENCAIRAN SALDO TUNAI KE E-WALLET",
        "subtitle": "Tugasan Tunggal: Warga Mencairkan Rupiah Likuid ke GoPay atau DANA (0% Admin)",
        "screen": "Tab 'Dompet' (Kelola Saldo Tunai)",
        "action": "1. Pilih e-wallet: [GoPay] atau [DANA]<br>2. Pilih preset nominal (cth: Rp 50.000)<br>3. Cek nomor HP e-wallet<br>4. Klik 'Tarik Tunai Saldo'",
        "decision": "Nominal >= 10k &<br>No HP Valid &<br>Saldo Mencukupi?",
        "happy_title": "Uang Tunai Cair",
        "happy_desc": "Saldo dipotong Rp 50.000 (0% biaya admin), dana tunai masuk ke akun GoPay/DANA warga detik itu juga.",
        "sad_title": "Di Bawah Min / Saldo Kurang",
        "sad_desc": "Toast 'Minimal penarikan Rp 10.000!' atau 'Saldo tidak mencukupi!'. Penarikan ditolak.",
        "end_happy": "Uang Masuk E-Wallet",
        "end_sad": "Perbaiki Nominal / Top Up"
    },
    {
        "id": "t8_snapsort_ai",
        "name": "Tugas 8 - Scan Sampah AI",
        "title": "TUGAS 8: PINDAI SAMPAH DENGAN KAMERA AI",
        "subtitle": "Tugasan Tunggal: Deteksi Material, Cek Harga/kg & Kelayakan Daur Ulang via Kamera",
        "screen": "Tab 'SnapSort' (AI Detector)",
        "action": "1. Arahkan kamera ponsel ke objek sampah (cth: Botol PET)<br>2. Klik tombol 'Pindai Sampah Sekarang'<br>3. AI menganalisis citra selama 1.2 detik",
        "decision": "Material Terdeteksi<br>& Bersih Layak?",
        "happy_title": "Deteksi AI Berhasil",
        "happy_desc": "AI kenali Plastik PET (96%), harga Rp 3.500/kg. Klik 'Langsung Setor' ➔ auto-redirect ke Setor.",
        "sad_title": "Objek Buram / Limbah B3",
        "sad_desc": "Pesan 'Objek tidak terdeteksi' atau peringatan 'Material tercemar B3/oli tidak dapat disetor'.",
        "end_happy": "Lanjut ke Tab Setor",
        "end_sad": "Foto Ulang / Buang B3"
    },
    {
        "id": "t9_verifikasi_mitra",
        "name": "Tugas 9 - Verifikasi Mitra",
        "title": "TUGAS 9: VERIFIKASI TIMBANGAN & TIKET OLEH MITRA",
        "subtitle": "Tugasan Tunggal: Pengurus Bank Sampah RW Memverifikasi Tiket & Input Bobot Timbangan Riil",
        "screen": "Portal Mitra Pengelola RW 05",
        "action": "1. Buka Portal Mitra RW 05<br>2. Ketik Kode Tiket Warga (PLH-386477)<br>3. Ketik Bobot Riil Timbangan Digital (11 kg)<br>4. Klik 'Verifikasi & Selesaikan Timbangan'",
        "decision": "Kode Tiket Valid &<br>Bobot Riil Terisi?",
        "happy_title": "Saldo Warga Terkredit",
        "happy_desc": "Saldo tunai masuk ke dompet warga seketika (+Rp 22.410), stok sampah RW bertambah, tiket selesai.",
        "sad_title": "Kode Tiket Tidak Ditemukan",
        "sad_desc": "Pesan 'Tiket tidak ditemukan / Kode tidak valid'. Mitra diminta memeriksa ejaan kode tiket warga.",
        "end_happy": "Penyetoran Tuntas 100%",
        "end_sad": "Koreksi Kode Tiket"
    }
]

def build_single_task_diagram(task, out_filepath):
    mxfile = ET.Element("mxfile", {
        "host": "app.diagrams.net",
        "modified": "2026-10-31T14:45:00.000Z",
        "agent": "Pilahin-Single-Task-Agent",
        "version": "21.6.8",
        "type": "device"
    })
    diagram = ET.SubElement(mxfile, "diagram", {"id": task["id"], "name": task["name"]})
    model, root = create_model()
    diagram.append(model)

    # 1. Title Header
    add_header(root, "hdr", task["title"], task["subtitle"])

    # 2. Start
    add_pill(root, "start", "MULAI TUGAS", 50, 180, 120, 40, fill="#0f172a", stroke="#334155", font="#ffffff")

    # 3. Screen Box
    add_screen_box(root, "scr", task["screen"], 210, 170, 200, 60)
    add_connector(root, "e1", "start", "scr")

    # 4. Action Box
    add_action_box(root, "act", task["action"], 450, 155, 260, 90)
    add_connector(root, "e2", "scr", "act")

    # 5. Decision Box
    add_decision(root, "dec", task["decision"], 750, 165, 170, 70)
    add_connector(root, "e3", "act", "dec")

    # 6. Happy Path Box (Horizontal Right)
    add_happy_box(root, "hp", task["happy_title"], task["happy_desc"], 970, 120, 260, 75)
    add_connector(root, "e_hp", "dec", "hp", label="YA / VALID", color="#16a34a", width=2.5)

    # 7. Happy End State
    add_pill(root, "end_hp", task["end_happy"], 1270, 137, 180, 40, fill="#16a34a", stroke="#15803d", font="#ffffff")
    add_connector(root, "e_hp_end", "hp", "end_hp", color="#16a34a", width=2)

    # 8. Sad Path Box (Below Decision)
    add_sad_box(root, "sp", task["sad_title"], task["sad_desc"], 705, 300, 260, 75)
    add_connector(root, "e_sp", "dec", "sp", label="TIDAK / GAGAL", color="#e11d48", width=2)

    # 9. Sad End / Loopback
    add_pill(root, "end_sp", task["end_sad"], 480, 317, 180, 40, fill="#ffe4e6", stroke="#e11d48", font="#9f1239")
    add_connector(root, "e_sp_end", "sp", "end_sp", color="#e11d48", width=1.5, dashed=True)
    add_connector(root, "e_sp_loop", "end_sp", "act", label="Perbaiki", color="#e11d48", width=1.5, dashed=True)

    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ")
    tree.write(out_filepath, encoding="utf-8", xml_declaration=True)

def build_master_multi_sheet(tasks, out_filepath):
    mxfile = ET.Element("mxfile", {
        "host": "app.diagrams.net",
        "modified": "2026-10-31T14:45:00.000Z",
        "agent": "Pilahin-Single-Task-Agent",
        "version": "21.6.8",
        "type": "device"
    })
    for task in tasks:
        diagram = ET.SubElement(mxfile, "diagram", {"id": task["id"], "name": task["name"]})
        model, root = create_model()
        diagram.append(model)

        add_header(root, f"{task['id']}_hdr", task["title"], task["subtitle"])
        add_pill(root, f"{task['id']}_start", "MULAI TUGAS", 50, 180, 120, 40, fill="#0f172a", stroke="#334155", font="#ffffff")
        add_screen_box(root, f"{task['id']}_scr", task["screen"], 210, 170, 200, 60)
        add_connector(root, f"{task['id']}_e1", f"{task['id']}_start", f"{task['id']}_scr")

        add_action_box(root, f"{task['id']}_act", task["action"], 450, 155, 260, 90)
        add_connector(root, f"{task['id']}_e2", f"{task['id']}_scr", f"{task['id']}_act")

        add_decision(root, f"{task['id']}_dec", task["decision"], 750, 165, 170, 70)
        add_connector(root, f"{task['id']}_e3", f"{task['id']}_act", f"{task['id']}_dec")

        add_happy_box(root, f"{task['id']}_hp", task["happy_title"], task["happy_desc"], 970, 120, 260, 75)
        add_connector(root, f"{task['id']}_e_hp", f"{task['id']}_dec", f"{task['id']}_hp", label="YA / VALID", color="#16a34a", width=2.5)

        add_pill(root, f"{task['id']}_end_hp", task["end_happy"], 1270, 137, 180, 40, fill="#16a34a", stroke="#15803d", font="#ffffff")
        add_connector(root, f"{task['id']}_e_hp_end", f"{task['id']}_hp", f"{task['id']}_end_hp", color="#16a34a", width=2)

        add_sad_box(root, f"{task['id']}_sp", task["sad_title"], task["sad_desc"], 705, 300, 260, 75)
        add_connector(root, f"{task['id']}_e_sp", f"{task['id']}_dec", f"{task['id']}_sp", label="TIDAK / GAGAL", color="#e11d48", width=2)

        add_pill(root, f"{task['id']}_end_sp", task["end_sad"], 480, 317, 180, 40, fill="#ffe4e6", stroke="#e11d48", font="#9f1239")
        add_connector(root, f"{task['id']}_e_sp_end", f"{task['id']}_sp", f"{task['id']}_end_sp", color="#e11d48", width=1.5, dashed=True)
        add_connector(root, f"{task['id']}_e_sp_loop", f"{task['id']}_end_sp", f"{task['id']}_act", label="Perbaiki Input", color="#e11d48", width=1.5, dashed=True)

    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ")
    tree.write(out_filepath, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    os.makedirs("/home/jansky/pilahin-app/drawio_tasks", exist_ok=True)
    
    # 1. Master Multi-sheet
    build_master_multi_sheet(TASKS, "/home/jansky/pilahin-app/userflow_pilahin.drawio")
    build_master_multi_sheet(TASKS, "/home/jansky/userflow_pilahin.drawio")
    print("Master multi-sheet userflow generated.")

    # 2. Individual Standalone Task Files
    for i, t in enumerate(TASKS, start=1):
        filename = f"/home/jansky/pilahin-app/drawio_tasks/tugas_{i}_{t['id']}.drawio"
        build_single_task_diagram(t, filename)
    print("Individual task Draw.io files generated in /home/jansky/pilahin-app/drawio_tasks/.")
