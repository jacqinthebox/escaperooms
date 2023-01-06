FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
EXPOSE 5006
ENTRYPOINT ["python"]
CMD ["main.py"]