import requests

LEAGUE = "Standard"
SEARCH_ID = "1"
BASE_URL = "http://www.pathofexile.com/api/trade2"
SEARCH_URL = f"{BASE_URL}/search/{LEAGUE}/{SEARCH_ID}"
FETCH_URL = f"{BASE_URL}/fetch"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

res = requests.get(f"{BASE_URL}/data/stats", headers=HEADERS)
if res.status_code != 200 :
    print(res.status_code)
    exit()
    
data = res.json()
print(data)