import os
import json
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

def get_crypto_tools(master_password: str, salt_b64: str = None):
    salt = base64.b64decode(salt_b64) if salt_b64 else os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000
        )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    
    return Fernet(key), base64.b64encode(salt).decode()

def save_password(file_path, master_password, account_name, new_password):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = {"salt": None, "vault": {}}

    fernet, salt_str = get_crypto_tools(master_password, data["salt"])
    data["salt"] = salt_str
    
    encrypted_bytes = fernet.encrypt(new_password.encode())
    data["vault"][account_name] = encrypted_bytes.decode()
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def read_password(file_path, master_password, account_name):
    if not os.path.exists(file_path):
        return "No vault found."
        
    with open(file_path, "r") as f:
        data = json.load(f)
        
    if account_name not in data["vault"]:
        return "Account not found."
        
    try:
        fernet, _ = get_crypto_tools(master_password, data["salt"])
        encrypted_password = data["vault"][account_name]
        
        decrypted_bytes = fernet.decrypt(encrypted_password.encode())
        return decrypted_bytes.decode()
    except Exception:
        return "Error: Invalid Master Password!"

