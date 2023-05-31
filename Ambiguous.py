import pandas as pd


def how_many_ambi(dataframe):
    df = pd.read_csv(dataframe)
    searchfor = ['R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N']
    df['AMBI'] = df['SEQ'].str.count('|'.join(searchfor))
    df['AMBIPERC'] = df['AMBI'] / df['LENGTH']
    print('Amount of ambiguous nucleotides were added to dataframe in absolute numbers and percentages')
    return df


def too_much_ambi(dataframe, threshold=0.01):
    df = dataframe
    df = df[df.AMBIPERC < threshold]
    print('Sequences containing more than 1% ambiguous nucleotides were deleted from dataframe')
    return df


def drop_all_ambi(dataframe):
    df = dataframe
    df = df[df.AMBIPERC == 0.0]
    return df


df = how_many_ambi('Taxonomy_99_final.csv')
df_lowambi = too_much_ambi(df)
df_noambi = drop_all_ambi(df)

dfwithambi = df.shape[0]
lowambi = df_lowambi.shape[0]
noambi = df_noambi.shape[0]
print(dfwithambi)
print(lowambi)
print(noambi)

