from keras.layers import Permute, Dense, Multiply, Flatten

from constants import TIME_STEPS, SOFTMAX_ACTIVATION, RANDOM_NORMAL_INITIALIZER, ZEROS_INITIALIZER

def attention_network(inputs):
    a = Permute((2, 1))(inputs)
    a = Dense(
        TIME_STEPS, 
        activation = SOFTMAX_ACTIVATION, 
        kernel_initializer = RANDOM_NORMAL_INITIALIZER, 
        bias_initializer = ZEROS_INITIALIZER
    )(a)
    a_probs = Permute((2, 1), name = 'attention_vec')(a)

    output_attention_mul = Multiply()([inputs, a_probs])
    output_attention_mul = Flatten()(output_attention_mul)
    
    return output_attention_mul