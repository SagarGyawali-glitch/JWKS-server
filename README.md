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
![image](https://github.com/SagarGyawali-glitch/JWKS-server/assets/115506851/86deb8ae-bd30-43ce-b06f-f4c3a3c096d9)


<img width="1662" alt="Screen Shot 2024-03-02 at 8 01 02 PM" src="https://github.com/SagarGyawali-glitch/JWKS-server/assets/115506851/d859fd48-a5ed-431b-8d66-a3683c09bd5f">
