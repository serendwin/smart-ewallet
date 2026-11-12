# Audit Bias dan Etika

## Tujuan
Memeriksa apakah sistem memberikan hasil berbeda secara tidak semestinya ketika preferensi yang relevan dibuat sama.

## Rancangan audit
Gunakan profil sintetis dengan bobot kriteria identik. Ubah hanya atribut demografis hipotetis (misalnya nama samaran atau kelompok usia) yang tidak menjadi fitur perhitungan. Peringkat seharusnya tetap sama karena atribut tersebut tidak dipakai oleh algoritma.

## Hasil yang diharapkan
- Atribut demografis tidak masuk ke rumus SAW.
- Peringkat hanya dipengaruhi bobot preferensi dan skor kriteria.
- Penjelasan AI tidak boleh membuat asumsi tentang kemampuan finansial atau karakter pengguna.

## Keterbatasan
Audit ini adalah rancangan awal. Jalankan pengujian terkendali pada versi final dan lampirkan hasil aktual. Data e-wallet contoh tidak mewakili seluruh penyedia maupun seluruh pengalaman pengguna.
