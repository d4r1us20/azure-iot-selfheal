import json
import requests
import logging
import os

def main(event: dict) -> None:
    data = json.loads(event.get_body().decode('utf-8'))
    logging.info(f"Received: {data}")

    endpoint = os.environ["ML_ENDPOINT"]
    key = os.environ["ML_KEY"]

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {key}'
    }

    response = requests.post(endpoint, headers=headers, json=data)
    result = response.json()

    if result['threat'] == 'anomaly':
        logging.warning(f"Anomaly detected: {data['deviceId']} [Simulated Restart]")
