from flask import Flask, url_for, redirect, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/inquery')
def inquery():
    name = request.args.get('name')
    return request.args

@app.route('/inbody', methods=['POST'])
def inbody():
    name = request.json['name']
    age = request.json['age']
    return f"Hello, {name}, you are {age} years old."

@app.route('/user')
def get_user():
    user = {
        'name': 'Atacan',
        'age': 33
    }
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)