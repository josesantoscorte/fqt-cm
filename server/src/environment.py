import os

def get_database_url() -> str:
    """Gets the URL for the database."""
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL environment variable not set")
    return url

def get_jwt_secret() -> str:
    """Gets the secret key for the server."""
    secret = os.environ.get("JWT_SECRET_KEY")
    if not secret:
        raise RuntimeError("JWT_SECRET_KEY environment variable not set")
    return secret

def get_register_rate_limits() -> str:
    """Gets the rate limits for register requests."""
    limits = os.environ.get("REGISTER_RATE_LIMITS")
    if not limits:
        raise RuntimeError("REGISTER_RATE_LIMITS environment variable not set")
    return limits

def get_login_rate_limits() -> str:
    """Gets the rate limits for login requests."""
    limits = os.environ.get("LOGIN_RATE_LIMITS")
    if not limits:
        raise RuntimeError("LOGIN_RATE_LIMITS environment variable not set")
    return limits

