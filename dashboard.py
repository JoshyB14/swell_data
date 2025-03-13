import streamlit as st
import pandas as pd
import duckdb

# ---------------------------------------------
### Connections

# Access streamlit secret from streamlit cloud TOML file
motherduck_token = st.secrets["MOTHERDUCK"]["MOTHERDUCK_TOKEN"]
conn = duckdb.connect(f'md:?motherduck_token={motherduck_token}')
local_conn = duckdb.connect('./locations.duckdb')


# ---------------------------------------------
### Streamlit COnfig

# Dashboard config
st.set_page_config(page_title="Swell Forecast", page_icon="🌊", layout="wide")

# Title 
st.title("Swell Forecast Dashboard")

# Latest update time (data refresh)
last_update_time = conn.execute("SELECT MAX(api_call_time) FROM swell_refined;").fetchone() # returns tuple
last_update_time = str(last_update_time[0].strftime('%Y-%m-%d %H:%M:%S'))
st.sidebar.write(f"Data last updated: {last_update_time}")


# Sidebar to select fields
locs = st.sidebar.selectbox("Select location: ",
                            conn.execute("SELECT DISTINCT location from swell_refined;").fetchdf().location.to_list())

# Time Slider
swell_data_time = conn.execute(f"SELECT time FROM swell_refined WHERE location = '{locs}';").fetchdf()
min_time = swell_data_time['time'].min().to_pydatetime()
max_time = swell_data_time['time'].max().to_pydatetime()

time_range = st.sidebar.slider("Select Time Range:",
                                min_value=min_time,
                                max_value=max_time,
                                value=(min_time, max_time))
start_time_str = time_range[0].strftime('%Y-%m-%d %H:%M:%S')
end_time_str = time_range[1].strftime('%Y-%m-%d %H:%M:%S')


# Filter data based on time range
query = f"""
    SELECT * FROM swell_refined
    WHERE time::text >= '{start_time_str}' AND time <= '{end_time_str}'
    AND location = '{locs}'
"""
swell_data_filtered = conn.execute(query).fetchdf()
swell_data_filtered['time'] = pd.to_datetime(swell_data_filtered['time'])

# Selectable parameters
params = st.sidebar.selectbox("Select Parameter:",
                              ['wave_height', 'wave_direction', 'wave_period',
                              'swell_wave_height', 'swell_wave_direction',
                              'swell_wave_period'])

# Centre line chart
st.subheader(f"{params.replace("_"," ").title()} for {locs}")
st.line_chart(swell_data_filtered.set_index('time')[params])

# Map chart
# TODO - understand why this is not dynamic at present and fix!
lat_long_query = f"""
    SELECT lat, long from locations 
    WHERE location = '{locs}'
"""
locations_lat_long = conn.execute(lat_long_query).fetchdf().to_dict()

st.subheader(f"Map of {locs}")
st.map(data=pd.DataFrame({"latitude":[str(locations_lat_long['lat'][0])],
    "longitude": [str(locations_lat_long['long'][0])],}))