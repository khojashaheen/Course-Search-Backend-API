# Course-Search-Backend-API-Project
A Backend Web API using FastAPI that searches for courses in  Elasticsearch Database. The Elasticsearch database is populated with data from web scraping using BeautifulSoup4.

## Overview:
1. This project scrapes a course list from the following website (https://hackr.io/blog/tag/courses) using BeautifulSoup4, and extracts relevant information about each course (course titles, tags, authors, course_date, course_link and first 4 paragraphs) as a CSV file.
2. Next, it reads data from the CSV file and inserts each row as a document into the Elasticsearch index.
3. Third, it employs:
  - FastAPI web framework for building a Backend API that allows users to search on scraped courses
  - Kibana platform for testing and debugging of the database


## System Architecture Overview:
This python project leverages Amazon EC2 instance for its infrastructure, and Docker to build images for ElasticSearch,FastAPI and Kibana and run the 3 containers.

![WeCloudDataProjects-Mini-project3](https://github.com/khojashaheen/Course-Search-Backend-API-Project/assets/132402838/93bf5909-6fae-4d63-9212-eb21be375167)


## Pre-Requisites:
### Sign up for an AWS Account
### Install the following on the EC2 Instance:
    Python 3.7+
    Docker
    Docker Compose

## Installation Steps:
### 1. create EC2 intance using Ubuntu image and config the system.

### 2. run ubuntu_sys_init.sh to update package manager, and install the Pre-Requisites
    chmod +x ubuntu_sys_init.sh
    sudo ./ubuntu_sys_init.sh
    
### 3. Build images for docker-compose:
    docker-compose build --no-cache
  
### 4. Start docker containers, which will run Elasticsearch on port 9200, Kibana on port 5601 and FastAPI on port 8000:
    docker-compose up
    
### 5. Verify docker processes running:
    docker ps

### 6. Start web scraping and store in database:
    rm data/output.csv
    python3 scripts/fetch_course.py
    python3 scripts/es_insert_items.py

### 7. Validate the course List using Kibana
    http://<EC2-IP>:5601/app/kibana#/dev_tools/
    GET courses/_search?size=10

### 8. Validate the search endpoint using FastAPI
    http://<EC2-IP>:8000/search/courses?query=<any keyword>





    
