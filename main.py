import csv
from datetime import datetime, timedelta
from interface import DeliveryInterface

def normalize_address(addr):
    # Remove newlines, extra spaces, and convert to lowercase.
    return ' '.join(addr.replace('\n', ' ').split()).lower()

class DeliverySystem:
    def __init__(self, package_file, addresses_file, distances_file):
        self.packages = self.load_packages(package_file)
        self.addresses = self.load_addresses(addresses_file)
        self.distances = self.load_distances(distances_file)
        self.trucks = [[], []]  # Two trucks to manage deliveries
        self.total_mileage = 0.0
        self.time = datetime.strptime("08:00 AM", "%I:%M %p")  # Start time
        self.assign_packages_to_trucks()

    def load_packages(self, filename):
        packages = {}
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            # Skip header rows that don't start with a number.
            for row in reader:
                if not row or not row[0].strip():
                    continue
                try:
                    package_id = int(row[0])
                except ValueError:
                    continue
                packages[package_id] = {
                    "Address": row[1].strip(),
                    "City": row[2].strip(),
                    "State": row[3].strip(),
                    "Zip": row[4].strip(),
                    "Deadline": row[5].strip(),
                    "Mass": row[6].strip(),
                    "Notes": row[7].strip() if len(row) > 7 else "",
                    "Status": "At Hub",
                    "Delivery Time": None
                }
        return packages

    def load_addresses(self, filename):
        addresses = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assume each row has one cell containing the address.
                if row and row[0].strip():
                    # Normalize the address upon loading.
                    addresses.append(normalize_address(row[0].strip()))
        return addresses

    def load_distances(self, filename):
        # distances.csv is assumed to contain only numeric values arranged in rows.
        distances = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    # Convert each cell to a float; ignore empty cells.
                    distances.append([float(cell.strip()) for cell in row if cell.strip() != ""])
                except ValueError:
                    continue
        return distances

    def get_index_for_address(self, package_address):
        norm_pkg_addr = normalize_address(package_address)
        for i, addr in enumerate(self.addresses):
            # Check if the package address is contained in the distance file address.
            if norm_pkg_addr in addr or addr in norm_pkg_addr:
                return i
        return None

    def get_distance(self, address1, address2):
        idx1 = self.get_index_for_address(address1)
        idx2 = self.get_index_for_address(address2)
        if idx1 is None or idx2 is None:
            return float('inf')
        # Since the distance matrix is lower triangular,
        # the row index is max(idx1, idx2) and the column index is min(idx1, idx2).
        try:
            return self.distances[max(idx1, idx2)][min(idx1, idx2)]
        except IndexError:
            return float('inf')

    def assign_packages_to_trucks(self):
        for pkg_id, pkg in self.packages.items():
            note = pkg["Notes"].lower()
            if "truck 2" in note or "delayed" in note or "wrong address" in note:
                self.trucks[1].append(pkg_id)
            else:
                self.trucks[0].append(pkg_id)

    def deliver_packages(self):
        for truck in self.trucks:
            location = "4001 South 700 East"  # Hub address
            while truck:
                valid_packages = [
                    p for p in truck
                    if self.get_distance(location, self.packages[p]["Address"]) != float('inf')
                ]
                if not valid_packages:
                    # Mark remaining packages as undeliverable.
                    for p in truck:
                        print(f"Error: Address '{self.packages[p]['Address']}' not found in distance table. Marking package {p} as undeliverable.")
                        self.packages[p]["Status"] = "Undeliverable"
                    break

                next_package = min(
                    valid_packages,
                    key=lambda p: self.get_distance(location, self.packages[p]["Address"])
                )
                distance = self.get_distance(location, self.packages[next_package]["Address"])
                if distance == float('inf'):
                    print(f"Error: Distance for package {next_package} returned infinity. Skipping package.")
                    truck.remove(next_package)
                    continue

                self.total_mileage += distance
                travel_time = timedelta(minutes=(distance / 18) * 60)
                self.time += travel_time
                self.packages[next_package]["Status"] = "Delivered"
                self.packages[next_package]["Delivery Time"] = self.time.strftime("%I:%M %p")
                location = self.packages[next_package]["Address"]
                truck.remove(next_package)

            # After finishing this truck's route, return to the hub.
            hub_distance = self.get_distance(location, "4001 South 700 East")
            if hub_distance != float('inf'):
                self.total_mileage += hub_distance
                self.time += timedelta(minutes=(hub_distance / 18) * 60)

    def display_results(self):
        for package_id, details in self.packages.items():
            print(f"Package {package_id}: {details}")

if __name__ == '__main__':
    # Note: Update the file names as needed.
    delivery_system = DeliverySystem("WGUPS_Package_File.csv", "Addresses.csv", "distances.csv")
    delivery_system.deliver_packages()
    delivery_system.display_results()
    interface = DeliveryInterface(delivery_system)
    interface.run()
