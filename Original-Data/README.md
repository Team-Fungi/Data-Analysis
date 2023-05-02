# Original Data - 	UNITE QIIME release for Fungi
Three sets of QIIME files are released, corresponding to the SHs resulting from clustering at the 3% distance (97% similarity) and 1% distance (99% similarity) threshold levels. The third set of files is the result of a dynamic use of clustering thresholds, such that some SHs are delimited at the 3% distance level, some at the 2.5% distance level, some at the 2% distance level, and so on; these choices were made manually by experts of those particular lineages of fungi. The syntax is the same throughout the three sets of files.

Each SH is given a stable name of the accession number type, here shown in the FASTA file of the dynamic set:

SH099456.05FU_FJ357315_refs
CACAATATGAAGGCGGGCTGGCACTCCTTGAGAGGACCGGC…

SH099456 = accession number of the SH
05FU = global key release 5, organism group FUngi
FJ357315 = GenBank/UNITE accession number of sequence chosen to represent the SH
refs = this is a manually designated RefS
(reps = this is an automatically chosen RepS)

In the corresponding text file, the classification string of the SH is found:

SH099456.05FU_FJ357315_refs    k__Fungi;p__Ascomycota;c__Dothideomycetes;o__Pleosporales;f__Pleosporaceae;g__Embellisia;s__Embellisia_planifunda

This specifies the hierarchical classification of the sequence. k = kingdom; p = phylum ; c = class ; o = order ; f = family ; g = genus ; and s = species. Missing information is indicated as "unidentified" item; “f__unidentified;” means that no family name for the sequence exists.

Citation:
Abarenkov, Kessy; Zirk, Allan; Piirmann, Timo; Pöhönen, Raivo; Ivanov, Filipp; Nilsson, R. Henrik; Kõljalg, Urmas (2022): UNITE QIIME release for Fungi. Version 16.10.2022. UNITE Community. https://doi.org/10.15156/BIO/2483915
