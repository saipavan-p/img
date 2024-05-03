import google.generativeai as genai
import os

# Configure GenAI with API key
API_KEY = "AIzaSyCkvI4TK4q6LmVpTCzvlIo3ulp7rlYBMbk"
genai.configure(api_key=API_KEY)

def process_image_and_generate_text(image_path):
    # Upload image to GenAI
    sample_file = genai.upload_file(path=image_path, display_name="Sample drawing")

    # Set the model to Gemini 1.5 Pro
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

    # Generate text based on the image
    response = model.generate_content(["Give a detailed description about the image in 20-25 lines", sample_file])

    # Construct response data
    response_data = {
        "generated_text": response.text,
        "image_path": image_path,
        "model_version": "gemini-1.5-pro-latest"
    }

    return response_data
