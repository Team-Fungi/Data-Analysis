from sklearn import preprocessing
import pandas as pd
import numpy as np
from sklearn import utils
import torch


def label_encoder(filecsv, tax):
    le = preprocessing.LabelEncoder()
    labels = pd.read_csv(filecsv)[tax]
    le.fit(labels)
    np.save(f'{filecsv[:-14]}_Y_{tax}5NA.npy', le.transform(labels))


label_encoder('Test_5%_noambi.csv', 'PHYLUM')
label_encoder('Train_5%_noambi.csv', 'PHYLUM')
label_encoder('Validation_5%_noambi.csv', 'PHYLUM')

label_encoder('Test_5%_noambi.csv', 'CLASS')
label_encoder('Train_5%_noambi.csv', 'CLASS')
label_encoder('Validation_5%_noambi.csv', 'CLASS')

label_encoder('Test_5%_noambi.csv', 'ORDER')
label_encoder('Train_5%_noambi.csv', 'ORDER')
label_encoder('Validation_5%_noambi.csv', 'ORDER')

label_encoder('Test_5%_noambi.csv', 'FAMILY')
label_encoder('Train_5%_noambi.csv', 'FAMILY')
label_encoder('Validation_5%_noambi.csv', 'FAMILY')

label_encoder('Test_5%_noambi.csv', 'GENUS')
label_encoder('Train_5%_noambi.csv', 'GENUS')
label_encoder('Validation_5%_noambi.csv', 'GENUS')