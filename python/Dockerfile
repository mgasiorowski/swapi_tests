FROM python:3

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENTRYPOINT ["pytest", "-v", "-s", "--color=yes"]