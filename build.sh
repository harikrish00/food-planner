#!/bin/bash
set -e

rm -rf _build
pipenv run pip install -r <(pipenv lock -r) --target _build/
rm my-deployment-package.zip
cp main.py _build
zip my-deployment-package.zip _build/*
aws lambda update-function-code --function-name MyLambdaFunction --zip-file fileb://my-deployment-package.zip