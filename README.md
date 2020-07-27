# landbot-test-bot


![test](https://github.com/kingoodie/landbot-backend/workflows/test/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/kingoodie/landbot-backend/branch/master/graph/badge.svg)](https://codecov.io/gh/kingoodie/landbot-backend)
[![Maintainability](https://api.codeclimate.com/v1/badges/21efa0909c8c43b8567d/maintainability)](https://codeclimate.com/github/kingoodie/landbot-backend/maintainability)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/5d1077b54e599d8c0072)

## Install

    pip install poetry
    poetry install

    
## Run

Firstly, rename the file `sample.env` to `.env` and fill in the following variables with the correct values
if you want to send an email when someone post a question:

- DEBUG=False
- SENDER_EMAIL=<yoursender@email.com>
- SMTP_PASSWORD=<yourmailpassword>

By default, it will use sqlite in memory, if you want to use another database or sqlite file fill `DB_URL`.

There are some other optional configurable variable, find their names in settings.py. You can change default values too.

To run the server execute:

    poetry run uvicorn api.app:app --port 80 --env-file .env
    

## Test

    poetry run pytest
    

# Landbot Test Bot API



## Indices

* [questions](#questions)

  * [Get question](#1-get-question)
  * [Get questions](#2-get-questions)
  * [Post question](#3-post-question)

* [users](#users)

  * [Get user](#1-get-user)
  * [Get users](#2-get-users)


--------


## questions



### 1. Get question



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1/questions/7c76e860-8dd2-4540-bd73-54ee36c24db9
```



***More example Requests/Responses:***


##### I. Example Request: No question with such id



##### I. Example Response: No question with such id
```js
{
    "detail": "There is no question with id 7c76e860-8dd2-4540-bd73-54ee36c24db9"
}
```


***Status Code:*** 404

<br>



##### II. Example Request: Get question



##### II. Example Response: Get question
```js
{
    "id": "8b3e9498-4211-4ca7-8307-133cea28cc4b",
    "text": "No, thank you",
    "user_id": "4bad9926-c2d0-4659-9bbc-68e6a66ed71e"
}
```


***Status Code:*** 200

<br>



### 2. Get questions



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1/questions
```



***More example Requests/Responses:***


##### I. Example Request: Get questions



##### I. Example Response: Get questions
```js
{
    "questions": [
        {
            "id": "8b3e9498-4211-4ca7-8307-133cea28cc4b",
            "text": "No, thank you",
            "user_id": "4bad9926-c2d0-4659-9bbc-68e6a66ed71e"
        },
        {
            "id": "f16b4b5f-669a-491e-b4d6-247f833c4cd1",
            "text": "No.",
            "user_id": "7b693f27-e6f0-445a-b177-bbacae141fdf"
        }
    ]
}
```


***Status Code:*** 200

<br>



### 3. Post question



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: http://127.0.0.1/questions
```



***Body:***

```js        
{
    "name": "Pablo",
    "last_name": "Guirado",
    "email": "poley@gmail.com",
    "phone": "687137049",
    "question": "No."
}
```



***More example Requests/Responses:***


##### I. Example Request: Post question



***Body:***

```js        
{
    "name": "Manuel",
    "last_name": "Jiménez",
    "email": "mjimenez@yahoo.com",
    "phone": "687137055",
    "question": "No."
}
```



##### I. Example Response: Post question
```js
{
    "name": "Manuel",
    "last_name": "Jiménez",
    "email": "mjimenez@yahoo.com",
    "phone": "687137055",
    "question": "No.",
    "id": "e1ce1630-090b-44d4-8767-5ebda989ebd1",
    "user_id": "9d06960e-2abf-4a01-843b-143f710d88a2"
}
```


***Status Code:*** 201

<br>



## users



### 1. Get user



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1/users/72e797ea-da53-4778-bfae-58a9f2538122
```



***More example Requests/Responses:***


##### I. Example Request: No user with such id



##### I. Example Response: No user with such id
```js
{
    "detail": "There is no user with id 7c76e860-8dd2-4540-bd73-54ee36c24db9"
}
```


***Status Code:*** 404

<br>



##### II. Example Request: Get user



##### II. Example Response: Get user
```js
{
    "id": "4bad9926-c2d0-4659-9bbc-68e6a66ed71e",
    "name": "Pablo",
    "last_name": "Cabezas Sales",
    "email": "pacasa@gmail.com",
    "phone": "+34689137050"
}
```


***Status Code:*** 200

<br>



### 2. Get users



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1/users
```



***More example Requests/Responses:***


##### I. Example Request: Get users



##### I. Example Response: Get users
```js
{
    "users": [
        {
            "id": "4bad9926-c2d0-4659-9bbc-68e6a66ed71e",
            "name": "Pablo",
            "last_name": "Cabezas Sales",
            "email": "pacasa@gmail.com",
            "phone": "+34689137050"
        },
        {
            "id": "7b693f27-e6f0-445a-b177-bbacae141fdf",
            "name": "Pablo",
            "last_name": "Guirado",
            "email": "poley@gmail.com",
            "phone": "688137050"
        }
    ]
}
```


***Status Code:*** 200

<br>



---
