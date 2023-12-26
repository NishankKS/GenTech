# Fashion-Generative AI

## Overview

This repository contains a Python application that leverages Generative AI models from Google's GenerativeAI and Hugging Face's API. The application is built with Streamlit and includes functionality for text-based conversations and image generation.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python
- [Streamlit](https://streamlit.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [PIL](https://pypi.org/project/Pillow/)
- [requests](https://pypi.org/project/requests/)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Create a `.env` file in the root directory with the following content:

    ```ini
    GOOGLE_API_KEY=your_google_api_key
    HUGGINGFACE_API_TOKEN=your_huggingface_api_token
    HUGGINGFACE_API_URL=your_huggingface_api_url
    ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Visit http://localhost:8501 in your browser to interact with the application.

## Image Generation
The application includes an image generation tool. To use it, include #generate in your input, and the tool will create and display the generated image.

## Deployment
The Streamlit app is deployed at https://fashiongenai.streamlit.app/. Visit the link to experience the live application.
