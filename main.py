from fastapi import FastAPI, HTTPException
from google.cloud import translate_v2 as translate
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize Google Translate client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("service-account-key.json")
translate_client = translate.Client()

# Request model
class TranslationRequest(BaseModel):
    text: str
    target_language: str

# Translation endpoint
@app.post("/translate")
def translate_text(request: TranslationRequest):
    try:
        result = translate_client.translate(
            request.text, target_language=request.target_language
        )
        return {
            "translated_text": result["translatedText"],
            "source_language": result["detectedSourceLanguage"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

print(os.path.exists(os.path.abspath("service-account-key.json")))