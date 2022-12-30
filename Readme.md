# A-team013-iloveCS411

## iCourse - Course Management Platform

Special thanks to all team members! We appreciate your great efforts!

### Play Online

Check this [link](http://cs411-team013.uc.r.appspot.com) to play with our application with the following test accounts!

> Student Test Account:
> NetId: ruipeng4
> Password: CS411@team013
>
> Professor Test Account:
> NetId: prof77
> Password: CS411@team013
>

**WARNING**: The trial for Google Cloud Platform will expire soon so you may be no longer able to access our project by the link above,

### Play locally

This project is based on Python3 and mysql. To run this project locally, you need to first install Python3 (>=3.5), and has access to a mysql server. If you do not have access to a mysql server, you can download mysql from [this website](https://dev.mysql.com/doc/mysql-getting-started/en/) and set up a local server. Once you have done the preprations, you can move on to next steps.

**1. Import data to Mysql database**

Access your Mysql database server and run [these queries](Cloud_SQL_Export_2022-12-30_icourse.sql) from "Cloud_SQL_Export_2022-12-30_icourse.sql". This is a script to import the schema and data to your database.

**WARNING**: If your mysql server happens to have a database named "icourse", this script will automatically **DESTROY** your original database and create a new one. Proceed with caution!

**2. Install Virtual Environment for Python3**

Set virtual envrionment, install flask and other required packages, and set environmental variables related to flask

The commands are for Linux. If you are using Windows you may need to set virtual envrionment and environmental variables in a different way.

```
cd flask
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP = app
export FLASK_DEBUG = 1
```

**3. Config database**

Go to [flask\app.yaml](flask\app.yaml) and change these variable to your database instance:

```
env_variables:
  INSTANCE_UNIX_SOCKET: 'YOUR CONNECTION NAME' # No need to fill in
  MYSQL_USER: 'root' # please put in your credentials
  MYSQL_PASSWORD: 'YOUR PASSWORD' # please put in your credentials
  MYSQL_DB: 'icourse' # please put in your credentials
  MYSQL_HOST: 'YOUR DATABASE' # please put in your credentials
```

You only need to fill in the last four variables for local application.

**3. Run Application**

```
flask run
```

Open your browser and visit http://127.0.0.1:5000

### Demo and Report


The video demo is [here](https://www.youtube.com/watch?v=pYg-fUh2HqY)

The project reflection report is [here](doc/ReflectionReport.md)
