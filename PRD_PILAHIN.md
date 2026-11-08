# Product Requirement Document (PRD)
## Pilah.in — Sistem Ekonomi Sirkular Berbasis Sampah

> **Tipe Dokumen:** Functional & Feature Specification (Logic-First)  
> **Fokus Dokumen:** Logika Bisnis, Alur Fungsional, Algoritma, dan Integrasi Sistem (Tanpa Spesifikasi UI)  
> **Stakeholders:** Tim Pengembang (Backend & Frontend Logic), Pengelola Bank Sampah, dan Warga Penyetor  

---

## 1. Latar Belakang & Visi Produk

### 1.1 Problem Statement
1. **Rendahnya Partisipasi Pemilahan di Tingkat Rumah Tangga:**
   Warga enggan memilah sampah karena tidak ada insentif ekonomi langsung yang likuid, serta tidak adanya kepastian transparansi harga dan akses penyaluran.
2. **Hambatan Operasional & Pasar Pengelola Lokal (Bank Sampah & TPS3R):**
   * Pasokan bahan baku daur ulang sering kali tercampur residu kotor yang menurunkan nilai jual.
   * Produk hasil olahan daur ulang (pupuk kompos terfermentasi, paving block limbah, pot daur ulang) sulit dipasarkan secara lokal dan menumpuk di gudang balai warga.
   * Pencatatan timbangan manual rentan kesalahan hitung dan ketidakpercayaan warga.

### 1.2 Visi & Nilai Solusi
Pilah.in beroperasi sebagai **platform sirkular dua arah (*two-sided circular marketplace*)** yang mengintegrasikan rantai pasok sampah dari hulu ke hilir:
* Menghargai sampah terpilah warga secara langsung ke dalam **saldo uang mengendap (Rupiah)**.
* Menyediakan siklus tertutup di mana saldo tersebut dapat **ditarik ke e-wallet tunai** ATAU **dibelanjakan kembali untuk membeli produk olahan daur ulang** milik pengelola lokal.

---

## 2. Alur Sistem & Model Sirkular Tertutup (Closed-Loop Engine)

```
[Warga: Registrasi & Pengajuan Setor Sampah]
                      │
                      ▼
[Sistem: Estimasi Berat & Kalkulasi Nilai Komoditas]
                      │
                      ▼
[Mitra: Penimbangan & Verifikasi Kualitas Fisik di Lokasi]
                      │
                      ▼
[Sistem: Settlement Saldo Bersih Masuk ke Dompet Warga]
                      │
         ┌────────────┴───────────────────────────┐
         ▼                                        ▼
[Alur Penarikan Dana]                 [Alur Belanja Produk Olahan]
• Validasi rekening e-wallet          • Katalog produk mitra lokal
• Eksekusi API Payout                 • Direct debit saldo sampah
• Potong saldo mengendap              • Pembukuan omzet bagi mitra
```

---

## 3. Spesifikasi Fungsional Fitur (Core Feature Requirements)

### 3.1 Fitur 1: Valuasi & Penyetoran Sampah (Deposit & Valuation Engine)

* **Deskripsi:**
  Mesin transaksi penyetoran yang menangani kalkulasi nilai sampah, pemilihan metode penyaluran, dan siklus hidup tiket setor.
