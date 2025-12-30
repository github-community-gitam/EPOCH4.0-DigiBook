import sqlite3


def init_db(db_path="library.db"):
    try:
        # using context manager so connection auto-closes
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()

            # create table (if not already there)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                year INTEGER,
                isbn TEXT
            )
            """)

            # create indexes to speed up searching
            cur.execute("CREATE INDEX IF NOT EXISTS idx_books_title ON books(title)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_books_author ON books(author)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_books_isbn ON books(isbn)")

        # if no error — success!
        print("Database created successfully!")

    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    init_db()
    

