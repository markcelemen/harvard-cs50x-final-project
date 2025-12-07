# Library Management System
#### Video Demo: https://youtu.be/Pr_r5xuD_Fs

#### Description:
Hi, I'm **Mark**, and this is my final project for Harvard CS50x, titled **Library Management System**. This project is a simulation designed to demonstrate the core functionalities of a library management system, including tracking books, authors, publishers, borrowers, and borrowing records. It showcases how such a system could work in a controlled environment, providing an interactive learning experience.

The system allows users to perform operations such as adding, updating, and deleting records, as well as generating basic reports. While the application simulates a library's processes, it is not intended for actual use by library staff or institutions. Instead, it serves as a project to demonstrate database design, web development, and programming skills. The project is implemented in Python using the **Flask** framework and runs on the CS50x IDE.

### Database Model
The foundation of this system is a relational database designed to simulate the operations of a library. The database consists of several interconnected tables that represent key entities.

Here’s a brief overview of the tables included in the database:
- **Authors Table**: Simulates storing information about authors, including their name, contact details, and alias.
- **Publishers Table**: Contains sample details about publishers, such as name, address, and contact information.
- **Books Table**: Tracks simulated book data, including title, publication year, publisher, author, and availability status.
- **Borrowers Table**: Simulates information about library borrowers, such as name, email address, and phone number.
- **BorrowRecords Table**: Tracks borrowing details, such as the date borrowed, expected return date, and any late fees.
- **BorrowerOffenses Table**: Records offenses, such as overdue returns or damaged books, to simulate consequences for borrowers.

Below is a screenshot of the **Library Management System Database Model**:

![Library Management System Database Model](images/LibraryManagementSystem%20DB%20Model.png)

### Creating and Populating the Database
To simulate real-world functionality, the database was designed and populated with random data.

**Creating the Database**:
The database schema was created using SQL scripts. Relationships between tables were carefully defined using foreign keys to demonstrate best practices in relational database design.

Here’s a screenshot of the **Creating the Database** process:

![Creating the Database](images/creating%20the%20database.png)

**Populating the Database**:
Sample data was added to the database to simulate real-world scenarios. This included authors, publishers, books, borrowers, and borrowing records.

Here’s a screenshot of the **Populating the Database** process:

![Populating the Database](images/populating%20the%20database.png)

### Running the Project
The project was developed on the **CS50x IDE** and is optimized for that environment. To run the project locally, you’ll need to set up an SQLite database and install the necessary dependencies.

### Files
The Library Management System consists of 21 files (excluding the database model and SQL script). The main components are:
- **app.py**: The main Flask application that handles the backend logic for records management, transactions, and reports.
- **templates/**: Contains HTML files for the frontend interface, such as the landing page, records page, transactions page, and reports page.
- **static/**: Contains CSS and JavaScript files for styling and interactivity.

### Core Features
The system has three primary functionalities: **Records Management**, **Transactions**, and **Reports**. Below is a summary of each section:

Here’s a screenshot of the **Index** page:

![Index Page](images/index.png)

#### 1. Records Management
Allows users to view the data for each table in the database. Users can view a list of authors, books, borrowers, and other relevant data stored in the database.

Here’s a screenshot of the **Records Management** page:

![Records Management](images/records.png)

#### 2. Transactions
Allows users to add, delete, or update records in the database. For example, users can mark a book as available, update return dates, or remove outdated records.

Here’s a screenshot of the **Transactions** page:

![Transactions](images/transactions.png)

#### 3. Reports
Generates reports, such as the **Top 10 Most Borrowed Books** and the **Top 10 Borrowers**. These reports demonstrate how to analyze borrowing patterns and identify popular books and borrowers.

Here’s a screenshot of the **Reports** page:

![Reports](images/reports.png)

### Design Choices
When designing this system, I made several key decisions:

- **Relational Database**: A relational database structure was chosen to demonstrate how data normalization and foreign keys ensure data integrity and prevent redundancy.
- **Flask Framework**: Flask was selected for its simplicity and flexibility, making it ideal for small-to-medium-sized projects like this simulation.
- **Reports Section**: The inclusion of a reports feature showcases how to use SQL queries for analysis and insights.

### Conclusion
The **Library Management System** project demonstrates the basic principles of library management using a database-backed design and web interface. While not intended for real-world use, it showcases my understanding of SQL, Python, and web development.

I hope you find this project insightful and engaging. Feel free to explore the code and try it out!
