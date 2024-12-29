from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "" # Replace with your secret key for session management

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt(app)
try:
   URI = "mongodb://localhost:27017/"

# Connect to MongoDB (ensure you have the correct URI)
   client = MongoClient('URI')  # Update with your MongoDB URI
   db = client['flask_app']  # Replace with your database name
   users_collection = db['flask_practice']  # Replace with your collection name@app.route("/")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")



@app.route("/")
def home():
  return "Welcome to the flask   Application"



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user already exists
        if users_collection.find_one({'username': username}):
            flash('Username already exists!')
            return redirect(url_for('signup'))
        
        # Hash the password and store user data in MongoDB
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users_collection.insert_one({'username': username, 'password': hashed_password})
        
        flash('Signup successful! Please sign in.')
        return redirect(url_for('signin'))
    
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = users_collection.find_one({'username': username})
        
        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username  # Store username in session
            return redirect(url_for('welcome'))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('signin'))
    
    return render_template('signin.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('signin'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove user from session
    flash('You have been logged out.')
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
