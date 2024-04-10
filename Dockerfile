#we are usinf pythonas base
FROM python:3.9-slim

#now we are settinf our workinf directory in the doctor where our real code exits
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python" , "app.py"]


