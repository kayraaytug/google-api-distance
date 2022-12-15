import requests
from geopy import distance
import time
import sys

API_KEY = "YOUR_API_KEY" # Google API key

def main(location, target):

    try:
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' 
        + location + '&key=' + API_KEY) # Get address data

    except requests.exceptions.ConnectionError: # Catch connection problems
        print("\nCheck your internet connection..")
        sys.exit()
    
    resp_json_payload = response.json()
   
    current_lat = resp_json_payload['results'][0]['geometry']['location']['lat'] #Response json stuff
    current_lng = resp_json_payload['results'][0]['geometry']['location']['lng'] 
    currentFullAddress = resp_json_payload['results'][0]['formatted_address']

    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' 
    + target + '&key=' + API_KEY) # Get address data

    resp_json_payload = response.json()
   
    target_lat = resp_json_payload['results'][0]['geometry']['location']['lat']
    target_lng = resp_json_payload['results'][0]['geometry']['location']['lng'] 
    targetFullAddress = resp_json_payload['results'][0]['formatted_address']
    

    currentLocation = (current_lat, current_lng)
    targetLocation = (target_lat, target_lng)
    evalDistance = round(distance.geodesic(
        currentLocation, targetLocation).meters,1) # Geodestic straight line distance

    print('\nCurrent Location: {currentLocation}, {currentFullAddress}\n'
    'Target Location: {targetLocation}, {targetFullAddress}\n'
    'Distance: {evalDistance} meters\n'
    .format(currentLocation = currentLocation, currentFullAddress=currentFullAddress, targetLocation=targetLocation, 
    targetFullAddress=targetFullAddress, evalDistance=evalDistance))
    

if __name__ == "__main__":
    
    while True:
        location = input("Location: ")
        target = input("Target: ")
        if location == "q":
            print("Exiting...")
            time.sleep(1)
            break
        else:
            try:
                main(location, target)
            except IndexError:
                print("Address not found.\n")