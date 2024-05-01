FROM python:3.12
WORKDIR /Likes-Comments
COPY . .
RUN pip install -r requirement.txt
EXPOSE 3025

CMD ["python", "./wsgi.py", "--bind", "0.0.0.0"]
