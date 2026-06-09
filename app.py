import streamlit as st
import pandas as pd
import joblib

model = joblib.load("cirrhosis_model.pkl")

st.set_page_config(
    page_title="Liver Cirrhosis Stage Detection",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪Liver Cirrhosis Stage Detection")


n_days = st.number_input("Number of Days", min_value=0, value=1000)
age = st.number_input("Age (Days)", min_value=0, value=20000)

bilirubin = st.number_input("Bilirubin (mg/dl)", min_value=0.0, value=2.0)
cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=0.0, value=250.0)
albumin = st.number_input("Albumin (gm/dl)", min_value=0.0, value=3.5)
copper = st.number_input("Copper (ug/day)", min_value=0.0, value=80.0)

alk_phos = st.number_input("Alkaline Phosphatase", min_value=0.0, value=1500.0)
sgot = st.number_input("SGOT", min_value=0.0, value=120.0)
triglycerides = st.number_input("Triglycerides", min_value=0.0, value=120.0)

platelets = st.number_input("Platelets", min_value=0.0, value=250.0)
prothrombin = st.number_input("Prothrombin", min_value=0.0, value=10.0)

status = st.selectbox(
    "Patient Status",
    ["Censored", "Censored due to Liver Transplant", "Death"]
)

drug = st.selectbox(
    "Drug",
    ["D-penicillamine", "Placebo"]
)

sex = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

ascites = st.selectbox(
    "Ascites Present?",
    ["No", "Yes"]
)

hepatomegaly = st.selectbox(
    "Hepatomegaly Present?",
    ["No", "Yes"]
)

spiders = st.selectbox(
    "Spiders Present?",
    ["No", "Yes"]
)

edema = st.selectbox(
    "Edema Level",
    [
        "No Edema",
        "Edema Controlled by Diuretics",
        "Edema Despite Diuretics"
    ]
)


status_map = {
    "Censored": 0,
    "Censored due to Liver Transplant": 1,
    "Death": 2
}

drug_map = {
    "D-penicillamine": 0,
    "Placebo": 1
}

sex_map = {
    "Female": 0,
    "Male": 1
}

yes_no_map = {
    "No": 0,
    "Yes": 1
}

edema_map = {
    "No Edema": 0,
    "Edema Controlled by Diuretics": 1,
    "Edema Despite Diuretics": 2
}

if st.button("Predict Stage"):

    input_data = pd.DataFrame([[
        n_days,
        status_map[status],
        drug_map[drug],
        age,
        sex_map[sex],
        yes_no_map[ascites],
        yes_no_map[hepatomegaly],
        yes_no_map[spiders],
        edema_map[edema],
        bilirubin,
        cholesterol,
        albumin,
        copper,
        alk_phos,
        sgot,
        triglycerides,
        platelets,
        prothrombin
    ]], columns=[
        'N_Days',
        'Status',
        'Drug',
        'Age',
        'Sex',
        'Ascites',
        'Hepatomegaly',
        'Spiders',
        'Edema',
        'Bilirubin',
        'Cholesterol',
        'Albumin',
        'Copper',
        'Alk_Phos',
        'SGOT',
        'Tryglicerides',
        'Platelets',
        'Prothrombin'
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🟢 Stage 1 - Early Liver Cirrhosis")
    elif prediction == 2:
        st.warning("🟡 Stage 2 - Moderate Liver Cirrhosis")
    else:
        st.error("🔴 Stage 3 - Advanced Liver Cirrhosis")