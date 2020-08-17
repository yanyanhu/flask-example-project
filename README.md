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

## Test
```
python -m pytest -v
```

## Run code style check
```
$ flake8 ./
```

## Install flask manually
```
$ python -m pip install Flask
$ python -m pip freeze > requirements.txt
```

## Manage data model and upgrade using alembic
### Cleanup existing data model history
```
$ rm -rf alembic
$ rm -rf alembic.ini
```
Drop existing tables and history alembic versions in the target DB if need, e.g.
```
DROP TABLE table1
DROP TABLE table2
DROP TABLE alembic_version
```
Warning: all data model update history will be lost by performing the above operation. So please just do in case you want to restart from scratch.

### Init alembic history
```
$ alembic init alembic
```
Edit the alembic.ini file to fill in correct `sqlalchemy.url` before continue.

### Generate baseline script
Generate baseline script
```
$ alembic revision -m "baseline"
```

### Init alembic history in the database
```
$ alembic upgrade head
```
This will generate `alembic_version` table in the target DB for keeping the datamodel updating history.

### Define data models
Define all required data models in the definition file, e.g. `db/models.py`. Then edit the `alembic/env.py` to  let alembic know where is the data models' metadata, e.g. adding the following line:
```
from db import models
...
...
target_metadata = models.Base.metadata
```

Then auto-generate the migration script uses the `--autogenerate` flag to the alembic revision command.
```
alembic revision --autogenerate -m "add init talbles"
```

### Upgrade target database to apply the data model changes
```
alembic upgrade head
```

## Reference
[1] https://realpython.com/flask-by-example-part-1-project-setup/

[2] https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
