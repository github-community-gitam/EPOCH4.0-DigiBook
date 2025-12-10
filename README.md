# DigiBook: A Library Management System

A simple and beginner-friendly GUI-based Library Management System built using:
- Python
- Tkinter (GUI)
- SQLite (database)

This project is perfect for learning CRUD operations, GUI development, and file-based databases.
Lightweight and easy to run on any system.

## Features

1. Add new books
2. View all books
3. Search books by Title, Author, Year, or ISBN
4. Update selected book
5. Delete selected book
6. Simple Tkinter graphical interface
7. SQLite local database (no installation required)

## Project Structure

```
library-management-gui-python/
├── README.md
├── CONTRIBUTING.md
├── create_db.py      # Creates SQLite database & table
└── main.py           # Main GUI application
```

## Requirements

- Python 3.x
- Tkinter (comes preinstalled with Python on Windows/Mac)
- SQLite (already included with Python)

## How to run

1. Clone the project

   ```
   git clone https://github.com/<your-username>/library-management-gui-python.git
    cd library-management-gui-python
   ```

3. Create the database

    Run the script once to generate `library.db`

    **Windows:**
  
    ```
    python create_db.py
    ```

    **Mac/Linux:**

    ```
    python create_db.py
    ```

    **Output:**
  
    ```
    Database created successfully!
    ```
  
4. Run the GUI Application

   **Windows:**
   ```
   python main.py
    ```

    **Mac/Linux:**

    ```
    python3 main.py
    ```

## 📌 Future Enhancements

You can extend this project with features like:

- User login system
- Issue/Return book tracking
- Due date & fine calculator
- Export records as Excel/PDF
- Modern UI (using CustomTkinter or PyQt5)
- Convert to Windows executable (.exe)

Please refer to the [guidelines](https://github.com/github-community-gitam/EPOCH4.0-DigiBook/blob/main/CONTRIBUTING.md) for making any contributions.
Thank you!
