# i_suck_at_interviewingBE
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
docker-compose up
```

## Run the flask app outside docker

Bring up the Postgres DB container
```
docker-compose up -d db
```

Install requirements.
`mypy` takes some time to install
```
pip install -r requirements.txt
```

Initialise environment variables. The `.env` is used in `docker-compose.yml`.
```
export FLASK_APP="src/main.py"
export POSTGRES_URL="127.0.0.1:5432"
export POSTGRES_DB="mydb"
export POSTGRES_USER="postgres"
export POSTGRES_PASSWORD="example"
```

Run migrations
```
chmod+x run-migrations.sh
./run-migrations.sh
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

Go live with a Continuous Deployment Pipeline using GitHub and Render's Infrastructure as code.

### Create your repository on GitHub

Ensure that you are using the GitHub username and project slug that you have entered earlier when cookie cutting.
This will match the settings in the [render.yaml](render.yaml) file.

Your repo should be accessible in: https://github.com/KGmajor/i_suck_at_interviewingBE

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

* Check the deployed API: `<API URL>/healthcheck`
* Ensure that you have deleted your resources from Render when you're done.
