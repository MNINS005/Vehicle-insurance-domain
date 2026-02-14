FROM python:3.10-slim-buster

#Set the working directory for any subsequent ADD, COPY, CMD, ENTRYPOINT, or RUN instructions that follow it in the Dockerfile.
WORKDIR /app

#Copy files or folders from source to the dest path in the image's filesystem.

COPY . /app
RUN pip install -r requirements.txt
#expose the port web will run on 
EXPOSE 5000
CMD ["python3","app.py"]