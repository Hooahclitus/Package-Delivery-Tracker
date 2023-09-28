from csv_parser import *


location_data = create_location_data('data/location_data.csv')

# todo: rename to closest_destination
def shortest_destination(truck):
    destinations_from_location = location_data.get(truck.get('location'))
    package_destinations = [package.get('addr') for package in truck.get('cargo')]
    valid_destinations = [(destination, distance) for destination, distance in destinations_from_location.items() if destination in package_destinations]
    min_distance = min(valid_destinations, key=lambda kv: kv[1])

    return min_distance
