# flask-example-project
A example project of building a service using python flask

## Create virtual environment
```
$ python3 -m venv env
$ source env/bin/activate
```

## Install dependencies
```
$ sudo yum install -y gcc gcc-c++
$ sudo yum install -y python3-devel
$ sudo yum install -y postgresql-devel
```

## Install py packages
```
$ pip install -r requirements.txt
```

## Install locally(required for running from local)
```
$ pip install -e .
```

## Run service
```
$ python application.py
```

## Run code style check
```
$ flake8 ./
```

## Test
Configure the following environment variables:
```
$ export DATABASE_URL="sqlite:////tmp/test.db"
$ export TESTING=True
```
Reinit test database:
```
$ rm /tmp/test.db
$ python db/manage.py db upgrade
```
Run test cases:
```
$ python -m pytest -v
```

## Update data model
To update data model, first edit the model definition(e.g. db/models.py). Then perform the migrate command to generate migration script:
```
python db/manage.py db migrate
```
Then perform the upgrade command to upgrade target database. Before doing that, config the environment variable `DATABASE_URL` to point to the target database.
```
python db/manage.py db upgrade
```
In case to purge the db migration history, remove the folder of `migrations` and rerun the following command:
```
python db/manage.py db init
```
Warning: all data model update history will be removed by performing the above operation.


## Install flask manually
```
$ python -m pip install Flask
$ python -m pip freeze > requirements.txt
```


## Reference
[1] https://realpython.com/flask-by-example-part-1-project-setup/

[2] https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
