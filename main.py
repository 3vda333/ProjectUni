from create_db import create_db
from load_csv_db import load_db

db_name = "ContentManagement"
create_db(db_name)
load_db(db_name)