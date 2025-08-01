# Use official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY ./app ./app
COPY ./model ./model
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]