import random
import c_Status
import queue

######################### 교체방식 
replace_type = 2 #### replace_type는 0: Random, 1: FIFO, 2: LRU 

#region 초기선언
################################# 초기 선언
class Cpu:

    def __init__(self):
        self.ac = 0
        self.r1 = 0
        self.r2 = 0

    def load(self, reg, file):
        reg = load_data(file)    

    # def store(self, reg, address):
    #     store_data(reg, address)
    # def add(self, load_reg, address, add_reg):
    #     load_reg = load(self, address)
    #     self.ac = load_reg + add_reg

    def cpu_start(self, file, loop_size, is_allcache=True):
        for i in range(0, loop_size, 1):
            # data = [address, data] * n
            #### 찾을 데이터 랜덤
            if file["load/store"][i] == 'l':
                self.load(self.r1, file.iloc[i]) # address
            else:
                self.load(self.r1, file.iloc[i]) # address

                # # print("접근 시간:", stat.access_time[-1])
                # print("검색 대상 데이터:", file.iloc[i]["address"])

                # print("L1:", L1.data)
                # print("L2:", L2.data)
                # print("L3:", L3.data)
                # print()
                # return

        stat.end(loop_size)

        print("LRU")
        print("연산 수행 횟수:", loop_size)
        print("hit rate:", stat.hit_rate)
        print("평균 접근 시간:", stat.average_time)
        print("hit count:", stat.hit_cnt)

##### Cache, RAM, DISK 모두 이 클래스로 인해 선언된다
class Memory:
    def __init__(self, size=1, replace_type=0):
        #### replace_type는 0: Random, 1: FIFO, 2: LRU 
        if replace_type == 1: ## FIFO 일시
            self.data = queue.Queue(size)
        else:
            self.data = [None] * size
            self.recent_log = []




drive_size = 50000
ram_size = 30000
L1_size = 64000
L2_size = 1000000
L3_size = 2000000

# L1_size = 1
# L2_size = 3
# L3_size = 1

##### 하드 디스크
drive = Memory()
drive.data =  list(range(0, drive_size + 1)) #  1 ~ 5000
# print(len(drive))


########### None으로 정의된 변수들은 init_var에서 제대로 정의해준다 (작업 반복할때 초기화용)

##### 램
ram = None

##### 캐시 클래스 선언
L1 = None
L2 = None
L3 = None

data_recency = []
##### CPU 클래스 선언
cpu = None

##### Status 클래스 선언
stat = None

##### 저장장치 딕셔너리
storage_structure = None

#################################
#endregion

#region 알고리즘

#### 리스트에서 비어있는 인덱스 가져오기 
def get_emptyindex(storage):
    indices = [i for i,x in enumerate(storage) if not x]
    return indices

#### 재귀로 데이터 찾고 저장하기
def load_data(file, storage_key=2):
    global data_recency
    storage = storage_structure[storage_key].data ####딕셔너리에서 현재 참고해야할 저장장치 변수를 storage에 담는다 (파이썬은 주소 개념이라 자동으로 바뀜)
    
    if file["address"] in storage: #### 찾고싶은 데이터가 저장공간에 있으면
        data_recency = [x + 1 for x in data_recency]

        index = storage.index(file["address"]) 
        data = storage[index]
        data_recency[data-1] = 0
        stat.set_location(storage_key)

    else: #### 없으면 다음 저장장치로 재귀
        if storage_key == len(storage_structure) -1:
            data = file["address"]
            stat.set_location(storage_key + 1)
        else:
            data = load_data(file, storage_key + 1) #재귀 후 발견된 데이터 반환
        indices = get_emptyindex(storage)
        if len(indices) == 0: #### 저장공간에 빈 공간이 없으면 LRU로 채움
            least_recent_idx = 0

            for i in range(1, len(storage), 1):
                if data_recency[storage[i] - 1] > data_recency[storage[least_recent_idx] - 1]:
                    least_recent_idx = i

            storage[least_recent_idx] = data
        else:
            storage[indices[0]] = data

    return data
    
#endregion


def print_status():
    print("접근 시간:", stat.access_time[-2], stat.access_time[-1])
    # print("검색 대상 데이터: %d, %d" % (cpu.mar1, cpu.mar2))
    # print("r1:", cpu.r1, "r2:", cpu.r2, "result:", cpu.ac, "answer:", cpu.mar1 + cpu.mar2)

    print("L1:", L1.data)
    print("L2:", L2.data)
    print("L3:", L3.data)
    print("RAM:", ram.data)
    print()

def init_var(is_allcache):
    global ram, L1, L2, L3, cpu, stat, storage_structure, data_recency

    ##### 램 클래스 선언
    ram = Memory(ram_size, replace_type)
    # print(len(ram))

    ##### 캐시 클래스 선언
    L1 = Memory(L1_size, replace_type)
    L2 = Memory(L2_size, replace_type)
    L3 = Memory(L3_size, replace_type)

    ##### CPU 클래스 선언
    cpu = Cpu()

    ##### Status 클래스 선언
    stat = c_Status.Status(is_allcache)
    
    data_recency = [0] * max(file["address"])
    if is_allcache:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: L2, 4: L3} #### 저장찾치
    else:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: ram, 4: drive} #### 저장찾치




def cycle(data, loop_size, is_allcache=True):
    init_var(is_allcache) #### 변수 정의


       

        # print_status()
    stat.end(loop_size)

    print("LRU")
    print("연산 수행 횟수:", loop_size)
    print("hit rate:", stat.hit_rate)
    print("평균 접근 시간:", stat.average_time)
    print("hit count:", stat.hit_cnt)


    return stat

    


if __name__ == "__main__":
    import pandas as pd
    file = pd.read_csv("./Data/spec2006_prop.csv")
    init_var(True)
    cpu.cpu_start(file, len(file))



    # data = [1,2,3,1,4,5,1,2,3,1,4,5,1,2,3,1,4,5,1,2,3,1,4,5,1,2,3,1,4,5,1,2,3,1,4,5,6,6]
