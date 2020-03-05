import random
import c_Status
import queue
import pickle
import pandas as pd

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
        
    def cpu_start(self, file, loop_size):
        index = 0
        for i in range(0, loop_size, 1):
            index += 1
            

            self.load(self.r1, file.iloc[i]) # address
            if index == 100000:
                print((i+1)/10000, "\b%")
                index = 0

            # print("L1:", L1.data)
            # print("L2:", L2.data)
            # print("L3:", L3.data)

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
L1_size = 64
L2_size = 1000
L3_size = 2000

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

        index = storage.index(file["address"]) 
        data = storage[index]

        for key in data_recency.keys():
            data_recency[key] = data_recency[key] + 1
        data_recency[data] = 0
        
        stat.set_location(storage_key)

    else: #### 없으면 다음 저장장치로 재귀
        if storage_key == len(storage_structure) -1:
            data = file["address"]

            for key in data_recency.keys():
                data_recency[key] = data_recency[key] + 1
            data_recency[data] = 0

            stat.set_location(storage_key + 1)
        else:
            data = load_data(file, storage_key + 1) #재귀 후 발견된 데이터 반환
        indices = get_emptyindex(storage)
        if len(indices) == 0: #### 저장공간에 빈 공간이 없으면 LRU로 채움
            last_recent_idx = 0

            for i in range(1, len(storage), 1):
                if data_recency[storage[i]] > data_recency[storage[last_recent_idx]]:
                    last_recent_idx = i

            storage[last_recent_idx] = data
        else:
            storage[indices[0]] = data

    return data
    
#endregion


def init_var(l1, l2, l3, file):
    global ram, L1, L2, L3, cpu, stat, storage_structure, data_recency
    global L1_size, L2_size, L3_size
    L1_size = l1
    L2_size = l2
    L3_size = l3
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

    for i, item in enumerate(file):
        data_recency[item] = data_recency.get(item, 0)
    
    if L2_size == 0:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1} #### 저장찾치
    elif L3_size == 0:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: L2} #### 저장찾치
    else:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: L2, 4: L3}

    stat = c_Status.Status(len(storage_structure))


data_recency = {}

def start(file, loop_size, l1=0, l2=0, l3=0):
    init_var(l1, l2, l3, file)
    cpu.cpu_start(file, loop_size)
    with open("./Result/LRU/"+str(L1_size)+"config.txt", "w") as f:
        f.write("Location: ./Result/LRU/"+str(L1_size)+"\nPolicy: LRU\nData: %s\nL1: %d\nL2: %d\nL3: %d"% ("cc1", L1_size, L2_size, L3_size))
    with open('./Result/LRU/'+str(L1_size)+'hit.txt','wb') as f:
        pickle.dump(stat.is_hit, f)
    with open('./Result/LRU/'+str(L1_size)+'time.txt','wb') as f:
        pickle.dump(stat.access_time, f)

if __name__ == "__main__":
    file = pd.read_csv("./Data/cc1.csv")
    start(file, 1000, 64, 1000, 2000)
    