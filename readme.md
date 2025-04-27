# Donation Tracker Application

This is a simple Python application designed to manage and track donations for a charity organization.

## Features
- **CRUD Operations**: Fully functional Create, Read, Update, and Delete for all entities (Donors, Events, Volunteers, Donations).
- **Database Normalization**: Designed following 3NF principles for efficiency.
- **Search Donations**: Easily search for donations by donor, event, or volunteer.
- **CSV Export**: Export donor and donation information to `.csv` files.
- **Error Handling**: Prevents deletion of donors, events, or volunteers with existing donations.

## Technologies Used
- **Python 3.x**
- **SQLite** (via `sqlite3`)
- **CSV module** (for exports)
- **pytest** (for automated testing) *(Optional, if implemented later)*

## Test Plan

### Objective
To verify that the Donation Tracker application works correctly by testing CRUD operations and search functionality.

### Test Environment
- Python 3.11
- SQLite3
- OS: Windows/Linux/MacOS

### Test Cases

#### Donor CRUD
- [x] Add new donor
- [x] View all donors
- [ ] Edit donor information *(To be implemented)*
- [ ] Delete donor without donations
- [ ] Prevent deletion if donations exist

#### Event CRUD
- [ ] Add new event
- [ ] View all events
- [ ] Edit event
- [ ] Delete event without donations
- [ ] Prevent deletion if donations exist

#### Volunteer CRUD
- [ ] Add volunteer
- [ ] View volunteers
- [ ] Update volunteer
- [ ] Delete volunteer

#### Donation CRUD
- [ ] Add donation (linked to donor or event)
- [ ] View all donations
- [ ] Edit donation
- [ ] Delete donation

#### Search
- [ ] Search donation by donor
- [ ] Search donation by event
- [ ] Search donation by volunteer

### Bugs/Issues
- Deletion constraints not yet implemented.
- Search functions pending development.

### Next Steps
- Complete missing CRUD and search functionality.
- Automate tests (e.g., with `pytest`).
- Add input validation and error handling.

---

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/donation-tracker.git
    ```
3. Install the required dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```
4. Run the `main.py` file:
    ```bash
    python main.py
    ```

## Future Features
- Email notifications for volunteers or donors.
- Advanced reporting and analytics for donations.
- User authentication for managing roles (Admin, Donor, Volunteer).

---
