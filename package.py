def group_by_address(packages):
    grouped = {}

    if not isinstance(packages, list):
        packages = [packages]

    for package in packages:
        address = package.get('address')
        if address in grouped:
            grouped[address].append(package)
        else:
            grouped[address] = [package]

    return grouped


def update_status_and_time(packages, status, time):
    for package in packages:
        package.assoc('status', status)
        package.assoc('delivery_time', str(time))
