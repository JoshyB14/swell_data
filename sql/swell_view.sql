/*
Creates a view of the forecast data using only the latest data called from 
the api for each hr. An example - The forecast for 2025-03-01 18:00:00 would be
called many times across a 7 day forecast. This view ensures that only the
closest forecast to the actual time is called.
*/

CREATE OR REPLACE VIEW swell_refined AS 
WITH swell_rn AS 
(
  SELECT
    swell.*,
    ROW_NUMBER() OVER(PARTITION BY location, time order by api_call_time desc) AS rn
  FROM swell
)

SELECT
  location,
  api_call_time,
  time,
  ROUND(wave_height,2) AS wave_height,
  wave_direction,
  ROUND(wave_period,2) AS wave_period,
  ROUND(swell_wave_height,2) AS swell_wave_height,
  swell_wave_direction,
  ROUND(swell_wave_period,2) AS swell_wave_period
FROM swell_rn
  WHERE rn = 1
;
