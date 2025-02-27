import streamlit as st
import duckdb

### Config
# ---------------------------------------------
#conn = duckdb.connect('md:?motherduck_token=MOTHERDUCK_TOKEN')
conn = duckdb.connect('swell_data.duckdb') # local duckdb for development
swell_data = conn.execute("SELECT * FROM swell;").fetchdf()

### Streamlit
# ---------------------------------------------
# Dashboard config
st.set_page_config(page_title="Swell Forecast", page_icon="🌊", layout="wide")

# Title 
st.title("Swell Forecast Dashboard")

# Latest update time (data refresh)
last_update_time = conn.execute("SELECT MAX(api_call_time) FROM swell;").fetchone() # returns tuple
last_update_time = str(last_update_time[0].strftime('%Y-%m-%d %H:%M:%S'))
st.sidebar.write(f"Last updated:{last_update_time}")

# location selection
# TODO: Implement location selection 
# selected_location = st.selectbox("Select a location", locations)

# Sidebar to select fields
params = st.sidebar.selectbox("Select Parameter:",
                              ['wave_height', 'wave_direction', 'wave_period',
                              'swell_wave_height', 'swell_wave_direction',
                              'swell_wave_period'])

# Time Slider
min_time = swell_data['time'].min()
max_time = swell_data['time'].max()
time_range = st.sidebar.slider("Select Time Range:",
                                min_value=min_time,
                                max_value=max_time,
                                value=(min_time, max_time),
                                format="YYYY-MM-DD HH:mm")

# Filter data based on time range
query = f"""
    SELECT * FROM swell
    WHERE time >= '{time_range[0]}' AND time <= '{time_range[1]}'
"""
swell_data_filtered = conn.execute(query).fetchdf()

# Centre line chart
st.subheader(f"{params.replace("_"," ").title()}")
st.line_chart(swell_data.set_index('time')[params])

