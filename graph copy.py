import matplotlib.pyplot as plt
import numpy as np

def hit_rate_bar(random, fifo, lru):
    plt.title("Replacement Algorithm Hit rate comparison")
    uni = np.arange(4)
    plt.bar(uni, random, color='green', width=0.1, label="Random")
    plt.bar(uni + 0.1, fifo, color='orange', width=0.1, label="FIFO")
    plt.bar(uni + 0.2, lru, width=0.1, label="LRU", align="center")

    plt.xlabel("Cache Size")
    plt.ylabel("Hit Rate")
    plt.xticks([0.1, 1.1, 2.1, 3.1], ["5, 20, 50", "10, 40, 100", "5", "10"])
    plt.legend()
    plt.savefig("Hitrate_comp.png")
    plt.show()



def access_time_bar(random, fifo, lru):
    plt.title("Replacement Algorithm Hit rate comparison")
    uni = np.arange(4)
    plt.bar(uni, random, color='green', width=0.1, label="Random")
    plt.bar(uni + 0.1, fifo, color='orange', width=0.1, label="FIFO")
    plt.bar(uni + 0.2, lru, width=0.1, label="LRU", align="center")

    plt.xlabel("Cache Size")
    plt.ylabel("Access Time(secs)")
    plt.xticks([0.1, 1.1, 2.1, 3.1], ["5, 20, 50", "10, 40, 100", "5", "10"])
    plt.legend()
    plt.savefig("AcessTime_comp.png")
    plt.show()



# random = [0.010955, 0.022910000000000003, 0.0008950000000000002, 0.00199]
# fifo = [0.009945, 0.020065, 0.0010149999999999998, 0.002025 ]
# lru = [0.00996, 0.020020000000000003, 0.0010149999999999998, 0.00202]
# hit_rate_bar(random, fifo, lru)

# random = [3.9934765000014956, 3.969163500001477, 3.80279499999992, 3.8024649999999185]
# fifo = [3.9920525000014946, 3.980911500001482, 3.801669999999917, 3.8006599999999153]
# lru = [3.991977500001495, 3.9814390000014823, 3.801429999999916, 3.8004249999999153]
# access_time_bar(random, fifo, lru)


import pickle
from scipy.interpolate import make_interp_spline, BSpline


with open('random_is_hit.txt', 'rb') as f:
    random_is_hit = pickle.load(f)

with open('fifo_is_hit.txt', 'rb') as f:
    fifo_is_hit = pickle.load(f)

with open('lru_is_hit.txt', 'rb') as f:
    lru_is_hit = pickle.load(f)

def plt_hitcnt(a, b, c):


    plt.title("Random replacement Hit count")
    plt.plot(a, color="green", label="Random")
    plt.plot(c, label="LRU")

    plt.plot(b, color="orange", label="FIFO")
    plt.xlabel("Cycle Count")
    plt.ylabel("Hit Count")
    plt.legend()
    plt.savefig("Hitcnt_comp.png")
    plt.show()

def preprocess(is_hit):
    is_hit = np.array(is_hit)
    arr = []

    for i in range(is_hit.shape[1]):
        add_sum = 0
        for j in range(is_hit.shape[0]):
            add_sum += is_hit[j][i]
        arr.append(add_sum)

    # print(arr)

    hit_cnt = 0
    hit_cnt_arr = []
    for i in range(0, len(arr)):
        hit_cnt += arr[i]
        hit_cnt_arr.append(hit_cnt)

    return hit_cnt_arr

a = preprocess(random_is_hit)
print(a)
b = preprocess(fifo_is_hit)
c = preprocess(lru_is_hit)
plt_hitcnt(a[:300], b[:300], c[:300])
