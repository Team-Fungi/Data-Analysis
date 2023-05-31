# Libraries
import pandas as pd


def data_cleaning(filecsv):
    # Performing the desired cleaning steps
    df = pd.read_csv(filecsv)
    df_noduplicates = df.drop_duplicates(subset='SEQ')
    df_final = df_noduplicates.dropna()
    # calculating 'losses' due to cleaning
    s_df = len(df.index)
    s_dup = len(df.index) - len(df_noduplicates.index)
    p_dup = f'{str(s_dup / s_df * 100)[:5]}%'
    s_nan = len(df.index) - len(df_final)
    p_nan = f'{str(s_nan / s_df * 100)[:5]}%'
    s_final = len(df_final.index)
    p_final = f'{str(s_final / s_df * 100)[:5]}%'
    df_sizes = pd.DataFrame({'': ["QIIME Release", "Duplicates", "Entries with NaN", "Final Dataset"],
                             'Amount of sequences': [s_df, s_dup, s_nan, s_final],
                             '% compared to QIIME release': ['/', p_dup, p_nan, p_final]})
    # Saving the cleaned data into csv and printing the 'losses' due to cleaning
    df_final.to_csv(f'{filecsv[:-4]}_final.csv', index=None)
    print(f'Data is cleaned and saved in {filecsv[:-4]}_final.csv\n'
          f'Loss of cleaning[NEEDS TO BE CHANGED]:\n'
          f'{df_sizes.to_markdown()}')


data_cleaning('Taxonomy_97.csv')
#data_cleaning('Taxonomy_99.csv')
#data_cleaning('Taxonomy_dynamic.csv')

# import squarify
#import matplotlib.pyplot as plt
# Plot sizes of cleaning of dataframe (kinda stupid with the 2 duplicates?)
#df_sizes = pd.DataFrame({'Size':[103654,93901,2], 'Consisting of':["Final Dataset", "Entries with NaN", "Duplicates"]})
#squarify.plot(sizes=df_sizes['Size'], label=df_sizes['Consisting of'], alpha=.8)
#plt.axis('off')
#plt.savefig('Sizes.png')
