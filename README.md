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

Create a key in [Google AI Studio](https://aistudio.google.com/) and provide it in **one** of these ways (checked in this order):

- an environment variable: `export GOOGLE_API_KEY="your_key_here"`
- a `.env` file next to `app.py` containing `GOOGLE_API_KEY=your_key_here` (the file is git-ignored)
- a Streamlit secret named `GOOGLE_API_KEY` (for example on Streamlit Community Cloud: Settings → Secrets)

Never commit your key. If the key is missing, the app shows an error instead of starting.

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

🔒 Data & Privacy

Each submitted patient record is stored in plain text in a local SQLite file, `diet_system.db`, created next to `app.py`. The file is git-ignored; keep it that way, and do not publish or share it, because it contains health information. Patient details are also sent to Google's Gemini API to generate the recommendation.
