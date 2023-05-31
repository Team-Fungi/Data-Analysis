import pandas as pd


def how_many_ambi(dataframe):
    df = pd.read_csv(dataframe)
    searchfor = ['R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N']
    df['AMBI'] = df['SEQ'].str.count('|'.join(searchfor))
    df['AMBIPERC'] = df['AMBI'] / df['LENGTH']
    print('Amount of ambiguous nucleotides were added to dataframe in absolute numbers and percentages')
    return df


def drop_all_ambi(dataframe):
    df = dataframe
    df = df[df.AMBIPERC == 0.0]
    return df


def processor(csv, minimumrequirement, ambiguous):
    df = how_many_ambi(csv)
    highest_genus = df.GENUS.value_counts()[0]
    if ambiguous == 'noambi':
        df = drop_all_ambi(df)
    df_upperlength = df[df.LENGTH <= 700]
    df_goodlength = df_upperlength[df_upperlength.LENGTH >= 400]
    freq = df_goodlength['GENUS'].value_counts()
    items = freq[freq > (highest_genus * minimumrequirement // 100)].index  # items that appear more than 3 times
    finaldf = df_goodlength[df_goodlength['GENUS'].isin(items)]
    finaldf.to_csv(f'Taxonomy_99_{minimumrequirement}%_{ambiguous}.csv', index=None)

processor('Taxonomy_99_final.csv', 1, 'noambi')
processor('Taxonomy_99_final.csv', 5, 'noambi')
processor('Taxonomy_99_final.csv', 1, 'ambi')
processor('Taxonomy_99_final.csv', 5, 'ambi')