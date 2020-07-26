# landbot-test-bot

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/5d1077b54e599d8c0072)
## Install

    pip install poetry
    poetry install
    
## Run

    poetry run uvicorn api.app:app --port 80 --env-file .env
    

## Test

    poetry run pytest