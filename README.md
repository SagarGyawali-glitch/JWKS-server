# JWKS-server
Implementing a basic JWKS Server
Endpoints:
1.	JWKS Endpoint:
•	/ .well-known/jwks.json
2.	Authentication Endpoint:
•	/auth
Usage:
1.	Install dependencies:
pip install Flask cryptography jwtpip 
install Flask cryptography jwt 
2.	Run:
python app.py
python app.py 
Server: http://localhost:8080

3.	Example:
# Generate JWT token
curl -X POST http://localhost:8080/auth

# Generate expired JWT token
curl -X POST http://localhost:8080/auth?expired=true

# Retrieve JWKS
curl http://localhost:8080/.well-known/jwks.json

