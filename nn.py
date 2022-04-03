from keras.layers import Dense, Dropout

from constants import NN_DROPOUT
from constants import RANDOM_NORMAL_INITIALIZER, ZEROS_INITIALIZER, ReLU_ACTIVATION, SOFTMAX_ACTIVATION

def output_decoding_network(inputs):
    # hidden layer 1
    dense_one = Dense(
        128, 
        kernel_initializer = RANDOM_NORMAL_INITIALIZER, 
        bias_initializer = ZEROS_INITIALIZER, 
        activation = ReLU_ACTIVATION
    )(inputs)
    dense_one = Dropout(NN_DROPOUT)(dense_one)

    # hidden layer 2
    dense_two = Dense(
        64, 
        kernel_initializer = RANDOM_NORMAL_INITIALIZER, 
        bias_initializer = ZEROS_INITIALIZER, 
        activation = ReLU_ACTIVATION
    )(dense_one)
    dense_two = Dropout(NN_DROPOUT)(dense_two)

    # hidden layer 3
    dense_three = Dense(
        32, 
        kernel_initializer = RANDOM_NORMAL_INITIALIZER, 
        bias_initializer = ZEROS_INITIALIZER, 
        activation = ReLU_ACTIVATION
    )(dense_two)
    dense_three = Dropout(NN_DROPOUT)(dense_three)

    # output layer
    outputs = Dense(13, activation = SOFTMAX_ACTIVATION)(dense_three)

    # returning the network
    return outputs