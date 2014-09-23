#Youten

[![Build Status](https://travis-ci.org/kirang89/youten.svg?branch=master)](https://travis-ci.org/kirang89/youten)

**Youten** is a simple app to help manage your code snippets. This repository contains the brains(a.k.a API)
behind the app.

##Installation

The following command creates a virtual environment and installs dependencies for you:

```make env```

##Usage

To run the project in development mode, do:

```python server.py```

If you want to run it with a [Gunicorn](http://gunicorn.org/) server instead, do:

```./gunicorn_server ```

##Testing

Youten uses [nose](https://nose.readthedocs.org/en/latest/) for testing. To run tests, simply do:

```make test``` or ```make testc```

to run with coverage report.

##Contributing

No code is perfect, so feel free to send me a pull request or create a git issue :)

##License

Youten is MIT licensed, so feel free to use it as you like.