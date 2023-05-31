import itertools
import re
import numpy as np

def count_kmer(sequence, k):
    # Define possible k-mers and create a dictionary to count the appereances in the sequence
    bases = ['A', 'T', 'G', 'C', 'N']
    possikmer = [''.join(p) for p in itertools.product(bases, repeat=k)]
    kmer_dict = dict.fromkeys(possikmer, 0)
    # Replace all the ambiguous nucleotides with N
    sequence = re.sub('Y|R|W|S|K|M|D|V|H|B', 'N', sequence)
    # Counting kmers in dictionary
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmer_dict[kmer] += 1

    kmerlist = np.array(list(kmer_dict.values()))
    som = np.sum(kmerlist)
    standardkmerlist = kmerlist / som

    return standardkmerlist
