# Use a smaller base image for production
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

# Install dependencies efficiently
RUN pip install --no-cache-dir "uvicorn[standard]" fastapi

# Copy the entire backend code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
