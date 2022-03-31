import requests

def location(ip, output): 
    if ip is None: return {}
    url = 'https://ipapi.co//' + ip +'/' + output
    data = requests.get(url).json()


    return data
