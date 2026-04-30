import os

import pandas as pd


def readfiles():
    rel_data_path = '../../data'
    return [pd.read_csv(os.path.join(rel_data_path, filename), sep=',') for filename in
            os.listdir(rel_data_path)]  # f(x) = i*x E (S) , where filename = x, S =


csvlist = readfiles()
print()
# if __name__ == '__main__':
#    x = readfiles()
#    print(x)

