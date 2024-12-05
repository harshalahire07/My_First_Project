#import modules/libraries that we are going to use in the program
import cohere
import os
from dotenv import load_dotenv

# Get The API Key
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Initialize the Cohere client
co = cohere.Client(COHERE_API_KEY)

# Function to pass prompt to the AI model
def ai_prompt(wbc_count, rbc_count, hemoglobin_count):
    prompt = (
        f"The patient has the following blood test results:\n"
        f"- WBC count: {wbc_count}\n"
        f"- RBC count: {rbc_count}\n"
        f"- Hemoglobin count: {hemoglobin_count} g/dL\n"
        f"Based on these values, provide a short 300 words analysis of possible conditions or diseases. "
        
    )

    diagnose = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=400, 
        temperature=0.7,
    )

    return diagnose.generations[0].text.strip()

def ai_response():
    print("Welcome to Doctor Precaution")
    wbc_count = input("Enter WBC count: ")
    rbc_count = input("Enter RBC count: ")
    hemoglobin_count = input("Enter Hemoglobin count (g/dL): ")

    diagnosis = ai_prompt(wbc_count, rbc_count, hemoglobin_count)
    print(f"""
Diagnosis based on the report: 
{diagnosis}

Please consult a doctor. Do not rely solely on the AI response!
""")


ai_response()
