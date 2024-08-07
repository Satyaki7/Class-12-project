# import mysql.connector
# from mysql.connector import Error
# import random
# import string
# from tkinter import messagebox

# def generate_booking_id(length=10):
#     return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# def add_booking_record(username, no_passengers, passenger_names, seating, depart, to, dateop):
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='bbit@123',
#             database='users_db'
#         )
#         cursor = conn.cursor()

#         booking_id = generate_booking_id()

#         passenger_names_str = passenger_names

#         cursor.execute('''
#         INSERT INTO bookinghistory (BOOKING_ID, USER, NO_PASSENGERS, PASSENGER_NAMES, SEATING_PREFERENCE, DEPARTURE, ARRIVAL, DATE)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         ''', (booking_id, username, no_passengers, passenger_names_str, seating, depart, to, dateop))

#         conn.commit()
#         print(f"Booking record added successfully with Booking ID: {booking_id}")
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def add_city_and_flights(city, flight1, flight2, flight3, flight4, flight5):
#     if not city or not flight1 or not flight2 or not flight3 or not flight4 or not flight5:
#         print("Error: All fields are required.")
#         return

#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='bbit@123',
#             database='users_db'
#         )
#         cursor = conn.cursor()

#         cursor.execute('''
#             INSERT INTO cities (CITY, FLIGHT1, FLIGHT2, FLIGHT3, FLIGHT4, FLIGHT5)
#             VALUES (%s, %s, %s, %s, %s, %s)
#         ''', (city, flight1, flight2, flight3, flight4, flight5))

#         conn.commit()
#         print("City and flights added successfully.")
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def view_database():
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='bbit@123',
#             database='users_db'
#         )
#         cursor = conn.cursor()

#         cursor.execute("SELECT * FROM users")
#         users = cursor.fetchall()
#         print("Users Table:")
#         for user in users:
#             print(user)
#         print("\n")

#         cursor.execute("SELECT * FROM cities")
#         cities = cursor.fetchall()
#         print("Cities Table:")
#         for city in cities:
#             print(city)
#         print("\n")

#         cursor.execute("SELECT * FROM bookinghistory")
#         bookings = cursor.fetchall()
#         print("Booking History Table:")
#         for booking in bookings:
#             print(booking)
#         print("\n")
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def initialop():
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='bbit@123',
#             database='users_db'
#         )
#         cursor = conn.cursor()

#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             username VARCHAR(255) NOT NULL UNIQUE,
#             password VARCHAR(255) NOT NULL
#         )
#         ''')

#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS cities (
#             CITY VARCHAR(255) PRIMARY KEY,
#             FLIGHT1 VARCHAR(255),
#             FLIGHT2 VARCHAR(255),
#             FLIGHT3 VARCHAR(255),
#             FLIGHT4 VARCHAR(255),
#             FLIGHT5 VARCHAR(255),
#             FLIGHT6 VARCHAR(255),
#             FLIGHT7 VARCHAR(255),
#             FLIGHT8 VARCHAR(255),
#             FLIGHT9 VARCHAR(255),
#             FLIGHT10 VARCHAR(255)
#         )
#         ''')

#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS bookinghistory (
#             BOOKING_ID VARCHAR(255) PRIMARY KEY,
#             USER VARCHAR(255) NOT NULL,
#             NO_PASSENGERS INT,
#             PASSENGER_NAMES TEXT,
#             SEATING_PREFERENCE VARCHAR(255),
#             DEPARTURE VARCHAR(255),
#             ARRIVAL VARCHAR(255),
#             DATE VARCHAR(255)
#         )
#         ''')

#         print("Database setup complete.")
#         view_database()
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def authenticate(username, password):
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='bbit@123',
#             database='users_db'
#         )
#         cursor = conn.cursor()

#         cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
#         user = cursor.fetchone()

#         if user is None:
#             return "user_not_found"

#         cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
#         user = cursor.fetchone()

#         if user:
#             return "authenticated"
#         else:
#             return "incorrect_password"
#     except Error as e:
#         print(f"Error: {e}")
#         return "error"
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def on_login(username, password):
#     if username == "Username" or password == "Password":
#         messagebox.showerror("Error", "Username and password cannot be empty.")
#         return

#     auth_result = authenticate(username, password)

