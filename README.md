# UMKM-Dyanamic-Pricing
# 🛒 Dynamic Pricing UMKM AI

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://umkmpricing.streamlit.app)

Sistem AI **Penentuan Harga Dinamis** untuk UMKM Indonesia menggunakan **Random Forest Regressor**. Otomatis hitung harga optimal berdasarkan **sisa stok, jam, hari**.

## 🎯 Fitur
- Input real-time: Stok, jam, hari
- Output: Harga Rp + rekomendasi (Diskon/Naik/Stabil)
- Akurasi tinggi: R² 0.88
- Mobile-friendly

## 📊 Demo
<img width="1353" height="623" alt="Screenshot 2026-03-26 185857" src="https://github.com/user-attachments/assets/a643226e-ccad-4df4-affd-7b8d6ccb339a" />


## 🚀 Deploy Live
https://umkmpricing.streamlit.app

## 🛠️ Tech Stack
Streamlit - Python - Scikit-Learn - Pandas - Joblib - Random Forest

## 📈 Cara Kerja
Train model dari data penjualan (stok, jam, harga)

Input: Stok 80 jam 10 → Output: "Rp18.500 DISKON!"

Feature Importance: Stok(45%) > Jam(30%) > Hari(15%)

## 🗄️ Files
| File | Deskripsi |
|------|-----------|
| `App_Fixed.py` | Web app Streamlit |
| `rf_model.pkl` | Model AI trained |
| `requirements.txt` | Dependencies |

## 📥 Setup Lokal
pip install -r requirements.txt
streamlit run App_Fixed.py

## 📚 Dataset
[Online Retail UCI - Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)

## 📝 Referensi
Dokumen: [UMKM-Help-Docs.pdf](UMKM-Help-Docs.pdf)

---
⭐ Star kalau berguna! Made by Night Watch (Jakarta)  
💬 [Discuss](https://github.com/nightwatch/umkm-pricing/discussions)
