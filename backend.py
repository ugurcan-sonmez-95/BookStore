import sqlite3

class Database:

    ### Connects to the database
    def __init__(self, db):
        self.connect = sqlite3.connect(db)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.connect.commit()

    ### View function
    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows

    ### Search function
    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    ### Add function
    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.connect.commit()

    ### Update function
    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.connect.commit()

    ### Delete function
    def delete(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
        self.connect.commit()

    ### Destructor
    def __del__(self):
        self.connect.close()

# insert("The Sun", "John Smith", 1918, 965959496)
# delete(2)
# update(3, "The moon", "John Smooth", 1917, 79956995)
# print(view())
# print(search(author="John Smooth"))