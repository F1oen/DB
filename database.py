# database.py
import sqlite3
from datetime import datetime

DB_NAME = 'donation_tracker.db'

def create_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    with create_connection() as conn:
        c = conn.cursor()
        # Donor Table
        c.execute('''CREATE TABLE IF NOT EXISTS donor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            surname TEXT NOT NULL,
            business_name TEXT,
            postcode TEXT,
            house_number TEXT,
            phone_number TEXT
        )''')

        # Event Table
        c.execute('''CREATE TABLE IF NOT EXISTS event (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            room_info TEXT,
            booking_datetime TEXT,
            cost REAL
        )''')

        # Volunteer Table
        c.execute('''CREATE TABLE IF NOT EXISTS volunteer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            surname TEXT NOT NULL,
            phone_number TEXT
        )''')

        # Donation Table
        c.execute('''CREATE TABLE IF NOT EXISTS donation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            source_type TEXT CHECK(source_type IN ('Donor', 'Event')),
            source_id INTEGER NOT NULL,
            gift_aid INTEGER,
            notes TEXT,
            volunteer_id INTEGER,
            FOREIGN KEY (volunteer_id) REFERENCES volunteer(id)
        )''')

        conn.commit()

# Example CRUD: Add donor
def add_donor(first_name, surname, business_name, postcode, house_number, phone_number):
    with create_connection() as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO donor (first_name, surname, business_name, postcode, house_number, phone_number)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (first_name, surname, business_name, postcode, house_number, phone_number))
        conn.commit()

def get_all_donors():
    with create_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM donor")
        return c.fetchall()

# Add similar functions for event, volunteer, donation CRUD and search
