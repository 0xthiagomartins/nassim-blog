FROM python:3.12-alpine

WORKDIR /app
ADD . ./

COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

EXPOSE 8082

CMD ["python", "run.py", "8082"]