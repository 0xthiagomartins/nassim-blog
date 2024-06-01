# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app
ADD . ./

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

RUN python ./src/generate_categories.py


# Make port 8082 available to the world outside this container
EXPOSE 8082

# Run mkdocs serve when the container launches
CMD ["mkdocs", "serve", "-f", "/app/blog/src/mkdocs.yml", "-a", "0.0.0.0:8082"]