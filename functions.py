from PIL import Image
import os, io
import requests
#from diffusers import StableDiffusionPipeline
#import torch
from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables


i = 1

def query(payload):
    API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
    API_URL = os.getenv('HUGGINGFACE_API_URL')
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def generate_image(prompt):
    image_bytes = query({
            "inputs": prompt, 
            "wait_for_model": True,
        })
    g = Image.open(io.BytesIO(image_bytes))
    image_path = f'./Assets/response_{globals()["i"]}.png'
    g.save(image_path)
    globals()["i"] += 1
    return image_path





if __name__ == '__main__':
    img_path = generate_image("Black shirt and white pant")
    #by_diffusers()
    print(img_path)
