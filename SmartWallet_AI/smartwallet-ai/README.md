# SmartWallet AI

Prototype Capstone: sistem rekomendasi e-wallet berdasarkan preferensi pengguna dengan penjelasan Generative AI.

## Fitur
- Kuesioner bobot preferensi.
- Pemeringkatan dengan Simple Additive Weighting (SAW).
- Perbandingan skor beberapa e-wallet.
- Penjelasan dengan Generative AI (OpenAI API), atau mode demo tanpa API key.
- Tiga teknik: Persona Prompting, Few-shot Prompting, Prompt Chaining.

## Persyaratan
Python 3.10 atau lebih baru.

## Menjalankan aplikasi
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Aplikasi dapat dibuka dalam mode demo tanpa API key. Untuk mengaktifkan Generative AI, salin `.env.example` menjadi `.env` dan isi `OPENAI_API_KEY`. Aplikasi memuat file `.env` secara otomatis. Alternatifnya, atur variabel lingkungan pada terminal. Jangan pernah mengunggah `.env` ke repositori publik.

Contoh PowerShell:
```powershell
$env:OPENAI_API_KEY="API_KEY_MILIKMU"
streamlit run app.py
```

## Cara kerja
1. Pengguna mengatur bobot lima kriteria.
2. Bobot dinormalisasi agar jumlahnya menjadi 1.
3. Skor SAW dihitung dari skor kriteria ilustratif skala 1–5.
4. Model AI menjelaskan hasil perhitungan; model tidak menentukan skor/ranking.

## Struktur repositori
```text
smartwallet-ai/
├── app.py
├── src/
│   ├── __init__.py
│   ├── recommender.py
│   └── ai_explainer.py
├── prompts/v1/
├── prompts/v2/
├── eval/
├── docs/
├── demo/
├── requirements.txt
└── README.md
```

## Batasan penting
Nilai Dompet A–E merupakan data sintetis untuk demonstrasi, bukan data aktual atau rekomendasi resmi. Ganti dengan data yang dikumpulkan secara sah dan diverifikasi sebelum membuat klaim tentang penyedia e-wallet. Hasil AI bukan nasihat keuangan.
