a, b = map(int, input().split())
d_list = list(map(int, input().split()))
N = 0
result = 0
for i, text in enumerate(d_list):
    if text >= N:
        result += text - N
    if result == b:
        print(result)
    N+=1
    