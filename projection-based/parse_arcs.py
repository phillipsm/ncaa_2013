import csv
import json

teams = csv.reader(open("teams.csv","rb"))

json_data=open('results.json')
results = json.load(json_data)
json_data.close()

for result in results:
	print result

#for row in teams:    
#    print row