import streamlit as st

# Judul aplikasi
st.title("🩺 Aplikasi Deteksi Obesitas ")


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

# Fungsi saran berdasarkan kondisi
def saran_personalisasi(kategori, gender, age, activity_level):
    saran = ""
    if kategori == "Obesitas":
        saran = "Anda berada dalam kategori obesitas. "
        if activity_level == "Rendah":
            saran += "Tingkatkan aktivitas fisik secara bertahap, seperti berjalan kaki setiap hari selama 30 menit. "
        elif activity_level == "Sedang":
            saran += "Pertimbangkan untuk meningkatkan durasi atau intensitas olahraga Anda. "
        else:
            saran += "Meski aktif, pola makan Anda mungkin perlu diperbaiki. "
        saran += "Konsultasikan dengan ahli gizi untuk rencana diet yang sesuai."
    elif kategori == "Overweight":
        saran = "Anda sedikit kelebihan berat badan. "
        if age < 30:
            saran += "Manfaatkan usia muda untuk membentuk kebiasaan sehat. "
        else:
            saran += "Jaga pola makan dan perbanyak aktivitas ringan seperti bersepeda atau berenang. "
        if gender == "Perempuan":
            saran += "Perhatikan hormon dan kebutuhan nutrisi harian."
    elif kategori == "Kurus":
        saran = "Berat badan Anda di bawah normal. "
        if activity_level == "Tinggi":
            saran += "Mungkin Anda membakar lebih banyak kalori dari yang dikonsumsi. Tambahkan asupan makanan bergizi. "
        else:
            saran += "Perbanyak konsumsi makanan tinggi kalori sehat seperti alpukat, kacang-kacangan, dan susu. "
        if age < 18:
            saran += "Konsultasi dengan dokter penting karena masa pertumbuhan."
    else:
        saran = "Berat badan Anda normal. Pertahankan gaya hidup sehat! 💪"
        if activity_level == "Rendah":
            saran += "Cobalah aktif minimal 3x seminggu agar tubuh tetap fit."

    return saran

# Tombol prediksi
if st.button("Cek Status Berat Badan"):
    bmi = hitung_bmi(weight, height)
    kategori, emoji = klasifikasi_bmi(bmi)
    st.subheader("Hasil:")
    st.write(f"**BMI Anda:** {bmi}")
    st.write(f"**Kategori:** {kategori} {emoji}")

    # Saran berdasarkan hasil
    saran = saran_personalisasi(kategori, gender, age, activity_level)
    st.info(saran)
