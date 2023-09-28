def find_shortest_destination(truck, location_data):
    destinations_from_location = location_data.get(truck.get_value('location'))
    package_destinations = [package.get_value('addr') for package in truck.get_value('cargo')]
    valid_destinations = [(destination, distance) for destination, distance in destinations_from_location.items() if destination in package_destinations]
    min_distance = min(valid_destinations, key=lambda kv: kv[1])

    return min_distance
