-- Create Database
-- CREATE DATABASE LibraryManagementSystem;
-- USE LibraryManagementSystem;

-- Authors Table
CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    middle_initial CHAR(1),
    last_name VARCHAR(50),
    alias VARCHAR(50),
    email_address VARCHAR(50),
    mobile_no VARCHAR(20)
);

-- Publishers Table
CREATE TABLE Publishers (
    publisher_id INT AUTO_INCREMENT PRIMARY KEY,
    publisher_name VARCHAR(50),
    address VARCHAR(100),
    email_address VARCHAR(50),
    mobile_no VARCHAR(20)
);

-- Books Table
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    title VARCHAR(50),
    publication_year INT,
    publisher_id INT,
    author_id INT,
    availability_status VARCHAR(20) DEFAULT 'Available',
    FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id) ON DELETE SET NULL,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE SET NULL
);

-- Borrowers Table
CREATE TABLE Borrowers (
    borrower_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    middle_initial CHAR(1),
    last_name VARCHAR(50),
    email_address VARCHAR(50),
    mobile_no VARCHAR(20)
);

-- BorrowRecords Table
CREATE TABLE BorrowRecords (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    date_borrowed DATE,
    date_expected_returned DATE,
    date_actual_returned DATE,
    late_fees_collected DECIMAL(10,2) DEFAULT 0.00,
    borrower_id INT,
    FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE SET NULL,
    FOREIGN KEY (borrower_id) REFERENCES Borrowers(borrower_id) ON DELETE SET NULL
);

-- Junction Table: BorroweerOffenses
CREATE TABLE BorrowerOffenses (
    offense_id INT AUTO_INCREMENT PRIMARY KEY,
    borrower_id INT,
    offense_date DATE,
    offense_description TEXT,
    FOREIGN KEY (borrower_id) REFERENCES Borrowers(borrower_id)
);

-- Populate Authors Table
INSERT INTO Authors (author_id, first_name, middle_initial, last_name, alias, email_address, mobile_no) VALUES
(1, 'J.K.', 'R', 'Rowling', 'Jo Rowling', 'jkrowling@gmail.com', '+44-123-456-7890'),
(2, 'George', 'R', 'Martin', 'GRR Martin', 'grrmartin@gmail.com', '+1-415-555-1234'),
(3, 'Suzanne', 'C', 'Collins', 'Suzanne Collins', 'suzannecollins@gmail.com', '+1-212-555-9876'),
(4, 'J.R.R.', 'T', 'Tolkien', 'JRR Tolkien', 'jrrtolkien@gmail.com', '+44-20-7946-0958'),
(5, 'Stephen', 'K', 'King', 'Stephen King', 'stephenking@gmail.com', '+1-207-555-3030');

-- Populate Publishers Table
INSERT INTO Publishers (publisher_id, publisher_name, address, email_address, mobile_no) VALUES
(1, 'Bloomsbury Publishing', '50 Bedford Square, London, WC1B 3DP, UK', 'bloomsbury@gmail.com', '+44-20-7631-5600'),
(2, 'Penguin Random House', '1745 Broadway, New York, NY 10019, USA', 'penguinhouse@gmail.com', '+1-212-366-2000'),
(3, 'Scholastic Corporation', '557 Broadway, New York, NY 10012, USA', 'scholastic@gmail.com', '+1-212-343-6100'),
(4, 'HarperCollins Publishers', '195 Broadway, New York, NY 10007, USA', 'harpercollins@gmail.com', '+1-212-207-7000'),
(5, 'Hachette Book Group', '237 Park Avenue, New York, NY 10017, USA', 'hachette@gmail.com', '+1-212-364-1100');

