# hiking-log [![Build Status](https://travis-ci.org/clair3st/hiking-log.svg?branch=master)](https://travis-ci.org/clair3st/hiking-log)
Personal Hiking log.

## Getting Started

Clone this repository into whatever directory you want to work from.
```
https://github.com/clair3st/hiking-log.git
```
Assuming that you have access to Python 3 at the system level, start up a new virtual environment.
```
$ cd hiking-log
$ python3 -m venv ENV
$ source ENV/bin/activate
```
Once your environment has been activated, make sure to install Django and all of this project's required packages.
```
(hiking-log) $ pip install -r requirements.pip
```
Navigate to the project root, hikinglog, and apply the migrations for the app.
```
(hiking-log) $ cd hikinglog

(hiking-log) $ ./manage.py migrate
```
Finally, run the server in order to server the app on localhost
```
(hiking-log) $ ./manage.py runserver
```
Django will typically serve on port 8000, unless you specify otherwise. You can access the locally-served site at the address http://localhost:8000.


## Current Models (outside of Django built-ins):

**The `Hike` model contains:**
- name
- date
- gain
- height
- duration
- distance
- region
- park
- weather
- notes
- lat
- lng

## Current URL Routes

- `/admin` Superuser admin page.
- `/` Home page.

## Running Tests

Running tests for the hiking-log is fairly straightforward. Navigate to the same directory as the manage.py file and type:
```
(hiking-log) $ coverage run manage.py test
```
This will show you which tests have failed, which tests have passed. If you'd like a report of the actual coverage of your tests, type
```
(hiking-log) $ coverage report
```
This will read from the included .coverage file, with configuration set in the .coveragerc file. Currently the configuration will show which lines were missing from the test coverage.