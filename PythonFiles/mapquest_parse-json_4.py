# Importing urllib.parse to help with encoding the URL parameters
import urllib.parse
# Importing requests to make the API request
import requests

# The base URL for the MapQuest API that we're using to get directions
main_api = "https://www.mapquestapi.com/directions/v2/route?" 
# API key for accessing the MapQuest API. Make sure to keep this key private!
key = "j0TXzdxxdVo8CkGkA7S6nHauluLomgxy" #(replace with your own)

# Starting an infinite loop that continues until the user decides to quit
while True:
   # Ask the user to input the starting location
   orig = input("Starting Location: ")
   # If the user types 'quit' or 'q', exit the loop
   if orig == "quit" or orig == "q":
       break
   # Ask the user to input the destination location
   dest = input("Destination: ")
   # If the user types 'quit' or 'q' for the destination, exit the loop
   if dest == "quit" or orig == "q":
       break
   # Construct the full URL with the origin, destination, and API key as query parameters
   url = main_api + urllib.parse.urlencode({"key":key,"from":orig, "to":dest})

   # Printing the URL to make sure it's correctly constructed (useful for debugging)
   print("URL: "+(url))
   # Sending the request to the MapQuest API and getting the response in JSON format
   json_data = requests.get(url).json()
   # Extracting the status code from the JSON response to check if the API call was successful
   json_status = json_data["info"]["statuscode"]
   # If the status code is 0, it means the route was successfully found
   if json_status == 0:
       # Print the success message with the status code
       print("API Status: " + str(json_status) + " = A successful route call.\n")