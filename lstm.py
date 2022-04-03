from keras.layers import Input, LSTM
from keras.layers.wrappers import Bidirectional

from constants import RANDOM_NORMAL_INITIALIZER, ZEROS_INITIALIZER, LSTM_DROPOUT

def bi_lstm_network(inputs):
    lstm_out = Bidirectional(LSTM(
        128, 
        return_sequences = True, 
        kernel_initializer = RANDOM_NORMAL_INITIALIZER, 
        dropout = LSTM_DROPOUT, 
        recurrent_dropout = LSTM_DROPOUT,
        recurrent_initializer = RANDOM_NORMAL_INITIALIZER, 
        bias_initializer = ZEROS_INITIALIZER
    ))(inputs)

    return lstm_out