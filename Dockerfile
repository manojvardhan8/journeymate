# Start from the official Python Alpine image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    python3-dev \
    musl-dev \
    postgresql-dev \
    gcc \
    git

# Install pipenv or requirements if you use requirements.txt
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose the port your app runs on (commonly 8000 for Django)
EXPOSE 8000

# Default command (change this based on your app, e.g., Flask/Django)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
