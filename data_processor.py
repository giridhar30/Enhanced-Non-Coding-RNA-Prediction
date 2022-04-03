import numpy as np
import pandas as pd
import h5py as h5

from data_encoder import encode_base
from constants import FAMILY_MAP, RAW_DATA_PATH, ENCODED_DATA_PATH, H5_EXTENSION

# data processing
def process_data(file_name):
    # getting the raw data
    input_data_path = RAW_DATA_PATH + file_name
    
    # saving the matrices and labels of ncRNAs
    list_matrix = []
    list_label = [] 

    # encoding the raw data
    for line in open(input_data_path):
        if(line[0] == '>'):
            list_label.append(FAMILY_MAP[line.split()[-1]])
        else:
            list_matrix.append(encode_base(line))

    list_matrix = np.array(list_matrix)
    list_label = np.array(list_label)

    # saving the encoded data as h5 files
    output_data_path = ENCODED_DATA_PATH + file_name + H5_EXTENSION

    f = h5.File(output_data_path, 'w') 
    f.create_dataset('Train_Data', data=list_matrix)
    f.create_dataset('Label', data=list_label)


