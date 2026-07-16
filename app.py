import streamlit as st
import joblib
import pandas as pd
import os
from datetime import datetime


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Smart Crop Recommendation AI",
    page_icon="🌱",
    layout="wide"
)


# -------------------------------------------------
# Load ML Model
# -------------------------------------------------

@st.cache_resource
def load_model():

    model = joblib.load(
        "models/best_crop_model.pkl"
    )

    encoder = joblib.load(
        "models/label_encoder.pkl"
    )

    return model, encoder


model, encoder = load_model()



# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("🌱 Smart Crop Recommendation AI Agent")

st.markdown(
"""
### AI-powered farming assistant

This system recommends the most suitable crop
based on soil nutrients and environmental conditions.

**Analyzed Parameters**

✔ Nitrogen  
✔ Phosphorus  
✔ Potassium  
✔ Soil pH  
✔ Temperature  
✔ Humidity  
✔ Rainfall  

"""
)


st.divider()



# -------------------------------------------------
# Sidebar
# -------------------------------------------------

st.sidebar.header("👨‍🌾 Farmer Details")


farmer_name = st.sidebar.text_input(
    "Farmer Name"
)


location = st.sidebar.text_input(
    "Location"
)


st.sidebar.info(
"""
The AI model helps farmers
select suitable crops using
machine learning.
"""
)



# -------------------------------------------------
# Input Section
# -------------------------------------------------

st.subheader(
    "🌍 Enter Soil and Climate Information"
)



col1, col2, col3 = st.columns(3)



with col1:

    nitrogen = st.number_input(
        "Nitrogen (N)",
        min_value=0,
        max_value=200,
        value=50
    )


    phosphorus = st.number_input(
        "Phosphorus (P)",
        min_value=0,
        max_value=200,
        value=40
    )


    potassium = st.number_input(
        "Potassium (K)",
        min_value=0,
        max_value=200,
        value=40
    )



with col2:

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=50.0,
        value=25.0
    )


    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )



with col3:

    ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5
    )


    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=300.0,
        value=100.0
    )



st.divider()



# -------------------------------------------------
# Prediction
# -------------------------------------------------

if st.button(
    "🌾 Recommend Best Crop",
    use_container_width=True
):


    input_data = pd.DataFrame(
        [[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    )


    prediction = model.predict(
        input_data
    )


    crop = encoder.inverse_transform(
        prediction
    )[0]


    # Confidence

    probabilities = model.predict_proba(
        input_data
    )


    confidence = max(
        probabilities[0]
    ) * 100



    # -------------------------------------------------
    # Result Dashboard
    # -------------------------------------------------

    st.success(
        f"🌱 Recommended Crop: {crop.upper()}"
    )


    c1,c2,c3 = st.columns(3)


    with c1:

        st.metric(
            "🌾 Crop",
            crop.upper()
        )


    with c2:

        st.metric(
            "🎯 Confidence",
            f"{confidence:.2f}%"
        )


    with c3:

        st.metric(
            "🌡 Temperature",
            f"{temperature} °C"
        )



    st.divider()



    # -------------------------------------------------
    # Farming Recommendations
    # -------------------------------------------------

    st.subheader(
        "🌿 AI Farming Recommendations"
    )


    crop_tips = {


        "rice":[
            "Maintain proper water level in fields",
            "Apply nitrogen fertilizer during growth stage",
            "Monitor pests regularly"
        ],


        "cotton":[
            "Avoid excessive irrigation",
            "Maintain soil moisture",
            "Control weeds regularly"
        ],


        "maize":[
            "Provide adequate sunlight",
            "Use balanced fertilizer",
            "Maintain proper spacing"
        ],


        "default":[
            "Perform regular soil testing",
            "Use recommended fertilizers",
            "Monitor crop health"
        ]

    }



    tips = crop_tips.get(
        crop.lower(),
        crop_tips["default"]
    )



    for tip in tips:

        st.write(
            "✅",
            tip
        )



    st.divider()



    # -------------------------------------------------
    # Save History
    # -------------------------------------------------

    os.makedirs(
        "logs",
        exist_ok=True
    )


    history_file = "logs/history.csv"



    new_record = pd.DataFrame(
        [{
            "Date":
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "Farmer":
            farmer_name,

            "Location":
            location,

            "Crop":
            crop,

            "Confidence":
            round(confidence,2)
        }]
    )



    if os.path.exists(history_file):

        old_data = pd.read_csv(
            history_file
        )

        final_data = pd.concat(
            [
                old_data,
                new_record
            ],
            ignore_index=True
        )


    else:

        final_data = new_record



    final_data.to_csv(
        history_file,
        index=False
    )



    st.info(
        "📌 Prediction saved successfully"
    )