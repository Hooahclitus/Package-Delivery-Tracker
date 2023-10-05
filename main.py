from truck import *
from navigation import *
from csv_parser import *
from datetime import time


package_data = create_package_data('data/package_data.csv')

tk_1 = package_data.get(*range(1, 17))
truck_1 = create_truck(tk_1)
# truck_1.get('cargo')
# del truck_1.get('cargo')['4300 S 1300 E']

# tk_2 = package_data.get(*range(17, 33))
# truck_2 = create_truck(tk_2)

# tk_3 = package_data.get(*range(33, 41))
# truck_3 = create_truck(tk_3)


def process_deliveries(truck, start_time=time(8), end_time=None):
    truck.assoc('depart_time', start_time)

    while truck.get('cargo'):
        (address, distance) = next(iter(closest_delivery_location(truck).items()))
        update_arrive_time(truck, distance)

        match end_time:
            case None:
                deliver_packages(truck, address, distance, 'Delivered')
            case enroute if end_time > truck.get('depart_time') and end_time < truck.get('arrive_time'):
                handle_enroute(truck, address, end_time)
                return truck
            case arrive if end_time == truck.get('arrive_time'):
                handle_arrive(truck, address, distance)
                return truck
            case depart if end_time == truck.get('depart_time'):
                handle_depart(truck)
                return truck
            case _:
                deliver_packages(truck, address, distance, 'Delivered')

    return_to_hub(truck)
    return truck

process_deliveries(truck_1, start_time=time(8), end_time=time(9,10))

for package in truck_1.get('log'):
    print(f"ID: {package.get('id'):4} STATUS: {package.get('status'):12} TIME: {package.get('delivery_time'):10}")

print(f"Distance Traveled: {round(truck_1.get('distance'), 2):<10}")
