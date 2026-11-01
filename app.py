import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("Resume–Job Match AI")
st.write("Paste your resume and a job description to get an AI-powered match analysis.")

resume = st.text_area("Paste your resume", height=250)
job_description = st.text_area("Paste the job description", height=250)

if st.button("Analyze Match"):
    if not resume or not job_description:
        st.warning("Please paste both your resume and the job description.")
    else:
        prompt = f"""
You are an expert technical recruiter and career coach.

Compare the resume with the job description.

Return your answer in this format:

Match Score: X/100

Matched Skills:
- skill 1
- skill 2

Missing Skills:
- skill 1
- skill 2

Resume Improvement Suggestions:
1. suggestion
2. suggestion
3. suggestion

Resume:
{resume}

Job Description:
{job_description}
"""

        model = genai.GenerativeModel("gemini-3.8-flash")
        response = model.generate_content(prompt)

        st.subheader("AI Analysis")
        st.write(response.text)