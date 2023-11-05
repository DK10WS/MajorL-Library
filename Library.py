import mysql.connector
import tkinter as tk
from tkinter import messagebox

conn = mysql.connector.connect(
    host="localhost",
    user="ENTER OWN DETAILS",
    password="ENETR OWN DETAILS",
    database="LibraryDB"
)
cursor = conn.cursor()

root = tk.Tk()
root.title("Library Management System")

def check_book_availability():
    book_id = book_id_entry.get()

    book_query = "SELECT Copies FROM Books WHERE BookID = %s"
    cursor.execute(book_query, (book_id,))
    copies = cursor.fetchone()

    if copies is not None and copies[0] > 0:
        messagebox.showinfo("Book Availability", "The book is available.")
    else:
        messagebox.showinfo("Book Availability", "The book is not available.")

def add_new_user():
    user_name = user_name_entry.get()
    address = address_entry.get()
    contact_info = contact_info_entry.get()
    library_card_number = library_card_entry.get()

    query = "INSERT INTO Users (UserName, Address, ContactInfo, LibraryCardNumber) VALUES ('%s', '%s', '%s','%s')"
    cursor.execute(query, (user_name, address, contact_info, library_card_number))
    conn.commit()
    messagebox.showinfo("Success", "User added successfully.")

def issue_book():
    user_id = user_id_entry.get()
    book_id = book_id_entry.get()

    user_query = "SELECT * FROM Users WHERE UserID = %s"
    cursor.execute(user_query, (user_id,))
    user = cursor.fetchone()

    book_query = "SELECT * FROM Books WHERE BookID = %s AND Copies > 0"
    cursor.execute(book_query, (book_id,))
    book = cursor.fetchone()

    if user is None:
        messagebox.showerror("Error", "User not found.")
    elif book is None:
        messagebox.showerror("Error", "Book not available or not found.")
    else:
        query = "INSERT INTO CirculationRecords (BookID, UserID) VALUES (%s, %s)"
        cursor.execute(query, (book_id, user_id))
        conn.commit()
        messagebox.showinfo("Success", "Book issued successfully.")
        cursor.execute("UPDATE Books SET Copies = Copies - 1 WHERE BookID = %s", (book_id,))
        conn.commit()

def check_fines():
    user_id = user_id_entry.get()
    query = "SELECT * FROM Fines WHERE UserID = %s"
    cursor.execute(query, (user_id,))
    fines = cursor.fetchall()

    if fines:
        fine_info = "\n".join([f"Fine ID: {fine[0]}, Amount: {fine[1]}, Reason: {fine[3]}" for fine in fines])
        messagebox.showinfo("Fines", fine_info)
    else:
        messagebox.showinfo("Fines", "No fines found for the user.")

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    publisher = publisher_entry.get()
    isbn = isbn_entry.get()
    copies = copies_entry.get()

    query = "INSERT INTO Books (Title, Author, Publisher, ISBN, Copies) VALUES ('%s', '%s', '%s', '%s', '%s')"
    cursor.execute(query, (title, author, publisher, isbn, copies))
    conn.commit()
    messagebox.showinfo("Success", "Book added successfully.")

user_name_label = tk.Label(root, text="User Name:")
user_name_entry = tk.Entry(root)

address_label = tk.Label(root, text="Address:")
address_entry = tk.Entry(root)

contact_info_label = tk.Label(root, text="Contact Info:")
contact_info_entry = tk.Entry(root)

library_card_label = tk.Label(root, text="Library Card Number:")
library_card_entry = tk.Entry(root)

user_id_label = tk.Label(root, text="User ID:")
user_id_entry = tk.Entry(root)

book_id_label = tk.Label(root, text="Book ID:")
book_id_entry = tk.Entry(root)

title_label = tk.Label(root, text="Title:")
title_entry = tk.Entry(root)

author_label = tk.Label(root, text="Author:")
author_entry = tk.Entry(root)

publisher_label = tk.Label(root, text="Publisher:")
publisher_entry = tk.Entry(root)

isbn_label = tk.Label(root, text="ISBN:")
isbn_entry = tk.Entry(root)

copies_label = tk.Label(root, text="Copies:")
copies_entry = tk.Entry(root)

check_availability_button = tk.Button(root, text="Check Book Availability", command=check_book_availability)
add_user_button = tk.Button(root, text="Add New User", command=add_new_user)
issue_book_button = tk.Button(root, text="Issue Book", command=issue_book)
check_fines_button = tk.Button(root, text="Check Fines", command=check_fines)
add_book_button = tk.Button(root, text="Add Book", command=add_book)

user_name_label.grid(row=0, column=0)
user_name_entry.grid(row=0, column=1)
address_label.grid(row=1, column=0)
address_entry.grid(row=1, column=1)
contact_info_label.grid(row=2, column=0)
contact_info_entry.grid(row=2, column=1)
library_card_label.grid(row=3, column=0)
library_card_entry.grid(row=3, column=1)

user_id_label.grid(row=4, column=0)
user_id_entry.grid(row=4, column=1)
book_id_label.grid(row=5, column=0)
book_id_entry.grid(row=5, column=1)

title_label.grid(row=6, column=0)
title_entry.grid(row=6, column=1)
author_label.grid(row=7, column=0)
author_entry.grid(row=7, column=1)
publisher_label.grid(row=8, column=0)
publisher_entry.grid(row=8, column=1)
isbn_label.grid(row=9, column=0)
isbn_entry.grid(row=9, column=1)
copies_label.grid(row=10, column=0)
copies_entry.grid(row=10, column=1)

check_availability_button.grid(row=11, column=0, columnspan=2)
add_user_button.grid(row=12, column=0, columnspan=2)
issue_book_button.grid(row=13, column=0, columnspan=2)
check_fines_button.grid(row=14, column=0, columnspan=2)
add_book_button.grid(row=15, column=0, columnspan=2)

root.mainloop()

conn.close()

