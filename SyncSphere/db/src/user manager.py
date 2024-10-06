from user_management.db_manager import UserManager

# Initialize UserManager
user_manager = UserManager()

# User inputs for registration
username = input("Enter your username: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

# Register the user
user_manager.register_user(username, email, password)

# Close connections when done
user_manager.close_connections()
