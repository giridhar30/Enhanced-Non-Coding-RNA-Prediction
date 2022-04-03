import numpy as np
import h5py as h5

from keras.utils import np_utils

from constants import ENCODED_DATA_PATH, H5_EXTENSION

def read_dataset(dataset):
    # fetching dataset
    h5_dataset = h5.File(ENCODED_DATA_PATH + dataset + H5_EXTENSION, 'r')

    # separating data and labels
    x = h5_dataset['Train_Data']
    y = h5_dataset['Label']

    # converting to numpy array
    x = np.array(x)
    y = np.array(y)

    # converting labels to binary categorical numpy array
    y = np_utils.to_categorical(y)

    # returning the dataset
    return (x, y)