#     if auth_result == "authenticated":
#         messagebox.showinfo("Success", "Signed in successfully!")
#         return True
#     elif auth_result == "user_not_found":
#         messagebox.showerror("Error", "User does not exist.")
#     elif auth_result == "incorrect_password":
#         messagebox.showerror("Error", "Incorrect password.")

# def on_signup(username, password, confirm_password):
#     if username == "Username" or password == "Password":
#         messagebox.showerror("Error", "Username and password cannot be empty.")
#         return
#     elif password != confirm_password:
#         messagebox.showerror("Error", "Passwords do not match.")
#         return

#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='bbit@123',
#             database='users_db'
#         )
#         cursor = conn.cursor()

#         cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
#         user = cursor.fetchone()

#         if user:
#             messagebox.showerror("Error", "Username already exists.")
#         else:
#             cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
#             conn.commit()
#             messagebox.showinfo("Success", "User signed up successfully!")
#             return True
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def searchfli(city_name):
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='bbit@123',
#             database='users_db'
#         )
#         cursor = conn.cursor()

#         city_name_lower = city_name.lower()

#         cursor.execute('''
#         SELECT FLIGHT1, FLIGHT2, FLIGHT3, FLIGHT4, FLIGHT5, FLIGHT6, FLIGHT7, FLIGHT8, FLIGHT9, FLIGHT10
#         FROM cities WHERE LOWER(CITY) = %s
#         ''', (city_name_lower,))
#         flights = cursor.fetchone()

#         if flights:
#             return flights
#         else:
#             return None
#     except Error as e:
#         print(f"Error: {e}")
#         return None
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def get_bookings_by_username(username):
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='bbit@123',
#             database='users_db'
#         )
#         cursor = conn.cursor()

#         cursor.execute('''
#         SELECT BOOKING_ID, DEPARTURE, ARRIVAL, NO_PASSENGERS, SEATING_PREFERENCE, DATE 
#         FROM bookinghistory 
#         WHERE USER = %s
#         ''', (username,))

#         bookings = cursor.fetchall()
#         booking_lists = [list(booking) for booking in bookings]

#         return booking_lists
#     except Error as e:
#         print(f"Error: {e}")
#         return []
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def search_and_delete(unique_id_var):
#     unique_id = unique_id_var.get()
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='bbit@123',
#             database='users_db'
#         )
#         cursor = conn.cursor()

#         cursor.execute("SELECT * FROM bookinghistory WHERE BOOKING_ID=%s", (unique_id,))
#         result = cursor.fetchone()

#         if result:
#             cursor.execute("DELETE FROM bookinghistory WHERE BOOKING_ID=%s", (unique_id,))
#             conn.commit()
#             messagebox.showinfo("Success", "Booking has been cancelled.")
#         else:
#             messagebox.showerror("Error", "Booking not found.")
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()



from tkinter import messagebox
import sqlite3
import pandas as pd
import random
import string


def generate_booking_id(length=10):
    # Generate a random booking ID
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def add_booking_record(username, no_passengers, passenger_names,seating,depart,to,dateop):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Generate a random booking ID
    booking_id = generate_booking_id()

    # Convert the list of passenger names to a single string
    passenger_names_str = passenger_names

    # Insert the booking record into the bookinghistory table
    cursor.execute('''
    INSERT INTO bookinghistory (BOOKING_ID, USER, NO_PASSENGERS, PASSENGER_NAMES,SEATING_PREFERENCE,DEPARTURE,ARRIVAL,DATE)
    VALUES (?, ?, ?, ?, ? ,?,?,?)
    ''', (booking_id, username, no_passengers, passenger_names_str,seating,depart,to,dateop))
    print("Details added to bookinghistory table.",booking_id, username, no_passengers, passenger_names_str,seating,depart,to,dateop)

    conn.commit()
    conn.close()
    print(f"Booking record added successfully with Booking ID: {booking_id}")

