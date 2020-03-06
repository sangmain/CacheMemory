import pickle

#region LRU import
with open("./Result/LRU/16hit.txt", 'rb') as f:
    lru_is_hit1 = pickle.load(f)
with open("./Result/LRU/32hit.txt", 'rb') as f:
    lru_is_hit2 = pickle.load(f)
with open("./Result/LRU/64hit.txt", 'rb') as f:
    lru_is_hit3 = pickle.load(f)
with open("./Result/LRU/128hit.txt", 'rb') as f:
    lru_is_hit4 = pickle.load(f)
with open("./Result/LRU/256hit.txt", 'rb') as f:
    lru_is_hit5 = pickle.load(f)
#endregion

#region RANDOM import
with open("./Result/random/16hit.txt", 'rb') as f:
    random_is_hit1 = pickle.load(f)
with open("./Result/random/32hit.txt", 'rb') as f:
    random_is_hit2 = pickle.load(f)
with open("./Result/random/64hit.txt", 'rb') as f:
    random_is_hit3 = pickle.load(f)
with open("./Result/random/128hit.txt", 'rb') as f:
    random_is_hit4 = pickle.load(f)
with open("./Result/random/256hit.txt", 'rb') as f:
    random_is_hit5 = pickle.load(f)
#endregion

#region FIFO import
with open("./Result/fifo/16hit.txt", 'rb') as f:
    fifo_is_hit1 = pickle.load(f)
with open("./Result/fifo/32hit.txt", 'rb') as f:
    fifo_is_hit2 = pickle.load(f)
with open("./Result/fifo/64hit.txt", 'rb') as f:
    fifo_is_hit3 = pickle.load(f)
with open("./Result/fifo/128hit.txt", 'rb') as f:
    fifo_is_hit4 = pickle.load(f)
with open("./Result/fifo/256hit.txt", 'rb') as f:
    fifo_is_hit5 = pickle.load(f)
#endregion

data_range1 = 0
data_range2 = 1000000
length = data_range2 - data_range1

# length = len(lru_is_hit1)

import numpy as np
import matplotlib.pyplot as plt

#region ISHIT
lru_slice_hit = [(sum(lru_is_hit1[data_range1:data_range2])/length) * 100, (sum(lru_is_hit2[data_range1:data_range2])/length) * 100,  (sum(lru_is_hit3[data_range1:data_range2])/length) * 100,  (sum(lru_is_hit4[data_range1:data_range2])/length) * 100,  (sum(lru_is_hit5[data_range1:data_range2])/length) * 100]
fifo_slice_hit = [(sum(fifo_is_hit1[data_range1:data_range2])/length) * 100, (sum(fifo_is_hit2[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit3[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit4[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit5[data_range1:data_range2])/length) * 100]
random_slice_hit = [(sum(random_is_hit1[data_range1:data_range2])/length) * 100, (sum(random_is_hit2[data_range1:data_range2])/length) * 100,  (sum(random_is_hit3[data_range1:data_range2])/length) * 100,  (sum(random_is_hit4[data_range1:data_range2])/length) * 100,  (sum(random_is_hit5[data_range1:data_range2])/length) * 100]
import matplotlib.pyplot as plt

plt.plot(lru_slice_hit, label="LRU")
plt.plot(fifo_slice_hit, label="FIFO")
plt.plot(random_slice_hit, label="RANDOM")
plt.ylabel("Hit Rate")
plt.xlabel("Cache Size")
plt.xticks([0, 1, 2, 3, 4], ["16/250/500", "32/500/1000", "64/1000/2000", "128/2000/4000", "256/4000/8000"])
plt.legend()
plt.title("Hit rate by cache size")
plt.savefig("hitrate_all.tiff")
plt.show()
#endregion

# #region ACCESSTIME
# access_time = lru_access_time
# slice_time = [sum(access_time[0:200])/200, sum(access_time[200: 400])/200, sum(access_time[400: 600])/200 , sum(access_time[600: 800])/200 , sum(access_time[800: 1000])/200 ]
# lru_time = slice_time

# access_time = fifo_access_time
# slice_time = [sum(access_time[0:200])/200, sum(access_time[200: 400])/200, sum(access_time[400: 600])/200 , sum(access_time[600: 800])/200 , sum(access_time[800: 1000])/200 ]
# fifo_time = slice_time


# access_time = random_access_time
# slice_time = [sum(access_time[0:200])/200, sum(access_time[200: 400])/200, sum(access_time[400: 600])/200 , sum(access_time[600: 800])/200 , sum(access_time[800: 1000])/200 ]
# random_time = slice_time


# plt.plot(lru_time, label="LRU")
# plt.plot(fifo_time, label="FIFO")
# plt.plot(random_time, label="RANDOM")
# plt.ylabel("Access Time")
# plt.xlabel("Instructions")
# plt.xticks([0, 1, 2, 3, 4], ["200000", "400000", "600000", "800000", "1000000"])
# plt.legend()
# plt.show()
# #endregion

