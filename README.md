# perched-peacock-api

A RESTful service to serve as a backend to https://perched-peacock-ui.herokuapp.com/ (https://github.com/gmdsam/perched-peacock-ui)

### Swagger URL

https://perched-peacock-api.herokuapp.com/swagger.json

### Technical Stack

- Language: **Python**
- Framework: **Flask**
- Database: **MongoDB**
- Deployment: **Docker**

### CI/CD

- [CI] All the commits are being tested for docker image build & code level unit tests

    Config file path: `.circleci/config.yml`

    Circle CI : https://circleci.com/gh/gmdsam/perched-peacock-api

- [CD] All the commits to `master` branch are being automatically deployed to heroku

    Config file path: `heroku.yml`

### Setup guide

#### Running with Python

1. Get python and mongoDB installed in your system. Recommended version for python is 3.6.9:

2. Download the dependencies using the command `pip install -r requirements.txt` at the project root

3. Set Environment variables as follows:
  PORT: <your port>
  PP_LOG_PATH: <path where you want to generate log file>
  DB_URL: `localhost:27017` or any other
  DB_NAME: `PerchedPeacock` or any other

4. Set PYTHONPATH for the project as `set PYTHONPATH=<path to root of project>`

5. Now, start the service using below commands at the project root:

- `python parking/api/main.py`
