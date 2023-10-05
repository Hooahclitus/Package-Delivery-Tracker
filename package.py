def group_by_address(packages):
    grouped = {}
    for package in packages:
        address = package.get('addr')
        if address in grouped:
            grouped[address].append(package)
        else:
            grouped[address] = [package]
    
    return grouped

def update_package_status(packages, status):
    for package in packages:
        package.assoc('status', status)

def update_package_time(packages, time):
    for package in packages:
        package.assoc('time, str(time)')
