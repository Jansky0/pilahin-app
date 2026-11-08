import React from 'react';
import {
  Recycle,
  Sparkles,
  Truck,
  Wallet,
  ShoppingBag,
  CheckCircle2,
  ArrowRight,
  ShieldCheck,
  Building2,
  Package,
  Layers,
  ChevronRight,
  MapPin,
  LogIn,
  UserPlus,
  ArrowLeft
} from 'lucide-react';

export default function LandingScreen({
  onNavigateLogin,
  onNavigateRegister,
  onEnterApp,
  wastePrices,
  formatRupiah
}) {
  return (
    <div className="flex-1 overflow-y-auto px-4 py-5 space-y-6">
      {/* Top Brand Header */}
      <div className="flex items-center justify-between pb-1 border-b border-slate-200/80">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 text-white flex items-center justify-center shadow-xs shadow-emerald-500/20">
            <Recycle className="w-5 h-5" />
          </div>
          <div>
            <span className="font-extrabold text-base tracking-tight text-slate-900">
              Pilah<span className="text-emerald-600">.in</span>
            </span>
            <span className="text-[10px] text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full font-bold ml-1.5">
              Ekonomi Sirkular
            </span>
          </div>
        </div>

        <button
          type="button"
          onClick={onEnterApp}
          className="text-xs font-bold text-emerald-700 hover:text-emerald-800 bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 px-3 py-1.5 rounded-xl transition cursor-pointer flex items-center gap-1 active:scale-95"
        >
          <span>Masuk ke Dasbor</span>
          <ChevronRight className="w-3.5 h-3.5" />
        </button>
      </div>

      {/* Hero Welcome Banner */}
      <div className="bg-gradient-to-br from-emerald-900 via-teal-900 to-slate-950 text-white rounded-3xl p-6 space-y-4 shadow-xl relative overflow-hidden">
        {/* Glow Effects */}
        <div className="absolute -top-10 -right-10 w-40 h-40 rounded-full bg-emerald-500/15 blur-2xl pointer-events-none" />
        <div className="absolute -bottom-10 -left-10 w-32 h-32 rounded-full bg-teal-500/10 blur-xl pointer-events-none" />

        <div className="inline-flex items-center gap-1.5 bg-emerald-800/80 text-emerald-200 border border-emerald-600/50 px-3 py-1 rounded-full text-xs font-bold">
          <Sparkles className="w-3.5 h-3.5 text-amber-300" />
          <span>Platform Sirkular Sampah Indonesia</span>
        </div>

        <div className="space-y-2">
          <h1 className="text-2xl font-black tracking-tight leading-tight">
            Sampah Jadi Lebih Bernilai
          </h1>
          <p className="text-xs text-emerald-100/90 leading-relaxed">
            Ubah sampah kering terpilah di rumahmu menjadi <strong>saldo uang tunai (Rupiah asli)</strong> dan produk olahan daur ulang berkualitas tinggi, sekaligus memberdayakan Bank Sampah RW &amp; TPS3R lokal.
          </p>
        </div>

        {/* Action Buttons */}
        <div className="pt-2 flex flex-col sm:flex-row gap-2.5">
          <button
            type="button"
            onClick={onNavigateLogin}
            className="flex-1 bg-emerald-400 hover:bg-emerald-500 active:scale-95 text-slate-950 font-extrabold text-xs py-3.5 px-4 rounded-2xl transition shadow-lg shadow-emerald-400/20 cursor-pointer flex items-center justify-center gap-2"
          >
            <LogIn className="w-4 h-4" />
            <span>Masuk ke Akun</span>
          </button>
          <button
            type="button"
            onClick={onNavigateRegister}
            className="flex-1 bg-white/10 hover:bg-white/20 active:scale-95 text-white border border-white/25 font-bold text-xs py-3.5 px-4 rounded-2xl transition cursor-pointer flex items-center justify-center gap-2"
          >
            <UserPlus className="w-4 h-4" />
            <span>Daftar Akun Baru</span>
          </button>
        </div>
      </div>

      {/* SEKSI DESKRIPSI LENGKAP & VISI SIRKULAR */}
      <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-4">
        <div className="flex items-center gap-2 text-slate-900 border-b border-slate-100 pb-3">
          <div className="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold">
            <Recycle className="w-4 h-4" />
          </div>
          <div>
            <h2 className="text-sm font-extrabold text-slate-900">
              Apa Itu Pilah.in?
            </h2>
            <p className="text-[11px] text-slate-500">Mengenal platform ekonomi sirkular tertutup</p>
          </div>
        </div>

        <div className="space-y-3 text-xs text-slate-700 leading-relaxed">
          <p>
            <strong>Pilah.in</strong> adalah platform ekonomi sirkular dua arah (*two-sided circular marketplace*) yang menghubungkan masyarakat (penyetor sampah terpilah) langsung dengan Bank Sampah RW dan TPS3R lokal.
          </p>

          {/* Problem & Solution Comparison */}
          <div className="grid grid-cols-1 gap-2.5 pt-1">
            <div className="bg-rose-50 border border-rose-200/80 rounded-2xl p-3 text-rose-950 space-y-1">
              <span className="font-bold text-[11px] text-rose-800 flex items-center gap-1.5">
                <span>❌ Masalah yang Dipecahkan:</span>
              </span>
              <p className="text-[11px] text-rose-900/90 leading-relaxed">
                Warga enggan memilah sampah karena dianggap merepotkan dan tidak memiliki nilai ekonomi, sementara di sisi lain pengurus Bank Sampah RW kesulitan mendapatkan bahan baku terpilah yang bersih dan kesulitan memasarkan produk pupuk kompos olahannya.
              </p>
            </div>

            <div className="bg-emerald-50 border border-emerald-200/80 rounded-2xl p-3 text-emerald-950 space-y-1">
              <span className="font-bold text-[11px] text-emerald-800 flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                <span>✅ Solusi Sirkular Pilah.in:</span>
              </span>
              <p className="text-[11px] text-emerald-900/90 leading-relaxed">
                Sampah kering terpilah ditimbang digital secara transparan di tempat. Nilai rupiah langsung masuk ke <strong>dompet digital warga dalam bentuk uang asli (bukan sistem poin fiktif)</strong>. Saldo bisa ditarik tunai ke GoPay/DANA atau dibelanjakan produk pupuk kompos &amp; pot daur ulang hasil binaan Bank Sampah.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* 4 LANGKAH CARA KERJA SISTEM */}
      <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3.5">
        <div>
          <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-700 block">
            Alur Terintegrasi
          </span>
          <h3 className="text-sm font-extrabold text-slate-900 mt-0.5">
            4 Langkah Mudah Memilah &amp; Menghasilkan
          </h3>
        </div>

        <div className="space-y-3">
          {/* Step 1 */}
          <div className="flex gap-3 bg-slate-50 border border-slate-200/80 rounded-2xl p-3.5 items-start">
            <div className="w-8 h-8 rounded-xl bg-emerald-600 text-white font-black text-sm flex items-center justify-center flex-shrink-0 shadow-xs">
              1
            </div>
            <div className="space-y-0.5">
              <h4 className="text-xs font-bold text-slate-900">Pilah Sampah di Rumah</h4>
              <p className="text-[11px] text-slate-600 leading-relaxed">
                Pisahkan kardus paket, botol plastik PET, minyak jelantah bekas, dan sisa organik dapur. Bersihkan dari sisa cairan &amp; lipat pipih.
              </p>
            </div>
          </div>

          {/* Step 2 */}
          <div className="flex gap-3 bg-slate-50 border border-slate-200/80 rounded-2xl p-3.5 items-start">
            <div className="w-8 h-8 rounded-xl bg-emerald-600 text-white font-black text-sm flex items-center justify-center flex-shrink-0 shadow-xs">
              2
            </div>
            <div className="space-y-0.5">
              <h4 className="text-xs font-bold text-slate-900">Pilih Jemput Armada atau Antar Mandiri</h4>
              <p className="text-[11px] text-slate-600 leading-relaxed">
                <strong>Jemput Motor Tossa:</strong> Armada roda tiga datang langsung ke teras rumahmu (potongan bensin armada 10%).<br />
                <strong>Antar Sendiri:</strong> Bawa langsung ke Bank Sampah terdekat untuk menikmati <strong>100% saldo utuh tanpa potongan</strong>.
              </p>
            </div>
          </div>

          {/* Step 3 */}
          <div className="flex gap-3 bg-slate-50 border border-slate-200/80 rounded-2xl p-3.5 items-start">
            <div className="w-8 h-8 rounded-xl bg-emerald-600 text-white font-black text-sm flex items-center justify-center flex-shrink-0 shadow-xs">
              3
            </div>
            <div className="space-y-0.5">
              <h4 className="text-xs font-bold text-slate-900">Ditimbang Digital &amp; Saldo Langsung Masuk</h4>
              <p className="text-[11px] text-slate-600 leading-relaxed">
                Petugas menimbang sampah di tempat secara transparan dengan timbangan digital gantung. Saldo uang mengendap seketika bertambah di aplikasi.
              </p>
            </div>
          </div>

          {/* Step 4 */}
          <div className="flex gap-3 bg-slate-50 border border-slate-200/80 rounded-2xl p-3.5 items-start">
            <div className="w-8 h-8 rounded-xl bg-emerald-600 text-white font-black text-sm flex items-center justify-center flex-shrink-0 shadow-xs">
              4
            </div>
            <div className="space-y-0.5">
              <h4 className="text-xs font-bold text-slate-900">Tarik ke E-Wallet atau Belanja Produk Upcycle</h4>
              <p className="text-[11px] text-slate-600 leading-relaxed">
                Cairkan saldo kapan saja ke GoPay / DANA tanpa biaya admin, atau tukarkan langsung dengan pupuk kompos organik super &amp; pot bunga daur ulang.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* INDEKS HARGA KOMODITAS REALTIME */}
      <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-xs font-extrabold text-slate-900">
              Indeks Harga Komoditas Sampah Terkini
            </h3>
            <p className="text-[10px] text-slate-500">Harga beli resmi dari jaringan Bank Sampah mitra</p>
          </div>
          <span className="text-[10px] text-emerald-800 bg-emerald-100 font-bold px-2 py-0.5 rounded-full">
            Real-time
          </span>
        </div>

        <div className="space-y-2">
          {wastePrices && Object.entries(wastePrices).map(([key, item]) => (
            <div key={key} className="bg-slate-50 border border-slate-200/70 rounded-2xl p-3 flex items-center justify-between">
              <div className="flex items-center gap-2.5">
                <span className="text-xl">{item.icon}</span>
                <div>
                  <div className="text-xs font-bold text-slate-900">{item.name}</div>
                  <div className="text-[10px] text-slate-500">Satuan: per {item.unit}</div>
                </div>
              </div>
              <div className="text-right">
                <div className="text-xs font-extrabold text-emerald-700">{formatRupiah(item.price)}/{item.unit}</div>
                <div className="text-[9px] text-emerald-600 font-bold">{item.trend}</div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Bottom CTA to explore Demo directly */}
      <div className="text-center pt-2 pb-6 space-y-2">
        <button
          type="button"
          onClick={onEnterApp}
          className="w-full bg-slate-900 hover:bg-slate-800 active:scale-95 text-white font-bold text-xs py-3.5 rounded-2xl transition shadow-md cursor-pointer flex items-center justify-center gap-2"
        >
          <span>Mulai Masuk ke Dasbor Aplikasi</span>
          <ArrowRight className="w-4 h-4 text-emerald-400" />
        </button>
        <p className="text-[11px] text-slate-400">
          Atau gunakan menu di atas untuk masuk / mendaftar akun baru
        </p>
      </div>
    </div>
  );
}
