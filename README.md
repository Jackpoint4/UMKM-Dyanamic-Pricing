# 🛒 Dynamic Pricing UMKM AI by Jackpoint4

[![Streamlit]([https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://umkm-jackpoint4.streamlit.app](https://umkm-dyanamic-pricing-zmda7z6cn5zw3xngteppdx.streamlit.app/))
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![AI](https://img.shields.io/badge/AI-Random%20Forest-orange)](https://scikit-learn.org)

**Sistem Penentuan Harga Dinamis Otomatis** untuk UMKM Indonesia. AI belajar dari data penjualan → rekomendasi harga real-time berdasarkan **stok + jam + hari**.

## 🎮 **DEMO LIVE**
https://umkm-jackpoint4.streamlit.app

## 📱 **Fitur**
🔹 Input: Sisa stok, jam transaksi, hari

🔹 Output: Harga Rp15.000-Rp25.000 + saran

🔹 Rekomendasi: Diskon/Stabil/Naikkan harga

🔹 Mobile friendly - HP/Laptop OK

🔹 Akurasi: R² 0.88 (target dokumen)

## 🏗️ **Cara Kerja AI**
Stok 80 jam 10:00 → "Rp18.500 - DISKON!"
Stok 5 jam 18:00 → "Rp22.500 - NAIK!"
Stok 45 jam 12:30 → "Rp20.000 - STABIL"


**Feature Importance (Dokumen Target)**:
- 🥇 Sisa Stok: **45%**
- 🥈 Jam Transaksi: **30%** 
- 🥉 Hari: **15%**
- 📦 Kategori: **10%**

## 📂 **Files**
| File | Fungsi |
|------|--------|
| `App_Fixed.py` | Web app Streamlit |
| `rf_model.pkl` | Model Random Forest |
| `requirements.txt` | Dependencies |

## 🚀 **Deploy Streamlit Cloud**
share.streamlit.io → GitHub login

New app → Jackpoint4/umkm-dynamic-pricing-ai

Main file: App_Fixed.py

Deploy → LIVE!


## 🗃️ **Dataset**
[Online Retail UCI - Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)

---
**Made with by Jackpoint4 (Jakarta, ID)**  
**Untuk UMKM Indonesia 🇮🇩**
