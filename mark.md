
{{TEST}}
With the introduction of the Flask command line interface, one of the more annoying things you have to do during development is set the environment variables each time you work on your app, namely FLASK_ENV and FLASK_APP. Well, Flask has a way for you to handle those things in a way to where you only have to do it once. And through the same functionality, you can also add other environment variables for your project. In this article, I'll show you how to use python-dotenv to have your environment variables loaded and ready to go every time you run your app.

The one package that makes this all work is [python-dotenv](https://github.com/theskumar/python-dotenv)

## What We'll Build

I'm going to demo how this works through a very simple Flask app.

Let's start by creating the directories and empty files we'll need. This is what our project directory will look like:

```
demo/__init__.py
demo/settings.py
.env
.flaskenv
run.py
```

This app won't do anything special. It'll just show us what configuration values we have.

## Set Up The Project

To start, on the command line create a new virtual environment and install flask and python-dotenv. I use pipenv, so I can do this all in one step:

```bash
pipenv install flask python-dotenv
pipenv shell
```

Next, in your demo/__init__.py, we'll need to create the basics of a Flask app, which means importing Flask, creating a application factory function (create_app), and instantiating Flask. Here's the code to do this. 

```python
# demo/__init__.py
from flask import Flask 

def create_app():
    app = Flask(__name__)

    return app
```

If you've worked with Flask at all, then you know exactly how this works.

Next, let's add in a simple route so we know our app actually works.

```python
# demo/__init__.py
from flask import Flask 

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '<h1>Hey There!</h1>'

    return app
```

## Add FLASK_APP Environment Variable

Once we've done that, we can use the Flask CLI to run the app. To run the app, use the following command while in the top level directory of your project.

```bash
flask run
```

But when we do that, we already get an error!

```
Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
```

This is a common error though. Normally, to fix this, we would export the environment variable FLASK_APP to be equal to the name of our app directory like this:

```bash
export FLASK_APP=demo
```

But since we're using python-dotenv and we want to avoid the inconvenience of using the command line, we'll have this load automatically by putting it in one of our dot files.

We have two dot files: .env and .flaskenv. We want to use .flaskenv for any Flask CLI configuration commands and use .env for our app configuration. 

We'll put our FLASK_APP enviornment variable inside of the .flaskenv file. 
