-- displays the max temperature of each state by state col

SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
