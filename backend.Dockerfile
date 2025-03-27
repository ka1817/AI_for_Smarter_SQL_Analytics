# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy only necessary files (Remove .env)
COPY requirements.txt .  
COPY main.py .  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 4000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000"]
