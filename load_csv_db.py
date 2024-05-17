import csv
import mysql.connector

def connect_to_db(host, user, password, database=None):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def insert_into_table(cursor, table_name, data):
    placeholders = ', '.join(['%s'] * len(data))
    columns = ', '.join(data.keys())
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(sql, list(data.values()))

def load_csv_data_to_db(cursor, table_name, csv_file_path):
    with open(csv_file_path, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            insert_into_table(cursor, table_name, row)

def load_db(db_name,writer_csv,images_csv,photgrapher_csv,articles_csv):
    mydb = connect_to_db("localhost", "root", "pass", db_name)
    cursor = mydb.cursor()

    load_csv_data_to_db(cursor, "Photographers", photgrapher_csv)
    load_csv_data_to_db(cursor, "Writers", writer_csv)
    load_csv_data_to_db(cursor, "Images", images_csv)
    load_csv_data_to_db(cursor, "Articles", articles_csv)

    mydb.commit()

