from controller.output import *
from controller.controller import *


def main(target_id=None, start_time=None, end_time=None):
    truck_1, truck_2, truck_3 = initialize_and_process_trucks(end_time)
    trucks = [truck_1, truck_2, truck_3]

    if target_id:
        lookup_package_by_id(target_id, trucks)

    print_route_data(trucks)

    print(f"COMBINED DISTANCE TRAVELED: {round(sum([truck.get('distance') for truck in trucks]), 2)}")


main(target_id=20, start_time=time(8, 25), end_time=time(9, 25))
