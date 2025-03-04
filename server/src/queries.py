# SQL queries for the server

INSERT_USER = """
INSERT INTO users (username, password) VALUES (%s, %s)
""" 

GET_PASSWORD = """
SELECT password FROM users WHERE username = %s
"""