-- Init table if not exists

CREATE TABLE IF NOT EXISTS swell (
    location TEXT,
    api_call_time TIMESTAMP,
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
    {location_var}::TEXT as location,
    now()::TIMESTAMP as api_call_time,
    unnest(json_file.hourly.time)::TIMESTAMP AS time,
    unnest(json_file.hourly.wave_height)::FLOAT AS wave_height,
    unnest(json_file.hourly.wave_direction)::FLOAT AS wave_direction,
    unnest(json_file.hourly.wave_period)::FLOAT AS wave_period,
    unnest(json_file.hourly.swell_wave_height)::FLOAT AS swell_wave_height,
    unnest(json_file.hourly.swell_wave_direction)::FLOAT AS swell_wave_direction,
    unnest(json_file.hourly.swell_wave_period)::FLOAT AS swell_wave_period
FROM read_json_auto('./landing_zone/{location_var}.json') AS json_file
;




