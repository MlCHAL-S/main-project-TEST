FROM python:3.9-slim

WORKDIR /service
COPY service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /service ./service

EXPOSE 5000

ENV FLASK_APP=service:create_app
ENV FLASK_ENV=development

# Command to run the Flask app
CMD ["flask", "--app", "service", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
