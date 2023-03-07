array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        # print(j)
        if array[j] < array[j - 1]: # 현재idx의 원소가 이전 idx의 원소보다 작다면 
            array[j], array[j - 1] = array[j - 1], array[j] # 서로 자리 바꿔주기.
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
