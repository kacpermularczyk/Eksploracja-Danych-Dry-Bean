import pandas as pd
import numpy as np

df = pd.read_csv("Dry_Bean.csv")

col1 = "Roundness"
col2 = "Perimeter"

fraction = 0.05

indices_col1 = df.sample(frac=fraction).index
indices_col2 = df.sample(frac=fraction).index

df.loc[indices_col1, col1] = np.nan
df.loc[indices_col2, col2] = np.nan

df.to_csv("Dry_Bean_modified.csv", index=False)

print(f"NaN w {col1}: {len(indices_col1)} wierszy")
print(f"NaN w {col2}: {len(indices_col2)} wierszy")