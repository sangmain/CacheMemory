import random
import pickle
import numpy as np

# seed = random.randint(0, 999999)
seed = 732936
random.seed(seed)

data_range = 5000 * 10
loop_size = 50000

data = np.arange(1, data_range+1)


prob = []
num = 0
for i in range(data_range):
    prob.append(num)
    num += 0.1

sum_num = sum(prob)
print(sum_num)
for i in range(data_range):
    prob[i] = prob[i] / sum_num



print(prob[0], prob[-1])
prob.reverse()
print(prob[0], prob[-1])

# data = [random.randint(1, data_range) for _ in range(loop_size)]
data = [np.random.choice(data, p=prob) for _ in range(loop_size)]

print(seed)

# with open('random_data.txt','wb') as f:
#     pickle.dump(data, f)

np.save("./Data/weighted_data2", data)