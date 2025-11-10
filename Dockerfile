# Use an official Python base image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy requirements and app files
COPY requirements.txt ./
COPY main.py ./
COPY .env ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
