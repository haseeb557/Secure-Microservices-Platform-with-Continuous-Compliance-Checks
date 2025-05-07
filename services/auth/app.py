from flask import Flask, jsonify, request

app = Flask(__name__)

# Example endpoint for login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# New endpoint for displaying Auth service information
@app.route('/auth_info', methods=['GET'])  # Change the route to '/auth_info'
def auth_info():
    return """
    <html>
        <head><title>Auth Service</title></head>
        <body>
            <h2>Auth Service</h2>
            <p>Use POST <code>/login</code> with JSON data to log in.</p>
            <h3>Example:</h3>
            <pre>
{
    "username": "admin",
    "password": "password"
}
            </pre>
        </body>
    </html>
    """

# Make sure Flask can find the app when using 'flask run'
application = app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

#http://localhost:5000/auth_info