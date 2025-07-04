import socket
import json
import threading
from tkinter import Tk, Label, StringVar, IntVar
from secure_comm import verify_signature, decrypt_message

HOST = 'localhost'
PORT = 9999

def handle_connection(attack_count, success_count, last_train, last_status):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print("[CONTROL CENTER] Listening...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                encrypted_data = conn.recv(2048)
                if encrypted_data:
                    try:
                        decrypted = decrypt_message(encrypted_data)
                        message = json.loads(decrypted.decode('utf-8'))
                        train_data = message["data"]
                        signature = message["signature"]

                        is_valid = verify_signature(json.dumps(train_data).encode('utf-8'), signature)

                        if is_valid:
                            success_count.set(success_count.get() + 1)
                            last_train.set(f"{train_data['train_id']} at {train_data['location']}")
                            last_status.set("✅ Valid message")
                        else:
                            attack_count.set(attack_count.get() + 1)
                            last_status.set("❌ Invalid signature")
                    except Exception as e:
                        attack_count.set(attack_count.get() + 1)
                        last_status.set(f"🚨 Error: {str(e)}")


def start_gui():
    window = Tk()
    window.title("🚆 Cyber Control Center")
    window.geometry("400x250")

    attack_count = IntVar()
    success_count = IntVar()
    last_train = StringVar()
    last_status = StringVar()

    Label(window, text="Secure Train Monitoring", font=("Arial", 16, "bold")).pack(pady=10)
    Label(window, text="✅ Successful messages:").pack()
    Label(window, textvariable=success_count, fg="green", font=("Arial", 12)).pack()
    Label(window, text="🚨 Attacks detected:").pack()
    Label(window, textvariable=attack_count, fg="red", font=("Arial", 12)).pack()
    Label(window, text="📍 Last train:").pack()
    Label(window, textvariable=last_train, font=("Arial", 10)).pack()
    Label(window, text="📡 Status:").pack()
    Label(window, textvariable=last_status, font=("Arial", 10)).pack()

    threading.Thread(target=handle_connection, args=(attack_count, success_count, last_train, last_status), daemon=True).start()
    window.mainloop()

if __name__ == "__main__":
    start_gui()

    
