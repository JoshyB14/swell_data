import streamlit as st
import duckdb

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


