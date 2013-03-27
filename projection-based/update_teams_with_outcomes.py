import csv

csv_teams = csv.reader(open("teams.csv","rb"))
# skip the header
csv_teams.next()

csv_arcs = csv.reader(open("arcs_gen.csv","rb"))
# skip the header
csv_arcs.next()

arcs = []
for line in csv_arcs:
	arcs.append(line)

csv_out = []

for team_line in csv_teams:
	outcome="true"
	for arc_line in arcs:
		if team_line[0] == arc_line[0] and arc_line[2] == "loss":
			outcome="false"
			
	csv_out.append([team_line[0],team_line[1],team_line[2],team_line[3],team_line[4],team_line[5],team_line[6],team_line[7],outcome])
	
tuo= csv.writer(open("team-updated-outcome.csv", "wb"))
tuo.writerow(["teamid","slug","name","team_region","seed","latitude","longitude","freebase","alive"])
for o in csv_out:
	tuo.writerow(o)