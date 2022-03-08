import pandas as pd

df_from_first = pd.read_csv (r'./temp/first.csv')

df_from_second = pd.read_csv (r'./temp/second.csv')

new_df = df_from_second[~df_from_second['id'].isin(df_from_first['id'])]

new_df.to_csv(r'./temp/output_only_in_second.csv', index = False)
