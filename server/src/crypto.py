# Cryptographic functions for the server

import os
import hashlib

def hash_password(password: str, salt: bytes = None) -> str:
    """Hashes a password using SHA-256 with a random salt."""
    if salt is None:
        salt = os.urandom(16)  # Generate a 16-byte random salt
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt.hex() + ':' + hashed.hex()

def verify_password(stored_password: str, provided_password: str) -> bool:
    """Verifies a password by hashing it with the stored salt and comparing the hashes."""
    salt_hex, stored_hash = stored_password['password'].split(':')
    salt = bytes.fromhex(salt_hex)
    new_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000).hex()
    return new_hash == stored_hash