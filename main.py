import streamlit as st

# Judul aplikasi
st.title("🩺 Aplikasi Deteksi Obesitas ")
st.write("Aplikasi ini membantu Anda mengklasifikasikan status berat badan berdasarkan BMI (Body Mass Index).")

# Input pengguna
gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
age = st.number_input("Umur (tahun)", min_value=1, max_value=120, value=25)
height = st.number_input("Tinggi Badan (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Berat Badan (kg)", min_value=30, max_value=200, value=70)
activity_level = st.selectbox("Tingkat Aktivitas Fisik", ["Rendah", "Sedang", "Tinggi"])

# Fungsi menghitung BMI dan klasifikasi
def hitung_bmi(berat, tinggi_cm):
    tinggi_m = tinggi_cm / 100
    bmi = berat / (tinggi_m ** 2)
    return round(bmi, 2)

def klasifikasi_bmi(bmi):
    if bmi < 18.5:
        return "Kurus", "⚠️"
    elif 18.5 <= bmi < 25:
        return "Normal", "✅"
    elif 25 <= bmi < 30:
        return "Overweight", "⚠️"
    else:
        return "Obesitas", "❗"

# Tombol prediksi
if st.button("Cek Status Berat Badan"):
    bmi = hitung_bmi(weight, height)
    kategori, emoji = klasifikasi_bmi(bmi)
    st.subheader("Hasil:")
    st.write(f"**BMI Anda:** {bmi}")
    st.write(f"**Kategori:** {kategori} {emoji}")

    # Saran berdasarkan hasil
    if kategori == "Obesitas":
        st.warning("Anda berada dalam kategori obesitas. Disarankan untuk berkonsultasi dengan ahli gizi dan memperbaiki pola makan serta olahraga.")
    elif kategori == "Overweight":
        st.info("Anda sedikit kelebihan berat badan. Jaga pola makan dan tambahkan aktivitas fisik.")
    elif kategori == "Kurus":
        st.info("Berat badan Anda di bawah normal. Konsultasikan dengan ahli gizi untuk pola makan yang lebih seimbang.")
    else:
        st.success("Berat badan Anda normal. Pertahankan gaya hidup sehat! 💪")
