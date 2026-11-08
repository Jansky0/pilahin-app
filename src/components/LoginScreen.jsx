import React, { useState } from 'react';
import {
  Recycle,
  HelpCircle,
  Smartphone,
  Mail,
  Lock,
  ArrowRight,
  ShieldCheck,
  CheckCircle2,
  AlertCircle,
  KeyRound,
  X
} from 'lucide-react';

export default function LoginScreen({
  onLoginSuccess,
  onNavigateRegister,
  onNavigateLanding,
  showToast
}) {
  const [loginMethod, setLoginMethod] = useState('phone'); // 'phone' | 'email'
  const [phone, setPhone] = useState('812 3456 7890');
  const [email, setEmail] = useState('raka@pilahin.id');
  const [pin, setPin] = useState('123456');
  const [showForgotModal, setShowForgotModal] = useState(false);
  const [showOtpLoginModal, setShowOtpLoginModal] = useState(false);
  const [otpCode, setOtpCode] = useState(['', '', '', '', '', '']);

  // Normal PIN Login
  const handleLogin = (e) => {
    e?.preventDefault();
    const identifier = loginMethod === 'phone' ? phone.trim() : email.trim();

    if (!identifier) {
      showToast(loginMethod === 'phone' ? 'Masukkan nomor WhatsApp Anda!' : 'Masukkan email Anda!');
      return;
    }
    if (!pin || pin.length < 6) {
      showToast('Masukkan 6-digit PIN transaksi Anda!');
      return;
    }

    const isMitra = identifier.includes('sri') || identifier.includes('mitra');
    const user = {
      id: isMitra ? 'usr-sri' : 'usr-raka',
      name: isMitra ? 'Ibu Sri Mulyani' : 'Raka Pradipta',
      email: isMitra ? 'sri@banksampah.id' : 'raka@pilahin.id',
      phone: isMitra ? '0813-8899-7711' : '0812-3456-7890',
      role: isMitra ? 'mitra' : 'warga',
      avatar: isMitra ? 'SM' : 'RP',
      primaryAddress: isMitra
        ? 'Pos Bank Sampah Berkah Lestari, Balai Warga'
        : 'Jl. Cemara No. 14, RT 03/RW 05, Cilandak Barat',
      addressBenchmark: isMitra
        ? 'Samping pos satpam utama'
        : 'Pagar hitam depan warung Bu Titin, sampah di teras depan',
      userRank: isMitra ? 'Pengurus Utama Mitra' : 'Pahlawan Hijau Level 3'
    };

    onLoginSuccess(user);
    showToast(`Selamat datang kembali, ${user.name}!`);
  };

  // WhatsApp OTP Login
  const handleOtpLogin = () => {
    const user = {
      id: 'usr-raka',
      name: 'Raka Pradipta',
      email: 'raka@pilahin.id',
      phone: '0812-3456-7890',
      role: 'warga',
      avatar: 'RP',
      primaryAddress: 'Jl. Cemara No. 14, RT 03/RW 05, Cilandak Barat',
      addressBenchmark: 'Pagar hitam depan warung Bu Titin, sampah di teras depan',
      userRank: 'Pahlawan Hijau Level 3'
    };
    setShowOtpLoginModal(false);
    onLoginSuccess(user);
    showToast('Masuk via WhatsApp OTP berhasil!');
  };

  return (
    <div className="flex-1 overflow-y-auto px-5 py-6 flex flex-col justify-between bg-white min-h-screen">
      {/* Top Bar: Logo & Help */}
      <div>
        <div className="flex items-center justify-between pb-4 border-b border-slate-100">
          <div
            onClick={onNavigateLanding}
            className="flex items-center gap-2 cursor-pointer group"
          >
            <div className="w-8 h-8 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-bold shadow-md shadow-emerald-500/20 group-hover:scale-105 transition">
              <Recycle className="w-4 h-4" />
            </div>
            <span className="font-extrabold text-base text-slate-900 tracking-tight">
              Pilah<span className="text-emerald-600">.in</span>
            </span>
          </div>

          <button
            type="button"
            onClick={() => showToast('Pusat Bantuan: Hubungi WhatsApp Admin di 0811-9876-5432')}
            className="flex items-center gap-1 text-xs font-semibold text-slate-500 hover:text-slate-800 transition px-2.5 py-1.5 rounded-lg hover:bg-slate-100"
          >
            <HelpCircle className="w-3.5 h-3.5" />
            <span>Bantuan?</span>
          </button>
        </div>

        {/* Center Illustration Placeholder & Title */}
        <div className="text-center mt-6 mb-6">
          <div className="w-16 h-16 rounded-full bg-slate-100 border border-slate-200/80 mx-auto flex items-center justify-center text-slate-400 mb-4 shadow-inner">
            <Recycle className="w-8 h-8 text-emerald-600" />
          </div>
          <h1 className="text-2xl font-black text-slate-900 tracking-tight">
            Masuk ke Pilah.in
          </h1>
          <p className="text-xs text-slate-500 mt-1 max-w-xs mx-auto">
            Kelola saldo tabungan daur ulang & jemput sampah langsung dari rumah
          </p>
        </div>

        {/* Segmented Control: Nomor HP | Email */}
        <div className="bg-slate-100 p-1 rounded-2xl flex gap-1 mb-5 border border-slate-200/60">
          <button
            type="button"
            onClick={() => setLoginMethod('phone')}
            className={`flex-1 py-2 text-xs font-bold rounded-xl transition ${
              loginMethod === 'phone'
                ? 'bg-white text-slate-900 shadow-xs'
                : 'text-slate-500 hover:text-slate-800'
            }`}
          >
            Nomor HP
          </button>
          <button
            type="button"
            onClick={() => setLoginMethod('email')}
            className={`flex-1 py-2 text-xs font-bold rounded-xl transition ${
              loginMethod === 'email'
                ? 'bg-white text-slate-900 shadow-xs'
                : 'text-slate-500 hover:text-slate-800'
            }`}
          >
            Email
          </button>
        </div>

        {/* Login Form */}
        <form onSubmit={handleLogin} className="space-y-4">
          {/* Input 1: Phone or Email */}
          <div>
            <div className="flex items-center justify-between mb-1.5">
              <label className="text-xs font-bold text-slate-800">
                {loginMethod === 'phone' ? 'Nomor WhatsApp / HP' : 'Alamat Email'}
              </label>
              <span className="text-[10px] font-semibold text-slate-400">Wajib</span>
            </div>

            {loginMethod === 'phone' ? (
              <div className="flex items-center rounded-2xl border border-slate-200 bg-white px-3.5 py-3 focus-within:border-slate-900 focus-within:ring-2 focus-within:ring-slate-900/10 transition shadow-2xs">
                <span className="text-xs font-bold text-slate-600 pr-2.5 border-r border-slate-200">
                  +62
                </span>
                <input
                  type="tel"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  placeholder="812 3456 7890"
                  className="w-full pl-3 text-xs font-semibold text-slate-800 placeholder-slate-400 outline-hidden bg-transparent"
                />
              </div>
            ) : (
              <div className="flex items-center rounded-2xl border border-slate-200 bg-white px-3.5 py-3 focus-within:border-slate-900 focus-within:ring-2 focus-within:ring-slate-900/10 transition shadow-2xs">
                <Mail className="w-4 h-4 text-slate-400 mr-2.5" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="nama@email.com"
                  className="w-full text-xs font-semibold text-slate-800 placeholder-slate-400 outline-hidden bg-transparent"
                />
              </div>
            )}
          </div>

          {/* Input 2: PIN 6-Digit */}
          <div>
            <div className="flex items-center justify-between mb-1.5">
              <label className="text-xs font-bold text-slate-800">
                PIN Transaksi 6-Digit
              </label>
              <button
                type="button"
                onClick={() => setShowForgotModal(true)}
                className="text-[11px] font-bold text-slate-500 hover:text-slate-900 transition underline underline-offset-2"
              >
                Lupa PIN?
              </button>
            </div>
            <div className="flex items-center rounded-2xl border border-slate-200 bg-white px-3.5 py-3 focus-within:border-slate-900 focus-within:ring-2 focus-within:ring-slate-900/10 transition shadow-2xs">
              <Lock className="w-4 h-4 text-slate-400 mr-2.5" />
              <input
                type="password"
                maxLength={6}
                value={pin}
                onChange={(e) => setPin(e.target.value.replace(/\D/g, ''))}
                placeholder="••••••"
                className="w-full text-xs font-bold tracking-widest text-slate-800 placeholder-slate-400 outline-hidden bg-transparent"
              />
            </div>
          </div>

          {/* Primary CTA: Masuk */}
          <button
            type="submit"
            className="w-full py-3.5 px-4 rounded-2xl bg-slate-950 hover:bg-slate-800 text-white font-extrabold text-sm transition cursor-pointer shadow-md shadow-slate-950/20 active:scale-98 mt-2"
          >
            Masuk
          </button>

          {/* Secondary CTA: Masuk via WhatsApp OTP */}
          <button
            type="button"
            onClick={() => setShowOtpLoginModal(true)}
            className="w-full py-3.5 px-4 rounded-2xl bg-white hover:bg-slate-50 text-slate-800 font-bold text-xs border border-slate-300 transition cursor-pointer shadow-2xs active:scale-98"
          >
            Masuk via WhatsApp OTP
          </button>
        </form>

        {/* Divider: Atau Daftar Mitra */}
        <div className="relative my-6 text-center">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t border-slate-200"></div>
          </div>
          <span className="relative bg-white px-3 text-[11px] font-semibold text-slate-400 uppercase tracking-wider">
            atau daftar mitra
          </span>
        </div>

        {/* Conversion Card: Belum punya akun? [Daftar] */}
        <div className="rounded-2xl border border-slate-200 p-4 bg-slate-50/60 flex items-center justify-between">
          <div>
            <p className="text-xs font-bold text-slate-900">
              Belum punya akun Pilah.in?
            </p>
            <p className="text-[10px] text-slate-500 mt-0.5">
              Daftar gratis dalam 2 menit & dapatkan saldo awal
            </p>
          </div>
          <button
            type="button"
            onClick={onNavigateRegister}
            className="px-4 py-2 rounded-xl bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs border border-slate-300 shadow-2xs transition active:scale-95"
          >
            Daftar
          </button>
        </div>
      </div>

      {/* Footer Links: Kebijakan • Syarat • FAQ */}
      <div className="pt-6 text-center border-t border-slate-100">
        <div className="flex items-center justify-center gap-3 text-[11px] text-slate-400 font-medium">
          <button
            type="button"
            onClick={() => showToast('Kebijakan Privasi: Data Anda dienkripsi aman 256-bit')}
            className="hover:text-slate-700 transition cursor-pointer"
          >
            Kebijakan
          </button>
          <span>•</span>
          <button
            type="button"
            onClick={() => showToast('Syarat & Ketentuan: Transparansi 100% tanpa biaya tersembunyi')}
            className="hover:text-slate-700 transition cursor-pointer"
          >
            Syarat
          </button>
          <span>•</span>
          <button
            type="button"
            onClick={() => showToast('FAQ: Saldo tunai bisa ditarik kapan saja ke GoPay/DANA')}
            className="hover:text-slate-700 transition cursor-pointer"
          >
            FAQ
          </button>
        </div>
      </div>

      {/* MODAL: Lupa PIN */}
      {showForgotModal && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-end sm:items-center justify-center p-0 sm:p-4 animate-fade-in">
          <div className="bg-white w-full max-w-sm rounded-t-3xl sm:rounded-3xl p-6 border border-slate-200 shadow-2xl space-y-4">
            <div className="flex items-center justify-between pb-2 border-b border-slate-100">
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 rounded-full bg-amber-50 text-amber-600 flex items-center justify-center font-bold">
                  <KeyRound className="w-4 h-4" />
                </div>
                <h3 className="font-bold text-sm text-slate-900">Pemulihan PIN Transaksi</h3>
              </div>
              <button
                onClick={() => setShowForgotModal(false)}
                className="p-1 rounded-full text-slate-400 hover:text-slate-700"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
            <p className="text-xs text-slate-600 leading-relaxed">
              Kami akan mengirimkan 6-digit kode reset keamanan ke nomor WhatsApp Anda (<b>+62 {phone}</b>).
            </p>
            <button
              type="button"
              onClick={() => {
                setShowForgotModal(false);
                showToast('Kode OTP Reset berhasil dikirimkan via WhatsApp!');
                setShowOtpLoginModal(true);
              }}
              className="w-full py-3 rounded-2xl bg-slate-900 text-white font-bold text-xs shadow-md"
            >
              Kirim Kode Reset via WhatsApp
            </button>
          </div>
        </div>
      )}

      {/* MODAL: Masuk via WhatsApp OTP */}
      {showOtpLoginModal && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-end sm:items-center justify-center p-0 sm:p-4 animate-fade-in">
          <div className="bg-white w-full max-w-sm rounded-t-3xl sm:rounded-3xl p-6 border border-slate-200 shadow-2xl space-y-4">
            <div className="w-12 h-1.5 bg-slate-200 rounded-full mx-auto sm:hidden mb-2"></div>
            <div className="flex items-center justify-between">
              <h3 className="font-extrabold text-base text-slate-900">Verifikasi WhatsApp OTP</h3>
              <button
                onClick={() => setShowOtpLoginModal(false)}
                className="p-1 rounded-full text-slate-400 hover:text-slate-700"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
            <p className="text-xs text-slate-500">
              Kode verifikasi 6-digit telah dikirimkan ke nomor WhatsApp <b>+62 {phone}</b>.
            </p>
            <div className="grid grid-cols-6 gap-2 my-3">
              {['4', '8', '2', '9', '1', '5'].map((d, i) => (
                <div
                  key={i}
                  className="h-12 rounded-xl border-2 border-slate-300 bg-slate-50 flex items-center justify-center font-black text-sm text-slate-900"
                >
                  {d}
                </div>
              ))}
            </div>
            <p className="text-[11px] text-center text-slate-400">
              Kirim ulang dalam <span className="font-bold text-slate-700">00:45</span>
            </p>
            <button
              type="button"
              onClick={handleOtpLogin}
              className="w-full py-3.5 rounded-2xl bg-slate-950 text-white font-extrabold text-xs shadow-md"
            >
              Verifikasi & Masuk Sekarang →
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
