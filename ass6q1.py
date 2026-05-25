import requests

def weather_data(city):
    url="https://api.openweathermap.org/data/2.5/weather?q={city}&appid=345b7307ead3b76a95697f5fc9adab3d&units=metric".format(city=city)
    
    try:
        response=requests.get(url)
        response.raise_for_status()  
        data=response.json()
        print(f"Weather data for {city}:")
        count=0
        for key, value in data['main'].items():
            print(f"{key}: {value}")
            count += 1
            if count > 6:
                break

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data for {city}: {e}")

city=input("Enter the city name: ")
weather_data(city)