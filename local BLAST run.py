import time
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline
import subprocess
start_time = time.time()

def create_blast_db(input_file, db_type, out_db):
    # command to create the database
    cmd = f"makeblastdb -in {input_file} -dbtype {db_type} -out {out_db}"
    subprocess.run(cmd, shell=True)

def run_blast(query_file, db, out_file, evalue=0.01):
    # command to run the blast search
    cmd = f"blastn -query {query_file} -db {db} -out {out_file} -evalue {evalue}"
    subprocess.run(cmd, shell=True)

# Step 1: create the database
fasta_file = 'C:/Users/maxim/anaconda3/envs/Programmeren/bachelors_project/BLAST/sh_general_release_dynamic_s_29.11.2022.fasta'
db_type = "nucl"  # "nucl" for nucleotide sequences, "prot" for protein sequences
output_db = "C:/Users/maxim/anaconda3/envs/Programmeren/bachelors_project/BLAST"  # replace with the desired output db name
create_blast_db(fasta_file, db_type, output_db)

# run the blast search
query_file = "testblast2.fasta"
out_file = 'C:/Users/maxim/anaconda3/envs/Programmeren/bachelors_project/BLAST/BLAST_Run_Test.txt'

run_blast(query_file, output_db, out_file)


print("--- %s seconds ---" % (time.time() - start_time))
_____________________________________________________________________
output:

