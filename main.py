import joblib
import numpy as np
import pandas as pd

# Load model dan encoder
model = joblib.load("decision_tree_obesitas.pkl")
label_encoder = joblib.load("label_encoder.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# Fungsi preprocessing input pengguna untuk prediksi
def preprocess_input_for_model(gender, age, height, weight, activity_level):
    # Buat DataFrame sesuai format pelatihan
    df = pd.DataFrame(columns=feature_columns)
    bmi = weight / ((height/100) ** 2)

    # Mapping manual
    data = {
        'Gender_Female': 1 if gender == "Perempuan" else 0,
        'Gender_Male': 1 if gender == "Laki-laki" else 0,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'BMI': bmi,
        'FAF': {"Rendah": 0.2, "Sedang": 1.0, "Tinggi": 2.5}[activity_level],
    }

    for col in df.columns:
        df.at[0, col] = data.get(col, 0)

    return df

# Prediksi dari model ML
if st.button("Cek Status Berat Badan dengan AI"):
    input_df = preprocess_input_for_model(gender, age, height, weight, activity_level)
    prediction = model.predict(input_df)
    label_prediksi = label_encoder.inverse_transform(prediction)[0]
    st.success(f"Model Prediksi Anda: **{label_prediksi}** 🎯")
