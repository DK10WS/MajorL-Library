# Library Management System Readme

This is a simple Library Management System (LMS) developed using Python's tkinter for the GUI and MySQL for the database. The LMS allows you to manage users, books, circulation records, and fines. This readme file will guide you through deploying and running the project.

## Prerequisites
- Python (3.6 or later)
- MySQL (make sure you have the MySQL server installed and running)
- MySQL Connector Python (you can install it using `pip install mysql-connector-python`)
- tkinter (usually included in Python installations)

## Database Setup
1. Create a MySQL database named `LibraryDB`.
2. Use the provided SQL script to create the necessary tables and views within the `LibraryDB` database. You can execute the SQL script using a MySQL client or by importing it through a tool like phpMyAdmin.

## Project Deployment
1. Download the provided Python script and save it as `library_management_system.py`.
2. Make sure the MySQL server is running and accessible.
3. Open the `library_management_system.py` file and replace the MySQL connection parameters with your own:
   - `host`: The MySQL server hostname.
   - `user`: The MySQL username.
   - `password`: The MySQL password.
   - `database`: The database name (should be `LibraryDB`).
4. Save the file after making the necessary changes.

## Running the Project
1. Open your terminal or command prompt.
2. Navigate to the directory where you saved `library_management_system.py`.
3. Run the script by executing the following command:

   ```bash
   python library_management_system.py
   ```

4. The Library Management System GUI will open.

## Using the Library Management System
The GUI provides the following features:
- **Check Book Availability**: Enter a book ID to check if a book is available in the library.
- **Add New User**: Add a new user to the library system with their details.
- **Issue Book**: Issue a book to a user by specifying the user ID and book ID. This will also update the number of copies available for the book.
- **Check Fines**: Check fines for a user by entering their user ID.
- **Add Book**: Add a new book to the library database.

## Troubleshooting
- If you encounter any issues with the project or need further assistance, please feel free to reach out for support.

## Project Cleanup
When you're done with the project, you can clean up the database and remove the project files.

1. **Database Cleanup**: To remove the database and tables, you can uncomment and execute the SQL `DROP` statements at the end of the SQL script used for setup. Please be careful when doing this, as it will delete all data in the database.

2. **Project Files Cleanup**: You can simply delete the `library_management_system.py` file to remove the project from your system.

## License
This project is open-source and is provided without any specific license. You are free to modify and distribute it as you see fit.