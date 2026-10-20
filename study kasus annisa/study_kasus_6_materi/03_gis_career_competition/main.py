from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).parent
df = pd.read_csv(ROOT / "data" / "facilities.csv")
coords = df[["longitude", "latitude"]]
scaled = StandardScaler().fit_transform(coords)
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(scaled)

print("Jumlah fasilitas per kategori:")
print(df["type"].value_counts())
print("\\nLokasi dan cluster:")
print(df[["name", "type", "latitude", "longitude", "cluster"]].to_string(index=False))

plt.figure(figsize=(8, 6))
for cluster in sorted(df["cluster"].unique()):
    subset = df[df["cluster"] == cluster]
    plt.scatter(subset["longitude"], subset["latitude"], label=f"Cluster {cluster}", s=70)
    for _, row in subset.iterrows():
        plt.annotate(row["name"], (row["longitude"], row["latitude"]), fontsize=8, xytext=(4, 3), textcoords="offset points")
plt.xlabel("Longitude"); plt.ylabel("Latitude")
plt.title("Peta Sebaran Fasilitas (Koordinat Contoh)")
plt.legend(); plt.grid(alpha=.25); plt.tight_layout()
plt.savefig(ROOT / "facility_map.png", dpi=160)
print("\\nVisualisasi disimpan sebagai facility_map.png")
print("Catatan: koordinat adalah data sintetis untuk demonstrasi, bukan data navigasi.")
