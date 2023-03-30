#Please register for free API access here:
#https://rapidapi.com/afmaster-O-sjBiUUm4z/api/waze-alerts/pricing
#Then replace your API key where it says "#Replace with your API key" below
#Otherwise we may get out of quota

#connect to Waze and get information on traffic jams within Mumbai

#location is defined as the smallest rectangle that includes all Mumbai AQ stations
#bottom left: 18.91,72.81; top right: 19.38,73.03"

import requests
import pandas as pd
from datetime import datetime, timezone, timedelta
from time import sleep

local_path = 'c:/Omdena/data/traffic'
#storing interval in minutes
storing_interval = 15

url = "https://waze.p.rapidapi.com/alerts-and-jams"

querystring = {"bottom_left":"18.91,72.81","top_right":"19.38,73.03","max_alerts":"100","max_jams":"100"}

#Replace with your API key:
headers = {
	"X-RapidAPI-Key": "3dcb9b4207msh96fdb7b9c085617p112547jsn83e986f61388",
	"X-RapidAPI-Host": "waze.p.rapidapi.com"
}

def get_current_jams():
   response = requests.request("GET", url, headers=headers, params=querystring)
   data = response.json()

   jams = data['data']['jams']
   atts = ['level', 'severity', 'speed_kmh', 'length_meters', 'delay_seconds', 'update_datetime_utc', 'line_coordinates']
   alerts_ar = []
   for jam in jams:
      alert = {}
      for att in atts:
         alert.update({att: jam[att]})
      alerts_ar.append(alert)
   df = pd.DataFrame(alerts_ar)
   return df
   
def save_current_jams():
    df = get_current_jams()
    df = df.rename(columns={"alert_reliability": "reliability", "alert_confidence": "confidence", 
          "publish_datetime_utc": "time"})
    utc_now = datetime.now(timezone.utc)
    timestamp = utc_now.strftime("%Y-%m-%d_%H-%M")
    filepath = local_path + '/' + timestamp + '.csv'
    outfile = open(filepath, 'wb')
    df.to_csv(filepath, index = False, header = True, sep = ',', encoding = 'utf-8')
    outfile.close()
    print("Saved data to " + filepath)
    
def loop():
    keep_sleeping = True
    while keep_sleeping:
        utc_now = datetime.now(timezone.utc)
        mins = utc_now.strftime("%M")
        mod = int(mins) % storing_interval
        remainder = storing_interval - mod
        nexttime = utc_now + timedelta(minutes=remainder, seconds=-utc_now.second, microseconds=-utc_now.microsecond)
        sleeptime = (nexttime - utc_now).total_seconds()
        print("Sleeping till " + nexttime.strftime("%H:%M") + ' UTC')
        print("Next API call is in " + str(round(sleeptime)) + " seconds")
        sleep(1)
        keep_sleeping = sleeptime > 2
    save_current_jams()
    sleep(60)

while True:
    loop()