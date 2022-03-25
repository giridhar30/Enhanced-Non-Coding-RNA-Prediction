import numpy as np
from constants import code_map

# encoding the given sequence
def encode_base(line):
    encoded_list = []

    for i in range(500):
        if(i < len(line)-1):
            encoded_list.append(code_map.get(line[i].upper(), code_map['N']))
        else:
            encoded_list.append(code_map['N'])

    return np.array(encoded_list)