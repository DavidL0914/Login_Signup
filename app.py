from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template

app = Flask(__name__)
users = {}

# Endpoint for user registration (signup)
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'Username already exists'}), 400

    users[username] = {'password': password}
    return jsonify({'message': 'Signup successful'}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username not in users or users[username]['password'] != password:
        return jsonify({'message': 'Invalid credentials'}), 401

    # Set a cookie to simulate user login
    response = jsonify({'message': 'Login successful'})
    response.set_cookie('username', username)
    return response

# Endpoint for checking if a user is logged in
@app.route('/check_login', methods=['GET'])
def check_login():
    username = request.cookies.get('username')

    if username:
        return jsonify({'message': f'Logged in as {username}'})

    return jsonify({'message': 'Not logged in'}), 401

# Route for rendering the login template
@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)