-- Populate Books Table
INSERT INTO Books (book_id, title, publication_year, publisher_id, author_id, availability_status) VALUES
(1, 'Harry Potter and the Sorcerer''s Stone', 1997, 1, 1, 'Available'),
(2, 'A Game of Thrones', 1996, 2, 2, 'Available'),
(3, 'The Hunger Games', 2008, 3, 3, 'Unavailable'),
(4, 'The Fellowship of the Ring', 1954, 4, 4, 'Available'),
(5, 'The Shining', 1977, 5, 5, 'Available'),
(6, 'Harry Potter and the Chamber of Secrets', 1998, 1, 1, 'Available'),
(7, 'A Clash of Kings', 1998, 2, 2, 'Available'),
(8, 'Catching Fire', 2009, 3, 3, 'Available'),
(9, 'The Return of the King', 1955, 4, 4, 'Available'),
(10, 'It', 1986, 5, 5, 'Available'),
(11, 'Harry Potter and the Prisoner of Azkaban', 1999, 1, 1, 'Available'),
(12, 'A Storm of Swords', 2000, 2, 2, 'Unavailable'),
(13, 'Mockingjay', 2010, 3, 3, 'Available'),
(14, 'The Two Towers', 1954, 4, 4, 'Available'),
(15, 'Carrie', 1974, 5, 5, 'Unavailable');

-- Populate Borrowers Table
INSERT INTO Borrowers (borrower_id, first_name, middle_initial, last_name, email_address, mobile_no) VALUES
(1, 'Maria', 'L', 'Santos', 'mariasantos@gmail.com', '+63-909-512-2653'),
(2, 'John', 'A', 'Smith', 'johnsmith@gmail.com', '+1-215-456-7890'),
(3, 'Jake', 'B', 'Doe', 'jakedoe@gmail.com', '+63-922-512-4001'),
(4, 'Emily', 'C', 'Jones', 'emilyjones@gmail.com', '+1-301-555-1122'),
(5, 'Sophia', 'D', 'Lee', 'sophialee@gmail.com', '+63-920-505-3761'),
(6, 'James', 'E', 'Taylor', 'jamestaylor@gmail.com', '+1-415-555-2005'),
(7, 'Liam', 'F', 'White', 'liamwhite@gmail.com', '+63-905-515-4521'),
(8, 'Isabella', 'G', 'Miller', 'isabellamiller@gmail.com', '+1-212-555-3145'),
(9, 'Benjamin', 'H', 'Davis', 'benjamindavis@gmail.com', '+63-939-526-4530'),
(10, 'Ava', 'I', 'Martinez', 'avamartinez@gmail.com', '+1-303-555-7890');

