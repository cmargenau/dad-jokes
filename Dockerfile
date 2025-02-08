
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# COPY requirements.txt requirements.txt
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
CMD ["pytest", "-v"]
# CMD ["python", "-m", "pytest", "-v"]