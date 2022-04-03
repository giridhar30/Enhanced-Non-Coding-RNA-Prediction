from dataset_reader import read_dataset
from model import load_trained_model
from constants import TEST_FILE_NAME

def find_accuracy():
    # loading the testset
    x_test, y_test = read_dataset(TEST_FILE_NAME)

    # loading trained model
    m = load_trained_model()

    y = m.predict(x_test)
    count = 0
    for i in range(len(y)):
        if(y_test[i].argmax() == y[i].argmax()):
            count += 1

    return count * 100 / len(y)
