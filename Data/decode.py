import pickle

def process(strnum):
    # with open("./Result1/LRU/"+strnum+ "hit.txt", 'rb') as f:
    #     lru_is_hit = pickle.load(f)
    with open("./Result1/FIFO/"+strnum+ "hit.txt", 'rb') as f:
        fifo_is_hit = pickle.load(f)
    with open("./Result1/RANDOM/"+strnum+ "hit.txt", 'rb') as f:
        random_is_hit = pickle.load(f)

    # with open("./Result1/LRU/"+strnum+ "time.txt", 'rb') as f:
    #     lru_access_time = pickle.load(f)
    with open("./Result1/FIFO/"+strnum+ "time.txt", 'rb') as f:
        fifo_access_time = pickle.load(f)
    with open("./Result1/RANDOM/"+strnum+ "time.txt", 'rb') as f:
        random_access_time = pickle.load(f)

    data_range1 = 0
    data_range2 = 1000000
    length = data_range2 - data_range1


    # print("L1:", strnum)
    # print("LRU")
    print("Hit rate:",(sum(random_is_hit[data_range1:data_range2])/length) * 100)
    print("Access time:", sum(random_access_time[data_range1:data_range2])/length)
    # print()
    # print("Hit rate:",(sum(lru_is_hit[data_range1:data_range2])/length) * 100)
    # print("Access time:", sum(lru_access_time[data_range1:data_range2])/length)
    # print()
    # print("FIFO")
    print("Hit rate:",(sum(fifo_is_hit[data_range1:data_range2])/length) * 100)
    print("Access time:", sum(fifo_access_time[data_range1:data_range2])/length)
    # print()
    # print("RANDOM")
    print()

    return None, None, None
    # return (sum(lru_is_hit[data_range1:data_range2])/length) * 100, (sum(fifo_is_hit[data_range1:data_range2])/length) * 100, (sum(random_is_hit[data_range1:data_range2])/length) * 100
import numpy as np
import matplotlib.pyplot as plt
# a1, b1, c1 = process("16")
# a2, b2, c2 = process("32")
# a3, b3, c3 = process("64")
# a4, b4, c4 = process("128")
# a5, b5, c5 = process("256")

a1, b1, c1 = process("128-2000")
a2, b2, c2 = process("128-4000")
# a3, b3, c3 = process("128-4000")
# a4, b4, c4 = process("128")
# a5, b5, c5 = process("128-1000")

# a = [a1, a2, a3, a4, a5]
# b = [b1, b2, b3, b4, b5]
# c = [c1, c2, c3, c4, c5]

# uni = np.arange(5)
# plt.bar(uni, a, color='green', width=0.1, label="LRU")
# plt.bar(uni + 0.1, b, color='orange', width=0.1, label="FIFO")
# plt.bar(uni + 0.2, c, width=0.1, color='blue', label="RANDOM", align="center")

# plt.xlabel("Cache Size")
# plt.ylabel("Hit Rate")
# # plt.xticks([0.1, 1.1], ["50, 200, 500", "Not tested yet"])

# plt.legend()
# # plt.savefig("Hitrate_comp.png")
# plt.show()