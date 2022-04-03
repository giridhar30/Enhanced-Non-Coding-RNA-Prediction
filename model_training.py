from keras.models import Model
from keras.layers import Input

from data_processor import process_data
from dataset_reader import read_dataset

from lstm import bi_lstm_network
from attention_mechanism import attention_network
from nn import output_decoding_network

from constants import TRAIN_FILE_NAME, TEST_FILE_NAME, CATEGORICAL_CROSS_ENTROPY_LOSS, RMSPROP_OPTIMIZER 
from constants import INPUT_DIM, TIME_STEPS, BATCH_SIZE, EPOCHS, METRICS

def train_model(model_name):
    # processing and encoding the data
    # process_data(TRAIN_FILE_NAME)
    # process_data(TEST_FILE_NAME)

    # reading train and test set
    x_train, y_train = read_dataset(TRAIN_FILE_NAME)
    test_set = read_dataset(TEST_FILE_NAME)

    # preparing input layer
    inputs = Input(shape=(TIME_STEPS, INPUT_DIM,))

    # applying biderectional LSTM
    lstm_out = bi_lstm_network(inputs)

    # applying attention mechanism
    attention_out = attention_network(lstm_out)

    # applying fully connected network to decode output
    outputs = output_decoding_network(attention_out)

    # creating model architecture
    m = Model(inputs = [inputs], outputs = outputs)
    m.compile(
        loss = CATEGORICAL_CROSS_ENTROPY_LOSS, 
        optimizer = RMSPROP_OPTIMIZER, 
        metrics = METRICS
    )

    # training the model
    m.fit(
        x_train, 
        y_train, 
        batch_size = BATCH_SIZE, 
        epochs = EPOCHS, 
        validation_data = test_set)

    # saving the model
    m.save(model_name)
