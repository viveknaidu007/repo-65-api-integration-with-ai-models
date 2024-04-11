# repo-65-api-integration-with-ai-models


NAME : PMV VIVEK
CONTACT : 6303390566
linkedin : https://www.linkedin.com/in/vivek-pmv-1043b61b7
github : https://github.com/viveknaidu007





HOW TO RUN ?

1.CREATE PYTHON ENVIRONMENT
-im using conda environment
-conda create --name project
-conda activate project

2.install necessary dependencies in your environment
-pip install -r requirements.txt


3.PostgreSQL: create table in sql
#for creating table

CREATE TABLE sentiment_data (
    id SERIAL PRIMARY KEY,
    text TEXT,
    sentiment TEXT
);

4.python app.py  #in terminal
ctlt + c to stop




RUNNING WITH DOCKER :

DOCKER commands: run this in the terminal 

docker build -t nameforyouapp .             #for building docker image 

docker run --name firstpyc nameforyourapp   #for running the container

docker run -p 5000:5000 nameforyourapp      #flas is runninf default on 5000 port
