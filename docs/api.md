📌 API Documentation - Authentication Service

This API provides user authentication functionalities, including registration, login, password change, and JWT-protected endpoints.

🚀 Base URL

http://127.0.0.1:8000

🔐 Authentication Mechanism
	•	Uses JWT (JSON Web Token) for authentication.
	•	Rate-limited requests to prevent abuse.
	•	Secure password hashing and verification.

⸻

📌 Endpoints Overview

Method	Endpoint	Description	Auth Required
POST	/api/register	Register a new user	❌ No
POST	/api/login	Authenticate a user and obtain a JWT token	❌ No
POST	/api/changePassword	Change user password	✅ Yes (JWT)
GET	/api/protected	Access a protected route	✅ Yes (JWT)



⸻

📝 1. Register User

Endpoint:

POST /api/register

Description:

Registers a new user in the system.

Request:

Headers:

Content-Type: application/json

Body (JSON):

{
  "username": "user123",
  "password": "mypassword"
}

Response:

Success (200 OK):

{
  "success": "User registered successfully"
}

Errors:

Code	Description
400	Missing data
401	Invalid username
402	Invalid password



⸻

🔑 2. Login

Endpoint:

POST /api/login

Description:

Authenticates a user and generates a JWT token.

Request:

Headers:

Content-Type: application/json

Body (JSON):

{
  "username": "user123",
  "password": "mypassword"
}

Response:

Success (200 OK):

{
  "access_token": "eyJhbGciOiJIUzI1..."
}

Errors:

Code	Description
400	Missing data
401	Invalid username
402	Invalid password
500	User does not exist
501	Incorrect password



⸻

🔄 3. Change Password

Endpoint:

POST /api/changePassword

Description:

Allows an authenticated user to change their password.

Request:

Headers:

Authorization: Bearer <TOKEN>
Content-Type: application/json

Body (JSON):

{
  "password": "newpassword123"
}

Response:

Success (200 OK):

{
  "success": "Password changed successfully."
}

Errors:

Code	Description
400	Missing data
401	Invalid password



⸻

🔒 4. Protected Route

Endpoint:

GET /api/protected

Description:

Verifies if a user is authenticated by returning their username.

Request:

Headers:

Authorization: Bearer <TOKEN>

Response:

Success (200 OK):

{
  "logged_in_as": "user123"
}

Errors:

Code	Description
401	Missing or invalid token



⸻

⚠️ Rate Limiting
	•	Registration: Limited to prevent mass account creation.
	•	Login: Limited to avoid brute force attacks.
	•	If a rate limit is exceeded, the API returns:

{
  "error": "Too many requests. Please try again later."
}

(HTTP 429 Too Many Requests)

⸻

📌 cURL Examples

Register User

curl -X POST "http://127.0.0.1:8000/api/register" \
     -H "Content-Type: application/json" \
     -d '{
           "username": "user123",
           "password": "mypassword"
         }'

Login

curl -X POST "http://127.0.0.1:8000/api/login" \
     -H "Content-Type: application/json" \
     -d '{
           "username": "user123",
           "password": "mypassword"
         }'

Change Password

TOKEN="eyJhbGciOiJIUzI1..."  # Replace with actual token

curl -X POST "http://127.0.0.1:8000/api/changePassword" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $TOKEN" \
     -d '{
           "password": "newpassword123"
         }'

Access Protected Route

curl -X GET "http://127.0.0.1:8000/api/protected" \
     -H "Authorization: Bearer $TOKEN"



⸻

📚 Technologies Used
	•	Flask - Python Web Framework
	•	Flask-JWT-Extended - Authentication
	•	Flask-Limiter - Rate Limiting
	•	PostgreSQL - Database
	•	Bcrypt - Secure Password Hashing

⸻

📩 Contact & Support

For any issues or questions, please contact the API support team at josesantoscorte@gmail.com.