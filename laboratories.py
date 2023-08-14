class Facility:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def format_info(self):
        return f"{self.name}_{self.cost}"

    @staticmethod
    def enter_facility_info():
        name = input("Enter Facility name: ")
        cost = input("Enter Facility cost: ")
        return Facility(name, cost)

    @staticmethod
    def display_facilities(facilities):
        print("Facility Name     Cost")
        print("------------------------")
        for facility in facilities:
            print(f"{facility.name:16} {facility.cost:>5}")

    @staticmethod
    def write_list_to_file(facilities, filename):
        with open(filename, "w") as file:
            for facility in facilities:
                file.write(f"{facility.format_info()}\n")

    @staticmethod
    def read_from_file(filename):
        facilities = []
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 2:
                    name, cost = parts
                    facility = Facility(name, cost)
                    facilities.append(facility)
        return facilities

# Sample data: facilities.txt (data file provided)
facilities = Facility.read_from_file("facilities.txt")

# Display list of facilities
Facility.display_facilities(facilities)
