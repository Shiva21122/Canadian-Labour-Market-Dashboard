"""
Load cleaned labour force data into PostgreSQL warehouse.
Run from project root: python scripts/load_to_db.py
"""
import pandas as pd
import psycopg2
from psycopg2 import sql

# Load the cleaned dataset
df = pd.read_csv('data/processed/14100287_cleaned.csv')
print("Cleaned data loaded. Shape:", df.shape)

#Connect to PostgreSQL database
try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Tryingnew21"
    )
    print("Database connection successful.")
    cursor = conn.cursor()
except Exception as e:
    print("Error connecting to database:", e)
    exit()

# Create table
cursor.execute("""
               Drop table if exists employment_data;
         CREATE TABLE employment_data (
              id SERIAL PRIMARY KEY,
              date Varchar(10), 
              province VARCHAR(100),
              metric VARCHAR(50),
              value Decimal(5,2)
         );
         """)

# Insert data into table
for _, row in df.iterrows():
    cursor.execute(sql.SQL("""
        INSERT INTO employment_data (date, province, metric, value)
        VALUES (%s, %s, %s, %s);
    """), [row['date'], row['province'], row['metric'], row['value']])

conn.commit()
cursor.close()
conn.close()

print(f"Successfully inserted {len(df)} records into the database.")