from csv_parser import *


location_data = create_location_data('data/location_data.csv')

def closest_destination(truck):
    destinations_from_location = location_data.get(truck.get('location'))
    package_destinations = [package.get('addr') for package in truck.get('cargo') if package.get('status') != 'Delivered']
    
    valid_destinations = {dest: dist for dest, dist in destinations_from_location.items() if dest in package_destinations}
    min_address = min(valid_destinations, key=valid_destinations.get)
    
    return {min_address: valid_destinations[min_address]}

        
def return_to_hub(truck):
    return {'4001 South 700 East': location_data.get(truck.get('location')).get('4001 South 700 East')}
