import numpy as np


a = [[1,2,3,4,5,6,7,8,10],[1,2,3,4,5,6,7,8,10]]
np_a = np.array(a)

print(a)
print(np_a)
import time


start = time.time()
for i in range(100000): # 100000 list는 0.05200052261352539초
                        # 100000 python은   58.49431014060974 초
    np_a = np.append(np_a, [[1,2,3,4,5,6,7,8,10]], axis=0)
    # a.append([1,2,3,4,5,6,7,8,10])



print(time.time() - start)

