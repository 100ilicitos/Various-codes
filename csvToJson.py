# Cpnvert CSV to JSON
# by Busyman.INC

import pandas as pd
import csv,json
data=pd.read_csv("Core.csv")
print(data)
print("Convert Json file:")
print(json.dumps(list(csv.reader(open("Core.csv")))))
