import math
import json
from pprint import pprint
import urllib2

# A sandbox of funcs for playing with 2013 NCAA tournament data

center_lat = 38.548165
center_lon = -98.349609

def get_distance():

	# We have lat/lon for all teams now. Get the distance (in miles)
	# between the school and the center of Kansas

	json_data=open('team_data_lat_long.json')

	data = json.load(json_data)
	json_data.close()
	#    print data['pacific']['freebase']

	for key in data:
		#print data[key]
		distance = distance_on_unit_sphere(center_lat, center_lon, data[key]['latitude'], data[key]['longitude'])
		data[key]['distance_from_mdl_nowhere'] = distance * 3960

	serialized_data = json.dumps(data, indent=4, sort_keys=True)
	text_file = open("team_data_complete.json", "w")
	text_file.write(serialized_data)
	text_file.close()

def get_coord():
	
	# Get lat/longs from freebase
	
	json_data=open('team_data_base.json')

	data = json.load(json_data)
	json_data.close()
	#    print data['pacific']['freebase']

	for key in data:
		#print data[key]['freebase']
		fb = json.load(urllib2.urlopen(data[key]['freebase']))

		if '/location/location/geolocation' in fb['property']:
			#print key
			if '/location/geocode/latitude' in fb['property']['/location/location/geolocation']['values'][0]['property']:
				#print 'lat is ' + str(fb['property']['/location/location/geolocation']['values'][0]['property']['/location/geocode/latitude']['values'][0]['value'])
				data[key]['latitude'] = fb['property']['/location/location/geolocation']['values'][0]['property']['/location/geocode/latitude']['values'][0]['value']
			if '/location/geocode/longitude' in fb['property']['/location/location/geolocation']['values'][0]['property']:
				#print 'lat is ' + str(fb['property']['/location/location/geolocation']['values'][0]['property']['/location/geocode/longitude']['values'][0]['value'])
				data[key]['longitude'] = fb['property']['/location/location/geolocation']['values'][0]['property']['/location/geocode/longitude']['values'][0]['value']

	serialized_data = json.dumps(data)
	text_file = open("team_data_lat_long_partial.json", "w")
	text_file.write(serialized_data)
	text_file.close()

def distance_on_unit_sphere(lat1, long1, lat2, long2):

	# Get distance between two lat/longs
	# thanks to http://www.johndcook.com/python_longitude_latitude.html

	# Convert latitude and longitude to 
	# spherical coordinates in radians.
	degrees_to_radians = math.pi/180.0

	# phi = 90 - latitude
	phi1 = (90.0 - lat1)*degrees_to_radians
	phi2 = (90.0 - lat2)*degrees_to_radians

	# theta = longitude
	theta1 = long1*degrees_to_radians
	theta2 = long2*degrees_to_radians

	# Compute spherical distance from spherical coordinates.

	# For two locations in spherical coordinates 
	# (1, theta, phi) and (1, theta, phi)
	# cosine( arc length ) = 
	#    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
	# distance = rho * arc length

	cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
	math.cos(phi1)*math.cos(phi2))
	arc = math.acos( cos )

	# Remember to multiply arc by the radius of the earth 
	# in your favorite set of units to get length.
	return arc