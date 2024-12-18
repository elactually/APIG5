import urllib.parse
import requests

# MapQuest API for route directions
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "j0TXzdxxdVo8CkGkA7S6nHauluLomgxy"

# OpenWeatherMap API for weather data
weather_api_key = "b28c02e3c510b3c712d07200606b6a87"  # Replace with your OpenWeatherMap API key
weather_url = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather(location):
    """Get current weather for a given location using OpenWeatherMap API"""
    # Properly encode the location to handle spaces, commas, etc.
    location = urllib.parse.quote(location.strip())
    weather_query = f"{weather_url}q={location}&appid={weather_api_key}&units=metric"
    
    # Request the weather data
    weather_data = requests.get(weather_query).json()

    if weather_data["cod"] == 200:
        main = weather_data["main"]
        weather = weather_data["weather"][0]
        temp = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]
        return temp, humidity, description
    else:
        # Debugging: Print error message from the API
        print(f"Error fetching weather for {location}: {weather_data.get('message', 'Unknown error')}")
        return None

while True:
    orig = input("Starting Location: ")
    if orig.lower() in ["quit", "q"]:
        break
    dest = input("Destination: ")
    if dest.lower() in ["quit", "q"]:
        break

    # Get the route
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("==================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:  " + (json_data["route"]["formattedTime"]))
        print("Kilometers:     " + "{:.2f}".format(json_data["route"]["distance"] * 1.61))
        
        if "fuelUsed" in json_data["route"]:
            print("Fuel Used (Ltr): " + "{:.2f}".format(json_data["route"]["fuelUsed"] * 3.78))
        else:
            estimated_fuel_gallons = json_data["route"]["distance"] / 25
            print("Fuel Used (Ltr): " + "{:.2f}".format(estimated_fuel_gallons * 3.78))
        
        print("==================")
        
        # Weather information for the origin
        orig_weather = get_weather(orig)
        if orig_weather:
            orig_temp, orig_humidity, orig_description = orig_weather
            print(f"Weather at {orig}: {orig_description.capitalize()}, Temp: {orig_temp}°C, Humidity: {orig_humidity}%")
        else:
            print(f"Could not retrieve weather for {orig}.")
        
        # Weather information for the destination
        dest_weather = get_weather(dest)
        if dest_weather:
            dest_temp, dest_humidity, dest_description = dest_weather
            print(f"Weather at {dest}: {dest_description.capitalize()}, Temp: {dest_temp}°C, Humidity: {dest_humidity}%")
        else:
            print(f"Could not retrieve weather for {dest}.")
        
        # Display directions
        print("==================")
        for each in json_data['route']["legs"][0]["maneuvers"]:
            print(each['narrative'] + "(" + str("{:.2f}".format(each["distance"] * 1.61)) + "km)")
            print("==================\n")
    else:
        print("API Status: " + str(json_status) + " = Route not found or invalid input. Please try again.")
        print("================================\n")