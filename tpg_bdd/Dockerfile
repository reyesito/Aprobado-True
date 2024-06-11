# Dockerfile

# Use the official Python image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the app.py file into the container
COPY ./app.py /app

# Install Flask and MySQL client
RUN pip install Flask mysql-connector-python

# Expose the port Flask runs on
EXPOSE 5001

# Command to run the Flask application
CMD ["python", "app.py"]

