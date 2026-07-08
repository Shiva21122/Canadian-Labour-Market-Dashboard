import pandas as pd

df = pd.read_csv('14100287-eng/14100287.csv')
print("Initial data loaded. Shape:", df.shape)

print(df['Statistics'].unique())