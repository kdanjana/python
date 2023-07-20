import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        self.connection = None
        self.dbname = db_name

    #called when we are entering into context manager
    def __enter__(self):
        self.connection = sqlite3.connect(self.dbname)
        return self.connection
    
    # called when we are leaving context manager
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_type or exc_val:
            print(exc_type)
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()