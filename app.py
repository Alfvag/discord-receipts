from flask import Flask, request, jsonify
from pyngrok import ngrok
from escpos.printer import Network
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# Load the ngrok authtoken and printer local ip from environment variables
api_key = os.getenv("NGROK_AUTHTOKEN")
printer_ip = os.getenv("PRINTER_IP")

# Initialize the printer object
printer = Network(printer_ip, profile="TM-T88V")

# Start an ngrok tunnel
port = 5000  # Flask default port
public_url = ngrok.connect(port).public_url

# Print the url, this must be set in the webhook service
print(f"Public URL: {public_url}")


@app.route('/webhook', methods=['POST'])
def webhook():
    # Get JSON data from the request
    data = request.json

    # Check if data is valid
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Print name and message, send cut command to the printer
    printer.text(f"{data.get('name', 'Unknown')}: {data.get('message', 'No message provided')}\n")
    printer.cut()

    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(port=port)
