FROM python:3.11

WORKDIR /project

# Copying reqs seperately due to optimize Docker's Layer Caching mechanism
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]