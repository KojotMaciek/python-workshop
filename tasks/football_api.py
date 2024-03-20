import http.client
import json
import os

r_api_key = os.environ.get("RAPID_API_KEY")
leauges = {1 : 135, 2 : 140, 3 : 39}

def makeRequest():
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': r_api_key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    conn.request("GET", "/v3/standings?season=2023&league="+str(leauges[select_league]), headers=headers)
    res = conn.getresponse()
    data = res.read()
    global data_json
    data_json = json.loads(data)

def showData():
    print(data_json["response"][0]["league"]["name"] + ":\n")
    amount = len(data_json["response"][0]["league"]["standings"][0])

    for team_id in range(amount):
        position = data_json["response"][0]["league"]["standings"][0][team_id]["rank"]
        team = data_json["response"][0]["league"]["standings"][0][team_id]["team"]["name"]
        points = data_json["response"][0]["league"]["standings"][0][team_id]["points"]
        print(str(position) + ". " + team + " - " + str(points) + " points")

try:
    select_league = int(input("Select league:\n 1 - Serie A\n 2 - La Liga\n 3 - Premier League\nYour choice (1, 2 or 3): "))
except ValueError:
    print("Incorrect choice.\nSelect 1, 2 or 3.")
else:
    print("Processing...")
    makeRequest()
    showData()