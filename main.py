import cache_random
import cache_fifo
import c_Status

import pickle
import random

seeds = []
loop_size = 10

cycle_dict = {0:1000, 1:3000, 2:5000, 3:8000, 4:10000}

replace_alg = {0: cache_random, 1:cache_fifo}
def process(alg_index, cycle_cnt, is_allcache):
    stat = c_Status.Status()
    hit_rates = []
    is_hit = []
    hit_cnt = 0
    
    for i in range(loop_size):
        cycle_stat = replace_alg[alg_index].cycle(cycle_cnt, seeds[i], is_allcache)
        stat.access_time.append(cycle_stat.average_time)
        hit_rates.append(cycle_stat.hit_rate)
        is_hit.append(cycle_stat.is_hit)
        hit_cnt += cycle_stat.hit_cnt

    print("hit cnt:", hit_cnt/loop_size)


    print("access_time:", sum(stat.access_time) / loop_size)
    print("hit_rate:", sum(hit_rates) / loop_size)

    return 

for i in range(loop_size):
    seeds.append(random.randint(1, 1000000))

print(seeds)

for i in range(5):
    print(cycle_dict[i])    
    print("\nRandom ALL CACHE")
    process(0, cycle_dict[i], True)
    print("\nRandom L1 ONLY")
    process(0, cycle_dict[i], False)

    print("\nFIFO ALL CACHE")
    process(1, cycle_dict[i], True)
    print("\nFIFO L1 ONLY")
    process(1,cycle_dict[i], False)

    print("\n")


# # with open('fifo_is_hit.txt','wb') as f:
# #     pickle.dump(is_hit, f)
