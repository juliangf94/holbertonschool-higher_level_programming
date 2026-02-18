from flask import Flask, jsonify, request


# Create the instance of the app
app = Flask(__name__)
# In-memory dictionary to store users
users = {}

# Returns a simple string
@app.route("/")
def home():
    """Root route that returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all stored usernames."""
    # Takes the users's names and put them on a list
    # Convert the dictionary keys (usernames) into a list
    # jsonify converts the list to a JSON string and sets the Content-Type header to application/json
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Health check endpoint."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full user object based on the dynamic username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    # Return a 404 status code if the username does not exist in the dictionary
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user via a POST request."""
    # Attempt to parse the request body as JSON
    # silent=True prevents Flask from crashing on invalid JSON, returning None instead
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    # Extract the 'username' field from the parsed dictionary
    username = data.get("username")
    # Validation logic: Ensure the username is provided and unique
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    # Store the user object in the memory dictionary
    users[username] = data
    # Return success confirmation with the 201 Created status code
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
