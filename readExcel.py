# Read excel by sheet
# bY Busyman.Inc

import pandas as pd

sheet_one = pd.read_excel('sample.xlsx', sheet_name=0)
sheet_two = pd.read_excel('sample.xlsx', sheet_name="Sales")

print(sheet_one)
print(sheet_two)
