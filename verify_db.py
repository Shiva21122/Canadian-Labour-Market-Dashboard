import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Tryingnew21"
)
cur = conn.cursor()

# Check total rows
cur.execute("SELECT COUNT(*) FROM employment_data;")
print(f"Total rows: {cur.fetchone()[0]}")

# Check date range
cur.execute("SELECT MIN(date), MAX(date) FROM employment_data;")
print(f"Date range: {cur.fetchone()}")

# Check provinces
cur.execute("SELECT DISTINCT province FROM employment_data ORDER BY province;")
print(f"Provinces: {[row[0] for row in cur.fetchall()]}")

# Sample query - latest unemployment rate by province
cur.execute("""
    SELECT province, value
    FROM employment_data
    WHERE metric = 'Unemployment rate'
    AND date = (SELECT MAX(date) FROM employment_data)
    ORDER BY value DESC;
""")
print("\nLatest Unemployment Rates by Province:")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]}%")

cur.close()
conn.close()