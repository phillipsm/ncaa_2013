import json
import csv
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


# read in team_data_complete
# convert to csv

# slug-name,name,latitude,longitude
# indiana, Indiana University, 23, -94

play_ins = ['liberty', 'middle-tennessee', 'long-island', 'boise-state']

json_data=open('../team_data_complete.json')

partial_data = json.load(json_data)
json_data.close()

json_data=open('raw_team_data.json')

data = json.load(json_data)
json_data.close()


#new team csv looks like this
#teamid,name,seed,team_region,latitude,longitude,freebase,alive




c = csv.writer(open("teams.csv", "wb"))
c.writerow(["teamid","slug","name","team_region","seed","latitude","longitude","alive"])


i = 0
for key in data:
	
	if _slugify(key['team_name']) in partial_data:
		#print _slugify(key['team_name'])
		slugged_team_name = _slugify(key['team_name'])
		c.writerow([i, key['team_name'], slugged_team_name, key['team_region'], key['team_seed'], partial_data[slugged_team_name]['latitude'], partial_data[slugged_team_name]['longitude'], partial_data[slugged_team_name]['freebase'],'true'])
		i = i + 1
	else:
		print "not found: %s" % _slugify(key['team_name'])
	
#	for p in partial_data:
#		if _slugify(key['team_name']) == p:
#			print p
#			print _slugify(key['team_name'])
#			break

	#c.writerow([i, key['team_name'], key['team_seed'], data[key]['seed'], data[key]['latitude'], data[key]['longitude'], 'true'])
	
	