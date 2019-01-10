# sms_spam_classifier

A SMS spam classifier

# Execution

```
$ cd sms_spam_classifier
$ virtualenv venv
$ source ev/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
$ flask run
```

# Deploying to heroku

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

# requirents.txt

```
$ pip freeze > requirements.txt
```

## Dataset

[SMS Spam Collection Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset)