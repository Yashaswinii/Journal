import streamlit as st
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Set up the page configuration for a better presentation
st.set_page_config(page_title="SoulScribe", layout="centered")

# Define the main page
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Journaling", "Weekly Report"])

    if page == "Home":
        home_page()
    elif page == "Journaling":
        journaling_page()
    elif page == "Weekly Report":
        weekly_report_page()

def home_page():
    # Custom CSS for the overall aesthetic
    st.markdown("""
        <style>
            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(-20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
            
            .animated-title {
                font-family: 'Poppins', sans-serif;
                font-size: 64px;
                font-weight: bold;
                color: #fdf7e3;
                text-align: center;
                margin-top: 40px;
                animation: fadeIn 2s ease-in-out;
            }

            .message-box {
                font-family: 'Georgia', serif;
                font-size: 24px;
                color: #333;
                background-color: #f0d6d2;
                padding: 20px;
                border-radius: 12px;
                text-align: center;
                margin-top: 20px;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
            }

            .question {
                font-family: 'Poppins', sans-serif;
                font-size: 28px;
                color: #f5f5f5;
                text-align: center;
                margin-top: 30px;
            }

            .stButton > button {
                background-color: #5a5a5a;
                color: white;
                border: none;
                padding: 15px 30px;
                border-radius: 30px;
                font-size: 18px;
                margin: 10px;
                cursor: pointer;
                transition: background-color 0.3s;
            }

            .stButton > button:hover {
                background-color: #777;
                color: #f5f5f5;
            }
        </style>
    """, unsafe_allow_html=True)

    # Display the animated title
    st.markdown("""
    <div class="animated-title">
        SoulScribe.
    </div>
    """, unsafe_allow_html=True)

    # Display the aesthetic message box
    st.markdown("""
    <div class="message-box">
        Take a deep breath and think about today’s journey. Each moment contributed to who you are. Unwind with peace and gratitude.
    </div>
    """, unsafe_allow_html=True)

    # Display the question asking about the user's day
    st.markdown("""
    <div class="question">
        How's your day going?
    </div>
    """, unsafe_allow_html=True)

    # Display the buttons and responses
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("YAYY"):
            st.balloons()  # Celebrate with balloons
            st.success("That's wonderful! Keep spreading your joy and positivity!")

    with col2:
        if st.button("NAYY"):
            st.info("It's okay. Take this moment to rest and remind yourself that tomorrow is a new day. You’re doing great.")

def journaling_page():
    # Custom CSS for the options
    st.markdown("""
        <style>
            .option-box {
                background-color: #f0d6d2;
                border-radius: 12px;
                padding: 40px;
                margin: 20px;
                text-align: center;
                font-size: 24px;
                font-family: 'Poppins', sans-serif;
                cursor: pointer;
                transition: transform 0.3s, box-shadow 0.3s;
            }
            .option-box:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            }
        </style>
    """, unsafe_allow_html=True)

    st.write("Choose an option:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Journaling"):
            st.session_state.page = "Journaling"

    with col2:
        if st.button("Emotional Scoring"):
            st.session_state.page = "Emotional Scoring"

    if "page" in st.session_state:
        if st.session_state.page == "Journaling":
            journaling_form()
        elif st.session_state.page == "Emotional Scoring":
            emotional_scoring_page()

def journaling_form():
    st.write("Welcome back Jake! Take a moment to unwind and reflect on your day. Every experience, big or small, is a step forward. Let your thoughts flow, and end today with gratitude and peace. You deserve this moment of calm.")

    # Date Picker
    date = st.date_input("Select a date", datetime.now(), key="journal_date")

    # Journal Entry Box
    journal_entry = st.text_area("How was your day?", height=200, key="journal_entry")

    # Submit Button
    if st.button("Submit"):
        # Placeholder for sentiment analysis
        sentiment = "Neutral"  # This should be replaced with actual sentiment analysis
        st.success(f"Entry submitted! Your mood today is: {sentiment}")

def emotional_scoring_page():
    st.write("Emotional Scoring page content goes here.")

def weekly_report_page():
    # Weekly Emotion Report Section
    st.write("Weekly Emotion Report goes here.")

if __name__ == "_main_":
    main()
    
