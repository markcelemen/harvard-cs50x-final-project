import os

from cs50 import SQL
from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///LibraryManagementSystem.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Index
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/records")
def records():
    return render_template("records.html")

@app.route("/transactions")
def transactions():
    return render_template("transactions.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")


# Records Management
@app.route("/authors", methods=["GET", "POST"])
def authors():
    if request.method == "POST":
        # Get form data
        author_id = request.form.get("author_id")
        first_name = request.form.get("first_name")
        middle_initial = request.form.get("middle_initial")
        last_name = request.form.get("last_name")
        alias = request.form.get("alias")
        email_address = request.form.get("email_address")
        mobile_no = request.form.get("mobile_no")

        # Query the database for authors based on the form data
        query = "SELECT * FROM Authors WHERE 1=1"
        params = []

        # Check if all fields are empty
        if not author_id and not first_name and not middle_initial and not last_name and not alias and not email_address and not mobile_no:
            # If all fields are empty, show all authors
            authors = db.execute("SELECT * FROM Authors")
        else:
            # Query the database for authors based on the form data
            query = "SELECT * FROM Authors WHERE 1=1"
            params = []

            # Dynamically build query based on filled form fields
            if author_id:
                try:
                    author_id = int(author_id)
                    query += " AND author_id = ?"
                    params.append(author_id)
                except ValueError:
                    return render_template("authors.html", authors=[], message="Invalid Author ID input")
            if first_name:
                query += " AND first_name LIKE ?"
                params.append(f"%{first_name}%")
            if middle_initial:
                query += " AND middle_initial LIKE ?"
                params.append(f"%{middle_initial}%")
            if last_name:
                query += " AND last_name LIKE ?"
                params.append(f"%{last_name}%")
            if alias:
                query += " AND alias LIKE ?"
                params.append(f"%{alias}%")
            if email_address:
                query += " AND email_address LIKE ?"
                params.append(f"%{email_address}%")
            if mobile_no:
                query += " AND mobile_no LIKE ?"
                params.append(f"%{mobile_no}%")
            try:
                # Execute the query with the parameters
                authors = db.execute(query, params)
            except Exception as e:
                # Log the error for debugging
                print(f"Error executing query: {e}")
                return render_template("authors.html", authors=[], message="An error occurred while fetching authors.")

        return render_template("authors.html", authors=authors)

    else:
        authors = db.execute("SELECT * FROM Authors")
        return render_template("authors.html", authors=authors)

@app.route("/publishers", methods=["GET", "POST"])
def publishers():
    if request.method == "POST":
        # Get form data
        publisher_id = request.form.get("publisher_id")
        publisher_name = request.form.get("publisher_name")
        address = request.form.get("address")
        email_address = request.form.get("email_address")
        mobile_no = request.form.get("mobile_no")

        # Query the database for publishers based on the form data
        query = "SELECT * FROM Publishers WHERE 1=1"
        params = []

        # Check if all fields are empty
        if not publisher_id and not publisher_name and not address and not email_address and not mobile_no:
            # If all fields are empty, show all publishers
            publishers = db.execute("SELECT * FROM Publishers")
        else:
            # Query the database for publishers based on the form data
            query = "SELECT * FROM Publishers WHERE 1=1"
            params = []

            # Dynamically build query based on filled form fields
            if publisher_id:
                try:
                    publisher_id = int(publisher_id)
                    query += " AND publisher_id = ?"
                    params.append(publisher_id)
                except ValueError:
                    return render_template("publishers.html", publishers=[], message="Invalid Publisher ID input")
            if publisher_name:
                query += " AND publisher_name LIKE ?"
                params.append(f"%{publisher_name}%")
            if address:
                query += " AND address LIKE ?"
                params.append(f"%{address}%")
            if email_address:
                query += " AND email_address LIKE ?"
                params.append(f"%{email_address}%")
            if mobile_no:
                query += " AND mobile_no LIKE ?"
                params.append(f"%{mobile_no}%")
            try:
                # Execute the query with the parameters
                publishers = db.execute(query, params)
            except Exception as e:
                # Log the error for debugging
                print(f"Error executing query: {e}")
                return render_template("publishers.html", publishers=[], message="An error occurred while fetching publishers.")

        return render_template("publishers.html", publishers=publishers)

    else:
        publishers = db.execute("SELECT * FROM Publishers")
        return render_template("publishers.html", publishers=publishers)

