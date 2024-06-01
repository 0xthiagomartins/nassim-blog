FROM python:3.12-alpine

WORKDIR /app
ADD . ./

COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

RUN python src/generate_categories.py


EXPOSE 8082

CMD ["mkdocs", "serve", "-f", "src/mkdocs.yml", "-a", "0.0.0.0:8082"]