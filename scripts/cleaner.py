import pandas as pd

# pd.set_option('display.max_rows', 300)
# pd.set_option('display.max_columns', 300)

# Read file from
tmp_data = pd.read_csv("hf.csv", header=0, na_values=["", "---"])


# count na's
naDict = tmp_data.isna().sum().to_dict()

# drop cols with too many na's, automatically drops empty cols
for col, count in zip(naDict.keys(), naDict.values()):
    if count >= 20:
        tmp_data.drop(col, axis='columns', inplace=True)


# map col names easy to read col names
nameDict = {}
for j, col in enumerate(tmp_data.columns):
    nameDict[col] = str('x') + str(j)
tmp_data.set_axis(nameDict.values(), axis=1, inplace=True)
irrCols = ['x0', 'x1',  'x3', 'x4', 'x5', 'x6', 'x8', 'x10']
tmp_data.drop(irrCols, axis='columns', inplace=True)  # dropping irrelevant cols, see nameDict for specific names


# change col data types
list_cols_chType = ['x9', 'x7', 'x32'] + list(nameDict.values())[49:84]
for col in list_cols_chType:
    tmp_data[col] = tmp_data[col].astype('category')

# Perhaps changing string to factors will help.
tmp_data.to_csv('cleaned_data.csv', index=False)

print('cleaned data stored in file cleaned_data.csv')