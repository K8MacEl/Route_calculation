import requests
import pandas as pd
from pathlib import Path

#Checking to see if a CSV file already exits, if this is the first time running the program it will go to else
my_file = Path("hist.csv")
if my_file.is_file():
    hist_df = pd.read_csv('hist.csv')
    print("File exists and is loaded as pandas dataframe hist_df.")
else:
    print("File does not exist and new dataframe hist_df created")
    hist_df = pd.DataFrame()

# API Key
with open(".env", "r") as api_file:
    api_key = api_file.read().strip()

# Starting Address input
start = input("Enter starting point address\n")

# End point address input
end = input("Enter the end point address\n")

# Base URL
url = "https://maps.googleapis.com/maps/api/distancematrix/json?"

# GET response
r = requests.get(url + "origins=" + start + "&destinations=" + end + "&key=" + api_key[10:-1])

# Check if the request was successful
if r.status_code == 200:
    response_data = r.json()
    print(f"response: {response_data}")  # Print the entire response for debugging
    
    # Check if the response contains the expected structure
    if "rows" in response_data and len(response_data["rows"]) > 0:
        if "elements" in response_data["rows"][0] and len(response_data["rows"][0]["elements"]) > 0:
            # Return time as text and as seconds
            time = response_data["rows"][0]["elements"][0]["duration"]["text"]
            seconds = response_data["rows"][0]["elements"][0]["duration"]["value"]
            #Adding most recent calculation to the history in the dataframe
            row_to_append = pd.DataFrame([{'start':start, 'end':end,'travel_time':time}])
            hist_df = pd.concat([hist_df, row_to_append])
            print("\nThe total travel time from the starting point to the end point is", time)
        else:
            print("Error: 'elements' not found in response or empty.")
    else:
        print("Error: 'rows' not found in response or empty.")
else:
    print("Error:", r.status_code, r.text)

#Printing history and saving the new history to a CSV file
print(hist_df)
hist_df.to_csv('hist.csv',index=False)