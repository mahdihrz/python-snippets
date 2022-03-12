import pandas as pd

filename = input("csv file to iterate:")
#existent example input ./pandas/sources_input.csv
df_input = pd.read_csv (filename)

for index, csv_source in df_input.iterrows():
    print('category:', csv_source['category'],'source:', csv_source['source'])
