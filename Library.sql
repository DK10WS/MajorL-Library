CREATE DATABASE LibraryDB;
CREATE TABLE Users (
    UserID INT PRIMARY KEY,        	
    UserName VARCHAR(100),
    Address VARCHAR(255),
    ContactInfo VARCHAR(100),
    LibraryCardNumber VARCHAR(20)
);

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    Publisher VARCHAR(255),
    ISBN VARCHAR(13),
    Copies INT
);

CREATE TABLE CirculationRecords (
    RecordID INT PRIMARY KEY,
    BookID INT,
    UserID INT,
    DueDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE SET NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE cascade
);

CREATE TABLE Fines (
    FineID INT PRIMARY KEY,
    Amount DECIMAL(10, 2),
    UserID INT,
    Reason VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE cascade
);

-- Create a view to display book information
CREATE VIEW BookView AS
SELECT BookID, Title, Author, Publisher, ISBN, Copies
FROM Books;

-- Create a view to display circulation records
CREATE VIEW CirculationRecordView AS
SELECT CR.RecordID, CR.BookID, B.Title AS BookTitle, U.UserName AS UserName, CR.DueDate, CR.ReturnDate
FROM CirculationRecords CR
INNER JOIN Books B ON CR.BookID = B.BookID
INNER JOIN Users U ON CR.UserID = U.UserID;

-- Create a view to display user information
CREATE VIEW UserView AS
SELECT UserID, UserName, Address, ContactInfo, LibraryCardNumber
FROM Users;


-- Create a view to display fine information
CREATE VIEW FineView AS
SELECT FineID, Amount, U.UserName AS UserName, Reason
FROM Fines F
INNER JOIN Users U ON F.UserID = U.UserID;

-- Create a view to display overdue items
CREATE VIEW OverdueItems AS
SELECT CR.RecordID, B.Title AS BookTitle, U.UserName AS UserName, CR.DueDate
FROM CirculationRecords CR
INNER JOIN Books B ON CR.BookID = B.BookID
INNER JOIN Users U ON CR.UserID = U.UserID
WHERE CR.ReturnDate IS NULL AND CR.DueDate < CURDATE();


INSERT INTO Users (UserID, UserName, Address, ContactInfo, LibraryCardNumber)
VALUES (1, 'Karan', '123 Main St', 'karan@gmail.com', 'LC12345');
INSERT INTO Users (UserID, UserName, Address, ContactInfo, LibraryCardNumber)
VALUES (2, 'saransh', '456 Elm St', 'saransh@gmail.com', 'LC56789');
INSERT INTO Users (UserID, UserName, Address, ContactInfo, LibraryCardNumber)
VALUES (3, 'Dhruv', '789 Oak St', 'dhruv@gmail.com', 'LC98765');



INSERT INTO Books (BookID, Title, Author, Publisher, ISBN, Copies)
VALUES (1, 'Harry potter-Prisorner of Azkaban', 'Jk Rowling', 'Bloomsbury', 'ISBN12345', 20);
INSERT INTO Books (BookID, Title, Author, Publisher, ISBN, Copies)
VALUES (2, 'Harry potter-Chamber of secrets', 'Jk Rowling', 'Bloomsburry', 'ISBN54321', 15);
INSERT INTO Books (BookID, Title, Author, Publisher, ISBN, Copies)
VALUES (3, 'Harry potter-Goblet of fire', 'Jk Rowling', 'Bloomsburry', 'ISBN54341', 25);


INSERT INTO Fines (FineID, Amount, UserID, Reason)
VALUES (1, 10.50, 1, 'Overdue book');
INSERT INTO Fines (FineID, Amount, UserID, Reason)
VALUES (2, 5.75, 2, 'Late return');
INSERT INTO Fines (FineID, Amount, UserID, Reason)
VALUES (3, 15.25, 3, 'Damaged book');


INSERT INTO CirculationRecords (RecordID, BookID, UserID, DueDate, ReturnDate)
VALUES (1, 1, 1, '2023-10-30', NULL);
INSERT INTO CirculationRecords (RecordID, BookID, UserID, DueDate, ReturnDate)
VALUES (2, 2, 1, '2023-11-10', NULL);
INSERT INTO CirculationRecords (RecordID, BookID, UserID, DueDate, ReturnDate)
VALUES (3, 3, 3, '2023-11-05', NULL);



SELECT * FROM Users;
SELECT * FROM Books WHERE Copies > 10;
SELECT * FROM Fines WHERE UserID = 1;
UPDATE Users SET Address = '123 street,NY' WHERE UserID = 2;
UPDATE Users SET Address = '10101 lol' WHERE UserID = 1;
UPDATE Books SET Copies = Copies + 5 WHERE BookID = 3;
DELETE FROM Users WHERE UserID = 4;
DELETE FROM Books WHERE BookID = 2;

-- Drop the CirculationRecords table
-- DROP TABLE IF EXISTS CirculationRecords;

-- Drop the Fines table
-- DROP TABLE IF EXISTS Fines;

-- Drop the Books table
-- DROP TABLE IF EXISTS Books;

-- Drop the Users table
-- DROP TABLE IF EXISTS Users;

-- Drop the LibraryDB database
-- DROP DATABASE IF EXISTS LibraryDB;



