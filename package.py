def group_by_address(truck):
    grouped = {}
    for package in truck.get('cargo'):
        address = package.get('addr')
        if address in grouped:
            grouped[address].append(package)
        else:
            grouped[address] = [package]
    
    truck.update('cargo', grouped)
    return truck

def update_status(packages, status):
    for package in packages:
        package.update('status', status)
