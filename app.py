# loading env variables
import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=apikey)

# Gemini pro response
def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number]
        text += str(page.extract_text())
    return text

input_prompt = """
Act like a skilled or very experienced ATS(Application Tracking System) with a deep understanding of tech field,
software engineering, data science, data analyst and big data engineer. You task is to evaluate the resume based
on the given job description. You must consider the job market is very competitive and you should provide best assistance
for improving the resumes. Assign the percentage Matching based on Jd and the missing keywords with a high accuracy.
Resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match" : "%", "Missing Keywords : []", "Profile Summary":""}} 
"""

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Job Description")
uploaded_file = st.file_uploader("Upload Resume", type="pdf", help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)