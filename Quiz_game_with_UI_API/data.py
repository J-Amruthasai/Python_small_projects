# Used the API url to get the questions and answers instead of copy pasting the question like in previous Quiz game

import requests

parameters ={
    "amount":20,
    "type":"boolean",
    "category":12
}
# https://opentdb.com/api.php?amount=20&category=12&type=boolean
response = requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data =response.json()
questions=data["results"]
# print(questions)