* **Kebutuhan Fungsional:**
  1. **Daftar Komoditas & Dynamic Price Index:**
     * Sistem memuat daftar komoditas sampah yang diterima: Kardus/Kertas, Plastik PET Bening, Logam/Aluminium, dan Minyak Jelantah.
     * Harga per satuan unit (kg atau liter) bersifat terpusat dan dapat diperbarui secara dinamis oleh sistem.
     * Sistem melacak indikator tren perubahan harga harian (misal: naik, turun, stabil).
  2. **Dual-Method Dispatch:**
     * **Metode Jemput Armada (Pickup):**
       * Syarat minimal akumulasi berat pengajuan: 5 kg.
       * Memungkinkan penentuan alamat penjemputan dan nomor kontak aktif.
       * Pemilihan slot jadwal kedatangan armada (Pagi: 08.00–12.00, Siang: 13.00–16.00).
       * **Logistics Fee Rule:** Dikenakan potongan biaya operasional logistik sebesar **10%** dari estimasi total nilai kotor.
     * **Metode Antar Mandiri (Drop-off):**
       * Menampilkan titik lokasi Bank Sampah / TPS3R mitra aktif beserta jam operasional dan kuota tampung harian.
       * Pemilihan jadwal estimasi kedatangan warga.
       * **Zero-Fee Rule:** Tidak ada potongan biaya logistik (**100% hasil timbangan masuk ke saldo pengguna**).
  3. **Kalkulator Estimasi Nilai Kotor & Bersih:**
     * Menghitung: `Estimasi Nilai = Σ (Estimasi Berat Kategori x Harga per Unit)`.
     * Menghitung nilai bersih berdasarkan metode yang dipilih (`Nilai Kotor - Biaya Logistik jika Jemput`).
  4. **Manajemen Tiket & Validasi Timbangan Fisik:**
     * Menerbitkan tiket digital unik berstatus `Pending`.
     * Tiket memuat kode referensi transaksi untuk dipindai/diinput oleh petugas saat penimbangan fisik.
     * **Verifikasi Timbangan:** Petugas menginput berat riil bersih (*actual net weight*) setelah memilah residu kotor. Sistem melakukan *settlement* berdasarkan berat riil yang divalidasi, bukan berat estimasi warga.
     * Lifecycle Status Tiket: `Draft` ➔ `Pending (Dijadwalkan)` ➔ `In-Transit / Menuju Lokasi` ➔ `Weighed (Ditimbang)` ➔ `Completed (Saldo Dikreditkan)` / `Cancelled`.

---

### 3.2 Fitur 2: Pasar Produk Sirkular (Circular Exchange Marketplace)

* **Deskripsi:**
  Etalase terdesentralisasi bagi kelompok pengelola sampah untuk menjual produk hasil olahan bahan daur ulang kembali ke masyarakat.
* **Kebutuhan Fungsional:**
  1. **Manajemen Katalog Produk Mitra:**
     * Kategori produk: Pupuk Kompos & Nutrisi Tanaman, Pot & Wadah Daur Ulang, Paving Block/Bahan Bangunan Limbah, dan Kerajinan Upcycle.
     * Metadata produk: Nama pengelola mitra binaan yang memproduksi, transparansi asal bahan baku (misal: *"Dibuat dari 24 botol plastik warga"*), harga nominal (Rupiah), dan kuantitas stok.
  2. **Mekanisme Pembayaran Dual-Mode:**
     * **Mode Tukar Saldo (Direct Debit):** Memotong saldo hasil setor sampah yang mengendap di dompet pengguna secara instan tanpa perlu transfer manual.
     * **Mode Split Payment / Top-Up:** Jika saldo tidak mencukupi harga produk, sistem mengizinkan pembayaran selisih kekurangan via gateway eksternal.
  3. **Fulfillment & Pengambilan Barang:**
     * Opsi ambil mandiri di balai Bank Sampah mitra pembuat.
     * Opsi kirim bersamaan dengan slot armada penjemputan sampah berikutnya.
  4. **Pencatatan Omzet Pengelola:**
     * Saldo transaksi pembelian otomatis dibukukan sebagai pemasukan pengelola mitra pembuat produk.

---

### 3.3 Fitur 3: Dompet Sirkular & Escrow (Ledger & Cashout System)

* **Deskripsi:**
  Sistem penampungan dana (*escrow ledger*) yang menjaga keamanan nilai rupiah milik warga serta memproses penarikan dana ke rekening atau dompet digital eksternal.
* **Kebutuhan Fungsional:**
  1. **Escrow Balance (Saldo Mengendap):**
     * Saldo otomatis bertambah (*kredit*) saat tiket setor sampah berstatus `Completed`.
     * Saldo berkurang (*debit*) saat terjadi transaksi pembelian di Pasar Sirkular atau pengajuan pencairan dana.
  2. **Sistem Pencairan Dana (Cashout Engine):**
     * Integrasi jalur pencairan:
       * E-Wallet: GoPay, DANA, OVO, ShopeePay.
       * Transfer Rekening Bank: BCA, Mandiri, BRI, BNI.
     * Validasi nomor akun / HP tujuan penarikan.
     * Batasan penarikan:
       * Minimum penarikan: Rp 10.000.
       * Maksimum penarikan: Sesuai saldo tersedia.
     * Dukungan preset nominal penarikan cepat (Rp 25.000, Rp 50.000, Rp 100.000, dan Tarik Semua Saldo).
  3. **Auto-Reversal & Fail-Safe Protection:**
     * Jika request pencairan ke API e-wallet gagal (nomor tidak valid, jaringan error), status transaksi ditandai `Failed` dan dana **wajib dikembalikan seketika (*auto-reversal*)** ke saldo pengguna tanpa hangus.
  4. **Buku Mutasi Transaksi (Immutable Ledger):**
     * Mencatat setiap pergerakan dana secara permanen: ID Transaksi, timestamp presisi, tipe (`Kredit Setor`, `Debit Belanja`, `Debit Penarikan`), nominal, deskripsi pihak lawan (mitra/channel), dan status.

