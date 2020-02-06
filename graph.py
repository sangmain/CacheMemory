import matplotlib.pyplot as plt
import numpy as np


def plot1(array1, array2):
    plt.title("Random Replacement Access Time Comparison")
    uni = np.array(["1000", "3000", "5000", "8000", "10000"])
    plt.plot(uni, array1, label="L1")
    plt.plot(uni, array2, label="L1 L2 L3")

    plt.xlabel("Cycle Count")
    plt.ylabel("Time in Seconds")
    # plt.ylabel("Hit Rate")
    plt.legend()
    plt.savefig("Random_Time.png")
    plt.show()

def plot2(array1, array2):
    plt.title("FIFO Replacement Hit Rate Comparison")
    # uni = np.array([1000, 3000, 5000, 8000, 10000])
    uni = np.arange(5)
    plt.bar(uni+0.0, array1, color='green', width=0.3, label="L1")
    plt.bar(uni+0.3, array2, color='orange', width=0.3, label="L1 L2 L3")

    plt.xlabel("Cycle Count")
    # plt.ylabel("Time in Seconds")
    plt.ylabel("Hit Rate")
    plt.xticks([0, 1, 2, 3, 4], ["1000", "3000", "5000", "8000", "10000"])
    plt.legend()
    plt.savefig("FIFO_Hit.png")
    plt.show()



###### DATA 10000
### Random
array1 = [4.171900000000113, 4.158633333332887, 4.155050000000209, 4.1515500000012215, 4.15161500000156] 
array2 = [4.163900000000115,4.150716666666221, 4.146890000000205,4.145731250001219, 4.145585000001558]

### FIFO
array1 = [4.168650000000113, 4.156249999999553, 4.15309000000021, 4.150843750001223, 4.15081500000156] 
array2 = []

# Random
## Hit Rate
# plot1(array1, array2)
# plot2(array1, array2)

import pickle
from scipy.interpolate import make_interp_spline, BSpline


with open('random_is_hit.txt', 'rb') as f:
    is_hit = pickle.load(f)


def plt_accesstime(status_list, loop_size):

    
    # for i in range(len(time_list)): #### 평균을 계산하기 위한 계산
    #     time_sum += time_dict[time_list[i]]

    # average_time = time_sum / (loop_size * 2)
    plt.title("Access Time during " + str(loop_size*2) +" requests")
    plt.plot(time_list, label= "Access Time")
    # plt.plot(average_time, label="Average Time")
    plt.xlabel("Cycle Count")
    plt.ylabel("Time in Seconds")
    plt.yticks([6, 5, 4, 3, 2], ["DISK 4.3", "RAM 1.3", "L3 0.3", "L2 0.2", "L1 0.1"])
    plt.legend()
    plt.show()

def plt_hitcnt(is_hit, loop_size):

    x = np.linspace(0, (loop_size*2), 5)
    a = np.arange(0,(loop_size*2))

    spl = make_interp_spline(a, is_hit, k=3)  # type: BSpline
    power_smooth = spl(x)
    plt.title("Random replacement Hit count")
    plt.plot(is_hit, label="Hit count")
    plt.plot(x, power_smooth, label="Hit count Trend")
    plt.xlabel("Cycle Count")
    plt.ylabel("Hit Count")
    plt.legend()
    plt.savefig("Random0_Hitcnt.png")
    plt.show()

is_hit = np.array(is_hit)
arr = []

for i in range(is_hit.shape[1]):
    add_sum = 0
    for j in range(is_hit.shape[0]):
        add_sum += is_hit[j][i]
    arr.append(add_sum)

print(arr)

hit_cnt = 0
hit_cnt_arr = []
for i in range(0, len(arr)):
            JoinableQueue([maxsize])
    hit_cnt += arr[i]
    hit_cnt_arr.append(hit_cnt)

print(hit_cnt_arr)

plt_hitcnt(hit_cnt_arr, 10000)
