import matplotlib.pyplot as plt
import pickle
import pandas as pd
import numpy as np

seeds = [1]
loop_size = 50000
for seed in seeds:
    # with open('./Data/random_data'+ str(seed) + '.txt', 'rb') as f:
    #     data = pickle.load(f)
    # data = np.load('./Data/weighted_data2.npy')
    data = np.load('./Data/realweighted_data.npy')
    # data = np.load('./Data/weighted_data1.npy')
    print(data.tolist())
    # for i in range(loop_size):
    #     print(data[i])


    print(len(data))

    def count_elements(data):
        hist = [0] * loop_size
            
        for i in data:
            hist[i-1] += 1

        return hist


    hist = count_elements(data)
    print(hist)

    value_counts = pd.DataFrame({"Data":np.arange(1, loop_size+1), "Count": hist})
    # value_counts = value_counts[:10000]
    plt.bar(value_counts['Data'], value_counts['Count'])
    plt.savefig('./Data/realweighted_data' + ".png")
    plt.show()
