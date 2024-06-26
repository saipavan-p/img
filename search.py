import requests
import os 
from dotenv import load_dotenv

dotenv_path = '.env'
load_dotenv(dotenv_path)

# API_key = "AIzaSyBHQghHp4b6DdrlAftGluFOe6a6WQQpAn0"
# Engine_id = "8588cd97367ec4721"

API_key = os.environ.get('CSE_API_key')
Engine_id = os.environ.get('Engine_id')

def search_using_pse(keyword, api_key=API_key, engine_id=Engine_id):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": engine_id,
        "q": keyword
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return [item["link"] for item in data["items"]]
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
