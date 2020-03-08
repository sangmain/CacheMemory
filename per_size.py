import pickle

#region LRU import
with open("./Result/LRU/128-2000-0hit.txt", 'rb') as f:
    lru_is_hit1 = pickle.load(f)
with open("./Result/LRU/128hit.txt", 'rb') as f:
    lru_is_hit2 = pickle.load(f)
with open("./Result/LRU/128-4000-0hit.txt", 'rb') as f:
    lru_is_hit3 = pickle.load(f)
with open("./Result/LRU/128-8000-0hit.txt", 'rb') as f:
    lru_is_hit4 = pickle.load(f)
with open("./Result/LRU/128-2000-12000hit.txt", 'rb') as f:
    lru_is_hit5 = pickle.load(f)
with open("./Result/LRU/128-1000-12000hit.txt", 'rb') as f:
    lru_is_hit6 = pickle.load(f)
#endregion

#region RANDOM import
with open("./Result/random/128-2000-0hit.txt", 'rb') as f:
    random_is_hit1 = pickle.load(f)
with open("./Result/random/128hit.txt", 'rb') as f:
    random_is_hit2 = pickle.load(f)
with open("./Result/random/128-4000-0hit.txt", 'rb') as f:
    random_is_hit3 = pickle.load(f)
with open("./Result/random/128-8000-0hit.txt", 'rb') as f:
    random_is_hit4 = pickle.load(f)
with open("./Result/random/128-2000-12000hit.txt", 'rb') as f:
    random_is_hit5 = pickle.load(f)
with open("./Result/random/128-1000-12000hit.txt", 'rb') as f:
    random_is_hit6 = pickle.load(f)
#endregion

#region FIFO import
with open("./Result/fifo/128-2000-0hit.txt", 'rb') as f:
    fifo_is_hit1 = pickle.load(f)
with open("./Result/fifo/128hit.txt", 'rb') as f:
    fifo_is_hit2 = pickle.load(f)
with open("./Result/fifo/128-4000-0hit.txt", 'rb') as f:
    fifo_is_hit3 = pickle.load(f)
with open("./Result/fifo/128-8000-0hit.txt", 'rb') as f:
    fifo_is_hit4 = pickle.load(f)
with open("./Result/fifo/128-2000-12000hit.txt", 'rb') as f:
    fifo_is_hit5 = pickle.load(f)
with open("./Result/fifo/128-1000-12000hit.txt", 'rb') as f:
    fifo_is_hit6 = pickle.load(f)
#endregion

data_range1 = 0
data_range2 = 1000000
length = data_range2 - data_range1

# length = len(lru_is_hit1)

import numpy as np
import matplotlib.pyplot as plt

# #region ISHIT
# lru_slice_hit = [(sum(lru_is_hit1[data_range1:data_range2])/length) * 100, (sum(lru_is_hit2[data_range1:data_range2])/length) * 100,  (sum(lru_is_hit3[data_range1:data_range2])/length) * 100,  (sum(lru_is_hit4[data_range1:data_range2])/length) * 100,  (sum(lru_is_hit5[data_range1:data_range2])/length) * 100, (sum(lru_is_hit6[data_range1:data_range2])/length) * 100]
# fifo_slice_hit = [(sum(fifo_is_hit1[data_range1:data_range2])/length) * 100, (sum(fifo_is_hit2[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit3[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit4[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit5[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit6[data_range1:data_range2])/length) * 100]
# random_slice_hit = [(sum(random_is_hit1[data_range1:data_range2])/length) * 100, (sum(random_is_hit2[data_range1:data_range2])/length) * 100,  (sum(random_is_hit3[data_range1:data_range2])/length) * 100,  (sum(random_is_hit4[data_range1:data_range2])/length) * 100,  (sum(random_is_hit5[data_range1:data_range2])/length) * 100,  (sum(random_is_hit6[data_range1:data_range2])/length) * 100]
# import matplotlib.pyplot as plt

# plt.figure(dpi=600)
# plt.plot(lru_slice_hit, label="LRU")
# plt.plot(fifo_slice_hit, label="FIFO")
# plt.plot(random_slice_hit, label="RANDOM")
# plt.ylabel("Hit rate")
# plt.xlabel("Cache Size")
# # plt.xticks([0, 1, 2, 3, 4], ["64/1000/2000", "64/1000", "64/6000", "64/8000", "64/12000"])
# plt.xticks([0, 1, 2, 3, 4, 5], ["128/2K", "128/2K/4K", "128/4K", "128/8K", "-/2K/4K/12K", "-/1K/2K/12K"])
# plt.legend()
# plt.title("Hit rate by different cache level")
# plt.savefig("L1L2L3L4Hit.tiff")
# plt.show()
#endregion


