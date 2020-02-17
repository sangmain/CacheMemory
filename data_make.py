import random
import pickle
import numpy as np

seed = random.randint(0, 999999)
random.seed(seed)

data_range = 5000 * 10
loop_size = 50000

data = np.arange(1, data_range+1)
probab = []
num = 0.0
for i in range(data_range):
    probab = num
    num += 0.0002
for i in range(9):
    probab[i] = 0.

# data = [random.randint(1, data_range) for _ in range(loop_size)]
data = [np.random.choice(data, p=probab) for _ in range(loop_size)]

print(seed)

# with open('random_data.txt','wb') as f:
#     pickle.dump(data, f)

np.save("./weighted_data", data)