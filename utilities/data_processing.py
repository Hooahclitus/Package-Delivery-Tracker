import csv

from model.hash_table import HashTable


# Function to read a CSV file and create a dictionary of location data
def create_location_data(file_path):
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)[1:]
        location_data = {row[0]: {header[i]: float(row[i + 1]) for i in range(len(header))} for row in csv_reader}
    return location_data


# Function to read a CSV file and create a hash table of package data
def create_package_data(file_path):
    keys = ['id', 'address', 'city', 'state', 'zip', 'deadline', 'weight', 'req_truck', 'delayed', 'truck_grp',
            'wrong_address', 'has_deadline', 'status', 'delivery_time']
    package_table = HashTable(40)
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        # Create a hash table for each package and populate it
        for package in csv_reader:
            tbl = HashTable(13,
                            *[item for key, val in zip(keys, [package[i] for i in range(12)] + ['At Hub', 'N/A']) for
                              item in (key, val)])
            tbl.assoc('id', int(tbl.get('id')))
            package_table.assoc(int(package[0]), tbl)
    return package_table


# Function to group packages by their address
def group_by_address(packages):
    grouped = HashTable()
    for package in packages:
        address = package.get('address')
        existing_packages = grouped.get(address) or []
        existing_packages.append(package)
        grouped.assoc(address, existing_packages)
    return grouped


# Function to update the status and delivery time of a list of packages
def update_status_and_time(packages, status, time):
    for package in packages:
        package.assoc('status', status)
        package.assoc('delivery_time', time)
