import streamlit as st
import duckdb

### Config

# connect to motherduck
#conn = duckdb.connect('md:?motherduck_token=MOTHERDUCK_TOKEN')

conn = duckdb.connect('swell_data.duckdb') # local duckdb for development

### Streamlit

# page config
st.set_page_config(page_title="Swell Forecast", page_icon="🌊", layout="wide")

# title & desc
st.title("Swell Forecast Dashboard")

# location selection
# TODO: Implement location selection 
# selected_location = st.selectbox("Select a location", locations)


# wave direction
wave_dir = conn.execute("SELECT time, wave_direction from swell;").df()
st.line_chart(data=wave_dir, x='time', y='wave_direction', x_label='time', y_label='wave_direction')


