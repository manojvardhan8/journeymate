# Dockerfile

# 1. Base Image: Start from a modern, slim Python image.
FROM python:3.10-slim

# 2. Set Environment Variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set Working Directory
WORKDIR /app

# 4. Install Dependencies
#    This copy/run step is separate to leverage Docker's layer caching.
#    If requirements.txt doesn't change, this layer is reused, speeding up builds.
COPY requirements.txt .
RUN pip install -r requirements.txt

# 5. Copy Application Code
COPY . .

# 6. Expose the port Gunicorn will run on
EXPOSE 8000
ARG DJANGO_SECRET_KEY=dummy-secret-key-for-building
ENV SECRET_KEY=$DJANGO_SECRET_KEY

ARG DATABASE_URL="sqlite:////tmp/db.sqlite3"  # <--- ADD THIS
ENV DATABASE_URL=$DATABASE_URL                

ARG AMADEUS_API_KEY="dummy-amadeus-key"           # <--- ADD THIS
ENV AMADEUS_API_KEY=$AMADEUS_API_KEY              # <--- AND THIS

ARG AMADEUS_API_SECRET="dummy-amadeus-secret"     # <--- AND THIS
ENV AMADEUS_API_SECRET=$AMADEUS_API_SECRET
RUN python manage.py collectstatic --no-input

# 7. Set the command to run in production
#    This uses Gunicorn, your production-ready server.
#    Replace 'your_project_name' with the folder containing your wsgi.py
CMD ["gunicorn", "journeymate.wsgi:application", "--bind", "0.0.0.0:8000"]

