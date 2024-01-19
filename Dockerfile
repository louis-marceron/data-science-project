# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed system dependencies
# RUN apt-get update && apt-get install -y ...

# Copy the requirements.txt first to leverage Docker cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port that the web app runs on
EXPOSE 8050

# Run your app using the python command that corresponds to your webserver
# This could vary based on how you've structured your Dash application
CMD ["python", "./src/main.py"]
