-- Import in hbtn_0c_0 database this table dump: download
SELECT city, AVG(value) AS avg_temp
FROM temperatures
ORDER BY value DESC;
