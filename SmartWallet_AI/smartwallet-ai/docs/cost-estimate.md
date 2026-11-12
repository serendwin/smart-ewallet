# Perkiraan Biaya

## Asumsi
- Prototipe tugas kuliah, 100 sesi rekomendasi per bulan.
- Setiap sesi memanggil model dua kali untuk prompt chaining.
- Biaya API bergantung pada model, token input/output, dan harga resmi saat digunakan.
- Tidak ada biaya server pada penggunaan lokal.

## Komponen
| Komponen | Estimasi |
|---|---|
| Streamlit lokal | Rp0 |
| Penyimpanan lokal | Rp0 (menggunakan perangkat sendiri) |
| API Generative AI | Variabel; hitung dari token aktual dan harga penyedia |
| Hosting | Rp0 jika lokal; berbayar bila deploy pada layanan hosting |

Rumus anggaran API bulanan: `jumlah sesi × (token input per sesi × tarif input + token output per sesi × tarif output)`. Periksa harga resmi penyedia sebelum mengisi angka rupiah; jangan memakai tarif yang sudah kedaluwarsa.
