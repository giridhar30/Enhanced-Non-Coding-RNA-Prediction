import numpy as np

from model import load_trained_model
from data_encoder import encode_base
from constants import FAMILY_MAP

def predict_family(x):
    # loading trained model
    m = load_trained_model()

    y = m.predict(np.expand_dims(encode_base(x), axis=0))
    result = y[0].argmax()

    family = list(FAMILY_MAP.keys())[result]
    return family

