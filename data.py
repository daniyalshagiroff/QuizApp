import requests

response = requests.get("https://opentdb.com/api.php?amount=10&category=23&type=boolean")
data = response.json()
question_data = data["results"]

