import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Tryingnew21"
)

# Verify specific claims
queries = {
    "Alberta latest employment rate": """
        SELECT value FROM employment_data
        WHERE metric = 'Employment rate' AND province = 'Alberta'
        AND date = (SELECT MAX(date) FROM employment_data)
    """,
    "Newfoundland latest employment rate": """
        SELECT value FROM employment_data
        WHERE metric = 'Employment rate' AND province = 'Newfoundland and Labrador'
        AND date = (SELECT MAX(date) FROM employment_data)
    """,
    "Post-COVID low unemployment": """
        SELECT date, ROUND(AVG(value)::numeric, 2) as avg
        FROM employment_data
        WHERE metric = 'Unemployment rate'
        AND date BETWEEN '2022-01' AND '2024-12'
        GROUP BY date ORDER BY avg ASC LIMIT 3
    """
}

for name, q in queries.items():
    print(f"\n=== {name} ===")
    print(pd.read_sql(q, conn))

conn.close()