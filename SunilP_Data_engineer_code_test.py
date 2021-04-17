import pandas as pd

df = pd.read_excel('employee__1_.xls', dtype=object)

df['Date of Birth F'] = pd.to_datetime(df['Date of Birth'])
df['Date of Joining F'] = pd.to_datetime(df['Date of Joining'])

df = df.sort_values(['Quarter of Joining', 'Date of Birth F'], ascending=[True, True])
dfg = df.groupby(['Quarter of Joining'])['First Name'].apply(list).reset_index()
dt = dfg.set_index('Quarter of Joining').T.to_dict('records')

for item in dt:
    print(item)


	
