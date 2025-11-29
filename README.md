🩺 Patient Diet Recommendation System

A smart diet recommendation system built using Python, Machine Learning, LangChain, Google Generative AI, and Streamlit.
It analyzes patient details, medical conditions, allergies, and preferences to generate personalized meal plans.

🚀 Features

🧠 AI-generated diet plans using Google Generative AI (Gemini)

🍽️ Personalized meals based on:

Age, gender, height, weight

BMI

Diseases (Diabetes, BP, Obesity, etc.)

Allergies

Food preferences

📊 Calorie & nutrient estimation

⚡ Real-time response using LangChain

🌐 User-friendly web app built with Streamlit

📁 Export recommendations (optional future enhancement)

🛠️ Tech Stack
Frontend

Streamlit (UI)

Backend

Python

LangChain

Google Generative AI (Gemini)

Libraries

NumPy

Pandas

TensorFlow (optional ML components)

LangChain

Streamlit

google-generativeai

📂 Project Structure
Patient-Diet-Recommendation-System/
│── app.py                # Main Streamlit app
│── model/                # Any ML model files
│── utils/                # Helper scripts
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
│── assets/               # Images or UI assets

▶️ How to Run the Project
1. Install Dependencies
pip install -r requirements.txt

2. Add Your API Key

Create a .env file:

GOOGLE_API_KEY=your_key_here

3. Run Streamlit App
streamlit run app.py

🤖 How the AI Works

The system uses:

LangChain to structure prompts

Google Gemini to generate diet recommendations

Nutritional logic to calculate BMI and calorie needs

It sends:

Patient details + preferences → LangChain prompt → Gemini → Final diet plan

📈 Future Enhancements

Integration with Firebase or MongoDB

Mobile app version

Food image recognition

PDF export for diet charts

Multi-language support

🙌 Contributors

Zahid Shaikh – Developer
