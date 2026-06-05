import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Password"  
)

#Query 1 - Covid impact: unemployment rate Canada-wide average by year
print("Query 1 - Covid impact: unemployment rate Canada-wide average by year")
query1 = """
SELECT
    left(date, 4) AS year,
    round(avg(value), 2) AS avg_unemployment_rate
FROM employment_data
WHERE metric = 'Unemployment rate'
GROUP BY year
ORDER BY year;
"""
print(pd.read_sql_query(query1, conn))

#Query 2 - Province ranking by employment rate (latest month)
print("\nQuery 2 - Province ranking by employment rate (latest month)")
query2 = """
SELECT province, value AS employment_rate
FROM employment_data
WHERE metric = 'Employment rate'
AND date = (SELECT MAX(date) FROM employment_data)
ORDER BY employment_rate DESC;
"""
print(pd.read_sql_query(query2, conn))

#Query 3 - Trend: Quebec vs Ontario unemployment rate over time
print("\nQuery 3 - Trend: Quebec vs Ontario unemployment rate over time")
query3 = """
SELECT date, province, value AS unemployment_rate
FROM employment_data    
WHERE metric = 'Unemployment rate'
AND province IN ('Quebec', 'Ontario')
ORDER BY date;
"""
print(pd.read_sql_query(query3, conn))

conn.close()
