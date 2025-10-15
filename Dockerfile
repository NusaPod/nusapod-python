# Gunakan base image Python
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy file yang diperlukan
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Jalankan Flask
CMD ["python", "app.py"]
