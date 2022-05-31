import pandas as pd

dataset = "/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Multi-output RNN/Generated CSVs/MCRT3_multihead copy.csv"
df = pd.read_csv(dataset)

rolling =  df.rolling(window=5)
df= rolling.mean()
df.dropna(inplace=True)

df.to_csv("/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Multi-output RNN/Generated CSVs 2/MCRT.csv", index=False)