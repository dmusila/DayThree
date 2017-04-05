#this program takes in user input for the city the want to search for the weather
#before use ensure you have proper modules installed otherwise this Error will pop up"No module named request"

import re
import urllib.request
#http://www.weather-forecast.com/locations/Nairobi/forecasts/latest
cityname = input("Enter your city name : ")
url = "http://www.weather-forecast.com/locations/" + cityname + "/forecasts/latest"
weatherdata = urllib.request.urlopen(url).read()
data1 = weatherdata.decode("utf-8") #decode to readble format
m = re.search('span class="phrase">', data1)
start = m.end()
end = start + 100
newString = data1[start:end]
print(newString)
