import pandas as pd

df = pd.read_csv('14100287-eng/14100287.csv', nrows=50000)
print(" Labour Force Characteristics")
print(df['Labour force characteristics'].unique())

print("\n Gender")
print(df['Gender'].unique())

print("\n Age group")
print(df['Age group'].unique())     

print("\n Geo (first 20):")
print(df['GEO'].unique()[:20])