@app.route("/books", methods=["GET", "POST"])
def books():
    if request.method == "POST":
        # Get form data
        book_id = request.form.get("book_id")
        title = request.form.get("title")
        publication_year = request.form.get("publication_year")
        author_id = request.form.get("author_id")
        publisher_id = request.form.get("publisher_id")
        availability_status = request.form.get("availability_status")

        # Query the database for books based on the form data
        query = "SELECT * FROM Books WHERE 1=1"
        params = []

        # Check if all fields are empty
        if not book_id and not title and not publication_year and not author_id and not publisher_id and not availability_status:
            books = db.execute("SELECT * FROM Books")
        else:
            # Dynamically build the query based on the filled form fields
            if book_id:
                try:
                    book_id = int(book_id)
                    query += " AND book_id = ?"
                    params.append(book_id)
                except ValueError:
                    return render_template("books.html", books=[], message="Invalid Book ID input")
            if title:
                query += " AND title LIKE ?"
                params.append(f"%{title}%")
            if publication_year:
                try:
                    publication_year = int(publication_year)
                    query += " AND publication_year = ?"
                    params.append(publication_year)
                except ValueError:
                    return render_template("books.html", books=[], message="Invalid Publication Year input")
            if author_id:
                try:
                    author_id = int(author_id)
                    query += " AND author_id = ?"
                    params.append(author_id)
                except ValueError:
                    return render_template("books.html", books=[], message="Invalid Author ID input")
            if publisher_id:
                try:
                    publisher_id = int(publisher_id)
                    query += " AND publisher_id = ?"
                    params.append(publisher_id)
                except ValueError:
                    return render_template("books.html", books=[], message="Invalid Publisher ID input")
            if availability_status:
                query += " AND availability_status = ?"
                params.append(availability_status)
            try:
                # Execute the query with the parameters
                books = db.execute(query, params)
            except Exception as e:
                # Log the error for debugging
                print(f"Error executing query: {e}")
                return render_template("books.html", books=[], message="An error occurred while fetching books.")

        return render_template("books.html", books=books, message=None)

    else:
        books = db.execute("SELECT * FROM Books")
        return render_template("books.html", books=books, message=None)

@app.route("/borrowers", methods=["GET", "POST"])
def borrowers():
    if request.method == "POST":
        # Get form data
        borrower_id = request.form.get("borrower_id")
        first_name = request.form.get("first_name")
        middle_initial = request.form.get("middle_initial")
        last_name = request.form.get("last_name")
        email_address = request.form.get("email_address")
        mobile_no = request.form.get("mobile_no")

        # Query the database for borrowers based on the form data
        query = "SELECT * FROM Borrowers WHERE 1=1"
        params = []

        # Check if all fields are empty
        if not borrower_id and not first_name and not middle_initial and not last_name and not email_address and not mobile_no:
            # If all fields are empty, show all borrowers
            borrowers = db.execute("SELECT * FROM Borrowers")
        else:
            # Query the database for borrowers based on the form data
            query = "SELECT * FROM Borrowers WHERE 1=1"
            params = []

            # Dynamically build query based on filled form fields
            if borrower_id:
                try:
                    borrower_id = int(borrower_id)
                    query += " AND borrower_id = ?"
                    params.append(borrower_id)
                except ValueError:
                    return render_template("borrowers.html", borrowers=[], message="Invalid Borrower ID input")
            if first_name:
                query += " AND first_name LIKE ?"
                params.append(f"%{first_name}%")
            if middle_initial:
                query += " AND middle_initial LIKE ?"
                params.append(f"%{middle_initial}%")
            if last_name:
                query += " AND last_name LIKE ?"
                params.append(f"%{last_name}%")
            if email_address:
                query += " AND email_address LIKE ?"
                params.append(f"%{email_address}%")
            if mobile_no:
                query += " AND mobile_no LIKE ?"
                params.append(f"%{mobile_no}%")
            try:
                # Execute the query with the parameters
                borrowers = db.execute(query, params)
            except Exception as e:
                # Log the error for debugging
                print(f"Error executing query: {e}")
                return render_template("borrowers.html", borrowers=[], message="An error occurred while fetching borrowers.")

        return render_template("borrowers.html", borrowers=borrowers)

    else:
        borrowers = db.execute("SELECT * FROM Borrowers")
        return render_template("borrowers.html", borrowers=borrowers)

@app.route("/borrowrecords", methods=["GET", "POST"])
def borrowrecords():
    if request.method == "POST":
        # Get form data
        record_id = request.form.get("record_id")
        book_id = request.form.get("book_id")
        date_borrowed = request.form.get("date_borrowed")
        date_expected_returned = request.form.get("date_expected_returned")
        date_actual_returned = request.form.get("date_actual_returned")
        late_fees_collected = request.form.get("late_fees_collected")
        borrower_id = request.form.get("borrower_id")

        # Query the database for borrow records based on the form data
        query = "SELECT * FROM BorrowRecords WHERE 1=1"
        params = []

        # Check if all fields are empty
        if not record_id and not book_id and not date_borrowed and not date_expected_returned and not date_actual_returned and not late_fees_collected and not borrower_id:
            # If all fields are empty, show all borrow records
            borrowrecords = db.execute("SELECT * FROM BorrowRecords")
        else:
            # Query the database for borrow records based on the form data
            query = "SELECT * FROM BorrowRecords WHERE 1=1"
            params = []

            # Dynamically build query based on filled form fields
            if record_id:
                try:
                    record_id = int(record_id)
                    query += " AND record_id = ?"
                    params.append(record_id)
                except ValueError:
                    return render_template("borrowrecords.html", borrowrecords=[], message="Invalid Record ID input")
            if book_id:
                try:
                    book_id = int(book_id)
                    query += " AND book_id = ?"
                    params.append(book_id)
                except ValueError:
                    return render_template("borrowrecords.html", borrowrecords=[], message="Invalid Book ID input")
            if date_borrowed:
                query += " AND date_borrowed = ?"
                params.append(date_borrowed)
            if date_expected_returned:
                query += " AND date_expected_returned = ?"
                params.append(date_expected_returned)
            if date_actual_returned:
                query += " AND date_actual_returned = ?"
                params.append(date_actual_returned)
            if late_fees_collected:
                try:
                    late_fees_collected = int(late_fees_collected)
                    query += " AND late_fees_collected = ?"
                    params.append(late_fees_collected)
                except ValueError:
                    return render_template("borrowrecords.html", borrowrecords=[], message="Invalid Late Fees Collected input")
            if borrower_id:
                try:
                    borrower_id = int(borrower_id)
                    query += " AND borrower_id = ?"
                    params.append(borrower_id)
                except ValueError:
                    return render_template("borrowrecords.html", borrowrecords=[], message="Invalid Borrower ID input")
            try:
                # Execute the query with the parameters
                borrowrecords = db.execute(query, params)
            except Exception as e:
                # Log the error for debugging
                print(f"Error executing query: {e}")
                return render_template("borrowrecords.html", borrowrecords=[], message="An error occurred while fetching borrow records.")

        return render_template("borrowrecords.html", borrowrecords=borrowrecords)

    else:
        borrowrecords = db.execute("SELECT * FROM BorrowRecords")
        return render_template("borrowrecords.html", borrowrecords=borrowrecords)

