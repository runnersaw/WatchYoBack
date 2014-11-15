from geolocation import GeoLocation

def get_bbox(current_location):
    latitude, longitude = current_location
    loc = GeoLocation.from_degrees(latitude, longitude)
    distance = 1  # 1 kilometer
    SW_loc, NE_loc = loc.bounding_locations(distance)
    # print SW_loc
    # print NE_loc

    sw_string = SW_loc.__str__()
    sw_degrees = sw_string.split('=')[0]
    sw_degrees = sw_degrees[1:-1]
    south = sw_degrees[:7]
    west = sw_degrees[-12:-4]
    
    ne_string = NE_loc.__str__()
    ne_degrees = ne_string.split('=')[0]
    ne_degrees = ne_degrees[1:-1]
    
    north = ne_degrees[:7]
    east = ne_degrees[-12:-4]
    
    return "{},{},{},{}".format(west, south, east, north)

if __name__ == '__main__':
    LOC = (26.062951, -80.238853)
    print get_bbox(LOC)
