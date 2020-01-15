import random
import queue

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
ram = queue.Queue(ram_size)
# for i in range(5):
#     ram.put_nowait(i)
# print(ram.qsize())

# ram = [random.choice(drive) for i in range(ram_size)]
# print(len(ram))

##### 캐시
L1 = queue.Queue(L1_size)
L2 = queue.Queue(L2_size)
L3 = queue.Queue(L3_size)

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

#### 재귀로 데이터 찾고 저장하기
def find_data(tar_data, storage_key=2):
    storage = storage_structure[storage_key] ####딕셔너리에서 현재 참고해야할 저장장치 변수를 storage에 담는다 (파이썬은 주소 개념이라 자동으로 바뀜)

    try: #### 저장장치 종류가 queue이면
        list_storage = list(storage.queue)
    except: #### 저장장치가 queue가 아니면, 즉 하드디스크이면
        list_storage = storage

    if tar_data in list_storage: #### 찾고싶은 데이터가 저장공간에 있으면
        index = list_storage.index(tar_data) 
        data = list_storage[index]
    else: #### 없으면 다음 저장장치로 재귀
        data, storage_key = find_data(tar_data, storage_key + 1)

        if not storage.full(): #### 저장공간에 빈 공간이 없으면 랜덤으로 채움
            storage.put_nowait(data)
        else:
            storage.get_nowait()
            storage.put_nowait(data)

            


    return data, storage_key

#### 매번의 실행결과 
def print_status():
    print("접근 시간:", time_dict[location1], time_dict[location2])
    print("검색 대상 데이터: %d, %d" % (tar_data1, tar_data2))
    print("R1:", R1, "R2:", R2, "result:", R1 + R2, "answer:", tar_data1+tar_data2)

    print("L1:", L1.queue)
    print("L2:", L2.queue)
    print("L3:", L3.queue)
    print()


for i in range(loop_size):
    #### 찾을 데이터 랜덤
    tar_data1 = random.randint(1, drive_size)
    tar_data2 = random.randint(1, drive_size)

    #### 찾은 데이터와 어디서 찾았는지(정수형) 으로 받아온다
    R1, location1 = find_data(tar_data1)
    R2, location2 = find_data(tar_data2)

    #### HIT COUNT
    if location1 in [2,3,4]:
        hit_cnt += 1
    if location2 in [2,3,4]:
        hit_cnt += 1

    #### 시간 계산
    total_time += time_dict[location1]
    total_time = round(total_time, 1)
    total_time += time_dict[location2]
    total_time = round(total_time, 1)

    # print_status()

print("연산 수행 횟수:", loop_size)
print("hit rate:", hit_cnt / (i+1))
print("average access time:", total_time/ (loop_size * 2))
