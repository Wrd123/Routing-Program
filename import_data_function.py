# import_data_function.py
import csv
from packages import *
from hash_table import ChainingHashTable

# Global data structures for the system.
hash_table = ChainingHashTable()
distance_data = []
address_data = []

# Load package data from a CSV file and populate the hash table.
def load_packages(filename):
    with open(filename, newline='') as file:
        csv_reader = csv.reader(file, delimiter=",")
        # Process each row in the CSV file.
        for row in csv_reader:
            # Extract package attributes from the current row to create a package instance.
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = int(row[4])
            deadline = row[5]
            weight = int(row[6])
            notes = row[7]
            # Insert the package into the hash table with its ID serving as the key.
            hash_table.insert(package_id, Package(package_id, address, city, state, zip_code, deadline, weight, notes))

# Load distance data from a CSV file and complete the symmetric distance matrix.
def load_distances(filename):
    with open(filename, newline='') as file:
        csv_reader = csv.reader(file, delimiter=",")
        # Append each row from the CSV file into the distance_data list.
        for row in csv_reader:
            distance_data.append(row)
        # Iterate over all indices to populate the full distance matrix.
        for i in range(len(distance_data)):
            for j in range(len(distance_data)):
                distance_data[i][j] = distance_data[j][i]

# Load address data from a CSV file, extracting only the address field.
def load_addresses(filename):
    with open(filename, newline='') as file:
        csv_reader = csv.reader(file, delimiter=",")
        # Process each row and store the address (located at index 2) in the address_data list.
        for row in csv_reader:
            address_data.append(row[2])
