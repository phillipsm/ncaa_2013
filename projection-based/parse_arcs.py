import csv
import json


import re

_slugify_strip_re = re.compile(r'[^\w\s-]')
_slugify_hyphenate_re = re.compile(r'[-\s]+')
def _slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    
    From Django's "django/template/defaultfilters.py".

	thanks http://code.activestate.com/recipes/577257-slugify-make-a-string-usable-in-a-url-or-filename/
    """
    import unicodedata
    if not isinstance(value, unicode):
        value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(_slugify_strip_re.sub('', value).strip().lower())
    return _slugify_hyphenate_re.sub('-', value)

def get_slugs_and_ids(slug, list_of_teams):
	
	list_of_slugs_and_ids = []
	
	for team in list_of_teams:
		list_of_slugs_and_ids.append({team[2], team[0]})

	return list_of_slugs_and_ids


#loop through results. grab winner, loser names. get ids from teams
#add team ids to arcs.csv

play_ins = ['liberty', 'middle-tennessee', 'long-island', 'boise-state']

csv_reader = csv.reader(open("teams.csv","rb"))

teams = []
for line in csv_reader:
	teams.append(line)

json_data=open('results.json')
results = json.load(json_data)
json_data.close()

to_write_csv = []

for result in results:
	winner = _slugify(result['winner'])
	loser = _slugify(result['loser'])

	if winner and loser and winner not in play_ins and loser not in play_ins:

		for team in teams:
			if team[1] == winner:
				winner_id = team[0]
			elif team[1] == loser:
				loser_id = team[0]
				
		to_write_csv.append([winner_id, loser_id,  "win"])
		to_write_csv.append([loser_id, winner_id,  "loss"])
		
c = csv.writer(open("arcs_gen.csv", "wb"))

c.writerow(["origin","destination","outcome"])
for arc in to_write_csv:
	c.writerow(arc)