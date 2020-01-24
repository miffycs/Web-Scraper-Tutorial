# Simple Web Scraper Tutorial

Scrapes webpage for links filtered by element selector, store linkName and linkURL to CSV file.

## Environment Setup

(Optional, makes life easier)

Install [Pipenv](https://github.com/pypa/pipenv) if you don't have it:

```bash
$ pip install pipenv
# or
$ brew install pipenv
```

In an empty directory, running `$ pipenv install` will create a `Pipfile` and `Pipfile.lock`. These are intended to replace `$ pip install` usage, as well as manual virtualenv management `$ pipenv shell`.

```bash
$ pipenv install    # create Pipfile and Pipfile.lock
# if ^ doesn't work, try:
$ pipenv --python "[full path to your python3]"
$ pipenv sync       # installs all packages specified in Pipfile
$ pipenv shell      # spawns a shell within the virtualenv
$ exit              # exit shell
```

All you really need from this directory is `demo.py` if you've got everything set up in your python environment.

## Run

```
$ python3 demo.py
```
