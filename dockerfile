FROM python:3.9.23-trixie

WORKDIR /app

COPY requirements.txt .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]