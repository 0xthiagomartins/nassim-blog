# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app/blog

# Copy the requirements file and install dependencies
COPY requirements.txt /app/blog
RUN pip install -r requirements.txt
RUN python src/generate_categories.py

# Copy the application files
COPY src /app/blog/src

# Make port 8082 available to the world outside this container
EXPOSE 8082

# Run mkdocs serve when the container launches
CMD ["mkdocs", "serve", "-f", "/app/blog/src/mkdocs.yml", "-a", "0.0.0.0:8082"]