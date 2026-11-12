# Laporan Teknis Capstone Project

## 1. Ringkasan Eksekutif
SmartWallet AI merupakan prototipe sistem rekomendasi e-wallet yang membantu pengguna membandingkan alternatif berdasarkan prioritas pribadi. Sistem menggunakan metode Simple Additive Weighting (SAW) untuk menghitung peringkat, kemudian Generative AI menyusun penjelasan yang mudah dipahami. Prototipe menerapkan Persona Prompting, Few-shot Prompting, dan Prompt Chaining. Data Dompet A–E yang disertakan merupakan data sintetis/ilustratif dan tidak boleh dianggap sebagai penilaian resmi penyedia.

## 2. Masalah dan Konteks
Pengguna dapat memiliki prioritas berbeda saat memilih dompet digital, seperti biaya, keamanan, kemudahan, promo/fitur, dan penerimaan merchant. Membandingkan banyak kriteria secara manual dapat menyulitkan. SmartWallet AI menawarkan proses pembobotan dan penjelasan hasil yang transparan. Pihak terdampak adalah calon pengguna e-wallet yang membutuhkan bantuan membandingkan alternatif.

## 3. Kebutuhan
- R2: keluaran rekomendasi dan tabel perbandingan memiliki format konsisten.
- R3: proses rekomendasi melibatkan tahapan pembobotan, perhitungan, dan penjelasan.
- R4: peringkat SAW deterministik untuk input dan dataset yang sama.
- R7: sistem membaca input preferensi dan memprosesnya menjadi hasil.

R1 dan R5 belum menjadi kemampuan penuh karena dataset saat ini sintetis dan belum terhubung ke sumber resmi terkini. R6 belum diukur secara formal.

## 4. Rancangan Solusi
1. Persona prompting: model diberi peran konsultan e-wallet yang netral dan memiliki batasan privasi. Jika dihapus, gaya dan batasan jawaban lebih sulit dijaga.
2. Few-shot prompting: contoh jawaban diberikan agar penjelasan konsisten. Jika dihapus, format dan kedalaman jawaban dapat lebih bervariasi.
3. Prompt chaining: tahap pertama merangkum preferensi, tahap kedua menjelaskan hasil SAW. Jika dihapus, pemisahan tugas berkurang dan proses lebih sulit ditelusuri.

Teknik RAG tidak dipakai karena versi awal belum memakai dokumen eksternal terverifikasi. Function calling tidak dipakai karena aplikasi tidak perlu melakukan transaksi atau menulis ke sistem eksternal. Multimodal tidak diperlukan karena input proyek berupa preferensi terstruktur.

## 5. Implementasi
Aplikasi dibuat menggunakan Python dan Streamlit. Modul `recommender.py` menghitung skor SAW dari lima kriteria berskala 1–5. Bobot pengguna dinormalisasi dengan membagi setiap bobot dengan total bobot. Skor akhir adalah jumlah perkalian skor kriteria dan bobot normalisasi. Modul `ai_explainer.py` menggunakan OpenAI API bila API key tersedia; tanpa API key, aplikasi menyediakan mode demo berbasis template. Prompt versi awal dan versi perbaikan disimpan pada folder `prompts`.

## 6. Evaluasi
Set uji awal tersedia di `eval/testset.csv`. Pengujian mencakup bobot dominan, bobot sama, batas input, catatan kosong, dan mode tanpa API key. Hasil numerik harus dihasilkan dengan menjalankan aplikasi dan pengujian pada lingkungan pengguna; dokumen ini tidak mengklaim pengujian API eksternal telah dilakukan. Kriteria penerimaan: peringkat berubah sesuai bobot, input slider valid, dan mode demo dapat menghasilkan penjelasan tanpa API key. Tambahkan hasil aktual dan tangkapan layar sebelum pengumpulan.

## 7. Keamanan, Etika, dan Biaya
Checklist keamanan terdapat pada `security-checklist.md`, audit bias awal pada `bias-audit.md`, dan asumsi biaya pada `cost-estimate.md`. Aplikasi tidak meminta kredensial pembayaran. API key disimpan sebagai environment variable. Data contoh bersifat sintetis. Penggunaan nyata membutuhkan data yang diverifikasi, validasi keluaran, dan peninjauan manusia.

## 8. Keterbatasan
Skor e-wallet bukan data resmi, sehingga hasil tidak dapat digunakan untuk menyimpulkan layanan mana yang paling baik, aman, atau murah di dunia nyata. Belum ada survei pengguna yang representatif, pengujian beban, audit keamanan independen, maupun evaluasi kualitas generasi pada sampel besar. Penjelasan AI dapat keliru dan harus diperiksa.

## 9. Rencana Kelanjutan
Mengumpulkan data kriteria melalui kuesioner dan sumber resmi yang dapat diverifikasi; menambah sitasi sumber dan tanggal pembaruan; menguji konsistensi jawaban pada set uji; menambahkan validasi keluaran dan penanganan kegagalan API; serta melakukan uji coba dengan responden dan melaporkan hasil aktual.