---

### 3.4 Fitur 4: AI Classifier & Asisten Pemilahan (SnapSort Classification Engine)

* **Deskripsi:**
  Modul pengenalan citra untuk membantu warga mengidentifikasi kategori sampah, estimasi nilai ekonominya, dan mendeteksi residu sebelum diajukan setor.
* **Kebutuhan Fungsional:**
  1. **Klasifikasi Citra Sampah:**
     * Menerima input foto sampah.
     * Mengembalikan probabilitas klasifikasi jenis bahan: PET (Plastik Botol), HDPE (Plastik Keras), Kardus/Kertas, Logam/Aleng, Organik, atau Sampah Residu.
  2. **Valuasi Instan:**
     * Menautkan hasil klasifikasi dengan indeks harga komoditas terkini untuk menampilkan taksiran nilai pasar per kg dari sampah di foto tersebut.
  3. **Edukasi Syarat Kondisi Penyetoran:**
     * Menampilkan aturan kelayakan fisik barang:
       * Bersih dari sisa makanan/minyak.
       * Kering (tidak menampung genangan air).
       * Dalam keadaan dipipihkan/dilipat untuk efisiensi volume.

---

### 3.5 Fitur 5: Kalkulasi Dampak Lingkungan (Eco-Impact Metric Engine)

* **Deskripsi:**
  Algoritma perhitungan dampak ekologis riil dari akumulasi sampah yang berhasil dialihkan dari Tempat Pembuangan Akhir (TPA).
* **Kebutuhan Fungsional:**
  1. **Metrik Total Kilogram Teralihkan:**
     * Akumulasi berat seluruh transaksi berstatus `Completed`.
  2. **Formula Reduksi Jejak Karbon:**
     * Estimasi emisi CO2 yang dicegah: Menggunakan faktor emisi konversi standar per kategori sampah (misal: 1 kg plastik daur ulang ~ menghemat 1.5 kg CO2e; 1 kg kertas ~ 1.0 kg CO2e).
  3. **Formula Penyelamatan Sumber Daya:**
     * Ekuivalensi konservasi pohon dari penyetoran kardus/kertas.

---

## 4. Aturan Bisnis & Guardrails (Business Rules)

| ID Aturan | Skenario Kasus | Logika & Tindakan Sistem |
| :--- | :--- | :--- |
| **BR-01** | Sampah tercampur residu kotor/basah saat penimbangan | Petugas mitra berhak mengurangi berat kotor. Sistem mencatat `actualNetWeight` terverifikasi; nilai saldo yang dikreditkan hanya mengacu pada berat bersih. |
| **BR-02** | Pembatalan penjemputan oleh warga | Pengguna dapat membatalkan tiket jemput maksimal **2 jam** sebelum slot waktu kedatangan tanpa biaya penalti. |
| **BR-03** | Penarikan dana di bawah batas minimum | Sistem menolak pengajuan penarikan jika nominal < Rp 10.000 atau jika saldo mengendap lebih kecil dari nominal yang diajukan. |
| **BR-04** | Gangguan gateway pencairan e-wallet | Sistem menjalankan *rollback* transaksi (debit dibatalkan) dan memulihkan saldo mengendap dalam waktu < 5 detik dengan notifikasi status transaksi gagal. |
| **BR-05** | Stok produk daur ulang habis di Pasar Sirkular | Sistem menolak transaksi *Tukar Saldo* untuk SKU tersebut dan menandai ketersediaan sebagai *Sedang Dalam Siklus Produksi*. |
| **BR-06** | Penyetoran metode Antar Mandiri | Potongan biaya logistik diset tepat `0%`. Seluruh nominal hasil timbangan dikreditkan 100% ke akun pengguna. |

