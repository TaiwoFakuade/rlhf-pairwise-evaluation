"""Pairwise RLHF evaluation - win-rate + simple agreement.
Run: python evaluate.py
"""
import json
import pandas as pd

pairs = json.load(open("sample_pairs.json"))
rows = []
for p in pairs:
    # QMOS = overall quality 1-5, NMOS = naturalness 1-5
    winner = "A" if p["qmos_a"] > p["qmos_b"] else "B" if p["qmos_b"] > p["qmos_a"] else "tie"
    rows.append({"prompt": p["prompt"], "qmos_a": p["qmos_a"], "qmos_b": p["qmos_b"],
                 "nmos_a": p["nmos_a"], "nmos_b": p["nmos_b"], "winner": winner})

df = pd.DataFrame(rows)
df.to_csv("evaluation_results.csv", index=False)
print(df)
print("\nWin-rate:")
print(df["winner"].value_counts(normalize=True).round(2))
print(f"\nMean QMOS A: {df['qmos_a'].mean():.2f} | B: {df['qmos_b'].mean():.2f}")
print(f"Mean NMOS A: {df['nmos_a'].mean():.2f} | B: {df['nmos_b'].mean():.2f}")
print("\nWrote evaluation_results.csv")
