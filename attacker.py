import socket
import json
import os

fake_data = {
    "train_id": "🚨 FAKE-TRAIN",
    "location": "Blackout Zone",
    "speed": "999 km/h"
}

payload = {
    "data": fake_data,
    "signature": "THIS_IS_FAKE_SIGNATURE"
}


encrypted_fake = json.dumps(payload).encode('utf-8') 

HOST = 'localhost'
PORT = 9999

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(encrypted_fake)
        print("[ATTACKER] ❌ Spoofed plaintext sent to control center.")
except Exception as e:
    print(f"[ATTACKER] ❌ Error: {e}")