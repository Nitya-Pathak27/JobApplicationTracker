import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@Nitya2710",
    database = "job_tracker_db"
)

cursor = db.cursor()
print("Database connected successfully!")