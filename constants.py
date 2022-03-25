# constants for file read/write
raw_data_path = 'Train_Test_Raw_Data/'
encoded_data_path = 'Data/'
h5_extension = '.h5'

# constants for nucleotide sequence encoding
code_map = {
    'A': [1, 0, 0, 0, 0, 0, 1, 0],
    'T': [0, 0, 1, 0, 1, 0, 0, 0],
    'G': [0, 1, 0, 0, 0, 0, 0, 1],
    'C': [0, 0, 0, 1, 0, 1, 0, 0],
    'N': [0, 0, 0, 0, 0, 0, 0, 0]
}

# constants for mapping ncRNA families
family_map = {
    '5S_rRNA': 0,
    '5_8S_rRNA': 1,
    'tRNA': 2,
    'ribozyme': 3,
    'CD-box': 4,
    'miRNA': 5,
    'Intron_gpI': 6,
    'Intron_gpII': 7,
    'HACA-box': 8,
    'riboswitch': 9,
    'IRES': 10,
    'leader': 11,
    'scaRNA': 12
}