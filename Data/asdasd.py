import pandas as pd

file = pd.read_csv("./Data/cc1.csv")

a = file.duplicated(["address"])
# a = file.drop_duplicates(["address"], keep='first')
    
print(a)
