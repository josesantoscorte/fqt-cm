
# FQT-CM Project

## Project Structure

```
/fqt-cm/
├── database/
│   └── init.sql
├── server/
│   ├── src/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── environment.py
│   │   └── crypto.py
│   ├── requirements.txt
│   └── Dockerfile
├── .gitignore
├── compose.yml
└── README.md
```

## Prerequisites

- Docker: Make sure Docker is installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).

## Running the Project

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/fqt-cm.git
    cd fqt-cm
    ```

2. **Run the Docker Compose**:
    ```sh
    docker compose up
    ```
    This command will build the Docker images and start the containers.

4. **Access the application**:
    The docker engine will expose the application on port 8000. You can access any of the endpoints using `http://localhost:8000`.

## API Endpoints

- **POST /api/register**: Register a new user.
- **POST /api/login**: Login a user and get a JWT token.
- **GET /api/protected**: Tests the access to a protected route (requires JWT token).
- **POST /api/changePassword**: Change the password of the user (requires JWT token).

For a more detailed documentation of the API, please refer to the [API Documentation](docs/api.md).

## Environment Variables

Environment variables can be set on the docker compose file. The following environment variables are required:

- `JWT_SECRET_KEY`: Secret key for JWT.
- `LOGIN_RATE_LIMITS`: Rate limits for login endpoint.
- `REGISTER_RATE_LIMITS`: Rate limits for register endpoint.
- `DATABASE_URL`: Database URL.
- `FLASK_APP`: Flask application source file.