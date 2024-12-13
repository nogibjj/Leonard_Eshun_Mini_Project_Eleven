### Extraction Test ### 
Removing existing CSV file exists <br />Confirming that CSV file doesn't exists... <br />Test Successful <br />Extracting data and saving... <br />Testing if CSV file exists... <br />Extraction Test Successful


### Transform and Load Test ### 
Creating non-lookup table: air_quality <br />Creating lookup table: indicator <br />Creating lookup table: geo_data <br />Tables created. <br />Skipping the first row... <br />Inserting table data... <br />Inserting table data completed <br />Transform and Load Test Successful


### One Record Reading Test ### 
Getting columns for air_quality <br />Asserting that row[0][data_value] == 16.4 <br />Assert Successful <br />One Record Reading Test Successful


### All Records Reading Test ### 
Executing query... <br />
```sql
select * from air_quality
```

Asserting that len(rows) == 18016 <br />All Records Reading Test Successful


### Record Saving Test ### 
Asserting there's no record in geo_data with ID 100000 <br />Getting columns for geo_data <br />Assert Successful <br />Saving new record with ID 100000 <br />Adding new record [(100000, 'Lancaster', 'UFO')] <br />Asserting there's now a record in geo_data with ID 100000 <br />Getting columns for geo_data <br />Assert Successful <br />Record Saving Test Successful


### Record Deletion Test ### 
Asserting there's a record in geo_data for row ID 100000 <br />Getting columns for geo_data <br />Assert Successful <br />Deleting record with ID 100000 <br />Filtering out record with id 100000 <br />Getting columns for geo_data <br />Asserting there's no record in geo_data with ID 100000 <br />Getting columns for geo_data <br />Assert Successful <br />Record Deletion Test Successful


### Reading All Column Test ### 
Getting columns for air_quality <br />Asserting the air_quality table has six (6) columns <br />Assert Successful <br />Reading All Column Test Successful


### Transform and Load Test ### 
Creating non-lookup table: air_quality <br />Creating lookup table: indicator <br />Creating lookup table: geo_data <br />Tables created. <br />Skipping the first row... <br />Inserting table data... <br />Inserting table data completed <br />Transform and Load Test Successful


Executing custom query... <br />
```sql
SELECT 
    indicator.indicator_name, 
    air_quality.time_period, 
    AVG(data_value) AS avg_data_value
FROM 
    air_quality
INNER JOIN 
    indicator 
ON 
    air_quality.fn_indicator_id = indicator.indicator_id
GROUP BY 
    indicator_name, time_period
ORDER BY 
    indicator_name, time_period
```

