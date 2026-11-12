import os
from pathlib import Path
from openai import OpenAI
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
except ImportError:
    pass

PERSONA = """Kamu adalah SmartWallet AI, asisten edukatif yang membantu pengguna memahami kecocokan e-wallet.
Bersikap netral, jelas, tidak mengiklankan merek, dan jangan mengklaim data contoh sebagai fakta resmi.
Jangan meminta atau mengungkap PIN, OTP, kata sandi, nomor kartu, atau data keuangan sensitif.
Jangan menyatakan suatu layanan paling aman atau paling murah tanpa bukti terverifikasi.
"""

FEW_SHOT = """Contoh gaya jawaban:
Input: Pengguna sangat mementingkan biaya dan kemudahan. Peringkat: Dompet B 4.6, Dompet A 4.3.
Output: "Dompet B berada di urutan pertama karena memperoleh skor tertinggi pada bobot preferensi ini. Pilihan ini paling sesuai dengan prioritas biaya dan kemudahan pada data contoh. Periksa kembali biaya dan ketentuan resmi sebelum menggunakannya."
"""

def generate_explanation(weights, use_case, notes, ranking):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        best = ranking[0]
        second = ranking[1] if len(ranking) > 1 else None
        text = (
            f"**{best['E-Wallet']}** memperoleh peringkat pertama dengan skor "
            f"{best['Skor']:.3f} ({best['Kecocokan']}). Bobot preferensi terbesar kamu "
            f"adalah {', '.join(k for k,v in weights.items() if v == max(weights.values()))}. "
            f"Tujuan penggunaan yang dipilih: **{use_case}**. "
        )
        if second:
            text += f"Pembanding terdekat adalah {second['E-Wallet']} dengan skor {second['Skor']:.3f}. "
        text += "Ini penjelasan mode demo berdasarkan data sintetis; bukan klaim kualitas resmi. Verifikasi biaya, fitur, dan ketentuan terbaru pada penyedia."
        return text, "template"
    client = OpenAI(api_key=api_key)
    # Prompt chaining: tahap 1 merangkum kebutuhan; tahap 2 menyusun penjelasan berdasarkan hasil SAW.
    stage1 = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        temperature=0.2,
        messages=[
            {"role": "system", "content": PERSONA + "\nEkstrak prioritas pengguna secara ringkas. Jangan membuat fakta baru."},
            {"role": "user", "content": f"Bobot: {weights}\nTujuan: {use_case}\nCatatan: {notes}"}
        ],
    ).choices[0].message.content
    stage2 = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        temperature=0.3,
        messages=[
            {"role": "system", "content": PERSONA + "\n" + FEW_SHOT + "\nJelaskan hasil dalam bahasa Indonesia. Tegaskan bahwa skor bersifat data contoh."},
            {"role": "user", "content": f"Ringkasan prioritas: {stage1}\nHasil SAW (sumber peringkat yang harus diikuti): {ranking}\nBuat ringkasan rekomendasi, alasan, pembanding, dan catatan verifikasi."}
        ],
    ).choices[0].message.content
    return stage2, "generative"
