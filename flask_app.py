from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file (for local development or Docker)
load_dotenv()

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Model initialization
model = genai.GenerativeModel("gemini-1.0-pro-latest")

app = Flask(__name__)

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# API route
@app.route("/api", methods=["POST"])
def api():
    message = request.form.get("message")

    if not message:
        return "No message provided", 400

    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}", 500


# Optional fallback for 404s
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
