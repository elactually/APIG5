# Importing urllib.parse to help with encoding the URL parameters
import urllib.parse
# Importing requests to make the API request
import requests

# The base URL for the MapQuest API that we're using to get directions
main_api = "https://www.mapquestapi.com/directions/v2/route?" 
# Setting the origin location (starting point) for the route
orig = "Rome, Italia"
# Setting the destination location (end point) for the route
dest = "Frascati, Italia"
# API key for accessing the MapQuest API. Make sure to keep this key private!
key = "j0TXzdxxdVo8CkGkA7S6nHauluLomgxy" #(replace with your own)
# Combining the main API URL with the parameters (API key, origin, destination) into a full URL
url = main_api + urllib.parse.urlencode({"key":key,"from":orig, "to":dest})

# Printing the full URL to check if it's correctly built (useful for debugging)
print("URL: " + (url))
# Sending a GET request to the API and getting the response as JSON data
json_data = requests.get(url).json()
# Extracting the status code from the API response to check if the request was successful
json_status = json_data["info"]["statuscode"]
# If the status code is 0, the API call was successful and we print a success message
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")