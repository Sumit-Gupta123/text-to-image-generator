from flask import Flask, render_template, request
import openai
import os
import requests
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your environment variables

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None
    error = None

    if request.method == 'POST':
        prompt = request.form['prompt']

        try:
            response = openai.Image.create(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="1024x1024",
                quality="hd"
            )
            image_url = response['data'][0]['url']
        except Exception as e:
            error = str(e)

    return render_template('index.html', image_url=image_url, error=error)

if __name__ == '__main__':
    app.run(debug=True)
