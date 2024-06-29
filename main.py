from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Backend servers configuration
backend_servers = {
    '/service1': ['http://127.0.0.1:8001', 'http://127.0.0.1:8002'],
    '/service2': ['http://127.0.0.1:8003', 'http://127.0.0.1:8004']
}

current_server_index = {
    '/service1': 0,
    '/service2': 0
}


def get_next_server(service):
    global current_server_index
    servers = backend_servers[service]
    index = current_server_index[service]
    current_server_index[service] = (index + 1) % len(servers)
    return servers[index]


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def load_balancer(path):
    service_path = f'/{path.split("/")[0]}'

    if service_path not in backend_servers:
        return Response("Service not found", status=404)

    backend_url = get_next_server(service_path) + '/' + '/'.join(path.split('/')[1:])
    print(f"backend url {backend_url}")
    print(f"path {path}")
    print(f"path {request.args}")
    try:
        if request.method == 'GET':
            resp = requests.get(backend_url, headers=request.headers, params=request.args)
        elif request.method == 'POST':
            resp = requests.post(backend_url, headers=request.headers, data=request.get_data())
        elif request.method == 'PUT':
            resp = requests.put(backend_url, headers=request.headers, data=request.get_data())
        elif request.method == 'DELETE':
            resp = requests.delete(backend_url, headers=request.headers)

        return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))
    except requests.exceptions.RequestException as e:
        print(e)
        return Response(f"Error: {e}", status=500)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
