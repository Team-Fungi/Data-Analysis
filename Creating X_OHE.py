import pandas as pd
import numpy as np




def to_numpy(seqs):
    nucl_map = {"A": 0, "C": 1, "G": 2, "T": 3, # four nucleotides
                "Y": 4, "R": 4, "W": 4, "S": 4, "K": 4, "M": 4, # degenerate bases (2 bases represented)
                "D": 4, "V": 4, "H": 4, "B": 4, # degenerate bases (3 bases represented)
                "N": 4 } # ambigous nucleotide (4 bases represented)
    return np.vstack([
        np.array([nucl_map[ch] for ch in s], dtype=np.uint8) for s in seqs
    ])


def one_hot_encode(seq_array):
    n, length = seq_array.shape
    enc = np.vstack([np.eye(4), [0, 0, 0, 0]]).astype(np.uint8)
    return np.stack([enc[seq] for seq in seq_array], axis=0)


def OHEr(csvfile):
    df = pd.read_csv(csvfile)
    sequences = []
    for seq in df['SEQ']:
        if len(seq) != 700:
            seq += 'N' * (700 - len(seq))
        sequences.append(seq)
    train_seqs_array = to_numpy(sequences)
    train_seqs_array_encoded = one_hot_encode(train_seqs_array)
    np.save(f"{csvfile[:-14]}_X_OHE5NA.npy", train_seqs_array_encoded)

OHEr('Train_5%_noambi.csv')
OHEr('Test_5%_noambi.csv')
OHEr('Validation_5%_noambi.csv')
