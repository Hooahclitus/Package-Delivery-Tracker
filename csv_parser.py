import csv
from hash_table import HashTable

def create_location_data(file_path):
    # Open provided CSV file
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        
        # Extract and store column headers, excluding the first column
        header = next(csv_reader)[1:]
        
        # Create a dictionary mapping the first column values to dictionaries of the remaining column values
        location_data = {row[0]: {header[i]: float(row[i+1]) for i in range(len(header))} for row in csv_reader}
    
    return location_data

def create_package_data(file_path):
    # Define keys for mapping package data
    keys = ['id', 'addr', 'city', 'state', 'zip', 'deadline', 'weight', 'status', 'delivery_time', 'req_truck', 'delayed', 'truck_grp', 'wrong_addr', 'has_deadline']

    # Initialize a hash table to store package data
    package_table = HashTable(40)

    # Open provided CSV file
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)

        # Iterate over packages, mapping package data to a hash table and adding it to the main package_table
        for package in csv_reader:
            # Create a hash table for each package, initializing with key-value pairs from keys and package data
            tbl = HashTable(13, *[item for key, val in zip(keys, [package[i] for i in range(14)]) for item in (key, val)])
            
            # Insert the constructed hash table into package_table using the package ID as the key
            package_table.insert(int(package[0]), tbl)

    return package_table
