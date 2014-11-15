from geolocation import GeoLocation

def get_bbox(current_location):
    print 'no'
    latitude, longitude = current_location
    print 'no'
    loc = GeoLocation.from_degrees(float(latitude), float(longitude))
    print 'no'
    distance = 1  # 1 kilometer
    print 'no'
    SW_loc, NE_loc = loc.bounding_locations(distance)
    print 'no'
    print SW_loc
    print NE_loc
    print 'no'

    sw_string = SW_loc.__str__()
    sw_degrees = sw_string.split('=')[0]
    sw_degrees = sw_degrees[1:-1]
    south = sw_degrees[:7]
    west = sw_degrees[-12:-4]
    print 'no'
    
    ne_string = NE_loc.__str__()
    ne_degrees = ne_string.split('=')[0]
    ne_degrees = ne_degrees[1:-1]
    print 'no'
    
    north = ne_degrees[:7]
    east = ne_degrees[-12:-4]
    print 'no'
    
    return "{},{},{},{}".format(west, south, east, north)

if __name__ == '__main__':
    LOC = (26.062951, -80.238853)
    print get_bbox(LOC)
