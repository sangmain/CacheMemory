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
with open("./Result/LRU/128-1000-12000hit.txt", 'rb') as f:
    lru_is_hit6 = pickle.load(f)
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
with open("./Result/random/128-1000-12000hit.txt", 'rb') as f:
    random_is_hit6 = pickle.load(f)
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
with open("./Result/fifo/128-1000-12000hit.txt", 'rb') as f:
    fifo_is_hit6 = pickle.load(f)
#endregion

with open("./Result/LRU/128hit.txt", 'rb') as f:
    lru_is_hit1 = pickle.load(f)
with open("./Result/LRU/128-4000-0hit.txt", 'rb') as f:
    lru_is_hit2 = pickle.load(f)
with open("./Result/LRU/128-4000hit.txt", 'rb') as f:
    lru_is_hit3 = pickle.load(f)
with open("./Result/LRU/128-8000-0hit.txt", 'rb') as f:
    lru_is_hit4 = pickle.load(f)
with open("./Result/LRU/128-2000-12000hit.txt", 'rb') as f:
    lru_is_hit5 = pickle.load(f)
with open("./Result/LRU/128-1000-12000hit.txt", 'rb') as f:
    lru_is_hit6 = pickle.load(f)
#endregion

#region RANDOM import
with open("./Result/random/128hit.txt", 'rb') as f:
    random_is_hit1 = pickle.load(f)
with open("./Result/random/128-4000-0hit.txt", 'rb') as f:
    random_is_hit2 = pickle.load(f)
with open("./Result/random/128-4000hit.txt", 'rb') as f:
    random_is_hit3 = pickle.load(f)
with open("./Result/random/128-8000-0hit.txt", 'rb') as f:
    random_is_hit4 = pickle.load(f)
with open("./Result/random/128-2000-12000hit.txt", 'rb') as f:
    random_is_hit5 = pickle.load(f)
with open("./Result/random/128-1000-12000hit.txt", 'rb') as f:
    random_is_hit6 = pickle.load(f)
#endregion

#region FIFO import
with open("./Result/fifo/128hit.txt", 'rb') as f:
    fifo_is_hit1 = pickle.load(f)
with open("./Result/fifo/128-4000-0hit.txt", 'rb') as f:
    fifo_is_hit2 = pickle.load(f)
with open("./Result/fifo/128-4000hit.txt", 'rb') as f:
    fifo_is_hit3 = pickle.load(f)
with open("./Result/fifo/128-8000-0hit.txt", 'rb') as f:
    fifo_is_hit4 = pickle.load(f)
with open("./Result/fifo/128-2000-12000hit.txt", 'rb') as f:
    fifo_is_hit5 = pickle.load(f)
with open("./Result/fifo/128-1000-12000hit.txt", 'rb') as f:
    fifo_is_hit6 = pickle.load(f)

data_range1 = 0
data_range2 = 1000000
length = data_range2 - data_range1

# length = len(lru_is_hit1)

import numpy as np
import matplotlib.pyplot as plt