-- Populate BorrowRecords Table
INSERT INTO BorrowRecords (record_id, book_id, date_borrowed, date_expected_returned, date_actual_returned, late_fees_collected, borrower_id) VALUES
(1, 1, '2024-01-10', '2024-01-17', '2024-01-18', 2.50, 1),
(2, 1, '2024-02-01', '2024-02-08', '2024-02-09', 1.00, 1),
(3, 2, '2024-02-15', '2024-02-22', '2024-02-23', 3.00, 2),
(4, 3, '2024-03-01', '2024-03-08', NULL, 0.00, 3),
(5, 4, '2024-04-12', '2024-04-19', NULL, 0.00, 4),
(6, 5, '2024-05-22', '2024-05-29', '2024-06-01', 1.50, 5),
(7, 5, '2024-06-20', '2024-06-27', NULL, 0.00, 5),
(8, 6, '2024-06-02', '2024-06-09', NULL, 0.00, 6),
(9, 7, '2024-07-15', '2024-07-22', NULL, 0.00, 7),
(10, 8, '2024-08-20', '2024-08-27', '2024-08-30', 4.00, 8),
(11, 9, '2024-09-05', '2024-09-12', NULL, 0.00, 9),
(12, 9, '2024-10-01', '2024-10-08', NULL, 0.00, 9),
(13, 10, '2024-10-12', '2024-10-19', NULL, 0.00, 10),
(14, 1, '2024-11-01', '2024-11-08', NULL, 0.00, 1),
(15, 2, '2024-11-15', '2024-11-22', NULL, 0.00, 2),
(16, 3, '2024-12-01', '2024-12-08', NULL, 0.00, 3),
(17, 4, '2024-12-10', '2024-12-17', NULL, 0.00, 4),
(18, 5, '2024-12-18', '2024-12-25', NULL, 0.00, 5),
(19, 6, '2024-01-20', '2024-01-27', NULL, 0.00, 6),
(20, 6, '2024-02-10', '2024-02-17', NULL, 0.00, 6),
(21, 7, '2024-03-10', '2024-03-17', NULL, 0.00, 7),
(22, 7, '2024-04-10', '2024-04-17', NULL, 0.00, 7),
(23, 8, '2024-05-10', '2024-05-17', NULL, 0.00, 8),
(24, 9, '2024-06-01', '2024-06-08', NULL, 0.00, 1),
(25, 9, '2024-07-01', '2024-07-08', NULL, 0.00, 2),
(26, 10, '2024-08-01', '2024-08-08', NULL, 0.00, 3),
(27, 15, '2024-09-01', '2024-09-08', NULL, 0.00, 4),
(28, 1, '2024-10-01', '2024-10-08', NULL, 0.00, 5),
(29, 1, '2024-11-01', '2024-11-08', NULL, 0.00, 1),
(30, 11, '2024-12-01', '2024-12-08', NULL, 0.00, 7),
(31, 12, '2024-01-05', '2024-01-12', NULL, 0.00, 8),
(32, 13, '2024-02-05', '2024-02-12', NULL, 0.00, 9),
(33, 14, '2024-03-05', '2024-03-12', NULL, 0.00, 10),
(34, 1, '2024-01-10', '2024-01-17', '2024-01-18', 2.50, 2),
(35, 3, '2024-02-03', '2024-02-10', NULL, 0.00, 3),
(36, 7, '2024-05-14', '2024-05-21', NULL, 0.00, 6),
(37, 8, '2024-03-25', '2024-04-01', '2024-04-04', 1.50, 4),
(38, 9, '2024-06-03', '2024-06-10', NULL, 0.00, 5),
(39, 1, '2024-09-14', '2024-09-21', '2024-09-23', 0.00, 1),
(40, 10, '2024-11-10', '2024-11-17', '2024-11-20', 3.00, 7),
(41, 5, '2024-06-30', '2024-07-07', NULL, 0.00, 2),
(42, 4, '2024-08-08', '2024-08-15', NULL, 0.00, 3),
(43, 3, '2024-10-05', '2024-10-12', NULL, 0.00, 6),
(44, 2, '2024-11-20', '2024-11-27', NULL, 0.00, 4),
(45, 6, '2024-09-12', '2024-09-19', NULL, 0.00, 5),
(46, 7, '2024-02-20', '2024-02-27', NULL, 0.00, 6),
(47, 1, '2024-01-02', '2024-01-09', NULL, 0.00, 1),
(48, 9, '2024-03-01', '2024-03-08', '2024-03-10', 0.00, 2),
(49, 11, '2024-04-15', '2024-04-22', NULL, 0.00, 3),
(50, 12, '2024-05-10', '2024-05-17', NULL, 0.00, 7);


-- Populate BorrowerOffenses Table 
INSERT INTO BorrowerOffenses (offense_id, borrower_id, offense_date, offense_description) VALUES
(1, 1, '2024-01-18', 'Late return by 1 day (Book ID: 1)'),
(2, 1, '2024-02-09', 'Late return by 1 day (Book ID: 1)'),
(3, 2, '2024-02-23', 'Late return by 1 day (Book ID: 2)'),
(4, 5, '2024-06-01', 'Late return by 3 days (Book ID: 5)'),
(5, 8, '2024-08-30', 'Late return by 3 days (Book ID: 8)'),
(6, 2, '2024-03-10', 'Late return by 2 days (Book ID: 1)'),
(7, 4, '2024-04-04', 'Late return by 3 days (Book ID: 8)'),
(8, 1, '2024-09-23', 'Late return by 2 days (Book ID: 9)'),
(9, 7, '2024-11-20', 'Late return by 3 days (Book ID: 10)'),
(10, 2, '2024-03-10', 'Late return by 2 days (Book ID: 9)'),
(11, 3, '2024-02-10', 'Lost book (Book ID: 3)'),
(12, 4, '2024-04-15', 'Damaged book (Book ID: 4)'),
(13, 5, '2024-07-05', 'Violation of library noise policy'),
(14, 6, '2024-08-12', 'Borrowed more books than allowed'),
(15, 7, '2024-06-18', 'Returned book with pages missing (Book ID: 7)'),
(16, 8, '2024-10-01', 'Failure to show ID when borrowing (Book ID: 8)'),
(17, 9, '2024-11-15', 'Violated library dress code policy'),
(18, 10, '2024-07-20', 'Borrowed book without proper documentation (Book ID: 10)'),
(19, 2, '2024-05-01', 'Failed to return book after multiple reminders (Book ID: 2)'),
(20, 1, '2024-12-01', 'Returned book with excessive markings (Book ID: 1)');
