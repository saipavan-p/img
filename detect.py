import google.generativeai as genai
import os

API_KEY = "AIzaSyCkvI4TK4q6LmVpTCzvlIo3ulp7rlYBMbk"
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










