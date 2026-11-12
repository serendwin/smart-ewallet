import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.recommender import recommend, DEFAULT_WALLETS

cases = [
    ("equal_weights", {"Biaya rendah":3,"Keamanan":3,"Kemudahan":3,"Promo dan fitur":3,"Penerimaan merchant":3}),
    ("security_priority", {"Biaya rendah":1,"Keamanan":5,"Kemudahan":1,"Promo dan fitur":1,"Penerimaan merchant":1}),
    ("merchant_priority", {"Biaya rendah":1,"Keamanan":1,"Kemudahan":1,"Promo dan fitur":1,"Penerimaan merchant":5}),
    ("cost_priority", {"Biaya rendah":5,"Keamanan":1,"Kemudahan":1,"Promo dan fitur":1,"Penerimaan merchant":1}),
]
for name, weights in cases:
    result = recommend(DEFAULT_WALLETS, weights)
    print(name, "=>", result.iloc[0]["E-Wallet"], f"({result.iloc[0]['Skor']:.3f})")
print("PASS: ranking generated for all deterministic test cases.")
