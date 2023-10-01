from truck import *
from csv_parser import *


location_data = create_location_data('data/location_data.csv')

def closest_delivery_location(truck):
    destinations_from_location = location_data.get(truck.get('location'))
    package_destinations = [address for address, _ in truck.get('cargo').items()]
    
    valid_destinations = {dest: dist for dest, dist in destinations_from_location.items() if dest in package_destinations}
    min_address = min(valid_destinations, key=valid_destinations.get)
    
    return {min_address: valid_destinations[min_address]}

# TODO remove if necessary or modify
def move_to_closest_destination(truck):
    if truck.get('cargo'):
        destination = closest_delivery_location(truck)
        (address, distance) = list(destination.items())[0]

        update_location(truck, address)
        update_arrive_time(truck, distance)
        update_depart_time(truck)
        update_distance_traveled(truck, distance)

        return truck
    return None

def return_to_hub(truck):
    if not truck.get('cargo'):
        address = '4001 South 700 East'
        distance = location_data.get(truck.get('location')).get(address)

        update_location(truck, address)
        update_distance_traveled(truck, distance)

        return truck
    return None
