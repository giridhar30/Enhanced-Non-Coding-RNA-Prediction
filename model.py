from keras.models import load_model

from constants import MODEL_NAME

def load_trained_model():
    model = load_model(MODEL_NAME)
    return model