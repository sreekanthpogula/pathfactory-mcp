# PathFactory MCP - FastAPI Microservice
This is a FastAPI microservice for PathFactory's MCP (Microservice Content Platform). It includes endpoints for user authentication, content recommendations, engagement tracking, and more.

## Features

- User authentication (login/signup)
- Content recommendations based on user preferences
- Engagement tracking (views, likes, shares)

## Getting Started

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/pathfactory-mcp.git
    cd pathfactory-mcp
    ```
2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application
    ```bash
    uvicorn main:app --reload
    ```
4. Access the API documentation at `http://localhost:8000/docs`
5. Use the `/token` endpoint to obtain a JWT token for authentication.
6. Use the token to access protected endpoints by including it in the `Authorization` header as `Bearer <token>`.
7. Example of accessing a protected endpoint:
    ```bash
    curl -X GET "http://localhost:8000/protected-endpoint" -H "Authorization: Bearer <token>"
    ```

## Endpoints
- **Authentication**
  - `POST /token`: Login and obtain JWT token
  - `POST /signup`: Register a new user
- **Content Library**
  - `GET /collection`: Get content collection
  - `GET /engagement`: Get engagement content
  - `GET /recommendations`: Get content recommendations
  - `GET /topics`: Get topics
- **Protected Endpoints**
  - All endpoints under `/collection`, `/engagement`, `/recommendations`, and `/topics` require authentication.

## Authentication
This microservice uses JWT for authentication. The `/token` endpoint allows users to log in and receive a token, which must be included in the `Authorization` header for subsequent requests to protected endpoints

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

# contributors
- Sreekanth Pogula - Initial work and implementation of the FastAPI microservice.

# Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements
- Ensure your code adheres to the existing style and conventions
- Write tests for new features or changes
- Update the documentation as necessary
- Submit a pull request with a clear description of your changes
- Ensure all tests pass before submitting the pull request
- Follow the project's coding standards and guidelines
- Provide a clear and concise description of your changes in the pull request
- If your changes include new features, consider adding examples or usage instructions in the documentation.