# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all project files
COPY . .

# Run the Flask app
CMD ["python", "app.py"]