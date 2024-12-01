# Translation API

A FastAPI-based translation service that leverages Google Cloud Translation API to translate text between different languages. This project demonstrates proficiency in API integration, cloud services, and backend development.

## Overview

The Translation API allows users to:
- Translate text from one language to another.
- Automatically detect the source language of the input text.
- Specify the target language for translation.

This project is designed for job application purposes and highlights key backend development skills using FastAPI and Google Cloud Platform.

## Features

- **Text Translation**: Translate text between multiple languages with ease.
- **Automatic Language Detection**: Automatically detects the language of the input text.
- **Error Handling**: Returns informative error messages for invalid requests or unsupported languages.
- **Swagger Documentation**: Explore and test the API through Swagger UI.

## Tech Stack

- **FastAPI**: A modern, fast (high-performance) web framework for Python.
- **Google Cloud Translation API**: Provides powerful translation capabilities.
- **Python-dotenv**: For managing environment variables securely.
- **Uvicorn**: ASGI server for running FastAPI apps.

## API Endpoints

### Translate Text
- **URL**: `/translate`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "text": "こんにちは",
    "target_language": "en"
  }
  ```
- **Response Example**
  ```json
  {
    "translated_text": "Hello",
    "source_language": "ja"
  }
  ```

## Setup Instructions
1. **Clone the Repository:**
  ```bash
  git clone https://github.com/yourusername/translation_app.git
  cd translation_app
  ```
2. **Install Dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
3. **Set up Google Cloud API:**
- Enable the **Google Cloud Translation API** in your GCP project.
- Navigate to the **Credentials** tab in GCP and create a service account key.
- Download the service account key JSON file.
- Place the JSON file in the project directory and name it `service-account-key.json`.
4. **Run the Application:**
  ```bash
  uvicorn main:app --reload
  ```
5. **Access the API Documentation:**
- Open your browser and navigate to `http://127.0.0.1:8000/docs`.

---

## How to Use
- Send a POST request to `/translate` with a JSON body containing the text and target language.
- The API will return the translated text along with the detected source language.
Future Improvements

---

## Future Improvements
This project can be further enhanced with additional features:
- Add user authentication for enhanced security.
- Support batch translation for multiple text inputs.
- Integrate with Docker for easier deployment and scalability.
- Expand API to support other Google Cloud services like Speech-to-Text.