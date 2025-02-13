import duckdb


# connect to local duckdb database
con = duckdb.connect('swell_data.duckdb')

# open table builder sql script
with open('build_tables.sql', 'r') as build_tables:
    sql_script = build_tables.read()
    
# run in duckdb
#result = con.execute(sql_script).fetchall()
