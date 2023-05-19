from enum import unique
from flask import Flask, jsonify, request
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import jwt



app = Flask(__name__)


# Configure database connection URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:reeltracker@2.84.243.5:3306/reel_tracker'
app.config['SECRET_KEY'] = 'reeltracker'
db = SQLAlchemy(app)

# User Model
class USERS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)

@app.route('/login', methods=['POST'])
def login():
    # Get login credentials
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # check if username and password are provided
    if not username or not password:
        return jsonify({"message": "Invalid username or password"}), 400
    
    # query the database
    user = USERS.query.filter_by(username=username).first()
    
    # Check if user exists and password is correct:
    if not user or user.password != password:
        return jsonify({"message": "Invalid username or password"}), 401
    
    # Authentication successful
    token = jwt.encode({'user_id': user.id, 'username': user.username}, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})
    
@app.route('/token_authentication', methods=['GET'])
def token_authentication():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Missing token'}), 401

    try:
        # Verify and decode the token
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

        # Access the user information from the token
        user_id = payload['user_id']
        username = payload['username']

        # Perform authorization logic based on the user information
        user = USERS.query.filter_by(username=username).first()
        
        if not user :
            return jsonify({"message": "Invalid token"}), 401
        
        # Return the protected resource
        return jsonify({'message': 'Access granted to protected resource'})

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Expired token'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

@app.route('/register', methods=['POST'])
def register():
    # Get the registration data from the request body
    data = request.get_json()

    # Extract the username and password from the data
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # Validate the username and password
    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    # Check if the username is already taken
    existing_user = USERS.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists.'}), 400

    # Create a new user object
    user = USERS(username=username, password=password, email=email)

    # Add the user to the database
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully.'}), 201

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)





