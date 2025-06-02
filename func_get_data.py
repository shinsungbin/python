import requests

def get_pm_data(location, api_key):
    url = f"http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    params = {
        'serviceKey': api_key,
        'returnType': 'json',
        'numOfRows': 100,
        'sidoName': location,
        'ver': '1.0'
    }
    response = requests.get(url, params=params)
    data = response.json()

    result = []
    for item in data['response']['body']['items']:
        station = item['stationName']
        pm10 = item['pm10Value']
        result.append((station, pm10))
    return result
