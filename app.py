import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
from PIL import Image

st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://images.unsplash.com/photo-1657035833978-996b9604a7d9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGhlYXJ0JTIwaGVhbHRoJTIwYWl8ZW58MHx8MHx8fDA%3D" width=300>
    </div>
    """,
    unsafe_allow_html=True
)

# Load data
heart_data = pd.read_csv('heart_disease_data.csv')
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# Split and train model
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Accuracy scores
training_data_accuracy = accuracy_score(model.predict(X_train), Y_train)
test_data_accuracy = accuracy_score(model.predict(X_test), Y_test)


# User Input Form
st.header("Provide Your Health Information")

sex_map = {'Female': 0, 'Male': 1}
cp_map = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-Anginal Pain': 2, 'Asymptomatic': 3}
fbs_map = {'False (<= 120 mg/dl)': 0, 'True (> 120 mg/dl)': 1}
restecg_map = {
    'Normal': 0,
    'ST-T Abnormality': 1,
    'Left Ventricular Hypertrophy': 2
}
exang_map = {'No': 0, 'Yes': 1}
slope_map = {'Downsloping': 0, 'Flat': 1, 'Upsloping': 2}
thal_map = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}

with st.form("input_form"):
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    sex = st.radio("Sex", list(sex_map.keys()))
    cp = st.selectbox("Chest Pain Type", list(cp_map.keys()))
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", list(fbs_map.keys()))
    restecg = st.selectbox("Resting ECG Result", list(restecg_map.keys()))
    thalach = st.number_input("Max Heart Rate Achieved", min_value=50, max_value=250)
    exang = st.radio("Exercise Induced Angina", list(exang_map.keys()))
    oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, step=0.1)
    slope = st.selectbox("Slope of ST Segment", list(slope_map.keys()))
    ca = st.slider("Number of Major Vessels (0–3)", min_value=0, max_value=3)
    thal = st.selectbox("Thalassemia", list(thal_map.keys()))
    
    submitted = st.form_submit_button("Predict")

    if submitted:
        input_data = np.array([
            age,
            sex_map[sex],
            cp_map[cp],
            trestbps,
            chol,
            fbs_map[fbs],
            restecg_map[restecg],
            thalach,
            exang_map[exang],
            oldpeak,
            slope_map[slope],
            ca,
            thal_map[thal]
        ]).reshape(1, -1)

        prediction = model.predict(input_data)
        if prediction[0] == 0:
            st.success("✅ This person is unlikely to have heart disease.")
        else:
            st.error("⚠️ This person is likely to have heart disease.")

# # Display info
# st.subheader("About the Dataset")
# st.write(heart_data.head())

# st.subheader("Model Performance")
# st.write(f"Training Accuracy: {training_data_accuracy:.2f}")
# st.write(f"Test Accuracy: {test_data_accuracy:.2f}")
