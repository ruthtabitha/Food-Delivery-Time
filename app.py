import streamlit as st
import joblib
import pandas as pd

# ======================
# Load model pipeline
# ======================
@st.cache_resource
def load_model():
    return joblib.load("model_ridge_pipeline.joblib")  # sudah sesuai nama file

model = load_model()

# ======================
# Streamlit UI
# ======================
st.set_page_config(page_title="🚀 Delivery ETA Predictor", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🚴 Prediksi Waktu Pengiriman</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Masukkan detail pengirimanmu dan lihat estimasi ETA secara instan ⏱️</p>", unsafe_allow_html=True)

# Input Form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        distance = st.number_input("📍 Jarak Pengiriman (km)", min_value=0.0, step=0.1)
        prep_time = st.number_input("👨‍🍳 Waktu Persiapan (menit)", min_value=0, step=1)
        courier_exp = st.slider("🧑‍✈️ Pengalaman Kurir (tahun)", 0, 20, 2)
    with col2:
        traffic = st.selectbox("🚦 Tingkat Lalu Lintas", ["Low", "Medium", "High"])
        weather = st.selectbox("🌦️ Kondisi Cuaca", ["Clear", "Rainy", "Storm", "Fog"])
        vehicle = st.selectbox("🚗 Jenis Kendaraan", ["Motor", "Mobil"])

    st.markdown("---")
    submitted = st.form_submit_button("✨ Prediksi ETA Sekarang")

# Mapping kategorikal → sesuai pipeline
traffic_map = {"Low": "Low", "Medium": "Medium", "High": "High"}
weather_map = {"Clear": "Clear", "Rainy": "Rainy", "Storm": "Storm", "Fog": "Fog"}
vehicle_map = {"Motor": "motorbike", "Mobil": "car","Scooter": "Scooter"}

# Prediction
if submitted:
    # Buat DataFrame sesuai input
    X_new = pd.DataFrame([{
        "Distance_km": distance,
        "Preparation_Time_min": prep_time,
        "Traffic_Level": traffic_map[traffic],
        "Weather": weather_map[weather],
        "Vehicle_Type": vehicle_map[vehicle],
        "Courier_Experience": courier_exp
    }])

    # Prediksi
    pred = model.predict(X_new)

    st.success(f"⏰ Estimasi waktu pengiriman: **{pred[0]:.2f} menit**")

    st.balloons()  # 🎉 efek animasi

    st.info("Tip: Coba ubah jarak atau kondisi lalu lintas untuk lihat bagaimana ETA ikut berubah! 🚀")

