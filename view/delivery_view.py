from itertools import zip_longest


# Format package data into a single line for table display
def format_package_line(package):
    if package is None:
        return "|" + " " * 54 + "|"
    return ("| ID: {:>2} | STATUS: {:<9} | DELIVERY TIME: {:<8} |"
            .format(*package.get('id', 'status'), str(package.get('delivery_time'))))


# Output travel logs and distances for all trucks
def output_travel_data(trucks):
    id_1, id_2, id_3 = [truck.get('id') for truck in trucks]
    log_1, log_2, log_3 = [truck.get('log') for truck in trucks]
    distances = [round(truck.get('distance'), 2) for truck in trucks]
    zipped_logs = list(zip_longest(log_1, log_2, log_3, fillvalue=None))

    # Templates for header and footer
    header_template = "+{0}-Truck {1}{0}++{0}-Truck {2}{0}++{0}-Truck {3}{0}+"
    footer_template = ("+{0}-Distance Traveled: {1:<4}{0}+"
                       "+{0}-Distance Traveled: {2:<4}{0}+"
                       "+{0}-Distance Traveled: {3:<4}{0}+")

    print(header_template.format('-' * 23, id_1, id_2, id_3))

    for package_1, package_2, package_3 in zipped_logs:
        print(format_package_line(package_1) + format_package_line(package_2) + format_package_line(package_3))

    print(footer_template.format('-' * 15, *distances))
    print(f"Combined Distance Traveled: {round(sum(distances), 2)}")
    print("\n")


# Find and output details of a package by its ID
def find_package_by_id(target_id, trucks):
    for truck in trucks:
        for package in truck.get('log'):
            if package.get('id') == target_id:
                output = ("| ID: {:>2} | Address: {:<} | Status: {:<9} | Delivery Time: {:<8} |"
                          .format(*package.get('id', 'address', 'status'), str(package.get('delivery_time'))))
                output_length = len(output)

                top_bottom = "+{}+".format("-" * (output_length - 2))

                print(top_bottom)
                print(output)
                print(top_bottom, "\n")
