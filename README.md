# Package Delivery Tracking Program

## Overview
This program is designed to track and manage deliveries for a delivery service. It allows users to view delivery data within specified time frames, find package details by ID, and manage trucks and their routes. The program utilizes a custom hash table implementation for efficient data storage and retrieval, crafted as a learning exercise, rather than using Python's built-in dictionary.

## Features
1. **Track Deliveries**: View detailed logs of package deliveries based on user-specified start and end times.
2. **Package Lookup**: Search for a package's status and details using its ID.
3. **Manage Trucks**: Track and manage multiple trucks, their routes, and the packages they carry.
4. **User-Friendly Interface**: A simple and intuitive command-line interface for users to interact with the program.
5. **Custom Hash Table**: The program uniquely incorporates a custom hash table implementation, developed to deepen understanding of data structures.

## Modules Overview
- `hash_table.py`: Contains the custom `HashTable` class used for data storage.
- `data_processing.py`: Provides utilities for reading CSV data and processing package information.
- `time_conversion.py`: Utilities for converting between distances and times.
- `delivery_controller.py`: Defines the logic for managing deliveries, processing truck routes, and updating package statuses.
- `truck_controller.py`: Defines the logic for managing individual trucks, including their location, cargo, and logs.
- `user_controller.py`: Manages user input and interactions, including parsing user requests.
- `delivery_view.py`: Defines the views for displaying delivery data.
- `user_view.py`: Defines the views for user interactions, including input prompts and error messages.
- `main.py`: The entry point of the program.

## Usage
1. Run `main.py` to start the program.
2. Follow the prompts in the main menu to choose an action.
3. For time-based queries, input the desired start and end times when prompted.
4. For package lookups, input the package ID when prompted.

## Installation and Setup
1. Ensure you have Python 3.11.5 installed on your system.
2. Clone the repository or download the code.
3. Navigate to the project directory in the terminal or command prompt.
4. Run `main.py` to start the program.

## License
This project is licensed under the MIT License. Please see the `LICENSE` file for more details.
