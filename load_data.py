import duckdb

# connect to local duckdb database
con = duckdb.connect('swell_data.duckdb')

# open table builder sql script
with open('./sql/build_tables.sql', 'r') as build_tables:
    sql_script = build_tables.read()
    
# run in duckdb
con.sql(sql_script)

# close connection
con.close()