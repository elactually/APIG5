# Importing urllib.parse to help with encoding the URL parameters
import urllib.parse
# Importing requests to make the API request
import requests

# The base URL for the MapQuest API that we're using to get directions
main_api = "https://www.mapquestapi.com/directions/v2/route?" 
# Setting the origin location (starting point) for the route
orig = "Washington, D.C"
# Setting the destination location (end point) for the route
dest = "Baltimore, Md"
# API key for accessing the MapQuest API. Make sure to keep this key private!
key = "j0TXzdxxdVo8CkGkA7S6nHauluLomgxy" #(replace with your own)
# Combining the main API URL with the parameters (API key, origin, destination) into a full URL
url = main_api + urllib.parse.urlencode({"key":key,"from":orig, "to":dest})

# Sending the GET request to the API and getting the response in JSON format
json_data = requests.get(url).json()
# Printing out the JSON data so we can see the result of the API request
print(json_data)
