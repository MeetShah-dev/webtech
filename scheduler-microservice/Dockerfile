FROM python:3.12
WORKDIR /Schedulers
COPY . .
RUN pip install -r requirement.txt

EXPOSE 3028

CMD ["python", "./wsgi.py", "--bind", "0.0.0.0"]
