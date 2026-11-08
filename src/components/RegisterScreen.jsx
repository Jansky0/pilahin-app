import React, { useState, useEffect } from 'react';
import {
  Recycle,
  User,
  Smartphone,
  Mail,
  MapPin,
  Lock,
  ArrowRight,
  ShieldCheck,
  CheckCircle2,
  X,
  Sparkles,
  Delete,
  Fingerprint
} from 'lucide-react';

export default function RegisterScreen({
  onRegisterSuccess,
  onNavigateLogin,
  onNavigateLanding,
  showToast
}) {
  // Step Management: 1 = Data Diri & Alamat, 2 = Buat PIN Transaksi
  const [step, setStep] = useState(1);
  const [showOtpModal, setShowOtpModal] = useState(false);

  // Form State - Step 1
  const [fullName, setFullName] = useState('Siti Rahmawati');
  const [phone, setPhone] = useState('812-3456-7890');
  const [email, setEmail] = useState('siti.rahma@email.com');
  const [address, setAddress] = useState('Jl. Danau Tamblingan No. 42, RT 02/RW 04, Cilandak Barat');
  const [agreeTerms, setAgreeTerms] = useState(true);

  // OTP State (Modal)
  const [otp, setOtp] = useState(['4', '8', '', '', '', '']);
  const [countdown, setCountdown] = useState(45);

  // PIN State - Step 2
  const [pinDigits, setPinDigits] = useState(['', '', '', '', '', '']);

  // Countdown timer for OTP
  useEffect(() => {
    let timer;
    if (showOtpModal && countdown > 0) {
      timer = setInterval(() => {
        setCountdown((prev) => prev - 1);
      }, 1000);
    }
    return () => clearInterval(timer);
  }, [showOtpModal, countdown]);

  // Handle Step 1 Next -> Trigger OTP Modal
  const handleProceedToOtp = (e) => {
    e?.preventDefault();
    if (!fullName.trim()) {
      showToast('Masukkan Nama Lengkap sesuai KTP!');
      return;
    }
    if (!phone.trim()) {
      showToast('Masukkan Nomor WhatsApp aktif!');
      return;
    }
    if (!address.trim()) {
      showToast('Lengkapi Alamat Domisili penjemputan sampah!');
      return;
    }
    if (!agreeTerms) {
      showToast('Centang persetujuan syarat & ketentuan untuk melanjutkan!');
      return;
    }

    setCountdown(45);
    setShowOtpModal(true);
  };

  // Handle OTP Verification Success -> Move to Step 2 (PIN)
  const handleVerifyOtp = () => {
    setShowOtpModal(false);
    setStep(2);
    showToast('Nomor WhatsApp terverifikasi! Silakan buat 6-digit PIN keamanan.');
  };

  // Custom Numeric Keypad Input for Step 2
  const handleKeyPress = (num) => {
    const nextIdx = pinDigits.findIndex((d) => d === '');
    if (nextIdx !== -1) {
      const updated = [...pinDigits];
      updated[nextIdx] = String(num);
      setPinDigits(updated);
    }
  };

  const handleBackspace = () => {
    const lastFilledIdx = pinDigits.map((d) => d !== '').lastIndexOf(true);
    if (lastFilledIdx !== -1) {
      const updated = [...pinDigits];
      updated[lastFilledIdx] = '';
      setPinDigits(updated);
    }
  };

  const handleBiometricDemo = () => {
    setPinDigits(['1', '2', '3', '4', '5', '6']);
    showToast('Biometrik sidik jari terkonfirmasi (PIN otomatis diisi)');
  };

  // Finalize Account Creation
  const handleFinishRegistration = () => {
    const fullPin = pinDigits.join('');
    if (fullPin.length < 6) {
      showToast('Masukkan lengkap 6 angka PIN Transaksi!');
      return;
    }

    const newUser = {
      id: 'usr-' + Date.now(),
      name: fullName.trim(),
      email: email.trim() || `${phone.replace(/\D/g, '')}@pilahin.id`,
      phone: phone.trim().startsWith('0') ? phone.trim() : '0' + phone.trim().replace(/^62/, ''),
      role: 'warga',
      avatar: fullName.trim().slice(0, 2).toUpperCase(),
      primaryAddress: address.trim(),
      addressBenchmark: 'Sampah di teras depan, dekat pagar',
      userRank: 'Warga Pemilah Baru (Level 1)'
    };

    onRegisterSuccess(newUser);
    showToast(`Registrasi Berhasil! Selamat datang di Pilah.in, ${newUser.name}!`);
  };

  return (
    <div className="flex-1 overflow-y-auto px-5 py-6 flex flex-col justify-between bg-white min-h-screen">
      {/* ================= STEP 1: INFORMASI PENGGUNA (Wireframe 2) ================= */}
      {step === 1 && (
        <div className="space-y-5">
          {/* Top Bar: Logo, Step Badge, Close */}
          <div className="flex items-center justify-between pb-3 border-b border-slate-100">
            <div className="w-8 h-8 rounded-xl bg-slate-900 text-white flex items-center justify-center font-bold">
              <Recycle className="w-4 h-4 text-emerald-400" />
            </div>

            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-slate-700 bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
                Langkah 1 dari 2
              </span>
              <button
                type="button"
                onClick={onNavigateLanding}
                className="w-7 h-7 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center transition"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          {/* Heading */}
          <div>
            <h1 className="text-2xl font-black text-slate-900 tracking-tight">
              Daftar Akun Pilah.in
            </h1>
            <p className="text-xs text-slate-500 mt-0.5">
              Registrasi Warga TPS3R & Bank Sampah Digital
            </p>
          </div>

          {/* Form Card: 1. INFORMASI PENGGUNA */}
          <div className="rounded-2xl border border-slate-200/90 p-4 bg-white shadow-xs space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 pb-2">
              <span className="text-xs font-black text-slate-800 tracking-wider uppercase">
                1. INFORMASI PENGGUNA
              </span>
              <div className="w-10 h-1.5 bg-slate-200 rounded-full"></div>
            </div>

            {/* Field 1: Nama Lengkap */}
            <div>
              <label className="text-xs font-bold text-slate-700 block mb-1">
                Nama Lengkap Sesuai KTP
              </label>
              <div className="flex items-center rounded-xl border border-slate-200 px-3 py-2.5 focus-within:border-slate-900 transition">
                <input
                  type="text"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                  placeholder="Contoh: Siti Rahmawati"
                  className="w-full text-xs font-semibold text-slate-800 placeholder-slate-400 outline-hidden bg-transparent"
                />
                <div className="w-3.5 h-3.5 rounded-full border border-slate-300"></div>
              </div>
            </div>

            {/* Field 2: Nomor WhatsApp */}
            <div>
              <label className="text-xs font-bold text-slate-700 block mb-1">
                Nomor WhatsApp Aktif
              </label>
              <div className="flex items-center rounded-xl border border-slate-200 px-3 py-2.5 focus-within:border-slate-900 transition">
                <span className="text-xs font-bold text-slate-600 pr-2 border-r border-slate-200">
                  +62
                </span>
                <input
                  type="tel"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  placeholder="812-3456-7890"
                  className="w-full pl-2.5 text-xs font-semibold text-slate-800 placeholder-slate-400 outline-hidden bg-transparent"
                />
              </div>
            </div>

            {/* Field 3: Email */}
            <div>
              <label className="text-xs font-bold text-slate-700 block mb-1">
                Alamat Email Aktif
              </label>
              <div className="flex items-center rounded-xl border border-slate-200 px-3 py-2.5 focus-within:border-slate-900 transition">
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Contoh: nama@email.com"
                  className="w-full text-xs font-semibold text-slate-800 placeholder-slate-400 outline-hidden bg-transparent"
                />
                <div className="w-3.5 h-3.5 rounded-full border border-slate-300"></div>
              </div>
            </div>

            {/* Field 4: Alamat Domisili */}
            <div>
              <label className="text-xs font-bold text-slate-700 block mb-1">
                Alamat Domisili / Tempat Tinggal
              </label>
              <textarea
                rows={3}
                value={address}
                onChange={(e) => setAddress(e.target.value)}
                placeholder="Alamat lengkap tempat tinggal untuk akses motor Tossa"
                className="w-full rounded-xl border border-slate-200 p-2.5 text-xs font-semibold text-slate-800 placeholder-slate-400 outline-hidden focus:border-slate-900 transition resize-none bg-transparent"
              />
            </div>
          </div>

          {/* Terms Checkbox */}
          <div className="flex items-start gap-2.5 px-1">
            <input
              type="checkbox"
              id="terms"
              checked={agreeTerms}
              onChange={(e) => setAgreeTerms(e.target.checked)}
              className="mt-0.5 rounded-md border-slate-300 text-slate-900 focus:ring-slate-900 cursor-pointer"
            />
            <label htmlFor="terms" className="text-[11px] text-slate-500 leading-tight cursor-pointer">
              Saya menyetujui Syarat & Ketentuan serta Kebijakan Privasi platform sirkular Pilah.in.
            </label>
          </div>

          {/* CTA: Lanjut ke Pembuatan PIN */}
          <button
            type="button"
            onClick={handleProceedToOtp}
            className="w-full py-3.5 px-4 rounded-2xl bg-slate-950 hover:bg-slate-800 text-white font-extrabold text-xs transition cursor-pointer shadow-md active:scale-98 flex items-center justify-center gap-1.5"
          >
            <span>Lanjut ke Pembuatan PIN</span>
            <ArrowRight className="w-4 h-4" />
          </button>

          {/* Footer Back to Login */}
          <div className="text-center pt-2">
            <button
              type="button"
              onClick={onNavigateLogin}
              className="text-xs font-semibold text-slate-600 hover:text-slate-900 underline underline-offset-2 transition"
            >
              Sudah punya akun warga? Masuk
            </button>
          </div>
        </div>
      )}

      {/* ================= STEP 2: PEMBUATAN PIN 6-DIGIT (Wireframe 4) ================= */}
      {step === 2 && (
        <div className="space-y-4">
          {/* Top Bar: Progress, Step Badge, Close */}
          <div className="flex items-center justify-between pb-3 border-b border-slate-100">
            <div className="w-8 h-8 rounded-xl bg-slate-900 text-white flex items-center justify-center font-bold">
              <Recycle className="w-4 h-4 text-emerald-400" />
            </div>

            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-slate-700 bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
                Langkah 2 dari 2
              </span>
              <button
                type="button"
                onClick={onNavigateLanding}
                className="w-7 h-7 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center transition"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          {/* Heading */}
          <div>
            <h1 className="text-2xl font-black text-slate-900 tracking-tight">
              Buat PIN Saldo Pilah.in
            </h1>
            <p className="text-xs text-slate-500 mt-0.5">
              Amankan transaksi pencairan uang dan setor sampah Anda
            </p>
          </div>

          {/* Security Callout Card: Proteksi Finansial Sirkular */}
          <div className="rounded-2xl border border-slate-200 p-3.5 bg-slate-50/80 flex items-start gap-3">
            <div className="w-8 h-8 rounded-xl bg-white border border-slate-200 flex items-center justify-center text-slate-700 shrink-0 shadow-2xs">
              <ShieldCheck className="w-4 h-4 text-slate-800" />
            </div>
            <div>
              <h4 className="text-xs font-extrabold text-slate-900">
                Proteksi Finansial Sirkular
              </h4>
              <p className="text-[11px] text-slate-500 mt-0.5 leading-relaxed">
                PIN 6-digit ini akan digunakan setiap kali Anda mencairkan saldo daur ulang ke e-wallet/bank atau menukarnya di pasar sirkular.
              </p>
            </div>
          </div>

          {/* 6-Masked Bullet PIN Indicator */}
          <div className="py-2 text-center">
            <div className="flex items-center justify-center gap-3 mb-2">
              {pinDigits.map((d, i) => (
                <div
                  key={i}
                  className={`w-3.5 h-3.5 rounded-full transition-all duration-150 ${
                    d !== ''
                      ? 'bg-slate-950 scale-110 shadow-xs'
                      : 'border-2 border-slate-300 bg-transparent'
                  }`}
                />
              ))}
            </div>
            <p className="text-[11px] text-slate-400">
              Masukkan 6 angka yang sulit ditebak dan jangan gunakan tanggal lahir
            </p>
          </div>

          {/* Custom On-Screen Numeric Keypad */}
          <div className="grid grid-cols-3 gap-2 max-w-xs mx-auto pt-2">
            {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((n) => (
              <button
                key={n}
                type="button"
                onClick={() => handleKeyPress(n)}
                className="h-12 rounded-2xl bg-white border border-slate-200/90 text-slate-900 font-bold text-base hover:bg-slate-100 active:scale-95 transition shadow-2xs cursor-pointer flex items-center justify-center"
              >
                {n}
              </button>
            ))}

            <button
              type="button"
              onClick={handleBiometricDemo}
              title="Biometrik Sidik Jari"
              className="h-12 rounded-2xl bg-slate-50 border border-slate-200 text-slate-600 hover:text-slate-900 hover:bg-slate-100 active:scale-95 transition flex items-center justify-center cursor-pointer"
            >
              <Fingerprint className="w-5 h-5 text-emerald-600" />
            </button>

            <button
              type="button"
              onClick={() => handleKeyPress(0)}
              className="h-12 rounded-2xl bg-white border border-slate-200/90 text-slate-900 font-bold text-base hover:bg-slate-100 active:scale-95 transition shadow-2xs cursor-pointer flex items-center justify-center"
            >
              0
            </button>

            <button
              type="button"
              onClick={handleBackspace}
              title="Hapus Digit Terakhir"
              className="h-12 rounded-2xl bg-slate-50 border border-slate-200 text-slate-600 hover:text-slate-900 hover:bg-slate-100 active:scale-95 transition flex items-center justify-center cursor-pointer"
            >
              <Delete className="w-5 h-5" />
            </button>
          </div>

          {/* Final Button: Selesaikan & Buat Akun */}
          <div className="pt-2">
            <button
              type="button"
              onClick={handleFinishRegistration}
              className="w-full py-3.5 px-4 rounded-2xl bg-slate-950 hover:bg-slate-800 text-white font-extrabold text-xs transition cursor-pointer shadow-md active:scale-98 flex items-center justify-center gap-1.5"
            >
              <span>Selesaikan & Buat Akun</span>
              <ArrowRight className="w-4 h-4" />
            </button>
            <p className="text-[10px] text-center text-slate-400 mt-2">
              Lupa atau ingin mengganti PIN nanti? Dapat diubah melalui menu profil.
            </p>
          </div>
        </div>
      )}

      {/* ================= MODAL: VERIFIKASI NOMOR WHATSAPP (Wireframe 3 Bottom Sheet) ================= */}
      {showOtpModal && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-end sm:items-center justify-center p-0 sm:p-4 animate-fade-in">
          <div className="bg-white w-full max-w-sm rounded-t-3xl sm:rounded-3xl p-6 border border-slate-200 shadow-2xl space-y-4">
            {/* Drag Handle & Close */}
            <div className="w-12 h-1.5 bg-slate-200 rounded-full mx-auto sm:hidden mb-2"></div>
            <div className="flex items-center justify-between pb-1">
              <div className="w-7 h-7 rounded-lg bg-emerald-100 text-emerald-700 flex items-center justify-center">
                <CheckCircle2 className="w-4 h-4" />
              </div>
              <button
                onClick={() => setShowOtpModal(false)}
                className="w-7 h-7 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center transition"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            </div>

            <div>
              <h3 className="font-extrabold text-base text-slate-900">
                Verifikasi Nomor WhatsApp
              </h3>
              <p className="text-xs text-slate-500 mt-1 leading-relaxed">
                Kode verifikasi 6-digit telah dikirimkan via WhatsApp ke nomor{' '}
                <b className="text-slate-800">+62 {phone}</b>.
              </p>
            </div>

            {/* 6 OTP Boxes */}
            <div className="grid grid-cols-6 gap-2 my-2">
              {['4', '8', '3', '7', '1', '9'].map((digit, i) => (
                <div
                  key={i}
                  className="h-12 rounded-xl border-2 border-slate-300 bg-slate-50 flex items-center justify-center font-black text-sm text-slate-900 shadow-2xs"
                >
                  {digit}
                </div>
              ))}
            </div>

            {/* Sub-row: Timer */}
            <div className="flex items-center justify-between text-[11px] text-slate-400">
              <span>Tidak menerima kode?</span>
              <span className="font-bold text-slate-700">
                Kirim ulang dalam 00:{countdown < 10 ? `0${countdown}` : countdown}
              </span>
            </div>

            {/* CTA Button */}
            <button
              type="button"
              onClick={handleVerifyOtp}
              className="w-full py-3.5 rounded-2xl bg-slate-950 hover:bg-slate-800 text-white font-extrabold text-xs transition cursor-pointer shadow-md active:scale-98 flex items-center justify-center gap-1.5"
            >
              <span>Verifikasi & Lanjutkan</span>
              <ArrowRight className="w-4 h-4" />
            </button>

            {/* Link Salah Nomor */}
            <div className="text-center pt-1">
              <button
                type="button"
                onClick={() => setShowOtpModal(false)}
                className="text-xs font-semibold text-slate-500 hover:text-slate-800 underline underline-offset-2 transition"
              >
                Salah nomor? Ubah Nomor WhatsApp
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
