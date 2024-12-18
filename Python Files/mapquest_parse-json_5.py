import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "j0TXzdxxdVo8CkGkA7S6nHauluLomgxy"


while True:
   orig = input("Starting Location: ")
   if orig.lower in ["quit", "q"]:
      break
   dest = input("Destination: ")
   if dest.lower in ["quit", "q"]:
       break
   url = main_api + urllib.parse.urlencode({"key":key,"from":orig, "to":dest})

   print("URL: "+(url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("==================")
       print("Directions from " + (orig) + " to " + (dest))
       print("Trip Duration:  " + (json_data["route"]["formattedTime"]))
       print("Kilometers:     " + "{:.2f}".format(json_data["route"]["distance"]*1.61))
       if "fuelUsed" in json_data["route"]:
            print("Fuel Used (Ltr): " + "{:.2f}".format(json_data["route"]["fuelUsed"]*3.78))
        
       else:    
        estimated_fuel_gallons = json_data["route"]["distance"]/25
        print("Fuel Used (Ltr):" + "{:.2f}".format(estimated_fuel_gallons*3.78))     
       print("==================")


