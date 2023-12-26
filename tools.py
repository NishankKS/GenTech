from langchain.tools import BaseTool
from PIL import Image
import io,os,requests


i = 1
class ImageGenerationTool():
    name = "Image generator"
    description = "This tool is designed to generate images based on user input. Provide a prompt or description of the desired image, and include #generate in your request." \
                  "The tool will create and return the generated image file path." \
                  "Perfect for scenarios where you need custom images tailored to your specifications."

    def run(self, prompt, API_TOKEN, API_URL):
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        payload = {
            "inputs": prompt,
            "wait_for_model": True,
        }
        response = requests.post(API_URL, headers=headers, json=payload)

        g = Image.open(io.BytesIO(response.content))
        image_path = f'./response_{globals()["i"]}.png'
        g.save(image_path)
        globals()["i"] += 1
        return image_path

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")


