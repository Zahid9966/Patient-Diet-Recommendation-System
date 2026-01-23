import os
import streamlit as st
import sqlite3
from datetime import datetime

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI


os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"


def create_db():
    conn = sqlite3.connect("diet_system.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patient_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age TEXT,
            gender TEXT,
            weight TEXT,
            height TEXT,
            veg_or_nonveg TEXT,
            disease TEXT,
            region TEXT,
            state TEXT,
            allergics TEXT,
            foodtype TEXT,
            recommendation TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

create_db()

def save_to_db(data, recommendation):
    conn = sqlite3.connect("diet_system.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patient_records
        (age, gender, weight, height, veg_or_nonveg, disease, region, state, allergics, foodtype, recommendation, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data['age'], data['gender'], data['weight'], data['height'],
        data['veg_or_nonveg'], data['disease'], data['region'],
        data['state'], data['allergics'], data['foodtype'],
        recommendation,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()


generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}


model = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    generation_config=generation_config,
    verbose=True
)

prompt_template_resto = PromptTemplate(
    input_variables=[
        'age', 'gender', 'weight', 'height',
        'veg_or_nonveg', 'disease', 'region',
        'state', 'allergics', 'foodtype'
    ],
    template="""
Diet Recommendation System:

Based on the patient details below, recommend:
- 6 restaurants
- 6 breakfast items
- 5 dinner items
- 6 workout activities

Age: {age}
Gender: {gender}
Weight: {weight}
Height: {height}
Diet Preference: {veg_or_nonveg}
Disease: {disease}
Region: {region}
City/State: {state}
Allergies: {allergics}
Food Type: {foodtype}
"""
)

chain_resto = prompt_template_resto | model


st.title("PATIENT DIET RECOMMENDATION SYSTEM")

age = st.text_input("Age")
gender = st.selectbox("Gender", ["Male", "Female"])
weight = st.text_input("Weight (kg)")
height = st.text_input("Height (cm)")
veg_or_nonveg = st.selectbox("Veg or Non-Veg", ["Veg", "Non-Veg"])
disease = st.text_input("Disease")
region = st.text_input("Region")
state = st.text_input("State / City")
allergics = st.text_input("Allergics")
foodtype = st.text_input("Food Type")

if st.button("Get Recommendations"):
    if all([age, gender, weight, height, veg_or_nonveg, disease, region, state, allergics, foodtype]):

        input_data = {
            "age": age,
            "gender": gender,
            "weight": weight,
            "height": height,
            "veg_or_nonveg": veg_or_nonveg,
            "disease": disease,
            "region": region,
            "state": state,
            "allergics": allergics,
            "foodtype": foodtype
        }

       
        recommendation = chain_resto.invoke(input_data)

        st.subheader("Generated Recommendation")
        st.write(recommendation)

        
        save_to_db(input_data, recommendation)
        st.success("Patient data & recommendation saved successfully ✅")

    else:
        st.warning("Please fill all fields.")
