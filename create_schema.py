import sqlite3

# Define file names
schema_sql_file = "schema.sql"
database_file = "schema.db"

# Connect to SQLite (creates schema.db if it doesn't exist)
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Read and execute schema.sql
with open(schema_sql_file, "r") as f:
    schema_sql = f.read()
    cursor.executescript(schema_sql)  # Executes multiple statements

# Commit and close
conn.commit()
conn.close()

print(f"Database '{database_file}' created successfully.")
