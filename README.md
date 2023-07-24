# Login-System
This project demonstrates a simple login system built using FastAPI as the backend server and a basic HTML/JavaScript frontend. The backend server uses SQLite as the database to store user login information.

## How it Works

### 1. Backend Server (FastAPI):
* The backend server is built using FastAPI, a modern web framework for building APIs with Python.
* It provides a endpoint: /login (for user login)
* User login information is stored in a SQLite database (users.db).

### 2. Frontend (HTML/JavaScript):
* The frontend provides a simple login form where users can enter their username and password.
* When users submit the form, the frontend sends a POST request to the backend /login endpoint to verify the login.
* If the login is successful, the backend responds with a message "Login successful."
* If the login fails due to incorrect details or a non-existing user, the backend responds with a custom error message.

## How to Set Up and Run

### 1. Clone the Repository:
```
git clone https://github.com/your_username/your_project.git
cd your_project
```


### 2. Install Packages:
Run the following command in your terminal or command prompt:
```
pip install -r requirements.txt
```


### 3. Create the SQLite Database (Optional):
The 'users.db' file is provided. If you didn't have the 'users.db' file,  run the following Python script:
```
python create_db.py
```
This script will create the users.db file and the users table with columns for id, username, and password.


### 4. Run the Backend Server:
```
uvicorn main:app --reload
```
This will launch the backend server, and it will be accessible at 'http://127.0.0.1:8000'. 

### 5. Open the Frontend:
Open the index.html file location in your web browser. The frontend form will appear, allowing you to enter your username and password for login.


### 6. Test the Login System:
* Enter valid credentials and click the "Login" button to test successful login.
* Enter invalid credentials to test the error handling, and you should see appropriate error messages displayed on the   
  frontend.
