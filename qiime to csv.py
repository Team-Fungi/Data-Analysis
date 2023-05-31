import pandas as pd
from Bio import SeqIO


def QIIME_to_CSV(filetxt, filefasta):
    # Loading Taxonomy data into dataframe, make column names/header
    header = ['ACCNUM', 'KINGDOM', 'PHYLUM', 'CLASS', 'ORDER', 'FAMILY', 'GENUS', 'SPECIES']
    DataframeAll = pd.read_csv(filetxt,
                               delimiter=r'[\t;]',
                               engine='python',
                               names=header)

    # Removing prefixes from each column (k__, p__, ...)
    for column in DataframeAll:
        DataframeAll[column] = DataframeAll[column].str.lstrip(f'{str(column)[0].lower()}__')
        if str(column) == 'SPECIES':
            DataframeAll[column] = DataframeAll[column].str.rstrip('_sp')

    # Replacing XX_XX_Incertae_sedis with NaN
    for column in DataframeAll:
        DataframeAll.loc[DataframeAll[str(column)].str.contains('sedis'), str(column)] = 'NaN'

    # Create dataframe of sequences
    sequences = {}
    with open(filefasta) as fp:
        for record in SeqIO.parse(fp, "fasta"):
            sequences[record.id] = str(record.seq)
    df_seq = pd.DataFrame(list(sequences.items()), columns=['ACCN', 'SEQ'])

    # Adding column 'SEQ' with sequences to dataframe
    # Both dataframes are sorted on their common accession number, indexes reset
    # adding sequence column to dataframeall, same order!
    DataframeAll = DataframeAll.sort_values(by='ACCNUM').reset_index(drop=True)
    df_seq = df_seq.sort_values(by='ACCN').reset_index(drop=True)
    DataframeAll['SEQ'] = df_seq['SEQ']

    # Adding column 'LENGTH' with lengths of sequences
    DataframeAll['LENGTH'] = DataframeAll['SEQ'].str.len()

    # Saving csv file for further use
    DataframeAll.to_csv(f'Taxonomy_{str(filefasta)[19:-17]}.csv', index=None)
    print(f'QIIME set combined to Taxonomy_{str(filefasta)[19:-17]}.csv')


QIIME_to_CSV('sh_taxonomy_qiime_ver9_97_29.11.2022.txt', 'sh_refs_qiime_ver9_97_29.11.2022.fasta')
# QIIME_to_CSV('sh_taxonomy_qiime_ver9_99_29.11.2022.txt', 'sh_refs_qiime_ver9_99_29.11.2022.fasta')
# QIIME_to_CSV('sh_taxonomy_qiime_ver9_dynamic_29.11.2022.txt', 'sh_refs_qiime_ver9_dynamic_29.11.2022.fasta')
