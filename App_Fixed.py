import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os  # ← INI YANG BENER

st.set_page_config(page_title="UMKM Pricing", page_icon="🛒")
st.title("🛒 Dynamic Pricing UMKM AI")
st.markdown("Masukkan stok & jam → Dapatkan harga otomatis!")

# CEK MODEL PAKE OS.PATH (GA ERROR)
if os.path.exists('rf_model.pkl'):
    st.success("✅ Model AI ditemukan!")
    rf = joblib.load('rf_model.pkl')
    
    # INPUT
    col1, col2 = st.columns(2)
    with col1:
        stok = st.number_input("Sisa Stok", 1, 500, 50)
    with col2:
        jam = st.slider("Jam", 0, 23, 12)
    
    if st.button("💰 PREDIKSI HARGA", type="primary"):
        X = pd.DataFrame({
            'stock_level': [stok],
            'hour': [jam],
            'day_of_week': [1],
            'category': [0]
        })
        harga = max(15000, rf.predict(X)[0] * 3000)  # Min Rp15k, realistis UMKM
        
        st.metric("Harga Optimal", f"Rp {harga:.0f}")
        if stok > 70:
            st.balloons()
            st.success(f"🎉 DISKON {((harga-20000)/20000*100):.0f}% - Stok banyak!")
        elif stok < 20:
            st.warning(f"📈 NAIK {((20000-harga)/20000*100):.0f}% - Stok kritis!")
        else:
            st.info("✅ Harga pas")
            
else:
    st.warning("⚠️ rf_model.pkl ga ketemu. Run: python train_model_fixed.py")

st.markdown("---")
st.dataframe({
    "Stok": [80, 45, 5],
    "Jam": [10, 12, 18],
    "Harga AI": ["Rp18.5k", "Rp20k", "Rp22.5k"],
    "Action": ["Diskon!", "Stabil", "Naikkan"]
})