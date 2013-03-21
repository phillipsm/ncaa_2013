import math
import json
from pprint import pprint
import urllib2

def get_coord():
    json_data=open('team_data_small.json')

    data = json.load(json_data)
    json_data.close()
#    print data['pacific']['freebase']
    
    for key in data:
        print data[key]['freebase']
        fb = json.load(urllib2.urlopen(data[key]['freebase']))
        print fb['property']['/location/location/geolocation']
        



def distance_on_unit_sphere(lat1, long1, lat2, long2):

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
    


get_coord()