/*
Creates a view of the forecast data using only the latest data called from 
the api for each hr. An example - The forecast for 2025-03-01 18:00:00 would be
called many times across a 7 day forecast. This view ensures that only the
closest forecast to the actual time is called.
*/

CREATE OR REPLACE VIEW swell_refined AS 
WITH swell_rn as (
  SELECT
    swell.*,
    row_number() over(partition by time order by api_call_time desc) as rn
FROM swell
)
SELECT
location,
api_call_time,
time,
ROUND(wave_height,2) as wave_height,
wave_direction,
ROUND(wave_period,2) as wave_period,
ROUND(swell_wave_height,2) as swell_wave_height,
swell_wave_direction,
ROUND(swell_wave_period,2) as swell_wave_period
FROM swell_rn
WHERE rn = 1
;
