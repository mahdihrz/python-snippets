import pandas as pd
df_input = pd.read_csv (r'./temp/data_input.csv')

#df_filtred = df_input[df_input['installed']=='True']

#df_filtred = df_input[df_input['opt_in']==True]

#df_filtred = df_input[df_input['named_user_id'].notnull()]
df_filtred = df_input[df_input['device_type']=='ios']

#df_filtred = df_filtred[df_filtred['last_registration'].isnull()]
#df_input.groupby('named_user_id').count()


df_filtred.to_csv("./temp/data_filtered.csv", index=False)