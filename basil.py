import requests
import json
import pandas as pd
from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt

response=requests.get("https://cusap-iot.uc.r.appspot.com/system/listSystems")
response_dict=response.json()

system_dictionary = {}
for system in response_dict["_msg"]["payload"]:
  system_dictionary[system["name"]] = system["_id"]

hydrokit = system_dictionary["Node MCU 1.0"]

humidity = {"systemId": hydrokit, "timePeriod": "hour", "reading": "Air-Humidity"}
data = requests.get("https://cusap-iot.uc.r.appspot.com/system/getReadings", params = humidity)

humidity_d = data.json()
indiv_data = humidity_d["_msg"]["payload"]

for i in range(0, len(indiv_data)):
  del indiv_data[i]["_id"]
  del indiv_data[i]["system"]
  del indiv_data[i]["issue"]
  indiv_data[i]["timestamp"] = datetime.strptime(indiv_data[i]["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
  print(indiv_data[i])

hour_change = pd.DataFrame.from_records(indiv_data).groupby(["timestamp"]).mean()
plot_data = hour_change.to_numpy()

plt.figure(figsize=(20,3))
plt.title("Air Humidity of Basil")
plt.xlabel("Time (hr)")
plt.ylabel("Air Humidity (%)")
plt.plot(hour_change.index, plot_data)
plt.show()
