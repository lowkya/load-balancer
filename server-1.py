from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Response from Backend Server 1"

@app.route('/service1', methods=['GET', 'POST', 'PUT', 'DELETE'])
def service1():
    return f"Server 1 received {request.method} request"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001)
