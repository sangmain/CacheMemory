import numpy as np

prob = []
num = 0
for i in range(50000):
    prob.append(num)
    num += 0.1

sum_num = sum(prob)
for i in range(50000):
    prob[i] = prob[i] / sum_num

print(prob)

data = np.arange(1, 50001)
data = [np.random.choice(data, p=prob) for _ in range(50000)]

np.save("./weighted_data", data)

