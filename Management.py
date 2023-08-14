class Management:
    @staticmethod
    def DisplayMenu():
        print("=== Management System Menu ===")
        print("1. Display Doctors List")
        print("2. Display Facilities List")
        print("3. Display Laboratories List")
        print("4. Display Patients List")
        print("5. Exit")
        print("=============================")

    @staticmethod
    def Run():
        while True:
            Management.DisplayMenu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                print("Displaying Doctors List...")
                # Call the method to display doctors list
            elif choice == "2":
                print("Displaying Facilities List...")
                # Call the method to display facilities list
            elif choice == "3":
                print("Displaying Laboratories List...")
                # Call the method to display laboratories list
            elif choice == "4":
                print("Displaying Patients List...")
                # Call the method to display patients list
            elif choice == "5":
                print("Exiting the Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option (1-5).")


if __name__ == "__main__":
    Management.Run()
