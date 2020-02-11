import matplotlib.pyplot as plt
import pickle
import pandas as pd
import numpy as np

seeds = [826045, 26790, 861716, 375620, 275456, 428079, 624224, 734024, 921549, 869493]
disk_size = 5000
for seed in seeds:
    with open('./Data/data'+ str(seed) + '.txt', 'rb') as f:
        data = pickle.load(f)

    def count_elements(data):
        hist = [0] * disk_size
            
        for i in data:
            hist[i-1] += 1

        return hist


    hist = count_elements(data)
    print(hist)

    value_counts = pd.DataFrame({"Data":np.arange(1, disk_size+1), "Count": hist})
    plt.bar(value_counts['Data'], value_counts['Count'])
    plt.savefig(str(seed) + ".png")
    plt.show()
