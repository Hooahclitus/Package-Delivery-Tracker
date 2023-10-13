import csv

from model.hash_table import HashTable


def create_location_data(file_path):
    # Open provided CSV file
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)

        # Extract and store column headers, excluding the first column
        header = next(csv_reader)[1:]

        # Create a dictionary mapping the first column values to dictionaries of the remaining column values
        location_data = {row[0]: {header[i]: float(row[i + 1]) for i in range(len(header))} for row in csv_reader}

    return location_data


def create_package_data(file_path):
    # Define keys for mapping package data
    keys = ['id', 'address', 'city', 'state', 'zip', 'deadline', 'weight', 'req_truck', 'delayed', 'truck_grp',
            'wrong_address', 'has_deadline', 'status', 'delivery_time']

    # Initialize a hash table to store package data
    package_table = HashTable(40)

    # Open provided CSV file
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)

        # Iterate over packages, mapping package data to a hash table and adding it to the main package_table
        for package in csv_reader:
            # Create a hash table for each package, initializing with key-value pairs from keys and package data
            tbl = HashTable(13,
                            *[item for key, val in zip(keys, [package[i] for i in range(12)] + ['At Hub', 'N/A'])
                              for item in (key, val)])

            # Casts ID value from hash table to int and associates with key 'id'
            tbl.assoc('id', int(tbl.get('id')))

            # Insert the constructed hash table into package_table using the package ID as the key
            package_table.assoc(int(package[0]), tbl)

    return package_table


def group_by_address(packages):
    grouped = HashTable()

    if not isinstance(packages, list):
        packages = [packages]

    for package in packages:
        address = package.get('address')
        existing_packages = grouped.get(address)
        if existing_packages:
            existing_packages.append(package)
            grouped.assoc(address, existing_packages)
        else:
            grouped.assoc(address, [package])

    return grouped


def update_status_and_time(packages, status, time):
    for package in packages:
        package.assoc('status', status)
        package.assoc('delivery_time', time)
