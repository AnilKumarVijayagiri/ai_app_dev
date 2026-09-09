import requests
API_KEY = "bd5e378503939ddaee76f12ad7a97608"
city=input("Enter city name: ")
url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_KEY+"&units=metric"
parameters={
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}
response=requests.get(url,params=parameters)
print(response.status_code)
print(response.json())