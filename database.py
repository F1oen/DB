import sqlite3

def connect():
    return sqlite3.connect('donation_tracker.db')

def create_tables():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            business_name TEXT,
            postcode TEXT,
            house_number TEXT,
            phone_number TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            room_info TEXT,
            booking_datetime TEXT,
            cost REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            date_of_donation TEXT NOT NULL,
            source TEXT CHECK(source IN ('Donor', 'Event')),
            donor_id INTEGER,
            event_id INTEGER,
            volunteer_id INTEGER,
            gift_aid BOOLEAN,
            notes TEXT,
            FOREIGN KEY (donor_id) REFERENCES Donors(id),
            FOREIGN KEY (event_id) REFERENCES Events(id),
            FOREIGN KEY (volunteer_id) REFERENCES Volunteers(id)
        )
    ''')

    conn.commit()
    conn.close()

def add_donor(first_name, last_name, business_name, postcode, house_number, phone_number):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Donors (first_name, last_name, business_name, postcode, house_number, phone_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, business_name, postcode, house_number, phone_number))
    conn.commit()
    conn.close()

def add_event(event_name, room_info, booking_datetime, cost):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Events (event_name, room_info, booking_datetime, cost)
        VALUES (?, ?, ?, ?)
    ''', (event_name, room_info, booking_datetime, cost))
    conn.commit()
    conn.close()

def add_volunteer(first_name, last_name, phone_number):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Volunteers (first_name, last_name, phone_number)
        VALUES (?, ?, ?)
    ''', (first_name, last_name, phone_number))
    conn.commit()
    conn.close()

def add_donation(amount, date_of_donation, source, donor_id, event_id, volunteer_id, gift_aid, notes):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Donations (amount, date_of_donation, source, donor_id, event_id, volunteer_id, gift_aid, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (amount, date_of_donation, source, donor_id, event_id, volunteer_id, gift_aid, notes))
    conn.commit()
    conn.close()

def view_donors():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Donors')
    donors = cursor.fetchall()
    conn.close()
    return donors

def view_donations():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Donations')
    donations = cursor.fetchall()
    conn.close()
    return donations

def delete_donor(donor_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Donations WHERE donor_id = ?', (donor_id,))
    if cursor.fetchone():
        conn.close()
        return False
    cursor.execute('DELETE FROM Donors WHERE id = ?', (donor_id,))
    conn.commit()
    conn.close()
    return True

def delete_event(event_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Donations WHERE event_id = ?', (event_id,))
    if cursor.fetchone():
        conn.close()
        return False
    cursor.execute('DELETE FROM Events WHERE id = ?', (event_id,))
    conn.commit()
    conn.close()
    return True

def search_donations_by_donor(donor_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Donations WHERE donor_id = ?', (donor_id,))
    donations = cursor.fetchall()
    conn.close()
    return donations

def search_donations_by_event(event_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Donations WHERE event_id = ?', (event_id,))
    donations = cursor.fetchall()
    conn.close()
    return donations
