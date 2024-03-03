from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import traceback
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import jwt

app = Flask(__name__)

# Dictionary to store RSA keys with their expiration time and kid
keys = {}

# Generate RSA key pair and store it with an expiration time and kid
def generate_rsa_key(expired=False):
    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        key_id = datetime.utcnow().strftime("%f")  # Unique Key ID based on microsecond part of the current time
        # If the key is meant to be expired, set the expiration to the past
        expiration_time = datetime.utcnow() - timedelta(days=1) if expired else datetime.utcnow() + timedelta(days=30)
        keys[key_id] = {"public_key": public_key, "private_key": private_key, "expiration_time": expiration_time}
        return key_id
    except Exception as e:
        app.logger.error(f"Error generating RSA key: {e}\n{traceback.format_exc()}")
        return None

@app.route('/.well-known/jwks.json', methods=['GET'])
def jwks():
    try:
        # Exclude expired keys
        jwks_keys = [
            {
                "kid": kid,
                "kty": "RSA",
                "alg": "RS256",
                "use": "sig",
                "n": data["public_key"].public_numbers().n,
                "e": data["public_key"].public_numbers().e,
            }
            for kid, data in keys.items() if datetime.utcnow() < data["expiration_time"]
        ]
        return jsonify(keys=jwks_keys)
    except Exception as e:
        app.logger.error(f"Error in JWKS endpoint: {e}\n{traceback.format_exc()}")
        return jsonify(error="Internal server error"), 500


@app.route('/auth', methods=['POST'])
def authenticate():
    expired = request.args.get('expired', 'false').lower() == 'true'
    key_id = generate_rsa_key(expired=expired)
    private_key = keys[key_id]["private_key"]
    # Set the expiration time for the JWT. If expired, set it to the past
    exp_time = datetime.utcnow() - timedelta(minutes=1) if expired else datetime.utcnow() + timedelta(minutes=5)
    payload = {
        'username': 'fakeuser',
        'exp': exp_time
    }
    token = jwt.encode(payload, private_key, algorithm='RS256', headers={'kid': key_id})
    return jsonify(token=token.decode('utf-8') if isinstance(token, bytes) else token)

if __name__ == '__main__':
    app.run(port=8080)
