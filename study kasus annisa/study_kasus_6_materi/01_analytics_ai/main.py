from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

DATA = Path(__file__).parent / "data" / "sales.csv"
OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

print("=== Ringkasan data ===")
print(df.describe(numeric_only=True).round(2))
print("\n=== Produk dengan omzet terbesar ===")
product_sales = (df.assign(revenue=df["quantity"] * df["price"])
                 .groupby("product")["revenue"].sum().sort_values(ascending=False))
print(product_sales)

monthly = (df.assign(revenue=df["quantity"] * df["price"])
           .groupby("month", as_index=False)["revenue"].sum())
monthly.to_csv(OUT / "monthly_revenue.csv", index=False)

# Baseline prediksi: tren linear berdasarkan urutan bulan.
monthly["month_index"] = range(len(monthly))
model = LinearRegression().fit(monthly[["month_index"]], monthly["revenue"])
next_index = [[len(monthly)]]
prediction = model.predict(next_index)[0]
print(f"\nPrediksi omzet bulan berikutnya (baseline linear): Rp{prediction:,.0f}")

plt.figure(figsize=(9, 5))
plt.plot(monthly["month"], monthly["revenue"], marker="o", label="Omzet aktual")
plt.axhline(prediction, linestyle="--", label="Prediksi bulan berikutnya")
plt.title("Tren Omzet Bulanan")
plt.xlabel("Bulan"); plt.ylabel("Omzet (Rp)")
plt.xticks(rotation=45); plt.legend(); plt.tight_layout()
plt.savefig(OUT / "revenue_trend.png", dpi=150)
print(f"\nHasil disimpan di: {OUT}")
