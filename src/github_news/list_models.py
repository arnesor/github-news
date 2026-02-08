import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


def list_models():
    client = genai.Client(api_key=GEMINI_API_KEY)
    try:
        print("Listing models...")
        for model in client.models.list(config={"page_size": 5}):
            print(f"Name: {model.name}")
            # print(dir(model)) # Uncomment to see attributes if needed
            if hasattr(model, "supported_generation_methods"):
                print(f" - Methods: {model.supported_generation_methods}")
    except Exception as e:
        print(f"Error listing models: {e}")


if __name__ == "__main__":
    list_models()
