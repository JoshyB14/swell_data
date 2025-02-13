-- Init table if not exists

CREATE TABLE IF NOT EXISTS swell (
    location TEXT,
    time TIMESTAMP,
    wave_height FLOAT,
    wave_direction FLOAT,
    wave_period FLOAT,
    swell_wave_height FLOAT,
    swell_wave_direction FLOAT,
    swell_wave_period FLOAT
);


-- If table exits append data 
INSERT INTO swell
SELECT 
    'Freshwater'::TEXT as location,
    unnest(freshwater.hourly.time)::TIMESTAMP AS time,
    unnest(freshwater.hourly.wave_height)::FLOAT AS wave_height,
    unnest(freshwater.hourly.wave_direction)::FLOAT AS wave_direction,
    unnest(freshwater.hourly.wave_period)::FLOAT AS wave_period,
    unnest(freshwater.hourly.swell_wave_height)::FLOAT AS swell_wave_height,
    unnest(freshwater.hourly.swell_wave_direction)::FLOAT AS swell_wave_direction,
    unnest(freshwater.hourly.swell_wave_period)::FLOAT AS swell_wave_period
FROM read_json_auto('./landing_zone/freshwater_freshwater.json') AS freshwater
;




