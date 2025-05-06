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

# Make sure Flask can find the app when using 'flask run'
application = app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