Building a new DB, current time: 05/25/2023 04:22:05
New DB name:   C:\Users\maxim\anaconda3\envs\Programmeren\bachelors_project\BLAST
New DB title:  C:/Users/maxim/anaconda3/envs/Programmeren/bachelors_project/BLAST/sh_general_release_dynamic_s_29.11.2022.fasta
Sequence type: Nucleotide
Deleted existing Nucleotide BLAST database named C:\Users\maxim\anaconda3\envs\Programmeren\bachelors_project\BLAST
Keep MBits: T
Maximum file size: 3000000000B
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 23
Aspicilia_simoënsis|EU057927|SH0055795.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 24
Aspicilia_simoënsis|EU057927|SH0055795.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 175
Aspicilia_simoënsis|EU057927|SH0055795.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 176
Aspicilia_simoënsis|EU057927|SH0055795.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 23
Aspicilia_simoënsis|AF332114|SH0055797.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 24
Aspicilia_simoënsis|AF332114|SH0055797.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 175
Aspicilia_simoënsis|AF332114|SH0055797.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 176
Aspicilia_simoënsis|AF332114|SH0055797.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 23
Aspicilia_simoënsis|EU057927|SH0055795.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 24
Aspicilia_simoënsis|EU057927|SH0055795.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 175
Aspicilia_simoënsis|EU057927|SH0055795.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 176
Aspicilia_simoënsis|EU057927|SH0055795.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 23
Aspicilia_simoënsis|AF332114|SH0055797.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 24
Aspicilia_simoënsis|AF332114|SH0055797.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 175
Aspicilia_simoënsis|AF332114|SH0055797.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 176
Aspicilia_simoënsis|AF332114|SH0055797.09FU|reps_singleton|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 28
Ochrolechia_szatalaënsis|MK812256|SH0943002.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Ochrolechiaceae;g__Ochrolechia;s__Ochrolechia_szatalaënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 29
Ochrolechia_szatalaënsis|MK812256|SH0943002.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Ochrolechiaceae;g__Ochrolechia;s__Ochrolechia_szatalaënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 179
Ochrolechia_szatalaënsis|MK812256|SH0943002.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Ochrolechiaceae;g__Ochrolechia;s__Ochrolechia_szatalaënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 180
Ochrolechia_szatalaënsis|MK812256|SH0943002.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Ochrolechiaceae;g__Ochrolechia;s__Ochrolechia_szatalaënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 28
Ochrolechia_szatalaënsis|MK812256|SH0943002.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Ochrolechiaceae;g__Ochrolechia;s__Ochrolechia_szatalaënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 29
Ochrolechia_szatalaënsis|MK812256|SH0943002.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Ochrolechiaceae;g__Ochrolechia;s__Ochrolechia_szatalaënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 179
Ochrolechia_szatalaënsis|MK812256|SH0943002.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Ochrolechiaceae;g__Ochrolechia;s__Ochrolechia_szatalaënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 180
Ochrolechia_szatalaënsis|MK812256|SH0943002.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Ochrolechiaceae;g__Ochrolechia;s__Ochrolechia_szatalaënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 28
Tricholoma_borgsjoeënse|DQ389733|SH0950546.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Tricholomataceae;g__Tricholoma;s__Tricholoma_borgsjoeënse
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 29
Tricholoma_borgsjoeënse|DQ389733|SH0950546.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Tricholomataceae;g__Tricholoma;s__Tricholoma_borgsjoeënse
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 177
Tricholoma_borgsjoeënse|DQ389733|SH0950546.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Tricholomataceae;g__Tricholoma;s__Tricholoma_borgsjoeënse
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 178
Tricholoma_borgsjoeënse|DQ389733|SH0950546.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Tricholomataceae;g__Tricholoma;s__Tricholoma_borgsjoeënse
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 28
Tricholoma_borgsjoeënse|DQ389733|SH0950546.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Tricholomataceae;g__Tricholoma;s__Tricholoma_borgsjoeënse
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 29
Tricholoma_borgsjoeënse|DQ389733|SH0950546.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Tricholomataceae;g__Tricholoma;s__Tricholoma_borgsjoeënse
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 177
Tricholoma_borgsjoeënse|DQ389733|SH0950546.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Tricholomataceae;g__Tricholoma;s__Tricholoma_borgsjoeënse
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 178
Tricholoma_borgsjoeënse|DQ389733|SH0950546.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Tricholomataceae;g__Tricholoma;s__Tricholoma_borgsjoeënse
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 23
Aspicilia_simoënsis|EU057929|SH0991860.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 24
Aspicilia_simoënsis|EU057929|SH0991860.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 165
Aspicilia_simoënsis|EU057929|SH0991860.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 166
Aspicilia_simoënsis|EU057929|SH0991860.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 23
Aspicilia_simoënsis|MN906280|SH0991863.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 24
Aspicilia_simoënsis|MN906280|SH0991863.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 165
Aspicilia_simoënsis|MN906280|SH0991863.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 166
Aspicilia_simoënsis|MN906280|SH0991863.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 23
Aspicilia_simoënsis|EU057929|SH0991860.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 24
Aspicilia_simoënsis|EU057929|SH0991860.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 165
Aspicilia_simoënsis|EU057929|SH0991860.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 166
Aspicilia_simoënsis|EU057929|SH0991860.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 23
Aspicilia_simoënsis|MN906280|SH0991863.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 24
Aspicilia_simoënsis|MN906280|SH0991863.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 165
Aspicilia_simoënsis|MN906280|SH0991863.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 166
Aspicilia_simoënsis|MN906280|SH0991863.09FU|reps|k__Fungi;p__Ascomycota;c__Lecanoromycetes;o__Pertusariales;f__Megasporaceae;g__Aspicilia;s__Aspicilia_simoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 16
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 17
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 145
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 146
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 158
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 159
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 16
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 17
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 145
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 146
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 158
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 159
Epichloë_amarillans|AF385206|SH1111049.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_amarillans
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 16
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 17
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 143
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 144
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 156
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 157
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 16
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 17
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 143
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 144
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 156
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 157
Epichloë_sibirici|DQ675574|SH1111114.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_sibirici
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 29
Fomitiporia_hippophaëicola|UDB031565|SH1115797.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Hymenochaetales;f__Hymenochaetaceae;g__Fomitiporia;s__Fomitiporia_hippophaëicola
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 30
Fomitiporia_hippophaëicola|UDB031565|SH1115797.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Hymenochaetales;f__Hymenochaetaceae;g__Fomitiporia;s__Fomitiporia_hippophaëicola
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 188
Fomitiporia_hippophaëicola|UDB031565|SH1115797.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Hymenochaetales;f__Hymenochaetaceae;g__Fomitiporia;s__Fomitiporia_hippophaëicola
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 189
Fomitiporia_hippophaëicola|UDB031565|SH1115797.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Hymenochaetales;f__Hymenochaetaceae;g__Fomitiporia;s__Fomitiporia_hippophaëicola
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 29
Fomitiporia_hippophaëicola|UDB031565|SH1115797.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Hymenochaetales;f__Hymenochaetaceae;g__Fomitiporia;s__Fomitiporia_hippophaëicola
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 30
Fomitiporia_hippophaëicola|UDB031565|SH1115797.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Hymenochaetales;f__Hymenochaetaceae;g__Fomitiporia;s__Fomitiporia_hippophaëicola
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 188
Fomitiporia_hippophaëicola|UDB031565|SH1115797.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Hymenochaetales;f__Hymenochaetaceae;g__Fomitiporia;s__Fomitiporia_hippophaëicola
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 189
Fomitiporia_hippophaëicola|UDB031565|SH1115797.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Hymenochaetales;f__Hymenochaetaceae;g__Fomitiporia;s__Fomitiporia_hippophaëicola
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 24
Tilletia_buchloëana|EF204935|SH1199049.09FU|reps|k__Fungi;p__Basidiomycota;c__Exobasidiomycetes;o__Tilletiales;f__Tilletiaceae;g__Tilletia;s__Tilletia_buchloëana
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 25
Tilletia_buchloëana|EF204935|SH1199049.09FU|reps|k__Fungi;p__Basidiomycota;c__Exobasidiomycetes;o__Tilletiales;f__Tilletiaceae;g__Tilletia;s__Tilletia_buchloëana
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 167
Tilletia_buchloëana|EF204935|SH1199049.09FU|reps|k__Fungi;p__Basidiomycota;c__Exobasidiomycetes;o__Tilletiales;f__Tilletiaceae;g__Tilletia;s__Tilletia_buchloëana
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 168
Tilletia_buchloëana|EF204935|SH1199049.09FU|reps|k__Fungi;p__Basidiomycota;c__Exobasidiomycetes;o__Tilletiales;f__Tilletiaceae;g__Tilletia;s__Tilletia_buchloëana
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 24
Tilletia_buchloëana|EF204935|SH1199049.09FU|reps|k__Fungi;p__Basidiomycota;c__Exobasidiomycetes;o__Tilletiales;f__Tilletiaceae;g__Tilletia;s__Tilletia_buchloëana
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 25
Tilletia_buchloëana|EF204935|SH1199049.09FU|reps|k__Fungi;p__Basidiomycota;c__Exobasidiomycetes;o__Tilletiales;f__Tilletiaceae;g__Tilletia;s__Tilletia_buchloëana
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 167
Tilletia_buchloëana|EF204935|SH1199049.09FU|reps|k__Fungi;p__Basidiomycota;c__Exobasidiomycetes;o__Tilletiales;f__Tilletiaceae;g__Tilletia;s__Tilletia_buchloëana
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 168
Tilletia_buchloëana|EF204935|SH1199049.09FU|reps|k__Fungi;p__Basidiomycota;c__Exobasidiomycetes;o__Tilletiales;f__Tilletiaceae;g__Tilletia;s__Tilletia_buchloëana
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 30
Cladophialophora_samoënsis|EU137291|SH1280398.09FU|refs|k__Fungi;p__Ascomycota;c__Eurotiomycetes;o__Chaetothyriales;f__Herpotrichiellaceae;g__Cladophialophora;s__Cladophialophora_samoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 31
Cladophialophora_samoënsis|EU137291|SH1280398.09FU|refs|k__Fungi;p__Ascomycota;c__Eurotiomycetes;o__Chaetothyriales;f__Herpotrichiellaceae;g__Cladophialophora;s__Cladophialophora_samoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 193
Cladophialophora_samoënsis|EU137291|SH1280398.09FU|refs|k__Fungi;p__Ascomycota;c__Eurotiomycetes;o__Chaetothyriales;f__Herpotrichiellaceae;g__Cladophialophora;s__Cladophialophora_samoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 194
Cladophialophora_samoënsis|EU137291|SH1280398.09FU|refs|k__Fungi;p__Ascomycota;c__Eurotiomycetes;o__Chaetothyriales;f__Herpotrichiellaceae;g__Cladophialophora;s__Cladophialophora_samoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 30
Cladophialophora_samoënsis|EU137291|SH1280398.09FU|refs|k__Fungi;p__Ascomycota;c__Eurotiomycetes;o__Chaetothyriales;f__Herpotrichiellaceae;g__Cladophialophora;s__Cladophialophora_samoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 31
Cladophialophora_samoënsis|EU137291|SH1280398.09FU|refs|k__Fungi;p__Ascomycota;c__Eurotiomycetes;o__Chaetothyriales;f__Herpotrichiellaceae;g__Cladophialophora;s__Cladophialophora_samoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 193
Cladophialophora_samoënsis|EU137291|SH1280398.09FU|refs|k__Fungi;p__Ascomycota;c__Eurotiomycetes;o__Chaetothyriales;f__Herpotrichiellaceae;g__Cladophialophora;s__Cladophialophora_samoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 194
Cladophialophora_samoënsis|EU137291|SH1280398.09FU|refs|k__Fungi;p__Ascomycota;c__Eurotiomycetes;o__Chaetothyriales;f__Herpotrichiellaceae;g__Cladophialophora;s__Cladophialophora_samoënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 30
Cortinarius_grosmorneënsis|JQ746596|SH1282662.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Cortinariaceae;g__Cortinarius;s__Cortinarius_grosmorneënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 31
Cortinarius_grosmorneënsis|JQ746596|SH1282662.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Cortinariaceae;g__Cortinarius;s__Cortinarius_grosmorneënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 181
Cortinarius_grosmorneënsis|JQ746596|SH1282662.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Cortinariaceae;g__Cortinarius;s__Cortinarius_grosmorneënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 182
Cortinarius_grosmorneënsis|JQ746596|SH1282662.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Cortinariaceae;g__Cortinarius;s__Cortinarius_grosmorneënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 30
Cortinarius_grosmorneënsis|JQ746596|SH1282662.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Cortinariaceae;g__Cortinarius;s__Cortinarius_grosmorneënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 31
Cortinarius_grosmorneënsis|JQ746596|SH1282662.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Cortinariaceae;g__Cortinarius;s__Cortinarius_grosmorneënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 181
Cortinarius_grosmorneënsis|JQ746596|SH1282662.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Cortinariaceae;g__Cortinarius;s__Cortinarius_grosmorneënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 182
Cortinarius_grosmorneënsis|JQ746596|SH1282662.09FU|refs|k__Fungi;p__Basidiomycota;c__Agaricomycetes;o__Agaricales;f__Cortinariaceae;g__Cortinarius;s__Cortinarius_grosmorneënsis
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 16
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 17
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 152
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 153
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 165
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 166
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 16
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 17
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 152
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 153
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 165
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 166
Epichloë_glyceriae|L78301|SH1749225.09FU|refs_singleton|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_glyceriae
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 16
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 17
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 143
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 144
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 156
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 157
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 16
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 17
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 143
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 144
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xC3] in string at byte 156
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Error: (803.7) [makeblastdb] Blast-def-line-set.E.title
Bad char [0xAB] in string at byte 157
Epichloë_typhina|UDB039839|SH3321827.09FU|refs|k__Fungi;p__Ascomycota;c__Sordariomycetes;o__Hypocreales;f__Clavicipitaceae;g__Epichloë;s__Epichloë_typhina
Adding sequences from FASTA; added 206184 sequences in 6.36833 seconds.


--- 13538.845980405807 seconds ---

Process finished with exit code 0
