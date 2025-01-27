import random
import queue
import c_Status
import pickle
import pandas as pd

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
        
            
        print("FIFO")
        print("연산 수행 횟수:", loop_size)
        print("hit rate:", stat.hit_rate)
        print("평균 접근 시간:", stat.average_time)
        print("hit count:", stat.hit_cnt)



drive_size = 50000
ram_size = 30000
L1_size = 64
L2_size = 1000
L3_size = 2000

##### 하드 디스크
drive = list(range(1, drive_size + 1)) #  1 ~ 5000
# print(len(drive))

########### None으로 정의된 변수들은 init_var에서 제대로 정의해준다 (작업 반복할때 초기화용)

##### 램
ram = None

##### 캐시
L1 = None
L2 = None
L3 = None

##### CPU 클래스 선언
cpu = None

##### Status 클래스 선언
stat = None

##### 저장장치 딕셔너리
storage_structure = None

#################################
#endregion


#### 재귀로 데이터 찾고 저장하기
def load_data(file, storage_key=2):
    storage = storage_structure[storage_key] ####딕셔너리에서 현재 참고해야할 저장장치 변수를 storage에 담는다 (파이썬은 주소 개념이라 자동으로 바뀜)

    try: #### 저장장치 종류가 queue이면
        list_storage = list(storage.queue)
    except: #### 저장장치가 queue가 아니면, 즉 하드디스크이면
        list_storage = storage

    if file["address"] in list_storage: #### 찾고싶은 데이터가 저장공간에 있으면
        index = list_storage.index(file["address"]) 
        data = list_storage[index]
        stat.set_location(storage_key)

    else: #### 없으면 다음 저장장치로 재귀
        if storage_key == len(storage_structure) -1:
            data = file["address"]
            stat.set_location(storage_key + 1)

        else:
            data = load_data(file, storage_key + 1)        

        if not storage.full(): 
            storage.put_nowait(data)
        else: #### 저장공간에 빈 공간이 없으면 FIFO
            storage.get_nowait() 
            storage.put_nowait(data)


    return data

def init_var(l1, l2, l3):
    global ram, L1, L2, L3, cpu, stat, storage_structure
    global L1_size, L2_size, L3_size
    L1_size = l1
    L2_size = l2
    L3_size = l3

    ##### 램
    ram = queue.Queue(ram_size)

    ##### 캐시
    L1 = queue.Queue(L1_size)
    L2 = queue.Queue(L2_size)
    L3 = queue.Queue(L3_size)

    ##### CPU 클래스 선언
    cpu = Cpu()
    
    if L2_size == 0:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1} #### 저장찾치
    elif L3_size == 0:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: L2} #### 저장찾치
    else:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: L2, 4: L3}
        
    ##### Status 클래스 선언
    stat = c_Status.Status(len(storage_structure))

def start(file, loop_size, l1=0, l2=0, l3=0):
    init_var(l1, l2, l3)
    cpu.cpu_start(file, loop_size)
    with open("./Result/FIFO/"+str(L1_size) + "-" +  str(L2_size)+"config.txt", "w") as f:
        f.write("Location: ./Result/FIFO/"+str(L1_size) + "-" + str(L2_size)+"\nPolicy: FIFO\nData: %s\nL1: %d\nL2: %d\nL3: %d"% ("cc1", L1_size, L2_size, L3_size))
    with open('./Result/FIFO/'+str(L1_size) + "-" + str(L2_size)+'hit.txt','wb') as f:
        pickle.dump(stat.is_hit, f)
    with open('./Result/FIFO/'+str(L1_size) + "-" + str(L2_size)+'time.txt','wb') as f:
        pickle.dump(stat.access_time, f)

if __name__ == "__main__":
    file = pd.read_csv("./Data/cc1.csv")
    start(file, 1000, 64, 1000, 2000)
    