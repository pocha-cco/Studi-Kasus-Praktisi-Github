# Paket 6 Study Kasus Materi Data, AI, HPC, GIS, HCI

Repositori ini berisi enam mini-project yang dapat dijalankan dan dikembangkan untuk tugas kuliah.

## Daftar proyek
1. `01_analytics_ai` — analisis dan prediksi baseline omzet.
2. `02_hpc_local_challenges` — perbandingan komputasi serial vs paralel untuk simulasi data sensor.
3. `03_gis_career_competition` — pemetaan sebaran fasilitas dan clustering koordinat.
4. `04_introduction_machine_learning` — klasifikasi dataset Iris.
5. `05_hci_data_visualization` — dashboard interaktif pengalaman pengguna.
6. `06_deforestation_satellite_ai` — prototipe klasifikasi driver alert deforestasi berbasis fitur sintetis.

## Menjalankan
Masuk ke folder proyek, instal `requirements.txt`, lalu ikuti README proyek. Setiap proyek memiliki dependensi sendiri.

Contoh:
```bash
cd 01_analytics_ai
pip install -r requirements.txt
python main.py
```

Dashboard:
```bash
cd 05_hci_data_visualization
pip install -r requirements.txt
streamlit run app.py
```

## Upload ke GitHub
1. Ekstrak ZIP.
2. Buat repository baru di GitHub.
3. Upload folder dan file di dalam `study_kasus_6_materi` (atau jalankan git dari folder ini).
4. Untuk menggunakan Git:
```bash
git init
git add .
git commit -m "Add six study case projects"
git branch -M main
git remote add origin https://github.com/USERNAME/NAMA-REPO.git
git push -u origin main
```
Ganti URL remote dengan URL repository milik Anda.

## Batasan
Data contoh bersifat sintetis dan ditujukan untuk pembelajaran. Khusus proyek deforestasi, kode ini tidak memproses citra satelit mentah dan tidak dapat memastikan penyebab deforestasi di dunia nyata.
