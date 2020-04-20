CREATE EXTERNAL TABLE IF NOT EXISTS cloud_data (
  Article STRING,
  Dates STRING,
  Views STRING,
  Total_Views INT,
  Popularity INT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
LOCATION 's3://cloudoutput2/finaloutput/';

INSERT OVERWRITE DIRECTORY '${OUTPUT}/top100views' SELECT Article, Total_Views FROM cloud_data ORDER BY Total_Views DESC LIMIT 100;

INSERT OVERWRITE DIRECTORY '${OUTPUT}/top100popularity' SELECT Article, Popularity FROM cloud_data ORDER BY Popularity DESC LIMIT 100;