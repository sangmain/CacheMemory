import random
import c_Status

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


drive_size = 5000 * 100
ram_size = 500 * 100
L1_size = 5 * 100
L2_size = 20 * 100
L3_size = 50 * 100

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

#region 알고리즘

#### 리스트에서 비어있는 인덱스 가져오기 
def get_emptyindex(storage):
    indices = [i for i,x in enumerate(storage) if not x]
    return indices

#### 재귀로 데이터 찾고 저장하기
def load_data(address, storage_key=2):
    storage = storage_structure[storage_key] ####딕셔너리에서 현재 참고해야할 저장장치 변수를 storage에 담는다 (파이썬은 주소 개념이라 자동으로 바뀜)

    if address in storage: #### 찾고싶은 데이터가 저장공간에 있으면
        index = storage.index(address) 
        data = storage[index]
        stat.set_location(storage_key)
    else: #### 없으면 다음 저장장치로 재귀
        data = load_data(address, storage_key + 1)
        indices = get_emptyindex(storage)

        if len(indices) == 0: #### 저장공간에 빈 공간이 없으면 랜덤으로 채움
            storage[random.randint(0, len(storage)-1)] = data 
        else:
            storage[indices[0]] = data


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

    print("L1:", L1)
    print("L2:", L2)
    print("L3:", L3)
    print()

def init_var(is_allcache):
    global ram, L1, L2, L3, cpu, stat, storage_structure

    ##### 램
    ram = [None] * ram_size
    # print(len(ram))

    ##### 캐시
    L1 = [None] * L1_size
    L2 = [None] * L2_size
    L3 = [None] * L3_size

    ##### CPU 클래스 선언
    cpu = Cpu()

    ##### Status 클래스 선언
    stat = c_Status.Status(is_allcache)

    if is_allcache:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: L2, 4: L3, 5: ram, 6: drive} #### 저장찾치
    else:
        storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: ram, 4: drive} #### 저장찾치



def cycle(data, loop_size, is_allcache=True):
    init_var(is_allcache) #### 변수 정의

    for i in range(loop_size):

        #### 찾을 데이터 랜덤
        address1 = data[i]
        cpu.mar1 = address1

        address2 = data[i + 1]
        cpu.mar2 = address2

        cpu.process()

       

        # print_status()
    stat.end(loop_size)


    # print("Random")
    # print("연산 수행 횟수:", loop_size)
    # print("hit rate:", stat.hit_rate)
    # print("평균 접근 시간:", stat.average_time)
    # print("hit count:", stat.hit_cnt)


    return stat

    


if __name__ == "__main__":
    cycle(10000, 1, True)        
