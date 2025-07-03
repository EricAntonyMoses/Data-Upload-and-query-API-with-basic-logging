#  Data Upload and Query API

This project is a backend system built with **FastAPI** that allows users to:

- Upload CSV files
- Validate and store the data in a **SQLite** database
- Query records using RESTful endpoints
- View and test APIs using Swagger UI
- Log all API activity to a log file

---

##  What This Project Does

We created a simple backend application to demonstrate how structured data (in CSV format) can be processed, validated, stored, and retrieved via APIs.

### Main Features:
- **CSV Upload**: Upload a CSV file containing user data (name, age, score).
- **Validation**: Checks for missing or invalid data types.
- **Storage**: Stores data into a SQLite database using SQLAlchemy.
- **Query Endpoints**: Retrieve all records or a specific record by ID.
- **Logging**: Every API request is logged to a file (`api.log`).
- **Swagger UI**: Automatically generated API docs available at `/docs`.

---

##  Technologies Used

- **Python 3**
- **FastAPI**
- **SQLite (via SQLAlchemy)**
- **Pandas** for CSV parsing and validation
- **Pydantic** for data validation
- **Uvicorn** as the ASGI server

---

##  How to Run It Locally

1. Clone or extract the project
2. Open a terminal and navigate to the project folder
3. Run the following:

```bash
# Step 1: Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Start the server
uvicorn main:app --reload
