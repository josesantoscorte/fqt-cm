from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

import os
from database import get_connection
from queries import INSERT_USER, GET_PASSWORD
from crypto import hash_password, verify_password

# Initialize Flask app
app = Flask(__name__)

# Get the secret from the environment and set it for the JWT manager
secret = os.environ.get("DATABASE_URL")
if not secret:
    raise RuntimeError("JWT_SECRET_KEY environment variable not set")
app.config['JWT_SECRET_KEY'] = secret
jwt = JWTManager(app)

@app.post("/api/register")
def register():
    """
    Endpoint for registering a new user
    """
    
    # Get the data from the request
    data = request.json
    if not data:
        return jsonify({"error": "Missing data"}), 400
    
    # Check if the data is valid
    if not isinstance(data.get("username"), str):
        return jsonify({"error": "Invalid username"}), 401
    if not isinstance(data.get("password"), str):
        return jsonify({"error": "Invalid password"}), 402
    
    # Parse the data
    username = data["username"]
    password = data["password"]
    
    # Insert the new user into the database
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(INSERT_USER, (username, hash_password(password)))
            conn.commit()
            
    return jsonify({"message": "User registered successfully"}), 200

@app.post("/api/login")
def login():
    """
    Endpoint for logging in a user
    """
    
    # Get the data from the request
    data = request.json
    if not data:
        return jsonify({"error": "Missing data"}), 400
    
    # Check if the data is valid
    if not isinstance(data.get("username"), str):
        return jsonify({"error": "Invalid username"}), 401
    if not isinstance(data.get("password"), str):
        return jsonify({"error": "Invalid password"}), 402
    
    # Parse the data
    username = data["username"]
    password = data["password"]
    
    # Get the user password from the database
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(GET_PASSWORD, (username,))  
            stored_password = cur.fetchone()
    
    # Check if the user exists
    if not stored_password:
        return jsonify({"error": "User does not exist"}), 500
    
    # Check if the password is correct
    if not verify_password(stored_password, password):
        return jsonify({"error": "Incorrect password"}), 501
    
    return jsonify(access_token=create_access_token(identity=username)), 200

@app.get("/api/protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200