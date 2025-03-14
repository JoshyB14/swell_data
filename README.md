# Swell Data

A small data pipeline to get the local swell forcast for my local beach.

## Data Architecture

![Architecture](./images/architecture.png)

Every day at 9:00 AM Sydney Time (AEDT), a GitHub Action is triggered to run a Python script. This script retrieves the latest swell forecast for the specified locations from the Open-Meteo API, covering today +7 days. Location data to be passed to the API is stored in a local DuckDB database. The data returned from the API is initially written to disk within the GitHub Action VPC before being loaded into Motherduck.

Minor data cleaning and formatting tasks are performed within a view inside Motherduck to ensure the data is ready for visualisation. A Streamlit dashboard pulls the processed data from this view and is re-loaded each time the dashboard is accessed.

This architecture was chosen notably as all services offered generious free tiers.

## Streamlit Dashboard

Example below - Continually being built upon.

[Link to Streamlit Dashboard](https://swelldata-g8c7djod5rqc6xfwqzkcex.streamlit.app/)

![Dashboard](./images/dashboard_screengrab.png)



