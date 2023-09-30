FROM python:3.9
WORKDIR /app
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx
COPY main.py /app/
COPY dataset /app/dataset
COPY constants.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
