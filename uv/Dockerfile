FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 3000
CMD ["python", "app/main.py"]