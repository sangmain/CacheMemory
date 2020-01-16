import random
import CPU_c
import plt_graph as cg

#region 초기선언
################################# 초기 선언
drive_size = 5000
ram_size = 500
L1_size = 5
L2_size = 20
L3_size = 50

##### 하드 디스크
drive = list(range(1, drive_size + 1)) #  1 ~ 5000
# print(len(drive))

##### 램
ram = [None] * ram_size
# print(len(ram))

##### 캐시
L1 = [None] * L1_size
L2 = [None] * L2_size
L3 = [None] * L3_size

##### CPU 클래스 선언
cpu = CPU_c.CPU()

##### 딕셔너리
storage_structure = {0: cpu.r1, 1: cpu.r2, 2: L1, 3: L2, 4: L3, 5: ram, 6: drive} #### 저장찾치
time_dict = {2: 0.1, 3: 0.2, 4: 0.3, 5: 1.3, 6: 4.3} #### access time

#################################
#endregion

#region 알고리즘

#### 리스트에서 비어있는 인덱스 가져오기 
def get_emptyindex(storage):
    indices = [i for i,x in enumerate(storage) if not x]
    return indices

#### 재귀로 데이터 찾고 저장하기
def find_data(tar_data, storage_key=2):
    storage = storage_structure[storage_key] ####딕셔너리에서 현재 참고해야할 저장장치 변수를 storage에 담는다 (파이썬은 주소 개념이라 자동으로 바뀜)

    if tar_data in storage: #### 찾고싶은 데이터가 저장공간에 있으면
        index = storage.index(tar_data) 
        data = storage[index]
        location = storage_key
    else: #### 없으면 다음 저장장치로 재귀
        data, location = find_data(tar_data, storage_key + 1)
        indices = get_emptyindex(storage)

        if len(indices) == 0: #### 저장공간에 빈 공간이 없으면 랜덤으로 채움
            storage[random.randint(0, len(storage)-1)] = data 
        else:
            storage[indices[0]] = data


    return data, location

#### 매번의 실행결과 
def print_status(location1, location2, tar_data1, tar_data2):
    print("접근 시간:", time_dict[location1], time_dict[location2])
    print("검색 대상 데이터: %d, %d" % (tar_data1, tar_data2))
    print("r1:", cpu.r1, "r2:", cpu.r2, "result:", cpu.alu, "answer:", tar_data1+tar_data2)

    print("L1:", L1)
    print("L2:", L2)
    print("L3:", L3)
    print()

    

def get_data(tar_data):
    is_hit = False
    #### 찾은 데이터와 어디서 찾았는지(정수형) 으로 받아온다
    data2reg, location = find_data(tar_data)

    #### HIT COUNT
    if location in [2,3,4]:
        is_hit = True

    
    return data2reg, is_hit, location

#endregion


####### 그래프 그리기
def plt_group(status_list, loop_size):
    cg.plt_accesstime(status_list, loop_size)
    cg.plt_hitcnt(status_list, loop_size)


def cycle(loop_size=1000):
    #### 결과 출력용 변수
    hit_cnt = 0
    time_sum = 0.0

    ####그래프용
    status_list = [] #### [[히트여부, 접근시간]]

    for i in range(loop_size):
        #### 찾을 데이터 랜덤
        tar_data1 = random.randint(1, drive_size)
        cpu.r1, is_hit1, location1 =  get_data(tar_data1) # status 안에는 is_hit 여부와, access_time이 들어있다
        hit_cnt += is_hit1

        status_list.append([hit_cnt, location1])

        #### 찾을 데이터 랜덤
        tar_data2 = random.randint(1, drive_size)
        cpu.r2, is_hit2, location2 = get_data(tar_data2)
        hit_cnt += is_hit2

        status_list.append([hit_cnt, location2])


        cpu.process()

        # print_status(location1, location2, tar_data1, tar_data2)

    plt_group(status_list, loop_size)

    time_list = [i[1] for i in status_list]
    for i in range(len(time_list)): #### 평균을 계산하기 위한 계산
        time_sum += time_dict[time_list[i]]

    average_time = time_sum / (loop_size * 2)

    print("연산 수행 횟수:", loop_size)
    print("hit rate:", hit_cnt / (loop_size * 2))
    print("평균 접근 시간:", average_time)
    print("hit count:", hit_cnt)

    
if __name__ == "__main__":
    cycle(10000)