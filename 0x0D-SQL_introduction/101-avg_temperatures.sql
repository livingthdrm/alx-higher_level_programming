-- Import in hbtn_0c_0 database this table dump: download
mysql hbtn_0c_0 < temperatures.sql
USE hbtn_0c_0;
SELECT city, AVG(temperature) AS avg_temp
ORDER BY temperature DESC;
