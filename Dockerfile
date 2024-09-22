# image used to create your container 
FROM python:latest

# go to app dir and if this not exist create it and go to it
WORKDIR  /app

# copy requirements from it path to current working directory
COPY requirements.txt .

# run command to install all in requirements
RUN pip install -r requirements.txt

# copy app folders and files
COPY  modules .
COPY main.py .
COPY reviews.csv .

# Expose the port that FastAPI will run on (default is 8000)
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]