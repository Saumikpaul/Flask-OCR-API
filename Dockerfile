# Stage 1: Builder
FROM python:3.10-slim as builder

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.10-slim as runtime

# Create a non-root user for security
RUN groupadd -r appgroup && useradd -r -g appgroup -s /bin/false appuser
WORKDIR /home/appuser/app

# Copy only necessary files from builder and source
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app/requirements.txt .
COPY . .

# Set ownership
RUN chown -R appuser:appgroup /home/appuser

# Switch to non-root user
USER appuser

# Expose port and define command
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
