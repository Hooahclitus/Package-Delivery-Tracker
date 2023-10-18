from itertools import chain

from model.hash_table import HashTable


# Function to read a CSV file and create a dictionary of location data
def create_location_data():
    file_path = "data/location_data.csv"

    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        data = file.read()
        [_, *address_list], *distance_list = [
            line.split(",") for line in data.splitlines()
        ]

        location_data = {
            address: {k: float(v) for k, v in zip(address_list, distances)}
            for [address, *distances] in distance_list
        }

        return location_data


# Function to read a CSV file and create a hash table of package data
def create_package_data():
    keys = [
        "id",
        "address",
        "city",
        "state",
        "zip",
        "deadline",
        "weight",
        "req_truck",
        "delayed",
        "truck_grp",
        "wrong_address",
        "has_deadline",
        "status",
        "delivery_time",
    ]

    file_path = "data/package_data.csv"

    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        data = file.read()
        package_list = [line.split(",") for line in data.splitlines()]

        package_table = HashTable(40)

        for pid, *rest in package_list:
            zipped_data = list(
                chain.from_iterable(zip(keys, [int(pid)] + rest + ["At Hub", "N/A"]))
            )
            package_table.assoc(int(pid), HashTable(7, *zipped_data))

        return package_table


# Function to group packages by their address
def group_by_address(packages):
    grouped = HashTable()
    for package in packages:
        address = package.get("address")
        existing_packages = grouped.get(address) or []
        existing_packages.append(package)
        grouped.assoc(address, existing_packages)
    return grouped


# Function to update the status and delivery time of a list of packages
def update_status_and_time(packages, status, time):
    for package in packages:
        package.assoc("status", status)
        package.assoc("delivery_time", time)
