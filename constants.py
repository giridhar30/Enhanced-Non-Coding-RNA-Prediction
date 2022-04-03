# constants for file read/write
RAW_DATA_PATH = 'Train_Test_Raw_Data/'
ENCODED_DATA_PATH = 'Data/'
TRAIN_FILE_NAME = 'Train'
TEST_FILE_NAME = 'Test'
H5_EXTENSION = '.h5'
MODEL_NAME = 'Trained_ncRNA_Classifier'

# constants for nucleotide sequence encoding
CODE_MAP = {
    'A': [1, 0, 0, 0, 0, 0, 1, 0],
    'T': [0, 0, 1, 0, 1, 0, 0, 0],
    'G': [0, 1, 0, 0, 0, 0, 0, 1],
    'C': [0, 0, 0, 1, 0, 1, 0, 0],
    'N': [0, 0, 0, 0, 0, 0, 0, 0]
}

# constants for mapping ncRNA families
FAMILY_MAP = {
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

# constants for model training
INPUT_DIM = 8    
TIME_STEPS = 500
BATCH_SIZE = 128
EPOCHS = 50
LSTM_DROPOUT = 0.3
NN_DROPOUT = 0.4
METRICS = ['accuracy']
CATEGORICAL_CROSS_ENTROPY_LOSS = 'categorical_crossentropy'
RMSPROP_OPTIMIZER = 'RMSProp'
RANDOM_NORMAL_INITIALIZER = 'RandomNormal'
ZEROS_INITIALIZER = 'zeros'
ReLU_ACTIVATION = 'relu'
SOFTMAX_ACTIVATION = 'softmax'