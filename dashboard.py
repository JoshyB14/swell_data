import streamlit as st
import duckdb
import pandas as pd
import matplotlib.pyplot as plt

### Config

# connect to motherduck
#conn = duckdb.connect('md:?motherduck_token=MOTHERDUCK_TOKEN')
conn = duckdb.connect('swell_data.duckdb')

### Streamlit 

# page config
st.set_page_config(page_title="Swell Forecast", page_icon="🌊", layout="wide")

# title & desc
st.title("Swell Forecast Dashboard")
st.write("Get the latest wave height, period and direction for your favorite surf spots")

# location selection
# TODO: Implement location selection 
# selected_location = st.selectbox("Select a location", locations)

data = conn.execute('select * from swell').fetchdf()


# Plot the Wave Direction vs Time
st.subheader("Wave Direction Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['time'], data['wave_direction'], label='Wave Direction (°)', color='orange')
ax.set_xlabel("Time")
ax.set_ylabel("Wave Direction (°)")
ax.set_title("Wave Direction Over Time")
ax.grid(True)
st.pyplot(fig)