import numpy as np

data = np.load("./Data/random_data.npy")

f = open("random_data.txt", 'w')
for i in range(len(data)):
    line = data[i]
    f.write(str(line)+"\n")
f.close()