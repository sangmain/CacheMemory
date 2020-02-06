import numpy as np


a = [1,2,3,4,5,6,7,8,10]
np_a = np.array(a)

import time


start = time.time()
for i in range(100000): # 100000 list는 0.00999초
                        # 100000 python은 1.487초
    np_a = np_a + 100
    # a = [x + 100 for x in a]

print(time.time() - start)

print(a)
print(np_a)
