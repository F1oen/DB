import database
import export
import datetime

def main_menu():
    while True:
        print("\n--- Donation Tracker ---")
        print("1. Add Donor")
        print("2. Add Event")
        print("3. Add Volunteer")
        print("4. Add Donation")
        print("5. View Donors")
        print("6. View Donations")
        print("7. Delete Donor")
        print("8. Delete Event")
        print("9. Search Donations by Donor")
        print("10. Search Donations by Event")
        print("11. Export Donors to CSV")
        print("12. Export Donations to CSV")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_donor()
        elif choice == "2":
            add_event()
        elif choice == "3":
            add_volunteer()
        elif choice == "4":
            add_donation()
        elif choice == "5":
            view_donors()
        elif choice == "6":
            view_donations()
        elif choice == "7":
            delete_donor()
        elif choice == "8":
            delete_event()
        elif choice == "9":
            search_donations_by_donor()
        elif choice == "10":
            search_donations_by_event()
        elif choice == "11":
            export.export_donors()
        elif choice == "12":
            export.export_donations()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def add_donor():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    business_name = input("Business Name (optional): ")
    postcode = input("Postcode: ")
    house_number = input("House Number: ")
    phone_number = input("Phone Number: ")
    database.add_donor(first_name, last_name, business_name, postcode, house_number, phone_number)
    print("Donor added successfully.")

def add_event():
    event_name = input("Event Name: ")
    room_info = input("Room Information: ")
    booking_datetime = input("Booking Date and Time (YYYY-MM-DD HH:MM): ")
    cost = float(input("Cost: "))
    database.add_event(event_name, room_info, booking_datetime, cost)
    print("Event added successfully.")

def add_volunteer():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone Number: ")
    database.add_volunteer(first_name, last_name, phone_number)
    print("Volunteer added successfully.")

def add_donation():
    amount = float(input("Donation Amount: "))
    date_of_donation = input("Date of Donation (YYYY-MM-DD): ")
    source = input("Source (Donor/Event): ").capitalize()
    donor_id = input("Donor ID (leave blank if not applicable): ")
    event_id = input("Event ID (leave blank if not applicable): ")
    volunteer_id = input("Volunteer ID (leave blank if not applicable): ")
    gift_aid = input("Gift Aid (yes/no): ").lower() == 'yes'
    notes = input("Notes (optional): ")

    donor_id = int(donor_id) if donor_id else None
    event_id = int(event_id) if event_id else None
    volunteer_id = int(volunteer_id) if volunteer_id else None

    database.add_donation(amount, date_of_donation, source, donor_id, event_id, volunteer_id, gift_aid, notes)
    print("Donation added successfully.")

def view_donors():
    donors = database.view_donors()
    for donor in donors:
        print(donor)

def view_donations():
    donations = database.view_donations()
    for donation in donations:
        print(donation)

def delete_donor():
    donor_id = int(input("Enter Donor ID to delete: "))
    if database.delete_donor(donor_id):
        print("Donor deleted successfully.")
    else:
        print("Cannot delete donor with existing donations.")

def delete_event():
    event_id = int(input("Enter Event ID to delete: "))
    if database.delete_event(event_id):
        print("Event deleted successfully.")
    else:
        print("Cannot delete event with existing donations.")

def search_donations_by_donor():
    donor_id = int(input("Enter Donor ID to search donations: "))
    donations = database.search_donations_by_donor(donor_id)
    for donation in donations:
        print(donation)

def search_donations_by_event():
    event_id = int(input("Enter Event ID to search donations: "))
    donations = database.search_donations_by_event(event_id)
    for donation in donations:
        print(donation)

if __name__ == "__main__":
    database.create_tables()
    main_menu()
#     conn.close()
