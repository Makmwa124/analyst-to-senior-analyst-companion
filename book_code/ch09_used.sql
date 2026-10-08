-- Which requesters actually use what we deliver?
SELECT requester,
       COUNT(*) AS requests,
       SUM(used_in_decision = 'Yes') AS used,
       ROUND(100.0 * SUM(used_in_decision = 'Yes') / COUNT(*), 0)
           AS pct_used,
       ROUND(SUM(actual_hours), 0) AS hours
FROM requests
GROUP BY requester
ORDER BY hours DESC;