#region ISHIT
lru_slice_hit = [(sum(lru_is_hit1[data_range1:data_range2])/length) * 100, (sum(lru_is_hit2[data_range1:data_range2])/length) * 100,  (sum(lru_is_hit3[data_range1:data_range2])/length) * 100,  (sum(lru_is_hit4[data_range1:data_range2])/length) * 100,  (sum(lru_is_hit5[data_range1:data_range2])/length) * 100, (sum(lru_is_hit6[data_range1:data_range2])/length) * 100]
fifo_slice_hit = [(sum(fifo_is_hit1[data_range1:data_range2])/length) * 100, (sum(fifo_is_hit2[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit3[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit4[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit5[data_range1:data_range2])/length) * 100,  (sum(fifo_is_hit6[data_range1:data_range2])/length) * 100]
random_slice_hit = [(sum(random_is_hit1[data_range1:data_range2])/length) * 100, (sum(random_is_hit2[data_range1:data_range2])/length) * 100,  (sum(random_is_hit3[data_range1:data_range2])/length) * 100,  (sum(random_is_hit4[data_range1:data_range2])/length) * 100,  (sum(random_is_hit5[data_range1:data_range2])/length) * 100,  (sum(random_is_hit6[data_range1:data_range2])/length) * 100]
import matplotlib.pyplot as plt

uni = np.arange(6)
print(uni)
plt.figure(dpi=600)
# plt.bar(uni, lru_slice_hit,  width=0.3, label="LRU")
# plt.bar(uni + 0.2, fifo_slice_hit,  width=0.3, label="FIFO")
# plt.bar(uni + 0.4, random_slice_hit,  width=0.3, label="RANDOM")

plt.plot(lru_slice_hit, label="LRU")
plt.plot(fifo_slice_hit, label="FIFO")
plt.plot(random_slice_hit, label="RANDOM")

plt.ylabel("Hit Rate")
plt.xlabel("Cache level")
# plt.xticks([0, 1, 2, 3, 4], ["64/1000/2000", "64/1000", "64/6000", "64/8000", "64/12000"])
plt.xticks(uni, ["128/2K/4K", "128/4K", "128/4K/8K", "128/8K", "-/2K/4K/12K", "-/1K/2K/12K"])
# plt.xticks(uni, ["16/250/500", "32/500/1K", "64/1K/2K", "128/2K/4K", "256/4K/8K"])
plt.legend()
plt.title("Access Time by different cache level")
plt.savefig("L1L2L3L4Hit.tiff")
plt.show()
#endregion


# #region ACCESSTIME
# #region LRU import
# with open("./Result/LRU/128time.txt", 'rb') as f:
#     lru_is_time1 = pickle.load(f)
# with open("./Result/LRU/128-4000-0time.txt", 'rb') as f:
#     lru_is_time2 = pickle.load(f)
# with open("./Result/LRU/128-4000time.txt", 'rb') as f:
#     lru_is_time3 = pickle.load(f)
# with open("./Result/LRU/128-8000-0time.txt", 'rb') as f:
#     lru_is_time4 = pickle.load(f)
# with open("./Result/LRU/128-2000-12000time.txt", 'rb') as f:
#     lru_is_time5 = pickle.load(f)
# with open("./Result/LRU/128-1000-12000time.txt", 'rb') as f:
#     lru_is_time6 = pickle.load(f)
# #endregion

# #region RANDOM import
# with open("./Result/random/128time.txt", 'rb') as f:
#     random_is_time1 = pickle.load(f)
# with open("./Result/random/128-4000-0time.txt", 'rb') as f:
#     random_is_time2 = pickle.load(f)
# with open("./Result/random/128-4000time.txt", 'rb') as f:
#     random_is_time3 = pickle.load(f)
# with open("./Result/random/128-8000-0time.txt", 'rb') as f:
#     random_is_time4 = pickle.load(f)
# with open("./Result/random/128-2000-12000time.txt", 'rb') as f:
#     random_is_time5 = pickle.load(f)
# with open("./Result/random/128-1000-12000time.txt", 'rb') as f:
#     random_is_time6 = pickle.load(f)
# #endregion

# #region FIFO import
# with open("./Result/fifo/128time.txt", 'rb') as f:
#     fifo_is_time1 = pickle.load(f)
# with open("./Result/fifo/128-4000-0time.txt", 'rb') as f:
#     fifo_is_time2 = pickle.load(f)
# with open("./Result/fifo/128-4000time.txt", 'rb') as f:
#     fifo_is_time3 = pickle.load(f)
# with open("./Result/fifo/128-8000time.txt", 'rb') as f:
#     fifo_is_time4 = pickle.load(f)
# with open("./Result/fifo/128-2000-12000time.txt", 'rb') as f:
#     fifo_is_time5 = pickle.load(f)
# with open("./Result/fifo/128-1000-12000time.txt", 'rb') as f:
#     fifo_is_time6 = pickle.load(f)
# #endregion


# lru_slice_hit = [(sum(lru_is_time1[data_range1:data_range2])/length) , (sum(lru_is_time2[data_range1:data_range2])/length) ,  (sum(lru_is_time3[data_range1:data_range2])/length) ,  (sum(lru_is_time4[data_range1:data_range2])/length) ,  (sum(lru_is_time5[data_range1:data_range2])/length), (sum(lru_is_time6[data_range1:data_range2])/length)]
# fifo_slice_hit = [(sum(fifo_is_time1[data_range1:data_range2])/length) , (sum(fifo_is_time2[data_range1:data_range2])/length) ,  (sum(fifo_is_time3[data_range1:data_range2])/length) ,  (sum(fifo_is_time4[data_range1:data_range2])/length) ,  (sum(fifo_is_time5[data_range1:data_range2])/length),  (sum(fifo_is_time6[data_range1:data_range2])/length)]
# random_slice_hit = [(sum(random_is_time1[data_range1:data_range2])/length) , (sum(random_is_time2[data_range1:data_range2])/length) ,  (sum(random_is_time3[data_range1:data_range2])/length) ,  (sum(random_is_time4[data_range1:data_range2])/length) ,  (sum(random_is_time5[data_range1:data_range2])/length),  (sum(random_is_time6[data_range1:data_range2])/length)]

# # uni = np.arange(6)
# plt.figure(dpi=600)
# plt.bar(uni, lru_slice_hit,  width=0.3, label="LRU")
# plt.bar(uni + 0.2,fifo_slice_hit,  width=0.3, label="FIFO")
# plt.bar(uni + 0.4, random_slice_hit,  width=0.3, label="RANDOM")
# plt.ylabel("Access Time")
# plt.xlabel("Cache level")
# uni = uni + 0.2
# plt.xticks(uni, ["128/2K/4K", "128/4K", "128/4K/8K", "128/8K", "-/2K/4K/12K", "-/1K/2K/12K"])
# # plt.xticks(uni, ["64/1000/2000", "64/1000", "64/6000", "64/8000", "64/12000"])

# # plt.xticks(uni, ["16/250/500", "32/500/1K", "64/1K/2K", "128/2K/4K", "256/4K/8K"])
# plt.legend()
# plt.title("Access Time by different cache level")
# plt.savefig("L1L2L3L4acessBar.tiff")
# plt.show()
# #endregion

