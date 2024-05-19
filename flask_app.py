
from flask import Flask, render_template, request

import google.generativeai as genai


GOOGLE_API_KEY = ""

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.0-pro-latest')


app = Flask(__name__)



# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.form.get("message")
    content = model.generate_content(message)
    return content.text


if __name__=='__main__':
    app.run()


