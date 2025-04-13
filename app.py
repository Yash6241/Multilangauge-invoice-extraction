import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

# ✅ Move this to the top
st.set_page_config(page_title="MultiLanguage Invoice Extractor")

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Use a supported model (Try 'gemini-1.5-pro' or 'gemini-1.5-flash')
MODEL_NAME = "gemini-1.5-pro"

def get_gemini_response(input_text, image, prompt):
    """Generates a response using Gemini AI."""
    try:
        model = genai.GenerativeModel(MODEL_NAME)  # ✅ Updated model name
        response = model.generate_content([input_text, image[0], prompt])
        return response.text
    except Exception as e:
        return f"Error in API call: {e}"

def input_image_setup(uploaded_file):
    """Prepares the uploaded image for Gemini API."""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI
st.header("Multilanguage Invoice Extractor")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

# Display uploaded image
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

submit = st.button("Extract Invoice Details")

input_prompt = """
You are an expert in understanding invoices. We will upload an image of an invoice, 
and you will have to answer any questions based on the uploaded invoice image.
"""

# If submit button is clicked
if submit and uploaded_file:
    try:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_text, image_data, input_prompt)
        st.subheader("Extracted Invoice Details:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")


