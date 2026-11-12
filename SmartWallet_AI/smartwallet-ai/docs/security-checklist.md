# Checklist Keamanan Pra-Deploy

| Pemeriksaan | Status prototipe | Bukti/tindak lanjut |
|---|---|---|
| Tidak meminta PIN/OTP/password | Dirancang | Instruksi eksplisit pada persona; uji manual T07 |
| API key tidak ditulis di source code | Ya | Menggunakan environment variable OPENAI_API_KEY |
| Hak akses minimum | Sebagian | Prototipe tidak memiliki login atau akses database; bila ditambah, gunakan least privilege |
| Validasi input | Sebagian | Bobot slider dibatasi 1–5; tambahkan validasi server-side sebelum produksi |
| Validasi keluaran AI | Belum otomatis | Hasil harus ditinjau; tambahkan pemeriksaan format dan fakta sebelum deploy |
| Perlindungan data pengguna | Ya untuk prototipe | Catatan pengguna tidak disimpan ke database; hindari memasukkan data sensitif |
| Penanganan kegagalan API | Sebagian | Mode demo bila API key tidak ada; tambahkan try/except dan retry sebelum produksi |

Prototipe tidak boleh digunakan untuk keputusan finansial penting. Lakukan pengujian keamanan tambahan sebelum penggunaan publik.
