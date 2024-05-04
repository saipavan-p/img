import google.generativeai as genai
from dotenv import load_dotenv
import os

dotenv_path = '.env'
load_dotenv(dotenv_path)

# API_KEY = "AIzaSyCkvI4TK4q6LmVpTCzvlIo3ulp7rlYBMbk"
API_KEY = os.environ.get('G_API_KEY')
genai.configure(api_key=API_KEY)

def process_image_and_generate_text(image_path):
    sample_file = genai.upload_file(path=image_path, display_name="Sample drawing")
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    response = model.generate_content(["Give a detailed description about the image in 20-25 lines", sample_file])

    response_data = {
        "generated_text": response.text,
        "image_path": image_path,
        "model_version": "gemini-1.5-pro-latest"
    }

    return response_data


def process_image_and_generate_obj_name(image_path):
    sample_file = genai.upload_file(path=image_path, display_name="Sample drawing")
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    response = model.generate_content(["Identify the image and give the name as output.", sample_file])

    response_data = {
        "generated_text": response.text,
        "image_path": image_path,
        "model_version": "gemini-1.5-pro-latest"
    }

    return response_data










