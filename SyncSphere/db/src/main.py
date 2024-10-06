import mysql.connector
from mysql.connector import Error
import bcrypt
import logging

logging.basicConfig(level=logging.ERROR, filename='app.log')

def add_user(username, email, password):
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    try:
        conn1 = mysql.connector.connect(
            host='localhost',
            database='db1',
            user='your_user',
            password='your_password'
        )
        
        if conn1.is_connected():
            cursor1 = conn1.cursor()
            cursor1.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
                (username, email, password_hash)
            )
            user_id = cursor1.lastrowid
            conn1.commit()

            conn2 = mysql.connector.connect(
                host='localhost',
                database='db2',
                user='your_user',
                password='your_password'
            )

            if conn2.is_connected():
                cursor2 = conn2.cursor()
                cursor2.execute(
                    "INSERT INTO user_data (user_id, username, email, created_at) VALUES (%s, %s, %s, NOW())",
                    (user_id, username, email)
                )
                conn2.commit()
                print("User added successfully!")

    except Error as e:
        logging.error(f"Error adding user: {e}")
    
    finally:
        if conn1.is_connected():
            cursor1.close()
            conn1.close()
        if conn2.is_connected():
            cursor2.close()
            conn2.close()

def update_user(user_id, username=None, email=None):
    try:
        conn1 = mysql.connector.connect(
            host='localhost',
            database='db1',
            user='your_user',
            password='your_password'
        )

        if conn1.is_connected():
            cursor1 = conn1.cursor()
            query = "UPDATE users SET "
            params = []
            if username:
                query += "username = %s, "
                params.append(username)
            if email:
                query += "email = %s, "
                params.append(email)

            query = query.rstrip(', ') + " WHERE user_id = %s"
            params.append(user_id)

            cursor1.execute(query, tuple(params))
            conn1.commit()

            conn2 = mysql.connector.connect(
                host='localhost',
                database='db2',
                user='your_user',
                password='your_password'
            )

            if conn2.is_connected():
                cursor2 = conn2.cursor()
                cursor2.execute(
                    "UPDATE user_data SET username = %s, email = %s WHERE user_id = %s",
                    (username, email, user_id)
                )
                conn2.commit()
                print("User updated successfully!")

    except Error as e:
        logging.error(f"Error updating user: {e}")
    
    finally:
        if conn1.is_connected():
            cursor1.close()
            conn1.close()
        if conn2.is_connected():
            cursor2.close()
            conn2.close()

def delete_user(user_id):
    try:
        conn1 = mysql.connector.connect(
            host='localhost',
            database='db1',
            user='your_user',
            password='your_password'
        )

        if conn1.is_connected():
            cursor1 = conn1.cursor()
            cursor1.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            conn1.commit()

            conn2 = mysql.connector.connect(
                host='localhost',
                database='db2',
                user='your_user',
                password='your_password'
            )

            if conn2.is_connected():
                cursor2 = conn2.cursor()
                cursor2.execute("DELETE FROM user_data WHERE user_id = %s", (user_id,))
                conn2.commit()
                print("User deleted successfully!")

    except Error as e:
        logging.error(f"Error deleting user: {e}")
    
    finally:
        if conn1.is_connected():
            cursor1.close()
            conn1.close()
        if conn2.is_connected():
            cursor2.close()
            conn2.close()

def register_user(username, email, password):
    # Basic validation (you can enhance this as needed)
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return

    try:
        # Check if the email already exists in DB1
        conn1 = mysql.connector.connect(
            host='localhost',
            database='db1',
            user='your_user',
            password='your_password'
        )

        if conn1.is_connected():
            cursor1 = conn1.cursor()
            cursor1.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
            if cursor1.fetchone()[0] > 0:
                print("Email already in use.")
                return

            # Proceed to add user
            add_user(username, email, password)

    except Error as e:
        logging.error(f"Error during user registration: {e}")

    finally:
        if conn1.is_connected():
            cursor1.close()
            conn1.close()

# Example usage
register_user('john_doe', 'john@example.com', 'password123')
update_user(1, email='newemail@example.com')
delete_user(1)
