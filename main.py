import cache_random
import cache_fifo
import c_Status

import pickle

stat = c_Status.Status(False)

sum_time = 0.0
hit_rates = []
loop_size = 20
is_hit = []
# print("Random")
print("FIFO")
for i in range(loop_size):
    # cycle_stat = cache_random.cycle(10000, True)
    cycle_stat = cache_fifo.cycle(10000, True)
    
    stat.access_time.append(cycle_stat.average_time)
    hit_rates.append(cycle_stat.hit_rate)
    is_hit.append(cycle_stat.is_hit)

print("access_time:", sum(stat.access_time) / loop_size)
print("hit_rate:", sum(hit_rates) / loop_size)

# with open('fifo_is_hit.txt','wb') as f:
#     pickle.dump(is_hit, f)
