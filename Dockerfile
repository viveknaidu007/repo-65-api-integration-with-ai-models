#here it was using python image as base image
FROM python

# now we are setiing the working directory in the container
WORKDIR /app

# copying the current directory contents into the container at /app
COPY . /app

# now we can install dependenciess
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

#port Flask will run on
EXPOSE 5000

# command for running the application
CMD ["python", "app.py"]


