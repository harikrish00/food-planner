#!/bin/bash
set -e

rm -rf _build
pipenv run pip install -r <(pipenv lock -r) --target _build/
if [ -f "my-deployment-package.zip" ] ; then
    rm "my-deployment-package.zip"
fi
cp handler.py food_db.json _build
zip -r -j my-deployment-package.zip _build/*
aws lambda update-function-code --function-name MyLambdaFunction --zip-file fileb://my-deployment-package.zip
