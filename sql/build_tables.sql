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





