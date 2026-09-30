import requests

def fetch_students():
    url = "https://api.slingacademy.com/v1/sample-data/files/student-scores.json"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    return data 