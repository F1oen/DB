import csv
import database

def export_donors():
    donors = database.view_donors()
    with open('donors.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'First Name', 'Last Name', 'Business Name', 'Postcode', 'House Number', 'Phone Number'])
        for donor in donors:
            writer.writerow(donor)
    print("Donors exported successfully to donors.csv.")

def export_donations():
    donations = database.view_donations()
    with open('donations.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Amount', 'Date of Donation', 'Source', 'Donor ID', 'Event ID', 'Volunteer ID', 'Gift Aid', 'Notes'])
        for donation in donations:
            writer.writerow(donation)
    print("Donations exported successfully to donations.csv.")