---

## 5. Spesifikasi Entitas Data (Data Contracts & State)

### 5.1 User Account State
```typescript
interface UserProfile {
  id: string;
  fullName: string;
  phoneNumber: string;
  savedAddress: {
    label: string; // misal: "Rumah", "Kantor"
    street: string;
    subDistrict: string;
    city: string;
    latitude?: number;
    longitude?: number;
  };
  escrowBalance: number; // Saldo mengendap dalam IDR
  totalRecycledKg: number;
  carbonOffsetKg: number;
}
```

### 5.2 Waste Deposit Ticket State
```typescript
interface DepositTicket {
  ticketId: string;
  userId: string;
  partnerId: string;
  partnerName: string;
  dispatchMethod: 'PICKUP' | 'DROPOFF';
  logisticsFeePercentage: number; // 10 untuk PICKUP, 0 untuk DROPOFF
  scheduledDate: string;
  timeSlot: string;
  status: 'DRAFT' | 'PENDING' | 'IN_TRANSIT' | 'WEIGHED' | 'COMPLETED' | 'CANCELLED';
  items: Array<{
    categoryId: string;
    categoryName: string;
    pricePerUnit: number;
    estimatedQuantity: number;
    verifiedQuantity?: number;
    subtotal: number;
  }>;
  grossAmount: number;
  logisticsDeduction: number;
  finalSettlementAmount: number;
}
```

### 5.3 Circular Product State
```typescript
interface CircularProduct {
  productId: string;
  partnerId: string;
  partnerName: string;
  productName: string;
  category: 'KOMPOS' | 'POT' | 'PAVING' | 'KERAJINAN';
  rawMaterialSource: string; // Asal bahan baku daur ulang
  priceIDR: number;          // Nilai tukar dalam Rupiah (dapat dipotong dari saldo)
  stockQuantity: number;
  isAvailable: boolean;
}
```

### 5.4 Wallet Ledger Transaction State
```typescript
interface LedgerTransaction {
  transactionId: string;
  userId: string;
  type: 'CREDIT_DEPOSIT' | 'DEBIT_PURCHASE' | 'DEBIT_CASHOUT';
  amount: number;
  channelOrPartner: string; // 'Bank Sampah Berkah Lestari' | 'GoPay' | 'DANA'
  referenceId: string;      // ticketId atau orderId
  timestamp: string;
  status: 'PENDING' | 'SUCCESS' | 'FAILED';
  reversalReason?: string;
}
```

---

## 6. Kriteria Penerimaan & Verifikasi Sistem (Definition of Done)

Sistem dan implementasi fitur dinyatakan tuntas apabila memenuhi kriteria fungsional berikut:
1. **Kalkulasi & Valuasi:**
   * Sistem mampu mengkalkulasi estimasi nilai setor dari kuantitas per kategori secara akurat sesuai indeks harga komoditas aktif.
   * Potongan logistik 10% terhitung presisi saat mode *Jemput Armada* dipilih, dan 0% saat mode *Antar Mandiri*.
2. **Lifecycle Tiket Penyetoran:**
   * Tiket setor berhasil dibuat dengan status awal yang sesuai.
   * Sistem dapat memproses input berat fisik riil dari mitra dan memperbarui nilai kredit akhir secara deterministik.
3. **Integritas Saldo & Mutasi:**
   * Saldo mengendap bertambah tepat sebesar nilai bersih tiket yang diselesaikan.
   * Saldo mengendap berkurang tepat saat transaksi pembelian produk Pasar Sirkular atau penarikan tunai dieksekusi.
   * Setiap peristiwa kredit dan debit terdata lengkap di buku besar transaksi (*ledger*).
4. **Resiliensi Penarikan Dana:**
   * Validasi penarikan dana menolak nilai di bawah Rp 10.000 atau di atas saldo tersedia.
   * Kegagalan penarikan dana memicu pengembalian dana (*auto-reversal*) ke saldo mengendap tanpa ada dana yang hilang.
5. **Katalog Produk & Pembayaran Mandiri:**
   * Transaksi pembelian produk hanya dapat diselesaikan jika saldo pengguna mencukupi atau jika opsi pembayaran selisih didukung.
   * Stok produk otomatis berkurang setelah pesanan berhasil diproses.
