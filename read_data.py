import pandas as pd

df = pd.read_excel('US.xlsx')
list_of_columns = df.columns.values

geo_names = []
geo_ids = []

for col in range(2):
    for row in range(1, len(df)):
        if col == 0:
            geo_names.append(df[list_of_columns[col]][row])
        if col == 1:
            geo_ids.append(df[list_of_columns[col]][row])

print(geo_names)
print(geo_ids)
