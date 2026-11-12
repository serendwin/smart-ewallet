import streamlit as st
from src.recommender import recommend, compare_wallets, DEFAULT_WALLETS
from src.ai_explainer import generate_explanation

st.set_page_config(page_title="SmartWallet AI", page_icon="💳", layout="wide")
st.title("💳 SmartWallet AI")
st.caption("Rekomendasi e-wallet berdasarkan preferensi pengguna dengan bantuan Generative AI")

with st.sidebar:
    st.header("Preferensi kamu")
    st.write("Atur bobot setiap kriteria. Total bobot akan dinormalisasi otomatis.")
    weights = {
        "Biaya rendah": st.slider("Pentingnya biaya rendah", 1, 5, 5),
        "Keamanan": st.slider("Pentingnya keamanan", 1, 5, 5),
        "Kemudahan": st.slider("Pentingnya kemudahan", 1, 5, 4),
        "Promo dan fitur": st.slider("Pentingnya promo dan fitur", 1, 5, 3),
        "Penerimaan merchant": st.slider("Pentingnya penerimaan merchant", 1, 5, 4),
    }
    budget = st.selectbox("Kebiasaan penggunaan", [
        "Transaksi harian", "Belanja online", "Transportasi dan makanan",
        "Transfer dan pembayaran tagihan", "Campuran"
    ])
    notes = st.text_area("Preferensi tambahan (opsional)", placeholder="Contoh: saya sering belanja online dan ingin biaya rendah.")

st.info("Catatan: skor e-wallet pada aplikasi ini adalah **data contoh/sintetis untuk demonstrasi**, bukan penilaian resmi atau data biaya terkini dari penyedia.")

col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("Hasil rekomendasi")
    results = recommend(DEFAULT_WALLETS, weights)
    st.dataframe(results[["Peringkat", "E-Wallet", "Skor", "Kecocokan"]], hide_index=True, use_container_width=True)
    top = results.iloc[0]
    st.success(f"Rekomendasi utama: **{top['E-Wallet']}** (skor {top['Skor']:.3f})")
with col2:
    st.subheader("Bandingkan e-wallet")
    selected = st.multiselect("Pilih e-wallet", [w["name"] for w in DEFAULT_WALLETS],
                              default=[top["E-Wallet"], results.iloc[min(1, len(results)-1)]["E-Wallet"]])
    if selected:
        st.dataframe(compare_wallets(DEFAULT_WALLETS, selected), hide_index=True, use_container_width=True)

st.divider()
st.subheader("Penjelasan dari SmartWallet AI")
if st.button("✨ Buat penjelasan rekomendasi", type="primary"):
    with st.spinner("Menyusun penjelasan..."):
        explanation, mode = generate_explanation(
            weights=weights, use_case=budget, notes=notes,
            ranking=results.to_dict(orient="records")
        )
    if mode == "generative":
        st.caption("Mode: Generative AI aktif")
    else:
        st.caption("Mode demo: penjelasan berbasis template. Tambahkan OPENAI_API_KEY untuk mengaktifkan Generative AI.")
    st.markdown(explanation)

with st.expander("Bagaimana sistem bekerja?"):
    st.markdown("""
    1. Pengguna mengisi bobot kepentingan lima kriteria.
    2. Sistem menghitung skor menggunakan metode **Simple Additive Weighting (SAW)**.
    3. Persona prompting mengarahkan AI menjadi konsultan pemilihan e-wallet.
    4. Few-shot prompting memberikan contoh gaya penjelasan yang diharapkan.
    5. Prompt chaining memisahkan tahap interpretasi preferensi dan penyusunan penjelasan.

    AI hanya menjelaskan hasil perhitungan. Peringkat akhir ditentukan oleh perhitungan SAW, bukan tebakan model.
    """)

st.caption("SmartWallet AI | Prototype akademik | Gunakan data resmi yang telah diverifikasi sebelum penerapan nyata.")
