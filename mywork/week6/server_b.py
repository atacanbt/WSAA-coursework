# simple flask server

from flask import Flask, url_for, redirect

app = Flask(__name__, static_url_path='', static_folder='static_pages')

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/users', methods=['GET'])
def get_users():
    return 'getting all users'

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    return f'getting user {username}'

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return f'getting user with id {id}'

@app.route('/users', methods=['POST'])
def create_user():
    return 'creating a new user'

@app.route('/users', methods=['PUT'])
def update_user():
    return 'updating user'

@app.route('/invalid', methods=['GET'])
def invalid():
    return redirect(url_for('index'))

@app.route('/square/<int:id>', methods=['GET'])
def square(id):
    return f'{id} squared is {id**2}'

if __name__ == '__main__':
    app.run(debug=True)
    