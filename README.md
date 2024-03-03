# JWKS-server
Implementing a basic JWKS Server
Endpoints:
JWKS Endpoint:

/ .well-known/jwks.json
Authentication Endpoint:

/auth
Usage:
Install dependencies:

bash
Copy code
pip install Flask cryptography jwt
Run:

bash
Copy code
python app.py
Server: http://localhost:8080

Example:

bash
Copy code
# Generate JWT token
curl -X POST http://localhost:8080/auth

# Generate expired JWT token
curl -X POST http://localhost:8080/auth?expired=true

# Retrieve JWKS
curl http://localhost:8080/.well-known/jwks.json

<img width="1662" alt="Screen Shot 2024-03-02 at 8 01 02 PM" src="https://github.com/SagarGyawali-glitch/JWKS-server/assets/115506851/d859fd48-a5ed-431b-8d66-a3683c09bd5f">
