# main.py
from database import initialize_db, add_donor, get_all_donors

def menu():
    while True:
        print("\nDonation Tracker Menu")
        print("1. Add Donor")
        print("2. View All Donors")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            fn = input("First name: ")
            sn = input("Surname: ")
            bn = input("Business name: ")
            pc = input("Postcode: ")
            hn = input("House number: ")
            pn = input("Phone number: ")
            add_donor(fn, sn, bn, pc, hn, pn)
            print("Donor added successfully.")

        elif choice == "2":
            donors = get_all_donors()
            for d in donors:
                print(d)

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    initialize_db()
    menu()
