import defkmer
import pandas as pd
import numpy as np


dftrain = pd.read_csv("Train_1%_noambi.csv")
dftest = pd.read_csv("Test_1%_noambi.csv")
dfval = pd.read_csv("Validation_1%_noambi.csv")
# Saving 3-mers in npy for later use
k = 3
np.save('Train_X_3mer1NA.npy', np.array([defkmer.count_kmer(sequence, k) for sequence in dftrain['SEQ']], dtype=np.float32))
np.save('Test_X_3mer1NA.npy', np.array([defkmer.count_kmer(sequence, k) for sequence in dftest['SEQ']], dtype=np.float32))
np.save('Validation_X_3mer1NA.npy', np.array([defkmer.count_kmer(sequence, k) for sequence in dfval['SEQ']], dtype=np.float32))

# Saving 4-mers in npy for later use
k = 4
np.save('Train_X_4mer1NA.npy', np.array([defkmer.count_kmer(sequence, k) for sequence in dftrain['SEQ']], dtype=np.float32))
np.save('Test_X_4mer1NA.npy', np.array([defkmer.count_kmer(sequence, k) for sequence in dftest['SEQ']], dtype=np.float32))
np.save('Validation_X_4mer1NA.npy', np.array([defkmer.count_kmer(sequence, k) for sequence in dfval['SEQ']], dtype=np.float32))

# Saving 5-mers in npy for later use
k = 5
np.save('Train_X_5mer1NA.npy', np.array([defkmer.count_kmer(sequence, k) for sequence in dftrain['SEQ']], dtype=np.float32))
np.save('Test_X_5mer1NA.npy', np.array([defkmer.count_kmer(sequence, k) for sequence in dftest['SEQ']], dtype=np.float32))
np.save('Validation_X_5mer1NA.npy', np.array([defkmer.count_kmer(sequence, k) for sequence in dfval['SEQ']], dtype=np.float32))