# Basic Python Load Balancer

This project implements a simple Layer 7 (Application Layer) load balancer using Python and Flask. It distributes incoming HTTP requests to multiple backend servers using a round-robin algorithm.

## Features

- **Round-Robin Load Balancing**: Distributes incoming requests evenly across backend servers.
- **Basic HTTP Request Handling**: Supports GET, POST, PUT, and DELETE methods.

## Technologies Used

- **Python**
- **Flask**
- **Requests Library**

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Requests Library

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/load-balancer.git
   cd load-balancer

2. Install the required packages:
  `pip install flask requests`

3. Running the Backend Servers
4. Running the Load Balancer

### Usage
Send HTTP requests to the load balancer and see how it distributes them to the backend servers:

```bash
Copy code
curl http://127.0.0.1/service1
curl http://127.0.0.1/service2
