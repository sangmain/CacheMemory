import matplotlib.pyplot as plt
import numpy as np

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

from scipy.interpolate import make_interp_spline, BSpline
def plt_hitcnt(status_list, loop_size):
    hit_list = np.array([i[0] for i in status_list])

    x = np.linspace(0, (loop_size*2), 5)
    a = np.arange(0,(loop_size*2))

    spl = make_interp_spline(a, hit_list, k=3)  # type: BSpline
    power_smooth = spl(x)
    plt.title("Hit count during " + str(loop_size*2) +" requests")
    plt.plot(hit_list, label="Hit count")
    plt.plot(x, power_smooth, label="Hit count Trend")
    plt.xlabel("Cycle Count")
    plt.ylabel("Hit Count")
    plt.legend()
    plt.show()