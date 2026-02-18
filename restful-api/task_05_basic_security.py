from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Security Configuration
# Protects the sessions in Flask
app.config['SECRET_KEY'] = 'holberton_super_secret_key'
# A secret key used by JWT to sign the tokens
app.config['JWT_SECRET_KEY'] = 'jwt_super_secret_key'
# Initialize the security
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user data with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        # Transform the password into a hash
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- BASIC AUTHENTICATION ---
@auth.verify_password
# Callback: Flask-HTTPAuth calls this automatically to validate credentials
def verify_password(username, password):
    """Verifies the username and password for Basic Auth."""
    # Search the dictionary for an existing user
    user = users.get(username)
    # Compare the provided password with the stored hash
    if user and check_password_hash(user['password'], password):
        return user
    # Flask blocks the access
    return None


@app.route('/basic-protected')
# Forces the client to go to verify_password
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"


# --- JWT AUTHENTICATION ---
@app.route('/login', methods=['POST'])
def login():
    """Authenticates the user and returns a JWT token."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Additional claims store the role inside the token for fast authorization
        # create_access_token: Generates the token the client will use
        access_token = create_access_token(
            # Saves the user's name inside the token
            identity=username,
            # Saves if the user is a user or admin
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
# If someone tries to enter withouth a token, Flask-JWT-Extended stops the execution
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"


# --- Admin ---
@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Route protected by JWT with Role-Based Access Control (Admin only)."""
    # Retrieve the claims from the current JWT token (the role)
    claims = get_jwt()
    if claims.get("role") != "admin":
        # 403 Forbidden is used when the user is authenticated but lacks permissions
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- CUSTOM JWT ERROR HANDLERS ---
# These handlers ensure that all authentication errors return a 401 status code


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
