a , b = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

print(A_list)
print(B_list)

for a_idx, a_text in enumerate(A_list):
    A_min = min(A_list)
    B_min = max(B_list)
    for b_idx, b_text in enumerate(B_list):
        if a_text == A_min:
            A_list[a_idx] , B_list[b_idx] = B_list[b_idx], A_list[a_idx]

print(sum(A_list)) 
        