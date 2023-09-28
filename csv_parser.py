import csv


class CSV_Parser:
    @staticmethod
    def create_location_data(file_path):
        # Open the CSV file.
        with open(file_path, mode="r", encoding="utf-8-sig") as file:
            csv_reader = csv.reader(file)
            
            # Extract column headers (excluding the first column).
            header = next(csv_reader)[1:]
            
            # Create a dictionary where the key is the first column value and the values are the subsequent columns as key-value pairs.
            location_data = {row[0]: {header[i]: float(row[i+1]) for i in range(len(header))} for row in csv_reader}
        
        return location_data
