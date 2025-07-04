import socket
import json
from secure_comm import verify_signature, decrypt_message

HOST = 'localhost'
PORT = 9999

attack_count = 0  # 🔴 LICZNIK ATAKÓW

def start_control_center():
    global attack_count

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print("[CONTROL CENTER] Listening for encrypted train data...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"\n[CONTROL CENTER] Connection from {addr}")
                encrypted_data = conn.recv(2048)
                if encrypted_data:
                    try:
                        decrypted = decrypt_message(encrypted_data)
                        message = json.loads(decrypted.decode('utf-8'))
                        train_data = message["data"]
                        signature = message["signature"]

                        is_valid = verify_signature(json.dumps(train_data).encode('utf-8'), signature)

                        if is_valid:
                            print("[CONTROL CENTER] ✅ Valid encrypted data received:")
                            print(json.dumps(train_data, indent=4))
                        else:
                            attack_count += 1
                            print("🚨 [CONTROL CENTER] ❌ Signature mismatch! Possible spoofing.")
                            print(f"⚠️  Total attacks detected: {attack_count}")
                    except Exception as e:
                        attack_count += 1
                        print(f"🚨 [CONTROL CENTER] ❌ Error during decryption or parsing: {e}")
                        print(f"⚠️  Total attacks detected: {attack_count}")

if __name__ == "__main__":
    start_control_center()
    