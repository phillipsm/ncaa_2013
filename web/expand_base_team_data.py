import json
import csv

# merge base team data with incoming results data.
# the result is what we feed to d3

# Our team data with lats and longs and so on
json_data=open('team_data_base.json')
team_data = json.load(json_data)
json_data.close()

# Our incoming result data
json_data=open('raw_results.json')
result_data = json.load(json_data)
json_data.close()

for team_datum in team_data:
	team_datum["match_ups"] = {}
	wins_list = []
	loses_list = []
	
	# We're building our win and lost lists
	# and using them to augment our base team data
	for result in result_data:
		# Get wins
		if result['winner'] and result['winner'] == team_datum['name']:

			winning_score = result['homeScore']
			losing_score = result['awayScore']
			if result['homeScore'] < result['awayScore']:
				winning_score = result['awayScore']
				losing_score = result['homeScore']
			wins_object = {"round": int(result['round']), "loser": result['loser'], "winning_score": int(winning_score), "losing_score": int(losing_score)}
			wins_list.append(wins_object)
			
		# Get losses
		if result['loser'] and result['loser'] == team_datum['name']:
			winning_score = result['homeScore']
			losing_score = result['awayScore']
			if result['homeScore'] < result['awayScore']:
				winning_score = result['awayScore']
				losing_score = result['homeScore']
			loses_object = {"round": int(result['round']), "winner": result['winner'], "winning_score": int(winning_score), "losing_score": int(losing_score)}
			loses_list.append(loses_object)

	team_datum["match_ups"]["wins" ] = wins_list;
	team_datum["match_ups"]["loses" ] = loses_list;

# Data should be complete now. Contains all the team data and the win/loss matchup data. hollah.
print json.dumps(team_data, sort_keys=True, indent=4, separators=(',', ': '))		