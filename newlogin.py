from pymongo import MongoClient, errors
from flask import Flask, request, redirect, url_for, json

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return f'Hello World From Login!!!!'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #print(username)
        user = get_database(username, password)
        print(user)
        return user


def get_database(username, password):
     print(f'Username from Get Database Function {username}, {password}')
     connection_string = "mongodb+srv://harsh:12345@cluster0.rn74gvh.mongodb.net"
     client = MongoClient(connection_string)
     database = client.akash
     user_collection = database.users
     user = user_collection.find_one({"username": username, "password": password})
     print(f' From Get Database Object {user}')
     if user:
         print("success access")
         json = parse_json(user)
         return json
     else:
         print("access denied")
         return f'Not Able to login'

def parse_json(user):
    return json.loads(json.dumps(user, default=str))
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
