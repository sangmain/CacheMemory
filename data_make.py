import random
import pickle
import numpy as np

seed = random.randint(0, 999999)
random.seed(seed)

data_range = 5000 * 100
data = [random.randint(1, data_range) for _ in range(data_range)]

print(seed)

# with open('random_data.txt','wb') as f:
#     pickle.dump(data, f)

np.save("./random_data3", data)