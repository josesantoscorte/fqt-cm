import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Database connection string
url = os.environ.get("DATABASE_URL")
if not url:
    raise RuntimeError("DATABASE_URL environment variable not set")

# Function to establish a new database connection
def get_connection():
    return psycopg2.connect(url, cursor_factory=RealDictCursor)