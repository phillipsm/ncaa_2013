import json
import csv

# read in team_data_complete
# convert to csv

# slug-name,name,latitude,longitude
# indiana, Indiana University, 23, -94

json_data=open('../team_data_complete.json')

data = json.load(json_data)
json_data.close()

c = csv.writer(open("teams.csv", "wb"))
c.writerow(["slug","name","seed","latitude","longitude","alive"])

for key in data:
	c.writerow([key, key, data[key]['seed'], data[key]['latitude'], data[key]['longitude'], 'true'])
	
	#print data[key]
	