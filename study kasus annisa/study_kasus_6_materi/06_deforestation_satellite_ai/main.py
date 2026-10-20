from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

ROOT = Path(__file__).parent
df = pd.read_csv(ROOT / "data" / "deforestation_alerts.csv")
target = "driver"
X = df.drop(columns=[target, "alert_id"])
y = df[target]
categorical = ["land_cover", "nearby_activity"]
numeric = ["alert_area_ha", "distance_to_road_km", "distance_to_settlement_km", "ndvi_change"]

preprocess = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
    ("num", "passthrough", numeric),
])
model = Pipeline([
    ("preprocess", preprocess),
    ("classifier", RandomForestClassifier(n_estimators=150, random_state=42, class_weight="balanced"))
])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("PROTOTIPE ATRIBUSI PENYEBAB ALERT DEFORESTASI")
print(f"Jumlah sampel sintetis: {len(df)}")
print(f"Akurasi evaluasi: {accuracy_score(y_test, pred):.3f}")
print("\\nLaporan klasifikasi:")
print(classification_report(y_test, pred, zero_division=0))
print("\\nContoh hasil prediksi:")
example = X_test.iloc[[0]]
print(example.to_string(index=False))
print("Prediksi driver:", model.predict(example)[0])
print("\\nPeringatan: label dan fitur dibuat sintetis untuk pembelajaran.")
print("Penggunaan nyata membutuhkan citra satelit tervalidasi, ground truth, analisis ahli,")
print("pengujian bias, serta verifikasi lapangan. Model ini tidak membuktikan penyebab.")
