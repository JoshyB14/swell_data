import duckdb
import os

#--------------------------------
# Config

# get secret from Github repo
motherduck_token = os.getenv("MOTHERDUCK_TOKEN")
# connect to motherduck database
con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')


#--------------------------------
# Init tables & views

with open('./sql/build_tables.sql', 'r') as build_tables:
    sql_script = build_tables.read()

con.sql(sql_script)

with open('./sql/swell_view.sql', 'r') as swell_view:
    sql_script = swell_view.read()

con.sql(sql_script)

#--------------------------------
# Load data into Motherduck

for file in os.listdir('./landing_zone'):

    location_str = file.split('_')[0] # get location name

    sql_script = f"""
    INSERT INTO swell
    SELECT 
        {location_str}::TEXT as location,
        now()::TIMESTAMP as api_call_time,
        unnest(json_file.hourly.time)::TIMESTAMP AS time,
        unnest(json_file.hourly.wave_height)::FLOAT AS wave_height,
        unnest(json_file.hourly.wave_direction)::FLOAT AS wave_direction,
        unnest(json_file.hourly.wave_period)::FLOAT AS wave_period,
        unnest(json_file.hourly.swell_wave_height)::FLOAT AS swell_wave_height,
        unnest(json_file.hourly.swell_wave_direction)::FLOAT AS swell_wave_direction,
        unnest(json_file.hourly.swell_wave_period)::FLOAT AS swell_wave_period
    FROM read_json_auto("./landing_zone/{location_str}_data.json") AS json_file
    ;

    """

    # run in duckdb
    con.sql(sql_script)


#--------------------------------
# Clean up

# close connection
con.close()

# remove json files
for file in os.listdir('./landing_zone'):
    os.remove(f'./landing_zone/{file}')

