import psycopg2
from psycopg2.extras import RealDictCursor

from environment import get_database_url

# Function to establish a new database connection
def get_connection():
    return psycopg2.connect(get_database_url(), cursor_factory=RealDictCursor)

# SQL queries for the server
INSERT_USER = """
INSERT INTO users (username, password) VALUES (%s, %s)
""" 
GET_PASSWORD = """
SELECT password FROM users WHERE username = %s
"""