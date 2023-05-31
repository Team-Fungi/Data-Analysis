import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

# Project settings for plots
plt.style.use('bmh')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'UGent Panno Text'
plt.rcParams['font.monospace'] = 'UGent Panno Text'
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['legend.fontsize'] = 20
# For main: (UGent blue: color='#1E64C8')
# For main: (black: color='black')
# For accents: (UGent yellow: color='#FFD200', linestyle='dashed', linewidth=2)

rep = pd.read_csv('Taxonomy_99_final.csv')
print(rep.GENUS.value_counts())
freq = rep['GENUS'].value_counts()
items = freq[freq > 670].index  # items that appear more than 3 times
more_than_1_df = rep[rep['GENUS'].isin(items)]
more_than_1_df['GENUS'].value_counts().plot.bar(color='#1E64C8')
print(rep['GENUS'].value_counts().mean())
items2 = freq[freq < 65].index
less_than_10df = rep[rep['GENUS'].isin(items2)]
print(less_than_10df)
plt.axhline(rep['GENUS'].value_counts().mean(), color='#FFD200', linestyle='dashed', linewidth=2, label='Mean')
plt.title(f'Top 15 genus abundance in cleaned dataset', fontweight='bold')
plt.xlabel('Genus')
plt.ylabel('Abundance')
plt.legend()
plt.savefig(f'RepresentationDistribution99.svg')
plt.show()


