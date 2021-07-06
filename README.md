# ISA_interviewing
This repo is where we host our open-source website and soon to be member hub.

## Contributing

> To get started...

1. 🍴 [Fork](https://github.com/kgmajor/ISA_interviewing/fork) this repository
2. 🔨 View our [contributing guidelines](.github/CONTRIBUTING.MD)
3. 🎉 [Open a new pull request](https://github.com/kgmajor/ISA_interviewing/compare) and get it approved!

You can even [report a bug or request a feature](https://github.com/kgmajor/ISA_interviewing/issues/new) - any little bit of help counts! 😊


## 💛️ Contributors

### This project exists thanks to all the **people who contribute**. 

#### Maintainers

- [Kristal Garcia](https://github.com/kgmajor)

#### Contributors


## Run locally with docker

Use docker-compose
```
docker compose up

```
If you get an error that says "Error response from daemon: Duplicate mount point:"

```
docker compose down

```
Then try the 'up' command again!

## Run the flask app outside docker

Bring up the MySQL DB container
```
docker compose up -d db
```

Install requirements.
`mypy` takes some time to install
```
pip install -r requirements.txt
```

Initialise environment variables. The `.env` is used in `docker-compose.yml`.
```
export FLASK_APP="src/main.py"
export SECRET_KEY="cool_app_bro"
export MYSQL_HOST="127.0.0.1:5432"
export MYSQL_DB="mydb"
export MYSQL_USER="postgres"
export MYSQL_PASSWORD="example"
```

Run flask
```
# initialise environment variables
flask run
```

## Run tests

```
py.test -vv
```


## Run with gunicorn
For production.
```
cd src && gunicorn main:app
```

## Continuous Deployment Pipeline

We're utilizing a continuous deployment pipeline where all merges on the 'main' branch are 'automagically' deployed into production. When a PR is opened, you'll have a 'staging' URL to view and check for accuracy. 

[![We deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/)


