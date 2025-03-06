import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(stored_password: str, provided_password: str) -> bool:
    return bcrypt.checkpw(provided_password.encode(), stored_password.encode())