@app.route("/borroweroffenses", methods=["GET", "POST"])
def borroweroffenses():
    if request.method == "POST":
        # Get form data
        offense_id = request.form.get("offense_id")
        borrower_id = request.form.get("borrower_id")
        offense_date = request.form.get("offense_date")
        offense_description = request.form.get("offense_description")

        # Query the database for borrow offenses based on the form data
        query = "SELECT * FROM BorrowerOffenses WHERE 1=1"
        params = []

        # Check if all fields are empty
        if not offense_id and not borrower_id and not offense_date and not offense_description:
            # If all fields are empty, show all borrow offenses
            borroweroffenses = db.execute("SELECT * FROM BorrowerOffenses")
        else:
            # Query the database for borrow offenses based on the form data
            query = "SELECT * FROM BorrowerOffenses WHERE 1=1"
            params = []

            # Dynamically build query based on filled form fields
            if offense_id:
                try:
                    offense_id = int(offense_id)
                    query += " AND offense_id = ?"
                    params.append(offense_id)
                except ValueError:
                    return render_template("borroweroffenses.html", borroweroffenses=[], message="Invalid Offense ID input")
            if borrower_id:
                try:
                    book_id = int(borrower_id)
                    query += " AND borrower_id = ?"
                    params.append(borrower_id)
                except ValueError:
                    return render_template("borroweroffenses.html", borroweroffenses=[], message="Invalid Borrower ID input")
            if offense_date:
                query += " AND offense_date = ?"
                params.append(offense_date)
            if offense_description:
                query += " AND offense_description LIKE ?"
                params.append(f"%{offense_description}%")
            try:
                # Execute the query with the parameters
                borroweroffenses = db.execute(query, params)
            except Exception as e:
                # Log the error for debugging
                print(f"Error executing query: {e}")
                return render_template("borroweroffenses.html", borroweroffenses=[], message="An error occurred while fetching borrower offenses.")

        return render_template("borroweroffenses.html", borroweroffenses=borroweroffenses)

    else:
        borroweroffenses = db.execute("SELECT * FROM BorrowerOffenses")
        return render_template("borroweroffenses.html", borroweroffenses=borroweroffenses)


# Transactions
@app.route("/authortransactions")
def authortransactions():
    authors = db.execute("SELECT * FROM Authors")
    return render_template("authortransactions.html", authors=authors)

@app.route("/publishertransactions")
def publishertransactions():
    publishers = db.execute("SELECT * FROM Publishers")
    return render_template("publishertransactions.html", publishers=publishers)

@app.route("/booktransactions")
def booktransactions():
    books = db.execute("SELECT * FROM Books")
    # Get unique author_ids and publisher_ids from the books data
    unique_author_ids = db.execute("SELECT DISTINCT author_id FROM Books")
    unique_publisher_ids = db.execute("SELECT DISTINCT publisher_id FROM Books")
    return render_template("booktransactions.html", books=books, unique_author_ids=unique_author_ids, unique_publisher_ids=unique_publisher_ids)

@app.route("/borrowertransactions")
def borrowertransactions():
    borrowers = db.execute("SELECT * FROM Borrowers")
    return render_template("borrowertransactions.html", borrowers=borrowers)

@app.route("/borrowrecordtransactions")
def borrowrecordtransactions():
    borrowrecords = db.execute("SELECT * FROM BorrowRecords")
    # Get unique book_ids and borrower_ids from the borrowrecords data
    unique_book_ids = db.execute("SELECT DISTINCT book_id FROM BorrowRecords ORDER BY book_id")
    unique_borrower_ids = db.execute("SELECT DISTINCT borrower_id FROM BorrowRecords")
    return render_template("borrowrecordtransactions.html", borrowrecords=borrowrecords, unique_book_ids=unique_book_ids, unique_borrower_ids=unique_borrower_ids)

@app.route("/borroweroffensetransactions")
def borroweroffensetransactions():
    borroweroffenses = db.execute("SELECT * FROM BorrowerOffenses")
    # Get unique borrower_ids from borroweroffenses data
    unique_borrower_ids = db.execute("SELECT DISTINCT borrower_id FROM BorrowerOffenses ORDER BY borrower_id")
    return render_template("borroweroffensetransactions.html", borroweroffenses=borroweroffenses, unique_borrower_ids=unique_borrower_ids)