def add_city_and_flights(city, flight1, flight2, flight3, flight4, flight5):
    # Check if any input is empty
    if not city or not flight1 or not flight2 or not flight3 or not flight4 or not flight5:
        print("Error: All fields are required.")
        return

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        # Insert the data into the cities table
        cursor.execute('''
            INSERT INTO cities (CITY, FLIGHT1, FLIGHT2, FLIGHT3, FLIGHT4, FLIGHT5)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (city, flight1, flight2, flight3, flight4, flight5))

        conn.commit()
        print("City and flights added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Example usage of the function
def view_database():
    conn = sqlite3.connect('users.db')

    # View all data from the users table
    print("Users Table:")
    users_df = pd.read_sql_query("SELECT * FROM users", conn)
    print(users_df.to_string(index=False))
    print("\n")

    # View all data from the cities table
    print("Cities Table:")
    cities_df = pd.read_sql_query("SELECT * FROM cities", conn)
    print(cities_df.to_string(index=False))
    print("\n")

    # View all data from the history table
    print("Boooking History Table:")
    cities_df = pd.read_sql_query("SELECT * FROM bookinghistory", conn)
    print(cities_df.to_string(index=False))
    print("\n")

    conn.close()


# Call the function to view the users table

def initialop():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Create the users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        CITY TEXT PRIMARY KEY,
        FLIGHT1 TEXT,
        FLIGHT2 TEXT,
        FLIGHT3 TEXT,
        FLIGHT4 TEXT,
        FLIGHT5 TEXT,
        FLIGHT6 TEXT,
        FLIGHT7 TEXT,
        FLIGHT8 TEXT,
        FLIGHT9 TEXT,
        FLIGHT10 TEXT
    )
    ''')

    # Create the bookinghistory table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookinghistory (
        BOOKING_ID TEXT PRIMARY KEY,
        USER TEXT NOT NULL,
        NO_PASSENGERS INTEGER,
        PASSENGER_NAMES TEXT,
        SEATING_PREFERENCE TEXT,
        DEPARTURE TEXT,
        ARRIVAL TEXT,
        DATE TEXT
    )
    ''')
    
    print("Booking history table setup complete.")
    # Execute a query to list all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch and print the results
    tables = cursor.fetchall()
    for table in tables:
        print(table)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database setup complete.")
    view_database()
    
# Function to authenticate the user just checking the login info
def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if username exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    # If username does not exist
    if user is None:
        conn.close()
        return "user_not_found"

    # If username exists, check password
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return "authenticated"
    else:
        return "incorrect_password"

# Function to handle sign-in button click
def on_login(username, password):
    if username == "Username" or password == "Password":
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return

    auth_result = authenticate(username, password)

    if auth_result == "authenticated":
        messagebox.showinfo("Success", "Signed in successfully!")
        return True
    elif auth_result == "user_not_found":
        messagebox.showerror("Error", "User does not exist.")
    elif auth_result == "incorrect_password":
        messagebox.showerror("Error", "Incorrect password.")

# Function to handle sign-up button click
def on_signup(username, password, confirm_password):
    if username == "Username" or password == "Password":
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if username already exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if user:
        messagebox.showerror("Error", "Username already exists.")
    else:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User signed up successfully!")
        return True

    conn.close()
def searchfli(city_name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Convert city_name to lowercase for case-insensitive comparison
    city_name_lower = city_name.lower()

    # Query to retrieve flights for the given city (case-insensitive)
    cursor.execute('SELECT FLIGHT1, FLIGHT2, FLIGHT3, FLIGHT4, FLIGHT5,FLIGHT6,FLIGHT7,FLIGHT8,FLIGHT9,FLIGHT10 FROM cities WHERE LOWER(CITY) = ?', (city_name_lower,))
    flights = cursor.fetchone()

    conn.close()

    if flights:
        return flights
    else:
        return None
# Initialize the database and print the tables
initialop()

def get_bookings_by_username(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Query to retrieve all booking records for the given username
    cursor.execute('''
    SELECT BOOKING_ID, DEPARTURE, ARRIVAL,NO_PASSENGERS, SEATING_PREFERENCE,  DATE 
    FROM bookinghistory 
    WHERE USER = ?
    ''', (username,))

    bookings = cursor.fetchall()
    conn.close()

    # Convert each row to a list
    booking_lists = [list(booking) for booking in bookings]

    return booking_lists
    
def search_and_delete(unique_id_var):
    unique_id = unique_id_var.get()
    conn = sqlite3.connect('users.db')  # Replace with your actual database file
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookinghistory WHERE BOOKING_ID=?", (unique_id,))
    result = cursor.fetchone()

    if result:
        cursor.execute("DELETE FROM bookinghistory WHERE BOOKING_ID=?", (unique_id,))
        conn.commit()
        messagebox.showinfo("Success", "Booking has been cancelled.")
    else:
        messagebox.showerror("Error", "Booking not found.")

    conn.close()
    return True
    
