def getData():
    import requests
    parameters = {
        "amount": 10,
        "type": "boolean",

    }
    apiResponse = requests.get(url="https://opentdb.com/api.php",params=parameters)
    apiResponse.raise_for_status()
    question_data = apiResponse.json()["results"]
    return question_data


