from flask import Flask, request, jsonify
from pyngrok import ngrok
from escpos.printer import Network
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# Load the ngrok authtoken from environment variables
api_key = os.getenv("NGROK_AUTHTOKEN")

# Start an ngrok tunnel
port = 5000  # Flask default port
public_url = ngrok.connect(port).public_url
print(f"Public URL: {public_url}")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Get JSON data from POST request
    print(f"Received webhook data: {data}")
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(port=port)
