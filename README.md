# sms_spam_classifier

A SMS spam classifier

## Virtualenv

```
$ virtualenv venv
$ source ev/bin/activate
$ pip install -r requirements.txt
```

## Anaconda Enviroment

```
$ conda create --name sms-spam-classifier python=3.7
$ conda activate sms-spam-classifier
$ pip install -r requirements.txt
```
or
```
$ conda env export > sms-spam-classifier.yml
$ conda env create -f sms-spam-classifier.yml
```
## Run

```
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
$ flask run
```

## Deploying to heroku

```
$ heroku create sms-spam-classifer --buildpack heroku/python
$ heroku git:remote -a sms-spam-classifer
$ pip install gunicorn
$ touch procfile
$ echo "web: gunicorn app:app --log-file=-" >> procfile
$ echo "python-3.7.1" >> runtime.txt
$ heroku local
$ heroku local web
$ git add .
$ git commit -m "commit msg"
$ git push heroku master
$ git push origin master
```

## requirents.txt

```
$ pip freeze > requirements.txt
```
or 
```
$ conda list -e > requirements.txt
```

## Dataset

[SMS Spam Collection Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset)