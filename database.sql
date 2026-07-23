-- Write your PostgreSQL query statement below
SELECT ROUND(SUM(tiv_2016)::NUMERIC, 2) AS tiv_2016
FROM Insurance i
WHERE i.tiv_2015 IN (SELECT ii.tiv_2015 FROM Insurance ii WHERE i.pid<>ii.pid)
AND (i.lat, i.lon) NOT IN (SELECT ii.lat, ii.lon FROM Insurance ii WHERE i.pid<>ii.pid);


SELECT ROUND(SUM(tiv_2016)::numeric, 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);


SELECT ROUND(SUM(tiv_2016)::numeric, 2) AS tiv_2016
FROM (
    SELECT *,
           COUNT(*) OVER (PARTITION BY tiv_2015) AS tiv_cnt,
           COUNT(*) OVER (PARTITION BY lat, lon) AS loc_cnt
    FROM Insurance
) t
WHERE tiv_cnt > 1
  AND loc_cnt = 1;