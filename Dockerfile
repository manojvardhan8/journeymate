# Start from the official Python Alpine image
FROM python:3.11-alpine


# Set work directory
WORKDIR /app

# Install pipenv or requirements if you use requirements.txt
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose the port your app runs on (commonly 8000 for Django)
EXPOSE 8000

# Default command (change this based on your app, e.g., Flask/Django)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
EXPOSE 8031