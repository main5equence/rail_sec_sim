import hmac
import hashlib
from cryptography.fernet import Fernet

# Ustalony klucz wspólny
SECRET_KEY = b'my_shared_secret_key_123'
FERNET_KEY = Fernet.generate_key()  # 👉 Do testów — potem zamień na stały!

fernet = Fernet(FERNET_KEY)

def sign_message(message_bytes):
    return hmac.new(SECRET_KEY, message_bytes, hashlib.sha256).hexdigest()

def verify_signature(message_bytes, signature):
    expected = sign_message(message_bytes)
    return hmac.compare_digest(expected, signature)

def encrypt_message(plaintext_bytes):
    return fernet.encrypt(plaintext_bytes)

def decrypt_message(cipher_bytes):
    return fernet.decrypt(cipher_bytes)