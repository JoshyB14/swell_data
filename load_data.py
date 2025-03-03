import duckdb
import os

# get secret from Github repo
motherduck_token = os.getenv("MOTHERDUCK_TOKEN")
# connect to motherduck database
con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')

#--------------------------------
# Load data into Motherduck

for file in os.listdir('./landing_zone'):

    location_str = file.split('_')[0] # get location name
    print(location_str)

    with open('./sql/build_tables.sql', 'r') as build_tables:
        sql_script = build_tables.read() 

    sql_script.format(location_var=location_str) # format location variable

    # run in duckdb
    con.sql(sql_script)

#--------------------------------
# Create Motherduck views

# init views
with open('./sql/swell_view.sql', 'r') as swell_view:
    sql_script = swell_view.read()
# run in duckdb
con.sql(sql_script)

# close connection
con.close()

# remove json files
for file in os.listdir('./landing_zone'):
    os.remove(f'./landing_zone/{file}')

