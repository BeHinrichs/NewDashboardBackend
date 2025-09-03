import requests

def get_sunData(coords):
    # coords{lat, lon} from Backend
    url = f"sunrise_sunset_api"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None