import duckdb
import os

# get secret from Github repo
motherduck_token = os.getenv("MOTHERDUCK_TOKEN")

# connect to motherduck database
con = duckdb.connect('md:?motherduck_token={MOTHERDUCK_TOKEN}')

# open table builder sql script
with open('./sql/build_tables.sql', 'r') as build_tables:
    sql_script = build_tables.read()
    
# run in duckdb
con.sql(sql_script)

# close connection
con.close()
