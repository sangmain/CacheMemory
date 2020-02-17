import cache_random
import cache_fifo
import cache_lru
import c_Status

import pickle
import random
import numpy as np

seeds = []
loop_size = 2

replace_alg = {0: cache_random, 1:cache_fifo, 2:cache_lru}
def process(alg_index, cycle_cnt, is_allcache):
    stat = c_Status.Status()
    hit_rates = []
    is_hit = []
    hit_cnt = 0
    
    for i in range(loop_size):
        cycle_stat = replace_alg[alg_index].cycle(data[i], int(cycle_cnt/2), is_allcache)
        stat.access_time.append(cycle_stat.average_time)
        hit_rates.append(cycle_stat.hit_rate)
        is_hit.append(cycle_stat.is_hit)
        hit_cnt += cycle_stat.hit_cnt
        print("hit cnt:", cycle_stat.hit_cnt)


        print("access_time:", cycle_stat.average_time)
        print("hit_rate:",cycle_stat.hit_rate)

    print("avg hit cnt:", hit_cnt/loop_size)


    print("avg access_time:", sum(stat.access_time) / loop_size)
    print("avg hit_rate:", sum(hit_rates) / loop_size)

    return is_hit


# seeds = [826045, 26790, 861716, 375620, 275456, 428079, 624224, 734024, 921549, 869493]
data = []
data.append(np.load("./Data/prob_data.npy"))
data.append(np.load("./Data/weighted_data.npy"))
# data.append(np.load("./random_data3.npy"))




print("\nRandom ALL CACHE")
is_hit = process(0, 50000, True)
# print("\nRandom L1 ONLY")
# process(0, 100000, False)

with open('random_is_hit.txt','wb') as f:
    pickle.dump(is_hit, f)


print("\nFIFO ALL CACHE")
is_hit = process(1, 50000, True)
# print("\nFIFO L1 ONLY")
# process(1, 10000, False)

with open('fifo_is_hit.txt','wb') as f:
    pickle.dump(is_hit, f)

print("\nLRU ALL CACHE")
is_hit = process(2, 50000, True)
# print("\nLRU L1 ONLY")
# process(2, 10000, False)

with open('lru_is_hit.txt','wb') as f:
    pickle.dump(is_hit, f)



