FROM python:3.11.5-slim-bullseye

WORKDIR /flask_app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./flask_app .

EXPOSE 5000

# CMD ["waitress-serve","--host","0.0.0.0","--port","5000", "app:app"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
