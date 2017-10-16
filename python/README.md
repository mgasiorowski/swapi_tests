# Python

## Requirements
* python 3
* pip

## Install dependencies
`pip install -r requirements.txt`

## Run tests
`py.test`

## Docker
If you want to run tests in docker.

`docker build -t swapi-tests-python . && docker run --rm swapi-tests-python`