@app.route("/add_author", methods=["POST"])
def add_author():
    # Retrieve data from the form
    first_name = request.form.get("first_name")
    middle_initial = request.form.get("middle_initial")
    last_name = request.form.get("last_name")
    alias = request.form.get("alias")
    email_address = request.form.get("email_address")
    mobile_no = request.form.get("mobile_no")

    # Check if required fields are empty
    if not first_name or not middle_initial or not last_name or not alias or not email_address or not mobile_no:
        authors = db.execute("SELECT * FROM Authors")
        return render_template("authortransactions.html", authors=authors, error="Required fields are missing!")

    # Query the latest author_id
    latest_author = db.execute("SELECT MAX(author_id) AS max_id FROM Authors")
    latest_id = latest_author[0]["max_id"] if latest_author[0]["max_id"] else 0

    # Assign the new author_id manually
    author_id = latest_id + 1

    # Insert new author into the database
    db.execute("""
        INSERT INTO Authors (author_id, first_name, middle_initial, last_name, alias, email_address, mobile_no)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, author_id, first_name, middle_initial, last_name, alias, email_address, mobile_no)

    # Fetch updated data for display
    authors = db.execute("SELECT * FROM Authors")
    return render_template("authortransactions.html", authors=authors)

@app.route("/delete_author", methods=["POST"])
def delete_author():
    # Get the author from the form
    author_id = request.form.get("author_id")

    # Ensure the author is provided
    if not author_id:
        authors = db.execute("SELECT * FROM Authors")
        return render_template("authortransactions.html", authors=authors, error="Please select an author to delete!")

    # Delete the author from the database
    db.execute("DELETE FROM Authors WHERE author_id = ?", author_id)

    # Fetch updated data for display
    authors = db.execute("SELECT * FROM Authors")
    return render_template("authortransactions.html", authors=authors)

@app.route("/update_author", methods=["POST"])
def update_author():
    # Get the form data
    author_id = request.form.get("author_id")
    first_name = request.form.get("first_name")
    middle_initial = request.form.get("middle_initial")
    last_name = request.form.get("last_name")
    alias = request.form.get("alias")
    email_address = request.form.get("email_address")
    mobile_no = request.form.get("mobile_no")

    # Ensure author is provided
    if not author_id:
        authors = db.execute("SELECT * FROM Authors")
        return render_template("authortransactions.html", authors=authors, error="Author ID is required!")

    # Initialize query and parameters
    query = "UPDATE Authors SET"
    params = []

    # Dynamically add fields to the query if they are not empty
    if first_name:
        query += " first_name = ?,"
        params.append(first_name)
    if middle_initial:
        query += " middle_initial = ?,"
        params.append(middle_initial)
    if last_name:
        query += " last_name = ?,"
        params.append(last_name)
    if alias:
        query += " alias = ?,"
        params.append(alias)
    if email_address:
        query += " email_address = ?,"
        params.append(email_address)
    if mobile_no:
        query += " mobile_no = ?,"
        params.append(mobile_no)

    # Remove the trailing comma and add the WHERE clause
    query = query.rstrip(",") + " WHERE author_id = ?"
    params.append(author_id)

    # Execute the query
    db.execute(query, *params)

    # Fetch updated data for display
    authors = db.execute("SELECT * FROM Authors")
    return render_template("authortransactions.html", authors=authors)

@app.route("/add_publisher", methods=["POST"])
def add_publisher():
    # Get the form data
    publisher_name = request.form.get("publisher_name")
    address = request.form.get("address")
    email_address = request.form.get("email_address")
    mobile_no = request.form.get("mobile_no")

    # Ensure all fields are provided
    if not publisher_name or not address or not email_address or not mobile_no:
        publishers = db.execute("SELECT * FROM Publishers")
        return render_template("publishertransactions.html", publishers=publishers, error="All fields are required!")

    # Query the latest publisher_id
    latest_publisher = db.execute("SELECT MAX(publisher_id) AS max_id FROM Publishers")
    latest_id = latest_publisher[0]["max_id"] if latest_publisher[0]["max_id"] else 0

    # Assign the new publisher_id manually
    publisher_id = latest_id + 1

    # Add the publisher to the database
    db.execute("""
        INSERT INTO Publishers (publisher_id, publisher_name, address, email_address, mobile_no)
        VALUES (?, ?, ?, ?, ?)
    """, publisher_id, publisher_name, address, email_address, mobile_no)

    # Fetch updated data for display
    publishers = db.execute("SELECT * FROM Publishers")
    return render_template("publishertransactions.html", publishers=publishers)

@app.route("/delete_publisher", methods=["POST"])
def delete_publisher():
    # Get the publisher from the form
    publisher_id = request.form.get("publisher_id")

    # Ensure the publisher is provided
    if not publisher_id:
        publishers = db.execute("SELECT * FROM Publishers")
        return render_template("publishertransactions.html", publishers=publishers, error="Publisher ID is required!")

    # Delete the publisher from the database
    db.execute("DELETE FROM Publishers WHERE publisher_id = ?", publisher_id)

    # Fetch updated data for display
    publishers = db.execute("SELECT * FROM Publishers")
    return render_template("publishertransactions.html", publishers=publishers)

@app.route("/update_publisher", methods=["POST"])
def update_publisher():
    # Get the form data
    publisher_id = request.form.get("publisher_id")
    publisher_name = request.form.get("publisher_name")
    address = request.form.get("address")
    email_address = request.form.get("email_address")
    mobile_no = request.form.get("mobile_no")

    # Ensure the publisher is provided
    if not publisher_id:
        publishers = db.execute("SELECT * FROM Publishers")
        return render_template("publishertransactions.html", publishers=publishers, error="Publisher ID is required!")

    # Initialize query and parameters
    query = "UPDATE Publishers SET"
    params = []

    # Dynamically add fields to the query if they are not empty
    if publisher_name:
        query += " publisher_name = ?,"
        params.append(publisher_name)
    if address:
        query += " address = ?,"
        params.append(address)
    if email_address:
        query += " email_address = ?,"
        params.append(email_address)
    if mobile_no:
        query += " mobile_no = ?,"
        params.append(mobile_no)

    # Remove the trailing comma and add the WHERE clause
    query = query.rstrip(",") + " WHERE publisher_id = ?"
    params.append(publisher_id)

    # Execute the query
    db.execute(query, *params)

    # Fetch updated data for display
    publishers = db.execute("SELECT * FROM Publishers")
    return render_template("publishertransactions.html", publishers=publishers)

@app.route("/add_book", methods=["POST"])
def add_book():
    # Get the form data
    title = request.form.get("title")
    publication_year = request.form.get("publication_year")
    author_id = request.form.get("author_id")
    publisher_id = request.form.get("publisher_id")
    availability_status = request.form.get("availability_status")

    # Get unique author and publisher ids from books
    unique_author_ids = db.execute("SELECT DISTINCT author_id FROM Books")
    unique_publisher_ids = db.execute("SELECT DISTINCT publisher_id FROM Books")

    # Ensure all fields are provided
    if not title or not publication_year or not author_id or not publisher_id or not availability_status:
        books = db.execute("SELECT * FROM Books")
        return render_template("booktransactions.html", books=books, unique_author_ids=unique_author_ids, unique_publisher_ids=unique_publisher_ids, error="All fields are required!")

    # Query the latest book_id
    latest_book = db.execute("SELECT MAX(book_id) AS max_id FROM Books")
    latest_id = latest_book[0]["max_id"] if latest_book[0]["max_id"] else 0

    # Assign the new book_id manually
    book_id = latest_id + 1

    # Add the book to the database
    db.execute("""
        INSERT INTO Books (book_id, title, publication_year, author_id, publisher_id, availability_status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, book_id, title, publication_year, author_id, publisher_id, availability_status)

    # Fetch updated data for display
    books = db.execute("SELECT * FROM Books")
    return render_template("booktransactions.html", books=books, unique_author_ids=unique_author_ids, unique_publisher_ids=unique_publisher_ids)

@app.route("/delete_book", methods=["POST"])
def delete_book():
    # Get the book from the form
    book_id = request.form.get("book_id")

    # Get unique author and publisher ids from books
    unique_author_ids = db.execute("SELECT DISTINCT author_id FROM Books")
    unique_publisher_ids = db.execute("SELECT DISTINCT publisher_id FROM Books")

    # Ensure the book is provided
    if not book_id:
        books = db.execute("SELECT * FROM Books")
        return render_template("booktransactions.html", books=books, unique_author_ids=unique_author_ids, unique_publisher_ids=unique_publisher_ids, error="Book ID is required!")

    # Delete the book from the database
    db.execute("DELETE FROM Books WHERE book_id = ?", book_id)

    # Fetch updated data for display
    books = db.execute("SELECT * FROM Books")
    return render_template("booktransactions.html", books=books, unique_author_ids=unique_author_ids, unique_publisher_ids=unique_publisher_ids)

@app.route("/update_book", methods=["POST"])
def update_book():
    # Get the form data
    book_id = request.form.get("book_id")
    title = request.form.get("title")
    publication_year = request.form.get("publication_year")
    author_id = request.form.get("author_id")
    publisher_id = request.form.get("publisher_id")
    availability_status = request.form.get("availability_status")

    # Get unique author and publisher ids from books
    unique_author_ids = db.execute("SELECT DISTINCT author_id FROM Books")
    unique_publisher_ids = db.execute("SELECT DISTINCT publisher_id FROM Books")

    # Ensure the book_id is provided
    if not book_id:
        books = db.execute("SELECT * FROM Books")
        return render_template("booktransactions.html", books=books, unique_author_ids=unique_author_ids, unique_publisher_ids=unique_publisher_ids, error="Book ID is required!")

    # Initialize query and parameters
    query = "UPDATE Books SET"
    params = []

    # Dynamically add fields to the query if they are not empty
    if title:
        query += " title = ?,"
        params.append(title)
    if publication_year:
        query += " publication_year = ?,"
        params.append(publication_year)
    if author_id:
        query += " author_id = ?,"
        params.append(author_id)
    if publisher_id:
        query += " publisher_id = ?,"
        params.append(publisher_id)
    if availability_status:
        query += " availability_status = ?,"
        params.append(availability_status)

    # Remove the trailing comma and add the WHERE clause
    query = query.rstrip(",") + " WHERE book_id = ?"
    params.append(book_id)

    # Execute the query
    db.execute(query, *params)

    # Fetch updated data for display
    books = db.execute("SELECT * FROM Books")
    return render_template("booktransactions.html", books=books, unique_author_ids=unique_author_ids, unique_publisher_ids=unique_publisher_ids)

@app.route("/add_borrower", methods=["POST"])
def add_borrower():
    # Get the form data
    first_name = request.form.get("first_name")
    middle_initial = request.form.get("middle_initial")
    last_name = request.form.get("last_name")
    email_address = request.form.get("email_address")
    mobile_no = request.form.get("mobile_no")

    # Ensure all fields are provided
    if not first_name or not middle_initial or not last_name or not email_address or not mobile_no:
        borrowers = db.execute("SELECT * FROM Borrowers")
        return render_template("borrowertransactions.html", borrowers=borrowers, error="All fields are required!")

    # Query the latest borrower_id
    latest_borrower = db.execute("SELECT MAX(borrower_id) AS max_id FROM Borrowers")
    latest_id = latest_borrower[0]["max_id"] if latest_borrower[0]["max_id"] else 0

    # Assign the new borrower_id manually
    borrower_id = latest_id + 1

    # Add the borrower to the database
    db.execute("""
        INSERT INTO Borrowers (borrower_id, first_name, middle_initial, last_name, email_address, mobile_no)
        VALUES (?, ?, ?, ?, ?, ?)
    """, borrower_id, first_name, middle_initial, last_name, email_address, mobile_no)

    # Fetch updated data for display
    borrowers = db.execute("SELECT * FROM Borrowers")
    return render_template("borrowertransactions.html", borrowers=borrowers)

@app.route("/delete_borrower", methods=["POST"])
def delete_borrower():
    # Get the book from the form
    borrower_id = request.form.get("borrower_id")

    # Ensure the borrower is provided
    if not borrower_id:
        borrowers = db.execute("SELECT * FROM Borrowers")
        return render_template("borrowertransactions.html", borrowers=borrowers, error="Borrower ID is required!")

    # Delete the borrower from the database
    db.execute("DELETE FROM Borrowers WHERE borrower_id = ?", borrower_id)

    # Fetch updated data for display
    borrowers = db.execute("SELECT * FROM Borrowers")
    return render_template("borrowertransactions.html", borrowers=borrowers)

@app.route("/update_borrower", methods=["POST"])
def update_borrower():
    # Get the form data
    borrower_id = request.form.get("borrower_id")
    first_name = request.form.get("first_name")
    middle_initial = request.form.get("middle_initial")
    last_name = request.form.get("last_name")
    email_address = request.form.get("email_address")
    mobile_no = request.form.get("mobile_no")

    # Ensure the borrower is provided
    if not borrower_id:
        borrowers = db.execute("SELECT * FROM Borrowers")
        return render_template("borrowertransactions.html", borrowers=borrowers, error="Borrower ID is required!")

    # Initialize query and parameters
    query = "UPDATE Borrowers SET"
    params = []

    # Dynamically add fields to the query if they are not empty
    if first_name:
        query += " first_name = ?,"
        params.append(first_name)
    if middle_initial:
        query += " middle_initial = ?,"
        params.append(middle_initial)
    if last_name:
        query += " last_name = ?,"
        params.append(last_name)
    if email_address:
        query += " email_address = ?,"
        params.append(email_address)
    if mobile_no:
        query += " mobile_no = ?,"
        params.append(mobile_no)

    # Remove the trailing comma and add the WHERE clause
    query = query.rstrip(",") + " WHERE borrower_id = ?"
    params.append(borrower_id)

    # Execute the query
    db.execute(query, *params)

    # Fetch updated data for display
    borrowers = db.execute("SELECT * FROM Borrowers")
    return render_template("borrowertransactions.html", borrowers=borrowers)

@app.route("/add_borrowrecord", methods=["POST"])
def add_borrowrecord():
    # Get the form data
    book_id = request.form.get("book_id")
    date_borrowed = request.form.get("date_borrowed")
    date_expected_returned = request.form.get("date_expected_returned")
    date_actual_returned = request.form.get("date_actual_returned")
    late_fees_collected = request.form.get("late_fees_collected")
    borrower_id = request.form.get("borrower_id")

    # Get unique book and borrower ids from borrow records
    unique_book_ids = db.execute("SELECT DISTINCT book_id FROM Borrowrecords ORDER BY book_id")
    unique_borrower_ids = db.execute("SELECT DISTINCT borrower_id FROM BorrowRecords")

    # Ensure all fields are provided
    if not book_id or not date_borrowed or not date_expected_returned or not date_actual_returned or not late_fees_collected or not borrower_id:
        borrowrecords = db.execute("SELECT * FROM Borrowrecords")
        return render_template("borrowrecordtransactions.html", borrowrecords=borrowrecords, unique_book_ids=unique_book_ids, unique_borrower_ids=unique_borrower_ids, error="All fields are required!")

    # Query the latest borrow record
    latest_borrowrecord = db.execute("SELECT MAX(record_id) AS max_id FROM Borrowerrecords")
    latest_id = latest_publisher[0]["max_id"] if latest_borrowrecord[0]["max_id"] else 0

    # Assign the new record_id manually
    record_id = latest_id + 1

    # Add the borrow record to the database
    db.execute("""
        INSERT INTO BorrowRecords (record_id, date_borrowed, date_expected_returned, date_actual_returned, late_fees_collected, borrower_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, record_id, date_borrowed, date_expected_returned, date_actual_returned, late_fees_collected, borrower_id)

    # Fetch updated data for display
    borrowrecords = db.execute("SELECT * FROM BorrowRecords")
    return render_template("borrowrecordtransactions.html", borrowrecords=borrowrecords, unique_book_ids=unique_book_ids, unique_borrower_ids=unique_borrower_ids)

@app.route("/delete_borrowrecord", methods=["POST"])
def delete_borrowrecord():
    # Get the borrow record from the form
    record_id = request.form.get("record_id")

    # Get unique book and borrower ids from borrow records
    unique_book_ids = db.execute("SELECT DISTINCT book_id FROM BorrowRecords ORDER BY book_id")
    unique_borrower_ids = db.execute("SELECT DISTINCT borrower_id FROM BorrowRecords")

    # Ensure a borrow record is provided
    if not record_id:
        borrowrecords = db.execute("SELECT * FROM BorrowRecords")
        return render_template("borrowrecordtransactions.html", borrowrecords=borrowrecords, unique_book_ids=unique_book_ids, unique_borrower_ids=unique_borrower_ids, error="Record ID is required!")

    # Delete the borrow record from the database
    db.execute("DELETE FROM BorrowRecords WHERE record_id = ?", record_id)

    # Fetch updated data for display
    borrowrecords = db.execute("SELECT * FROM BorrowRecords")
    return render_template("borrowrecordtransactions.html", borrowrecords=borrowrecords, unique_book_ids=unique_book_ids, unique_borrower_ids=unique_borrower_ids)

@app.route("/update_borrowrecord", methods=["POST"])
def update_borrowrecord():
    # Get the form data
    record_id = request.form.get("record_id")
    book_id = request.form.get("book_id")
    date_borrowed = request.form.get("date_borrowed")
    date_expected_returned = request.form.get("date_expected_returned")
    date_actual_returned = request.form.get("date_actual_returned")
    late_fees_collected = request.form.get("late_fees_collected")
    borrower_id = request.form.get("borrower_id")

    # Get unique book and borrower ids from borrow records
    unique_book_ids = db.execute("SELECT DISTINCT book_id FROM Borrowrecords ORDER BY book_id")
    unique_borrower_ids = db.execute("SELECT DISTINCT borrower_id FROM BorrowRecords")

    # Ensure a borrow record is provided
    if not record_id:
        borrowrecords = db.execute("SELECT * FROM BorrowRecords")
        return render_template("borrowrecordtransactions.html", borrowrecords=borrowrecords, unique_book_ids=unique_book_ids, unique_borrower_ids=unique_borrower_ids, error="Record ID is required!")

    # Initialize query and parameters
    query = "UPDATE Borrowrecords SET"
    params = []

    # Dynamically add fields to the query if they are not empty
    if book_id:
        query += " book_id = ?,"
        params.append(book_id)
    if date_borrowed:
        query += " date_borrowed = ?,"
        params.append(date_borrowed)
    if date_expected_returned:
        query += " date_expected_returned = ?,"
        params.append(date_expected_returned)
    if date_actual_returned:
        query += " date_actual_returned = ?,"
        params.append(date_actual_returned)
    if late_fees_collected:
        query += " late_fees_collected = ?,"
        params.append(late_fees_collected)
    if borrower_id:
        query += " borrower_id = ?,"
        params.append(borrower_id)

    # Remove the trailing comma and add the WHERE clause
    query = query.rstrip(",") + " WHERE record_id = ?"
    params.append(record_id)

    # Execute the query
    db.execute(query, *params)

    # Fetch updated data for display
    borrowrecords = db.execute("SELECT * FROM BorrowRecords")
    return render_template("borrowrecordtransactions.html", borrowrecords=borrowrecords, unique_book_ids=unique_book_ids, unique_borrower_ids=unique_borrower_ids)

@app.route("/add_borroweroffense", methods=["POST"])
def add_borroweroffense():
    # Get the form data
    borrower_id = request.form.get("borrower_id")
    offense_date = request.form.get("offense_date")
    offense_description = request.form.get("offense_description")

    # Get unique borrower_ids from borroweroffenses data
    unique_borrower_ids = db.execute("SELECT DISTINCT borrower_id FROM BorrowerOffenses ORDER BY borrower_id")

    # Ensure all fields are provided
    if not borrower_id or not offense_date or not offense_description:
        borroweroffenses = db.execute("SELECT * FROM BorrowerOffenses")
        return render_template("borroweroffensetransactions.html", borroweroffenses=borroweroffenses, unique_borrower_ids=unique_borrower_ids, error="All fields are required!")

    # Query the latest offense_id
    latest_borroweroffense = db.execute("SELECT MAX(offense_id) AS max_id FROM BorrowerOffenses")
    latest_id = latest_borroweroffense[0]["max_id"] if latest_borroweroffense[0]["max_id"] else 0

    # Assign the new offense_id manually
    offense_id = latest_id + 1

    # Add the borrower offense to the database
    db.execute("""
        INSERT INTO BorrowerOffenses (offense_id, borrower_id, offense_date, offense_description)
        VALUES (?, ?, ?, ?)
    """, offense_id, borrower_id, offense_date, offense_description)

    # Fetch updated data for display
    borroweroffenses = db.execute("SELECT * FROM BorrowerOffenses")
    return render_template("borroweroffensetransactions.html", borroweroffenses=borroweroffenses, unique_borrower_ids=unique_borrower_ids)

@app.route("/delete_borroweroffense", methods=["POST"])
def delete_borroweroffense():
    # Get the borrower offense from the form
    offense_id = request.form.get("offense_id")

    # Get unique borrower_ids from borroweroffenses data
    unique_borrower_ids = db.execute("SELECT DISTINCT borrower_id FROM BorrowerOffenses ORDER BY borrower_id")

    # Ensure the borrower offense is provided
    if not offense_id:
        borroweroffenses = db.execute("SELECT * FROM BorrowerOffenses")
        return render_template("borroweroffensetransactions.html", borroweroffenses=borroweroffenses, unique_borrower_ids=unique_borrower_ids, error="Offense ID is required!")

    # Delete the borrower offense from the database
    db.execute("DELETE FROM BorrowerOffenses WHERE offense_id = ?", offense_id)

    # Fetch updated data for display
    borroweroffenses = db.execute("SELECT * FROM BorrowerOffenses")
    return render_template("borroweroffensetransactions.html", borroweroffenses=borroweroffenses, unique_borrower_ids=unique_borrower_ids)

@app.route("/update_borroweroffense", methods=["POST"])
def update_borroweroffense():
    # Get the form data
    offense_id = request.form.get("offense_id")
    borrower_id = request.form.get("borrower_id")
    offense_date = request.form.get("offense_date")
    offense_description = request.form.get("offense_description")

    # Get unique borrower_ids from borroweroffenses data
    unique_borrower_ids = db.execute("SELECT DISTINCT borrower_id FROM BorrowerOffenses ORDER BY borrower_id")

    # Ensure the borrower offense is provided
    if not offense_id:
        borroweroffenses = db.execute("SELECT * FROM BorrowerOffenses")
        return render_template("borroweroffensetransactions.html", borroweroffenses=borroweroffenses, unique_borrower_ids=unique_borrower_ids, error="Offense ID is required!")

    # Initialize query and parameters
    query = "UPDATE BorrowerOffenses SET"
    params = []

    # Dynamically add fields to the query if they are not empty
    if borrower_id:
        query += " borrower_id = ?,"
        params.append(borrower_id)
    if offense_date:
        query += " offense_date = ?,"
        params.append(offense_date)
    if offense_description:
        query += " offense_description = ?,"
        params.append(offense_description)

    # Remove the trailing comma and add the WHERE clause
    query = query.rstrip(",") + " WHERE offense_id = ?"
    params.append(offense_id)

    # Execute the query
    db.execute(query, *params)

    # Fetch updated data for display
    borroweroffenses = db.execute("SELECT * FROM BorrowerOffenses")
    return render_template("borroweroffensetransactions.html", borroweroffenses=borroweroffenses, unique_borrower_ids=unique_borrower_ids)


# Reports
@app.route("/top_books", methods=["POST", "GET"])
def top_books():
    # Get the selected month from the form (default is 0 for entire year)
    month = int(request.form.get("month", 0))

    # SQL Query for top 10 most borrowed books
    if month == 0:
        # Query for entire 2024 (no month filter)
        query = """
        SELECT b.book_id, b.title, b.publication_year,
               a.first_name AS author_first_name, a.last_name AS author_last_name,
               p.publisher_name, b.availability_status, COUNT(br.book_id) AS borrow_count
        FROM BorrowRecords br
        JOIN Books b ON br.book_id = b.book_id
        JOIN Authors a ON b.author_id = a.author_id
        JOIN Publishers p ON b.publisher_id = p.publisher_id
        WHERE strftime('%Y', br.date_borrowed) = '2024'
        GROUP BY b.book_id
        ORDER BY borrow_count DESC
        LIMIT 10;
        """
        # Execute the query
        top_books = db.execute(query)
    else:
        # Query for a specific month
        query = """
        SELECT b.book_id, b.title, b.publication_year,
               a.first_name AS author_first_name, a.last_name AS author_last_name,
               p.publisher_name, b.availability_status, COUNT(br.book_id) AS borrow_count
        FROM BorrowRecords br
        JOIN Books b ON br.book_id = b.book_id
        JOIN Authors a ON b.author_id = a.author_id
        JOIN Publishers p ON b.publisher_id = p.publisher_id
        WHERE strftime('%Y', br.date_borrowed) = '2024' AND strftime('%m', br.date_borrowed) = ?
        GROUP BY b.book_id
        ORDER BY borrow_count DESC
        LIMIT 10;
        """
        # Execute the query for a specific month
        top_books = db.execute(query, f"{month:02}")

    # Fetch updated data for display
    return render_template("topbookreports.html", top_books=top_books, month=month)


@app.route("/top_borrowers", methods=["POST", "GET"])
def top_borrowers():
    # Get the selected month from the form (default is 0 for entire year)
    month = int(request.form.get("month", 0))

    # SQL Query for top 10 borrowers
    if month == 0:
        # Query for entire 2024 (no month filter)
        query = """
        SELECT br.borrower_id, bo.first_name, bo.middle_initial, bo.last_name,
               bo.email_address, bo.mobile_no, COUNT(br.borrower_id) AS borrow_count
        FROM BorrowRecords br
        JOIN Borrowers bo ON br.borrower_id = bo.borrower_id
        WHERE strftime('%Y', br.date_borrowed) = '2024'
        GROUP BY br.borrower_id
        ORDER BY borrow_count DESC
        LIMIT 10;
        """
        # Execute the query
        top_borrowers = db.execute(query)
    else:
        # Query for a specific month
        query = """
        SELECT br.borrower_id, bo.first_name, bo.middle_initial, bo.last_name,
               bo.email_address, bo.mobile_no, COUNT(br.borrower_id) AS borrow_count
        FROM BorrowRecords br
        JOIN Borrowers bo ON br.borrower_id = bo.borrower_id
        WHERE strftime('%Y', br.date_borrowed) = '2024' AND strftime('%m', br.date_borrowed) = ?
        GROUP BY br.borrower_id
        ORDER BY borrow_count DESC
        LIMIT 10;
        """
        # Execute the query for a specific month
        top_borrowers = db.execute(query, f"{month:02}")

    # Fetch updated data for display
    return render_template("topborrowerreports.html", top_borrowers=top_borrowers, month=month)

