"""
Canadian Labour Market Pipeline - Data Cleaning
Business Question: How have unemployment, employment, and participation rates
evolved across Canadian provinces (2015-2026), incl. the COVID-19 shock and recovery?
Research: Statistics Canada Table 14-10-0287-01 (Labour force characteristics, monthly).
Data Types: REF_DATE (monthly date), GEO (categorical province), metric (categorical),
VALUE (float, %). Seasonally adjusted estimates only.
Cleaning: filter to 2015+, total gender, 15+ age group, seasonally adjusted estimates,
3 key metrics, 10 provinces; keep 4 columns and rename.
Output: data/processed/14100287_cleaned.csv (4,080 rows)
Run from project root: python scripts/clean.py
"""
import pandas as pd

# Load the dataset
print("Loading data...")
df = pd.read_csv('data/raw/14100287.csv', low_memory=False)
print(f"Data loaded. Shape: {df.shape}")

#Date range check
print("Date range in dataset:", df['REF_DATE'].min(), "to", df['REF_DATE'].max())

# Filter to what we need
df = df[df['REF_DATE'] >= '2015-01']
print(f"Data filtered to 2015 and later. Shape: {df.shape}")

df = df[df['Gender'] == 'Total - Gender']
print(f"GENDER filter applied. Shape: {df.shape}")

df = df[df['Age group'] == '15 years and over']
print(f"AGE GROUP filter applied. Shape: {df.shape}")

df = df[df['Data type'] == 'Seasonally adjusted']
print(f"DATA TYPE filter applied. Shape: {df.shape}")

df = df[df['Statistics'] == 'Estimate']
print(f"STATISTICS filter applied. Shape: {df.shape}")

df = df[df['Labour force characteristics'].isin(['Unemployment rate', 'Employment rate', 'Participation rate'])]
print(f"LABOUR FORCE CHARACTERISTICS filter applied. Shape: {df.shape}")

# keeping Only the province
provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', 'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', 'Alberta', 'British Columbia']
df = df[df['GEO'].isin(provinces)]
print(f"Data filtered. Shape: {df.shape}")

print(df['Data type'].unique())

# Keep only the columns we need
df = df[['REF_DATE', 'GEO', 'Labour force characteristics', 'VALUE']]
df.columns = ['date', 'province', 'metric', 'value']
print("Data cleaned. Final shape:", df.shape)

#drop nulls
df=df.dropna(subset=['value'])

#check for duplicates
print(f"\nDuplicate rows before dropping: {df.duplicated().sum()}")
df = df.drop_duplicates()

print(f"\nFinal shape after dropping duplicates: {df.shape}")
print(f'Date range: {df["date"].min()} to {df["date"].max()}')
print(f"Unique provinces: {df['province'].unique()}")
print(f"Unique metrics: {df['metric'].unique()}")
print("\n Sample data:")
print(df.head(10))

# Save the cleaned data
df.to_csv('data/processed/14100287_cleaned.csv', index=False) 
print("Cleaned data saved to 'data/processed/14100287_cleaned.csv'")