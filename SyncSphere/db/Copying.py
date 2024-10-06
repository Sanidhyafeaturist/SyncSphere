import mysql.connector
from datetime import datetime, timedelta

# Database configuration
db1_config = {
    'user': 'your_db1_user',
    'password': 'your_db1_password',
    'host': 'localhost',
    'database': 'db1'
}

db2_config = {
    'user': 'your_db2_user',
    'password': 'your_db2_password',
    'host': 'localhost',
    'database': 'db2'
}

def sync_data():
    # Connect to db1
    db1_conn = mysql.connector.connect(**db1_config)
    db1_cursor = db1_conn.cursor()

    # Connect to db2
    db2_conn = mysql.connector.connect(**db2_config)
    db2_cursor = db2_conn.cursor()

    # Fetch users from db1
    db1_cursor.execute("SELECT user_id, username, email FROM users")
    users = db1_cursor.fetchall()

    for user in users:
        user_id, username, email = user

        # Insert or update in db2
        db2_cursor.execute("""
            INSERT INTO user_data (user_id, username, email)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE username = %s, email = %s
        """, (user_id, username, email, username, email))

    # Commit changes and close connections
    db2_conn.commit()
    db1_cursor.close()
    db2_cursor.close()
    db1_conn.close()
    db2_conn.close()

if __name__ == "__main__":
    sync_data()
