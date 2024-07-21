# Route Calculation
This Python application utilizes Google's Distance Matrix API to calculate the time traveled between two destinations. Then using the Pandas library it stores the information into a CSV file.


## Getting Started:


- Ensure you have Python3 and Pandas on your environment
- Clone the GitHub Repo at https://github.com/K8MacEl/Route_calculation.git
- Create a new file titled ".env" for your local environment to securely store your Google API key. This will protect your Google API key if you push your code to an online repo such as GitHub.
- Obtain a Google Distance Matrix API by following the documentation: https://developers.google.com/maps/documentation/distance-matrix/overview
- Save you Google Distance Matrix API key in the .env file as follows: api_key: 'YOUR API KEY HERE'
- Run your code, you should receive a prompt in your terminal to enter a starting address, then an end address, and then it should provide you a total travel time and a new hist.csv file will be created with the date
- Each time you run the code and enter start and ends a new row will be added a new csv with the past history as well


<a href="https://imgur.com/iluNWM4"><img src="https://i.imgur.com/iluNWM4.png" title="source: imgur.com" /></a>


## Notes and Takeaways


This is a simple application using Google APIs and Pandas but can be expanded into a more complex mapping and routing tool. It is important to note that the current code stores all history of start and end points in the hist.csv, which if this tool is heavily used could result in extraneous data being stored in the application.
