import random

#region 초기선언
################################# 초기 선언
drive_size = 5000
ram_size = 500
L1_size = 5
L2_size = 20
L3_size = 50

loop_size = 1000
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

##### 레지스터
R1 = None; R2 = None

##### 저장장치 딕셔너리
storage_structure = {0: R1, 1: R2, 2: L1, 3: L2, 4: L3, 5: ram, 6: drive}
time_dict = {2: 0.1, 3: 0.2, 4: 0.3, 5: 1.3, 6: 4.3}

##### 결과 출력용 변수
hit_cnt = 0
total_time = 0.0

#################################
#endregion

################################# 시나리오 1
print("시나리오 1\n")

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
    else: #### 없으면 다음 저장장치로 재귀
        data, storage_key = find_data(tar_data, storage_key + 1)
        indices = get_emptyindex(storage)

        if len(indices) == 0: #### 저장공간에 빈 공간이 없으면 랜덤으로 채움
            storage[random.randint(0, len(storage)-1)] = data 
        else:
            storage[indices[0]] = data


    return data, storage_key

#### 매번의 실행결과 
def print_status():
    print("접근 시간:", time_dict[location1], time_dict[location2])
    print("검색 대상 데이터: %d, %d" % (tar_data1, tar_data2))
    print("R1:", R1, "R2:", R2, "result:", R1 + R2, "answer:", tar_data1+tar_data2)

    print("L1:", L1)
    print("L2:", L2)
    print("L3:", L3)
    print()

def process(tar_data):
    #### 찾은 데이터와 어디서 찾았는지(정수형) 으로 받아온다
    data2reg, location = find_data(tar_data)

    #### HIT COUNT
    if location in [2,3,4]:
        hit_cnt += 1

    #### 시간 계산
    total_time += time_dict[location1]
    total_time = round(total_time, 1)
    
    return data2reg


for i in range(loop_size):
    #### 찾을 데이터 랜덤
    R1 = process(random.randint(1, drive_size))
    R2 = process(random.randint(1, drive_size))

    # print_status()

print("연산 수행 횟수:", loop_size)
print("hit rate:", hit_cnt / (i+1))
print("average access time:", total_time/ (loop_size * 2))
print("hit count", hit_cnt)
