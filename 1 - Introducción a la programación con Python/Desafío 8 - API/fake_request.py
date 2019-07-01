import json
import requests


def request(method, url, payload=""):
    url = url + payload
    headers = {
        "Content-type": "application/json",
    }

    response = requests.request(method, url, headers=headers)
    if method != "DELETE":
        print(response)

        return json.loads(response.text)
    else:

        print(response)

        return response
    # return json.loads(response.text)


payload = "/2"

getJson = request("GET", "https://reqres.in/api/users", payload)

print(getJson)

getJson = request("POST", "https://reqres.in/api/users", payload)

print(getJson)

getJson = request("PUT", "https://reqres.in/api/users", payload)

print(getJson)


getJson = request("DELETE", "https://reqres.in/api/users", payload)

print(getJson)
