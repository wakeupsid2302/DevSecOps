# Dockerfile
FROM python:3.10-slim

# Security best practices
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Install dependencies as root
COPY requirements.txt .
ADD http .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Switch to non-root user
USER root

# Copy application files
COPY app/ .

CMD ["python", "main.py"]
