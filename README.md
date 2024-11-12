# Nginx-Python-App Assignment

This project demonstrates a simple web application built with Python, Nginx, and MySQL, deployed using Docker Compose. The Nginx container acts as a load balancer for the application containers, which connect to a MySQL database to store access logs.

## Project Structure

- **Python Application (`app.py`)**: A web app with two routes:
  - `/`: Increments a counter, sets a 5-minute cookie, logs the client IP, and displays the app container's internal IP.
  - `/showcount`: Shows the global counter value.

- **Nginx Load Balancer**: Routes requests to the application containers while enforcing session stickiness based on cookies.

- **MySQL Database**: Stores access logs with details such as client IP, internal IP, and request timestamp.

## Prerequisites

- Docker and Docker Compose installed.
- Python 3.11 or higher (for development only).


### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/nginx-python-app.git
cd nginx-python-app
```

### Step 2: Start the app and view the logs
```bash
docker-compose up --build
```
### Step 2: Access the cluster
```bash
curl -l -vvv http://localhost
curl -l -vvv http://localhost/showcount
```

### Step 3: Scale the app
```bash
bash -cx ./scale_apps.sh NUM_OF_REPLICA
```
