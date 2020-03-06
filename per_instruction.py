import pickle

with open("./Result/LRU/16hit.txt", 'rb') as f:
    lru_is_hit = pickle.load(f)
with open("./Result/FIFO/16hit.txt", 'rb') as f:
    fifo_is_hit = pickle.load(f)
with open("./Result/RANDOM/16hit.txt", 'rb') as f:
    random_is_hit = pickle.load(f)



import numpy as np
import matplotlib.pyplot as plt

#region ISHIT
slice_size = 200000
total = 1000000
def process(is_hit, slice_size, total):
    slice_hit = []; slice_miss = []
    for i in range(int(total/slice_size)):
        slice_hit.append(sum(is_hit[slice_size * i: slice_size * (i+1)]))
        slice_miss.append(slice_size - slice_hit[-1])
    return slice_miss

lru_miss = process(lru_is_hit, slice_size, total)
random_miss = process(random_is_hit, slice_size, total)
fifo_miss = process(fifo_is_hit, slice_size, total)

index = np.arange(int(total/slice_size))
value = [str((slice_size*(x+1))) for x in index]
# value = [str((slice_size*(x+1))) for x in index]
import matplotlib.pyplot as plt
# plt.figure(dpi=600)
plt.plot(lru_miss, label="LRU")
plt.plot(fifo_miss, label="FIFO")
plt.plot(random_miss, label="RANDOM")
plt.ylabel("Miss Count")
plt.xlabel("Instructions")
plt.xticks(index, ["200k","400k","600k","800k","1M"])
# plt.xticks(index, ["100k", "200k", "300k", "400k", "500k", "600k", "700k", "800k", "900k", "1M"])
plt.legend()
plt.title("Cache Size of 16")
plt.savefig("perI_16.tiff")
plt.show()
#endregion

#region ACCESSTIME
# with open("./Result/LRU/256time.txt", 'rb') as f:
#     lru_access_time = pickle.load(f)
# with open("./Result/FIFO/256time.txt", 'rb') as f:
#     fifo_access_time = pickle.load(f)
# with open("./Result/RANDOM/256time.txt", 'rb') as f:
#     random_access_time = pickle.load(f)
# access_time = lru_access_time
# slice_time = [sum(access_time[0: calc])/calc, sum(access_time[calc: calc*2])/calc, sum(access_time[calc*2: calc*3])/calc , sum(access_time[calc*3: calc*4])/calc , sum(access_time[calc*4: calc*5])/calc ]
# lru_time = slice_time

# # access_time = fifo_access_time
# # slice_time = [sum(access_time[0:200])/200, sum(access_time[200: 400])/200, sum(access_time[400: 600])/200 , sum(access_time[600: 800])/200 , sum(access_time[800: 1000])/200 ]
# # fifo_time = slice_time


# access_time = random_access_time
# slice_time = [sum(access_time[0: calc])/calc, sum(access_time[calc: calc*2])/calc, sum(access_time[calc*2: calc*3])/calc , sum(access_time[calc*3: calc*4])/calc , sum(access_time[calc*4: calc*5])/calc ]
# random_time = slice_time


# plt.plot(lru_time, label="LRU")
# # plt.plot(fifo_time, label="FIFO")
# plt.plot(random_time, label="RANDOM")
# plt.ylabel("Access Time")
# plt.xlabel("Instructions")
# plt.xticks([0, 1, 2, 3, 4], ["200000", "400000", "600000", "800000", "1000000"])
# plt.legend()
# plt.show()
#endregion

