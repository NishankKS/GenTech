# GenTech - Generative AI Based Fashion Recommendation System  

## Overview  
GenTech is an innovative fashion recommendation system powered by Generative AI. This application leverages advanced Natural Language Processing (NLP) techniques and machine learning models to deliver personalized fashion recommendations to users. The system is built using Python and integrates with cutting-edge AI models from Google's GenerativeAI and Hugging Face's API, providing an engaging and interactive experience for users.  

GenTech utilizes a chat-based interface that not only recommends fashion items based on user preferences but also offers an image generation feature to visualize recommended styles.  

## Features  
  
Text-Based Conversations: Users can interact with the system through natural language, asking for fashion recommendations or style advice.  
Personalized Style Recommendations: The application provides tailored suggestions based on individual preferences, taking into account factors such as color, fabric, occasion, and more.  
Image Generation: Users can request images of clothing items or entire outfits by including #generate in their input. The tool generates and displays visual representations of the recommended styles.  
  
## Tech Stack
Python: Main programming language used for backend development.  
LangChain: Framework for integrating large language models with external tools and APIs.  
GPT-3.5 Turbo API: OpenAI's language model used to generate personalized recommendations and responses.  
Streamlit: A powerful library for building interactive web applications with minimal code.  
Generative AI Models: Integrated through Google's GenerativeAI and Hugging Face's API for generating fashion-related content and visualizations.  
  
## How It Works
User Input: The user types a query or request (e.g., "Show me a stylish outfit for a summer day").  
Model Interaction: The application processes the query using GPT-3.5 Turbo API to generate a fashion recommendation.  
Image Generation: If the input includes #generate, the system utilizes the image generation tool to create a visual representation of the recommended fashion item or outfit.  
Display: The generated recommendation, along with the image (if requested), is shown to the user in a simple and interactive interface built with Streamlit.  

## Demo  
![295528979-dd8cf0ad-862a-488f-993a-725d835e76d4](https://github.com/user-attachments/assets/86e295e5-07bc-4de3-99f5-e5bb716c59f0)
  
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
streamlit run generative.py
```

Visit http://localhost:8501 in your browser to interact with the application.


