def lookup_package(hash_table, package_id):
    package = hash_table.search(package_id)
    if package:
        return {
            "Address": package["Address"],
            "Deadline": package["Deadline"],
            "City": package["City"],
            "Zip": package["Zip"],
            "Mass": package["Mass"],
            "Status": package["Status"],
            "Delivery Time": package["Delivery Time"]
        }
    else:
        return "Package not found"

if __name__ == '__main__':
    from packagehashtable import hash_table
    print(lookup_package(hash_table, 3))
