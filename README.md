# Optimized Python Docker API

## Project Description
A highly optimized and secure Python API deployed via Docker with CI/CD validation. This project demonstrates best practices including multi-stage Docker builds, non-root user security context, and automated testing integrated through GitHub Actions.

## Features
*   **Optimized Dockerfile with Multi-Stage Builds**: Ensures minimal image size and faster builds.
*   **Enhanced Security (Non-Root User)**: Runs the application as a dedicated, non-root user (`appuser`).
*   **Automated CI/CD validation via GitHub Actions**: Automatically runs tests and validates Docker builds on every push and pull request.
*   **Python 3.10 environment**: Utilizes the stable and slim Python 3.10 runtime.
*   **Uvicorn production server**: Serves the API efficiently.

## Tech Stack
| Category | Technology |
| :--- | :--- |
| Backend | Python 3.10, FastAPI/Uvicorn |
| CI/CD | GitHub Actions, Docker |
| Deployment | Docker |

## Getting Started

### Prerequisites
- Docker
- Python 3.10
- `pytest`

### Development Setup
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/your-username/optimized-python-docker-api.git
   cd optimized-python-docker-api
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Run tests:
   \`\`\`bash
   pytest test_api.py
   \`\`\`

## Docker Build and Run

The `Dockerfile` is highly optimized with multi-stage builds.

1.  **Build the Docker image:**
    \`\`\`bash
    docker build -t optimized-python-api:latest .
    \`\`\`

2.  **Run the container:**
    \`\`\`bash
    docker run -d -p 8000:8000 optimized-python-api:latest
    \`\`\`

The API will be accessible at `http://localhost:8000`.

## CI/CD Pipeline
The `.github/workflows/python-ci.yml` configuration ensures continuous integration. On every push or pull request to the `main` branch, GitHub Actions will:
1. Install dependencies.
2. Run `pytest`.
3. Validate the optimized `Dockerfile` build process.
