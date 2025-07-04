import socket
import json
from secure_comm import sign_message

train_data = {
    "train_id": "Train-A1",
    "location": "Sector 7",
    "speed": "123 km/h"
}

HOST = 'localhost'
PORT = 9999

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message_bytes = json.dumps(train_data).encode('utf-8')
        signature = sign_message(message_bytes)
        payload = {
            "data": train_data,
            "signature": signature
        }
        s.sendall(json.dumps(payload).encode('utf-8'))
        print("[TRAIN] Signed data sent to control center.")
except Exception as e:
    print(f"[TRAIN] Error: {e}")