#region ACCESSTIME
#region LRU import
with open("./Result/LRU/128-2000-0time.txt", 'rb') as f:
    lru_time1 = pickle.load(f)
with open("./Result/LRU/128time.txt", 'rb') as f:
    lru_time2 = pickle.load(f)
with open("./Result/LRU/128-4000-0time.txt", 'rb') as f:
    lru_time3 = pickle.load(f)
with open("./Result/LRU/128-8000-0time.txt", 'rb') as f:
    lru_time4 = pickle.load(f)
with open("./Result/LRU/128-2000-12000time.txt", 'rb') as f:
    lru_time5 = pickle.load(f)
with open("./Result/LRU/128-1000-12000time.txt", 'rb') as f:
    lru_time6 = pickle.load(f)
#endregion

#region RANDOM import
with open("./Result/random/128-2000-0time.txt", 'rb') as f:
    random_time1 = pickle.load(f)
with open("./Result/random/128time.txt", 'rb') as f:
    random_time2 = pickle.load(f)
with open("./Result/random/128-4000-0time.txt", 'rb') as f:
    random_time3 = pickle.load(f)
with open("./Result/random/128-8000-0time.txt", 'rb') as f:
    random_time4 = pickle.load(f)
with open("./Result/random/128-2000-12000time.txt", 'rb') as f:
    random_time5 = pickle.load(f)
with open("./Result/random/128-1000-12000time.txt", 'rb') as f:
    random_time6 = pickle.load(f)
#endregion

#region FIFO import
with open("./Result/fifo/128-2000-0time.txt", 'rb') as f:
    fifo_time1 = pickle.load(f)
with open("./Result/fifo/128time.txt", 'rb') as f:
    fifo_time2 = pickle.load(f)
with open("./Result/fifo/128-4000-0time.txt", 'rb') as f:
    fifo_time3 = pickle.load(f)
with open("./Result/fifo/128-8000-0time.txt", 'rb') as f:
    fifo_time4 = pickle.load(f)
with open("./Result/fifo/128-2000-12000time.txt", 'rb') as f:
    fifo_time5 = pickle.load(f)
with open("./Result/fifo/128-1000-12000time.txt", 'rb') as f:
    fifo_time6 = pickle.load(f)
#endregion
lru_slice_hit = [(sum(lru_time1[data_range1:data_range2])/length) , (sum(lru_time2[data_range1:data_range2])/length) ,  (sum(lru_time3[data_range1:data_range2])/length) ,  (sum(lru_time4[data_range1:data_range2])/length) ,  (sum(lru_time5[data_range1:data_range2])/length) , (sum(lru_time6[data_range1:data_range2])/length)]
fifo_slice_hit = [(sum(fifo_time1[data_range1:data_range2])/length) , (sum(fifo_time2[data_range1:data_range2])/length) ,  (sum(fifo_time3[data_range1:data_range2])/length) ,  (sum(fifo_time4[data_range1:data_range2])/length) ,  (sum(fifo_time5[data_range1:data_range2])/length) ,  (sum(fifo_time6[data_range1:data_range2])/length)]
random_slice_hit = [(sum(random_time1[data_range1:data_range2])/length) , (sum(random_time2[data_range1:data_range2])/length) ,  (sum(random_time3[data_range1:data_range2])/length) ,  (sum(random_time4[data_range1:data_range2])/length) ,  (sum(random_time5[data_range1:data_range2])/length) ,  (sum(random_time6[data_range1:data_range2])/length)]


plt.figure(dpi=600)
plt.plot(lru_slice_hit, label="LRU")
plt.plot(fifo_slice_hit, label="FIFO")
plt.plot(random_slice_hit, label="RANDOM")
plt.ylabel("Access Time")
plt.xlabel("Cache Size")
# plt.xticks([0, 1, 2, 3, 4], ["64/1000/2000", "64/1000", "64/6000", "64/8000", "64/12000"])
plt.xticks([0, 1, 2, 3, 4, 5], ["128/2K", "128/2K/4K", "128/4K", "128/8K", "-/2K/4K/12K", "-/1K/2K/12K"])
plt.legend()
plt.title("Access Time by different cache level")
plt.savefig("L1L2L3L4acess.tiff")
plt.show()
#endregion

