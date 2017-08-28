# Scrapy Bench Speedcenter
Codespeed for scrapy-bench

## Instructions for setting up :

* Clone the repository : `git clone https://github.com/scrapy/scrapy-bench-speedcenter.git`
* Create a virtualenv : `virtualenv venv`
* Activate the virtualenv : `. venv/bin/activate`
* Install `codespeed` : `pip install codespeed --upgrade`
* `cd` into `center` folder : `cd center`
* Initialise the database : `python manage.py migrate`
* Load initial data : `python manage.py loaddata center/initial-data.json`
* Run the app on `localhost:8000/` : `python manage.py runserver`
* The app would be running on `localhost:8000/`

To add the results, do `tox -- {benchmark-name}` in [scrapy-bench](https://github.com/scrapy/scrapy-bench/) folder.

## Docker setup

Start the codespeed app (provide ``SECRET_KEY` value):

    SECRET_KEY= docker-compose up -d

Initialize the database (it is sored in ``./db`` folder):

    docker-compose exec app bash init-db.sh

Example of how to run one benchmark and upload results:

    docker-compose exec app bash \
        tox.sh -e py36-scrapy1.4 -- --upload_result cssbench
