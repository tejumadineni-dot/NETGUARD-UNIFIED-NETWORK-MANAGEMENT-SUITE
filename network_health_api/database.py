# SQLite database library
import sqlite3


# Create database connection
conn = sqlite3.connect("network_history.db")

# Create cursor object
cursor = conn.cursor()


# Create alerts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    ip TEXT,

    threat_type TEXT,

    bandwidth TEXT,

    timestamp TEXT

)
""")
# Create trusted IPs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS trusted_ips(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    ip TEXT UNIQUE

)
""")

# Save changes
conn.commit()

# Close connection
conn.close()


print("Database created successfully")