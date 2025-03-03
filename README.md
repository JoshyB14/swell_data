# Swell Data

## Overview

A small data pipeline to get the local swell forcast for my local beach.

### Streamlit Dashboard Example

Example below - Continually being built upon.

![Dashboard](dashboard_screengrab.png)

### Data Architecture

![Architecture](architecture.png)

Every day at 9:00 AM Sydney Time (AEDT), a GitHub Action is triggered to run a Python script. This script retrieves the latest swell forecast for the specified location from the Open-Meteo API, covering today +7 days. The data is initially written to disk within the GitHub Action VPC before being loaded into Motherduck.

Minor data cleaning and formatting tasks are performed within a view inside Motherduck to ensure the data is ready for visualisation. A Streamlit dashboard pulls the processed data from this view and is re-loaded each time the dashboard is accessed.

