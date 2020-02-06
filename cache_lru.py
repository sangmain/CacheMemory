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

        self.mar1 = 0
        self.mar2 = 0

    def process(self):
        self.r1 = load_data(self.mar1)
        self.r2 = load_data(self.mar2)

        self.cpu_add()


    def cpu_add(self):
        self.ac = self.r1 + self.r2

class Memory:
    def __init__(self, size=1, replace_type=0):
        #### replace_type는 0: Random, 1: FIFO, 2: LRU 
        if replace_type == 1: ## FIFO 일시
            self.data = queue.Queue(size)
        else:
            self.data = [None] * size
            self.recent_log = []


drive_size = 1000
ram_size = 500
L1_size = 5
L2_size = 20
L3_size = 50

##### 하드 디스크
drive = Memory()
drive.data =  list(range(1, drive_size + 1)) #  1 ~ 5000
# print(len(drive))


########### None으로 정의된 변수들은 init_var에서 제대로 정의해준다 (작업 반복할때 초기화용)

##### 램
ram = None

##### 캐시 클래스 선언
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

#region 알고리즘

#### 리스트에서 비어있는 인덱스 가져오기 
def get_emptyindex(storage):
    indices = [i for i,x in enumerate(storage) if not x]
    return indices

#### 재귀로 데이터 찾고 저장하기
def load_data(address, storage_key=2):
    storage = storage_structure[storage_key].data ####딕셔너리에서 현재 참고해야할 저장장치 변수를 storage에 담는다 (파이썬은 주소 개념이라 자동으로 바뀜)
    recent_log = storage_structure[storage_key].recent_log
    
    if address in storage: #### 찾고싶은 데이터가 저장공간에 있으면
        index = storage.index(address) 
        data = storage[index]
        stat.set_location(storage_key)

        

        for i in range(storage_key, len(storage_structure)-1, 1):
            recent_log = storage_structure[i].recent_log
            recent_log[index] = 0
            try:
                recent_log[index] = 0
            except:
                recent_log.append(0)

            recent_log = [x + 1 for x in recent_log]
            storage_structure[i].recent_log = recent_log


        
    else: #### 없으면 다음 저장장치로 재귀
        data = load_data(address, storage_key + 1) #재귀 후 발견된 데이터 반환
        indices = get_emptyindex(storage)

        if len(indices) == 0: #### 저장공간에 빈 공간이 없으면 LRU로 채움
            recent_log = storage_structure[storage_key].recent_log
            lfu_index = recent_log.index(max(recent_log))
            storage[lfu_index] = data
            recent_log[lfu_index] = 0

        else:
            storage[indices[0]] = data

            recent_log = storage_structure[storage_key].recent_log
            recent_log.append(0)

        recent_log = [x + 1 for x in recent_log]
        storage_structure[storage_key].recent_log = recent_log



   
        
    return data
    
#endregion


# ####### 그래프 그리기
# def plt_group(status_list, loop_size):
#     cg.plt_accesstime(status_list, loop_size)
#     cg.plt_hitcnt(status_list, loop_size)

def print_status():
    print("접근 시간:", stat.access_time[-2], stat.access_time[-1])
    print("검색 대상 데이터: %d, %d" % (cpu.mar1, cpu.mar2))
    print("r1:", cpu.r1, "r2:", cpu.r2, "result:", cpu.ac, "answer:", cpu.mar1 + cpu.mar2)

    print("L1:", L1.data)
    print("L2:", L2.data)
    print("L3:", L3.data)
    print()

def init_var(is_allcache):
    global ram, L1, L2, L3, cpu, stat, storage_structure

    ##### 램
    ram = Memory(ram_size, replace_type)
    # print(len(ram))

    ##### 캐시
    L1 = Memory(L1_size, replace_type)
    L2 = Memory(L2_size, replace_type)
    L3 = Memory(L3_size, replace_type)

    ##### CPU 클래스 선언
    cpu = Cpu()

    ##### Status 클래스 선언
    stat = c_Status.Status(is_allcache)

    if is_allcache:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: L2, 4: L3, 5: ram, 6: drive} #### 저장찾치
    else:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: ram, 4: drive} #### 저장찾치




def cycle(loop_size, seed, is_allcache=True):
    init_var(is_allcache) #### 변수 정의
    random.seed(seed)

    for i in range(loop_size):

        #### 찾을 데이터 랜덤
        address1 = random.randint(1, drive_size)
        cpu.mar1 = address1

        address2 = random.randint(1, drive_size)
        cpu.mar2 = address2

        cpu.process()

       

        # print_status()
    stat.end(loop_size)

    # print("LRU")
    # print("연산 수행 횟수:", loop_size)
    # print("hit rate:", stat.hit_rate)
    # print("평균 접근 시간:", stat.average_time)
    # print("hit count:", stat.hit_cnt)


    return stat

    


if __name__ == "__main__":
    cycle(3, 1, True)        
