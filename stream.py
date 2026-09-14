import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Page title
# --------------------------------------------------

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction App")

st.write(
    "This application uses a machine learning model to predict "
    "a person's diabetes status based on selected health indicators."
)


# --------------------------------------------------
# How the system works
# --------------------------------------------------

with st.expander("ℹ️ How does this system work?"):

    st.markdown("""
    ### What do I need to do?

    Enter the health information requested below. Most questions
    ask you to select an option or enter a value based on your
    health information.

    ### What does the system do?

    Once you click **Predict Diabetes Status**, the system:

    1. Takes the information you entered.
    2. Applies the same preprocessing used when training the model.
    3. Uses a **class-weighted Logistic Regression model** to make
       a prediction.
    4. Displays one of three possible results:
       - **No Diabetes**
       - **Prediabetes**
       - **Diabetes**

    ### Important

    The prediction is based on patterns learned from the training
    data. It is intended for demonstration and educational purposes
    and **should not be used as a medical diagnosis**.
    """)


st.header("Health Information")

st.write(
    "Please provide the following information as accurately as possible."
)
# --------------------------------------------------
# Load saved model and preprocessing
# --------------------------------------------------

model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("robust_scaler.pkl")
continuous_features = joblib.load("continuous_features.pkl")


# --------------------------------------------------
# Page title
# --------------------------------------------------

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction App")

st.write(
    "Enter the health information below to predict the diabetes status."
)


# --------------------------------------------------
# User inputs
# --------------------------------------------------

st.header("Health Information")


HighBP = st.selectbox(
    "Do you have High Blood Pressure?",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

HighChol = st.selectbox(
    "Do you have High Cholesterol?",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

BMI = st.number_input(
    "What is your BMI",
    min_value=10.0,
    max_value=100.0,
    value=25.0
)

Stroke = st.selectbox(
    "Do you have any history of having a stroke?",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

HeartDiseaseorAttack = st.selectbox(
    "Do you have any Heart Disease or ever gotten a Heart Attack?",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

PhysActivity = st.selectbox(
    "Have you participated in any physical activity recently?",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

GenHlth = st.slider(
    "General Health (1 = Excellent, 5 = Poor)",
    min_value=1,
    max_value=5,
    value=3
)

MentHlth = st.number_input(
    "How many days of poor Mental Health have you experienced in the last 30 days?",
    min_value=0,
    max_value=30,
    value=0
)

PhysHlth = st.number_input(
    "How many days of poor physical health have you had in the last 30 days?",
    min_value=0,
    max_value=30,
    value=0
)

DiffWalk = st.selectbox(
    "Do you have any difficulty walking?",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

Age = st.slider(
    "What is your age?",
    min_value=1,
    max_value=13,
    value=5
)

Education = st.slider(
    "What is your education level?",
    min_value=1,
    max_value=6,
    value=4
)

Income = st.slider(
    "Kindly state your income level",
    min_value=1,
    max_value=8,
    value=5
)

dual_distress = st.selectbox(
    "Any mental and physical health distress?",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

BMI_category = st.slider(
    "BMI Category",
    min_value=0,
    max_value=4,
    value=2
)

total_unhealthy_days = st.number_input(
    "Total Unhealthy Days",
    min_value=0,
    max_value=60,
    value=0
)


# --------------------------------------------------
# Create input dataframe
# --------------------------------------------------

input_data = pd.DataFrame([{
    "HighBP": HighBP,
    "HighChol": HighChol,
    "BMI": BMI,
    "Stroke": Stroke,
    "HeartDiseaseorAttack": HeartDiseaseorAttack,
    "PhysActivity": PhysActivity,
    "GenHlth": GenHlth,
    "MentHlth": MentHlth,
    "PhysHlth": PhysHlth,
    "DiffWalk": DiffWalk,
    "Age": Age,
    "Education": Education,
    "Income": Income,
    "dual_distress": dual_distress,
    "BMI_category": BMI_category,
    "total_unhealthy_days": total_unhealthy_days
}])


# --------------------------------------------------
# Apply the same preprocessing used during training
# --------------------------------------------------

input_data[continuous_features] = scaler.transform(
    input_data[continuous_features]
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Diabetes Status"):

    prediction = model.predict(input_data)[0]

    target_labels = {
        0: "No Diabetes",
        1: "Prediabetes",
        2: "Diabetes"
    }

    prediction_label = target_labels[prediction]

    st.subheader("Prediction")

    if prediction == 0:
        st.success(f"Prediction: **{prediction_label}**")

    elif prediction == 1:
        st.warning(f"Prediction: **{prediction_label}**")

    else:
        st.error(f"Prediction: **{prediction_label}**")

    st.info(
        "This prediction is generated by the machine learning model "
        "and should not be used as a medical diagnosis."
    )