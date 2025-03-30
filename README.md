# Discord Receipts

A Flask-based local web service that prints Discord messages to a thermal receipt printer via webhooks.

## Overview

- Exposes a webhook endpoint using ngrok
- Receives messages from Discord via webhooks
- Prints the messages to a connected thermal receipt printer

## Webhooks

- I tested it using Zapiers free tier which works fine
- Set it up so that it sends a POST request to the ngrok link generated on startup. The payload should be JSON and contain:
``` JSON
    "data": [
        {
            "name": String,
            "message": String
        }
    ]
```

## Prerequisites

- Python 3.6+
- Packages: flask, python-escpos, python-dotenv
- Network-connected thermal receipt printer (compatible with ESC/POS). Could easily be rewritten to use USB or Serial
- ngrok account (for the authentication token)

## Installation & running

1. Clone the repository:
   ```bash
   git clone https://github.com/AlexanderAlfvag/discord-receipts.git
   cd discord-receipts

2. Install dependencies:
    ```python
    pip install flask pyngrok python-escpos python-dotenv

3. Environment variables

    Create a .env file in the root directory that contains the following:
    ```env
    NGROK_AUTHTOKEN="" # Auth token provided by Ngrok
    PRINTER_IP="" # The local IP of your printer

4. Run:
    ```python
    flask run

5. (Optional) provide ngrok link

    If you use ngrok's free tier, the link will be randomly generated on each startup, copy the provided link and use that as the webhook endpoint

## Have fun!