import pandas as pd

# Data sintetis/ilustratif skala 1-5. Bukan rating resmi penyedia.
DEFAULT_WALLETS = [
    {"name": "GoPay", "biaya": 4, "keamanan": 4, "kemudahan": 5, "promo_fitur": 4, "merchant": 4},
    {"name": "ShopeePay", "biaya": 5, "keamanan": 4, "kemudahan": 4, "promo_fitur": 3, "merchant": 3},
    {"name": "Dana", "biaya": 3, "keamanan": 5, "kemudahan": 4, "promo_fitur": 5, "merchant": 5},
    {"name": "Ovo", "biaya": 4, "keamanan": 3, "kemudahan": 3, "promo_fitur": 5, "merchant": 4},
    {"name": "LinkAja", "biaya": 5, "keamanan": 3, "kemudahan": 4, "promo_fitur": 3, "merchant": 4},
]
CRITERIA = {
    "Biaya rendah": "biaya",
    "Keamanan": "keamanan",
    "Kemudahan": "kemudahan",
    "Promo dan fitur": "promo_fitur",
    "Penerimaan merchant": "merchant",
}

def recommend(wallets, user_weights):
    """SAW dengan semua atribut berupa skor benefit 1-5; bobot dinormalisasi."""
    total = sum(user_weights.values()) or 1
    normalized_weights = {k: v / total for k, v in user_weights.items()}
    rows = []
    for wallet in wallets:
        score = sum(wallet[CRITERIA[k]] * normalized_weights[k] for k in CRITERIA)
        rows.append({
            "E-Wallet": wallet["name"],
            "Skor": score,
            "Kecocokan": f"{score / 5 * 100:.1f}%",
            **{k: wallet[v] for k, v in CRITERIA.items()}
        })
    rows.sort(key=lambda x: x["Skor"], reverse=True)
    for i, row in enumerate(rows, 1):
        row["Peringkat"] = i
    return pd.DataFrame(rows)

def compare_wallets(wallets, selected):
    rows = []
    for w in wallets:
        if w["name"] in selected:
            rows.append({"E-Wallet": w["name"], **{k: w[v] for k, v in CRITERIA.items()}})
    return pd.DataFrame(rows)
