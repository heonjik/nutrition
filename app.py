from flask import Flask, redirect, render_template, request, url_for
from db_config import DBFunctions, UserAuth

app = Flask(__name__)

@app.route('/')
def home():
    message = request.args.get('message')
    return render_template('home.html', message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    message = request.args.get('message')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        # check if the username already exists
        user_exist = UserAuth.check_username(username)

        if not username or not password or not password_confirm:
            return redirect(url_for('register', message='All fields are required.'))
        if password != password_confirm:
            return redirect(url_for('register', message='Passwords do not match.'))
        if user_exist == True:
            return redirect(url_for('login', message='Username already exists. Please login instead.'))
        
        return redirect(url_for('home', message='You are now registered.'))
    
    return render_template('register.html', message=message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = request.args.get('message')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # get the data from the DB
        user_data = UserAuth.get_user_data(username, password)
        if user_data and username == user_data['username'] and password == user_data['password']:
            return redirect(url_for('home', message='You are now logged in.'))
        else:
            return redirect(url_for('login', message='Invalid username or password. Please try again.'))
        
    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run()