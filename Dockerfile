FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /src

# Copy the current directory contents into the container at /app
COPY . /src

# Install MkDocs and other dependencies
RUN pip install mkdocs mkdocs-material mkdocs-macros-plugin

# Make port 8082 available to the world outside this container
EXPOSE 8082

# Define environment variable
ENV PORT 8082

# Run mkdocs serve when the container launches
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8082"]