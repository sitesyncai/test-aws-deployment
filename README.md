# FastAPI AWS App Runner Deployment

A simple FastAPI application ready for deployment on AWS App Runner with Docker support.

## 🚀 Features

- **FastAPI** web framework with automatic API documentation
- **Hello World** endpoint and additional API routes
- **Docker** containerization optimized for AWS App Runner
- **Health checks** for monitoring
- **CORS** enabled for frontend integration
- **Development** setup with hot reload

## 📁 Project Structure

```
test-aws-deployment/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── apprunner.yaml      # AWS App Runner configuration
├── run_local.py        # Local development server
├── setup.sh            # Automated setup script
├── .gitignore          # Git ignore patterns
└── README.md           # This file
```

## 🛠️ Local Development

### Prerequisites

- Python 3.11+
- pip
- venv (usually comes with Python)

### Quick Setup (Automated)

**Option 1: Use the setup script (recommended):**

```bash
./setup.sh
```

### Manual Setup

**Option 2: Manual setup:**

1. **Create and activate virtual environment:**

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate

   # On Windows:
   # venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start development server:**

   ```bash
   python run_local.py
   ```

   Or directly with uvicorn:

   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

4. **Deactivate virtual environment when done:**

   ```bash
   deactivate
   ```

### Access the Application

Once the server is running:

- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🐳 Docker

### Build and run locally:

```bash
# Build the image
docker build -t fastapi-app .

# Run the container
docker run -p 8000:8000 fastapi-app
```

## ☁️ AWS App Runner Deployment

### Method 1: Using AWS Console

1. **Push code to GitHub repository**

2. **Create App Runner service:**

   - Go to AWS App Runner console
   - Click "Create service"
   - Choose "Source code repository"
   - Connect your GitHub repository
   - Select automatic deployment
   - Configure build settings (App Runner will use the `apprunner.yaml`)

3. **Service will automatically:**
   - Build the Docker image
   - Deploy the application
   - Provide a public URL

### Method 2: Using AWS CLI

```bash
# Create apprunner.yaml in your repo (already included)
# Then create the service
aws apprunner create-service \
    --service-name "fastapi-hello-world" \
    --source-configuration '{
        "ImageRepository": {
            "ImageIdentifier": "your-account.dkr.ecr.region.amazonaws.com/fastapi-app:latest",
            "ImageConfiguration": {
                "Port": "8000"
            },
            "ImageRepositoryType": "ECR"
        },
        "AutoDeploymentsEnabled": true
    }'
```

## 📊 API Endpoints

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| GET    | `/`         | Hello World message     |
| GET    | `/health`   | Health check            |
| GET    | `/api/info` | Application information |
| POST   | `/api/echo` | Echo received message   |

## 🔧 Configuration

### Environment Variables

- `PORT`: Server port (default: 8000)
- `ENVIRONMENT`: Runtime environment (local/development/production)

### AWS App Runner Configuration

The `apprunner.yaml` file configures:

- Build commands
- Runtime settings
- Port configuration
- Environment variables

## 📝 Example Requests

```bash
# Hello World
curl http://localhost:8000/

# Health Check
curl http://localhost:8000/health

# App Info
curl http://localhost:8000/api/info

# Echo Message
curl -X POST http://localhost:8000/api/echo \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello from client!"}'
```

## 🔍 Monitoring

The application includes:

- Health check endpoint at `/health`
- Docker health checks
- Structured logging
- CORS support for frontend integration

## 🚦 Next Steps

1. **Deploy to AWS App Runner** using the steps above
2. **Add database** integration if needed
3. **Implement authentication** for secure endpoints
4. **Add more business logic** to your API endpoints
5. **Set up monitoring** with CloudWatch

## 📞 Support

For issues or questions:

- Check AWS App Runner documentation
- Review FastAPI documentation
- Check application logs in AWS CloudWatch
