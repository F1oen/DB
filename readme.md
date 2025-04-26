# Donation Tracker Application

This is a simple Python application to manage and track donations for a charity organization.

The application allows users to:
- Create, view, update, and delete donors, events, volunteers, and donations
- Search donations by donor or event
- Export donors and donations to CSV files

## Features

- **CRUD Operations**: Fully functional Create, Read, Update, and Delete for all entities
- **Database Normalization**: Designed following 3NF principles for efficiency
- **Search Donations**: Easily search for donations by donor or event
- **CSV Export**: Export donor and donation information to `.csv` files
- **Error Handling**: Prevents deletion of donors or events with existing donations

## Technologies Used

- Python 3
- SQLite (via sqlite3)
- CSV module for exports

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository.
3. Run the `main.py` file:

```bash
 python main.py
```
