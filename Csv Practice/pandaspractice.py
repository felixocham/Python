import pandas as pd
import pprint


df = pd.read_csv("sales.csv")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
print(df.head(10))
