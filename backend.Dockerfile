FROM python:3.10

WORKDIR /app


COPY requirements.txt .  
COPY main.py .  

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000"]
