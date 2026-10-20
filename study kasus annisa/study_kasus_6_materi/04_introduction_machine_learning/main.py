from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = load_iris(as_frame=True)
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("STUDY KASUS: Klasifikasi spesies bunga Iris")
print(f"Jumlah data: {len(X)} | fitur: {list(X.columns)}")
print(f"Akurasi test: {accuracy_score(y_test, pred):.3f}")
print("\\nLaporan klasifikasi:")
print(classification_report(y_test, pred, target_names=data.target_names))
print("Confusion matrix:")
print(confusion_matrix(y_test, pred))
print("\\nAturan model (pohon keputusan):")
print(export_text(model, feature_names=list(X.columns)))
print("\\nContoh prediksi untuk 1 baris data uji:")
print(f"Fitur: {X_test.iloc[0].to_dict()}")
print(f"Prediksi: {data.target_names[pred[0]]} | Aktual: {data.target_names[y_test.iloc[0]]}")
