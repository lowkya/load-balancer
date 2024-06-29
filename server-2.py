from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Response from Backend Server 2"

@app.route('/service1', methods=['GET', 'POST', 'PUT', 'DELETE'])
def service1():
    return f"Server 2 received {request.method} request"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8002)
