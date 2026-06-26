FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

EXPOSE 5000

# Use gunicorn for production-style serving, not the Flask dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
