import os
import shutil

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "databases")

if not os.path.isdir(BASE_DIR):
    os.mkdir(BASE_DIR)


class DatabaseManager:
    def __init__(self):
        self.databases = []
        for folder in os.listdir(BASE_DIR):
            self.databases.append(Database(folder))

    def get_database(self, name):
        for database in self.databases:
            if database.name == name:
                return database

    def list_databases(self):
        temp_databases = ""
        for database in self.databases:
            temp_databases += "%s, " % database.name
        print("Databases: %s" % temp_databases)

    def create(self, name):
        if self.get_database(name) in self.databases:
            print("Database already exists.")
            return

        try:
            os.mkdir(os.path.join(BASE_DIR, name))
            self.databases.append(Database(name))
            print("Created database %s." % name)
        except Exception:
            print("Creation of the database %s failed" % name)

    def drop(self, name):
        if self.get_database(name) not in self.databases:
            print("Database %s does not exist." % name)
            return

        try:
            shutil.rmtree(os.path.join(BASE_DIR, name))
            self.databases.remove(self.get_database(name))
            print("Deleted database %s." % name)
        except Exception:
            print("Deletion of the database %s failed" % name)


class Database:
    def __init__(self, name):
        self.name = name
