class DeliveryInterface:
    def __init__(self, delivery_system):
        self.delivery_system = delivery_system

    def display_package_status(self, package_id):
        if package_id in self.delivery_system.packages:
            package = self.delivery_system.packages[package_id]
            print(f"Package {package_id} - Address: {package['Address']}, Status: {package['Status']}, Delivery Time: {package['Delivery Time']}")
        else:
            print("Package not found.")

    def display_total_mileage(self):
        print(f"Total mileage traveled by all trucks: {self.delivery_system.total_mileage:.2f} miles")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. View package status")
            print("2. View total mileage")
            print("3. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                package_id = int(input("Enter package ID: "))
                self.display_package_status(package_id)
            elif choice == "2":
                self.display_total_mileage()
            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
