import mysql.connector

def create_database(cursor, database_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    print(f"Database {database_name} created successfully.")

def show_databases(cursor):
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print("Databases:", databases)
    return databases

def create_table(cursor, table_query):
    cursor.execute(table_query)
    print("Table created successfully.")

def connect_to_db(host, user, password, database=None):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
def create_db(db_name):
    mydb = connect_to_db("localhost", "root", "pass")
    cursor = mydb.cursor()

    # db_name = "ContentManagement"
    create_database(cursor, db_name)
    databases = show_databases(cursor)

    if (db_name,) in databases:
        print("Connected to the database successfully.")
        mydb = connect_to_db("localhost", "root", "pass", db_name)
        cursor = mydb.cursor()

        photographers_table_query = """
            CREATE TABLE IF NOT EXISTS Photographers (
                PhotographerID INT AUTO_INCREMENT,
                Name VARCHAR(255),
                Email VARCHAR(255),
                UNIQUE (Email),
                PRIMARY KEY (PhotographerID)
            )
        """
        create_table(cursor, photographers_table_query)

        writers_table_query = """
            CREATE TABLE IF NOT EXISTS Writers (
                WriterID INT AUTO_INCREMENT,
                Name VARCHAR(255),
                Email VARCHAR(255),
                UNIQUE (Email),
                PRIMARY KEY (WriterID)
            )
        """
        create_table(cursor, writers_table_query)

        images_table_query = """
            CREATE TABLE IF NOT EXISTS Images (
                ImageID INT AUTO_INCREMENT,
                Path VARCHAR(255),
                Title VARCHAR(255),
                Tags VARCHAR(255),
                Description TEXT,
                Category VARCHAR(255),
                PhotographerID INT,
                FOREIGN KEY (PhotographerID) REFERENCES Photographers(PhotographerID),
                PRIMARY KEY (ImageID)
            )
        """
        create_table(cursor, images_table_query)

        articles_table_query = """
            CREATE TABLE IF NOT EXISTS Articles (
                ArticleID INT AUTO_INCREMENT,
                Content TEXT,
                Keywords VARCHAR(255),
                Title VARCHAR(255),
                Category VARCHAR(255),
                WriterID INT,
                FOREIGN KEY (WriterID) REFERENCES Writers(WriterID),
                PRIMARY KEY (ArticleID)
            )
        """
        create_table(cursor, articles_table_query)
