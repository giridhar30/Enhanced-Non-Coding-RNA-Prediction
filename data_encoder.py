import numpy as np
from constants import CODE_MAP

# encoding the given sequence
def encode_base(line):
    encoded_list = []

    for i in range(500):
        if(i < len(line)-1):
            encoded_list.append(CODE_MAP.get(line[i].upper(), CODE_MAP['N']))
        else:
            encoded_list.append(CODE_MAP['N'])

    return np.array(encoded_list)