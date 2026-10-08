import sqlite3
import pandas as pd

con = sqlite3.connect("data/paperbark.db")
sql = open("book_code/ch09_used.sql").read()
print(pd.read_sql(sql, con).to_string(index=False))
