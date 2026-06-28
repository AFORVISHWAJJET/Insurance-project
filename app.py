import streamlit as st
import pickle as pkl
import pandas as pd

 

st.set_page_config(
    page_title="Insurance Premium Prediction",
    page_icon="🏥",
    layout="centered"
)



model = pkl.load(open("model.pkl", "rb"))


st.title("🏥 Insurance Premium Prediction System")
st.write("Enter the details below to predict the insurance charges.")


age = st.number_input(
    "Enter Age",
    min_value=18,
    max_value=100,
    value=25,
    step=1
)

sex = st.selectbox(
    "Select Gender",
    ["male", "female"]
)

bmi = st.number_input(
    "Enter BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0,
    step=0.1
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0,
    step=1
)

smoker = st.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.selectbox(
    "Region",
    [
        "northeast",
        "northwest",
        "southeast",
        "southwest"
    ]
)

if st.button("Predict Insurance Charges"):

    data = [[
        age,
        sex,
        bmi,
        children,
        smoker,
        region
    ]]

    columns = [
        "age",
        "sex",
        "bmi",
        "children",
        "smoker",
        "region"
    ]

    df = pd.DataFrame(data, columns=columns)

    prediction = model.predict(df)

    st.success(
        f"Predicted Insurance Charges: ₹ {prediction[0]:,.2f}"
    )

    st.write("### Input Summary")
    st.dataframe(df)