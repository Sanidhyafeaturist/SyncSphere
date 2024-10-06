# SyncSphere

## Overview
The SyncSphere is a Python-based application that provides functionalities for user registration, updating, and deletion. It utilizes a MySQL database to store user data securely.

## Features
- User registration with email and password
- Update user details
- Delete user accounts
- Input validation and error handling
- Password hashing for secure storage

## Technologies Used
- Python
- MySQL
- bcrypt for password hashing
- MySQL Connector/Python

## Installation

### Prerequisites
- Python 3.x
- MySQL server
- pip for installing packages

### Steps to Install
1. Clone the repository:
   - `git clone https://github.com/Sanidhyafeaturist/SyncSphere.git`
   - `cd SyncSphere`

3. Set up the databases:
   - Run the SQL scripts located in the db directory:
     - `db1.sql` for user credentials
     - `db2.sql` for additional user data

4. Update Configuration:
   - Edit `user_management/config.py` to set your database connection parameters.

## Usage
To use the User Management System, you can run the main script or integrate it into your own application.

### Example Usage
1. Import the UserManager class:
   - `from user_management.db_manager import UserManager`

2. Initialize UserManager:
   - `user_manager = UserManager()`

3. User inputs for registration:
   - `username = input("Enter your username: ")`
   - `email = input("Enter your email: ")`
   - `password = input("Enter your password: ")`

4. Register the user:
   - `user_manager.register_user(username, email, password)`

5. Close connections when done:
   - `user_manager.close_connections()`

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- MySQL for the database.
- bcrypt for password hashing.

## Contact
For any questions or inquiries, please reach out to your_email@example.com.
