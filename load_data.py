import duckdb
import os
# connect to motherduck database
con = duckdb.connect('md:?motherduck_token=')

# open table builder sql script
with open('./sql/build_tables.sql', 'r') as build_tables:
    sql_script = build_tables.read()
    
# run in duckdb
con.sql(sql_script)

# close connection
con.close()
