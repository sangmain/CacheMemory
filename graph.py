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



# Random
## Hit Rate
# array1 = [0.0009750000000000002, 0.0010083333333333333,  0.0009599999999999999,  0.00104375, 0.0009950000000000002]
# array2 = [0.010850000000000004,  0.011616666666666666, 0.01076,  0.011484375, 0.011082499999999999]

#Access Time
array1 = [4.019655000000128, 3.9964408333329002, 3.993258000000099, 3.993122812501146, 3.987665500001493]
array2 = [4.024045000000127, 3.998774166666233, 3.9930820000000984, 3.9885034375011434, 3.993021000001497]

# FIFO 
## Hit Rate
# array1 = [0.0008750000000000005, 0.0008916666666666667, 0.0010350000000000001, 0.0009562500000000003, 0.00097]
# array2 = [0.010225000000000003, 0.009441666666666664,  0.01011, 0.009731249999999999, 0.009845]

##Access Time
# array1 = [4.026307500000128, 4.004261666666233, 3.997147000000102, 3.9978815625011492, 3.9952670000014967]
# array2 = [4.028917500000128, 4.0062708333329, 3.995551500000102, 3.9938328125011457, 3.995675250001498]

# plot1(array1, array2)
# plot2(array1, array2)

import pickle
from scipy.interpolate import make_interp_spline, BSpline


with open('random_is_hit.txt', 'rb') as f:
    is_hit = pickle.load(f)


def plt_accesstime(status_list, loop_size):
    time_sum = 0.0
    time_list = [i[1] for i in status_list]
    
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
    hit_cnt += arr[i]
    hit_cnt_arr.append(hit_cnt)

print(hit_cnt_arr)

plt_hitcnt(hit_cnt_arr, 10000)
