babbling = ["aya", "yee", "u", "maa", "wyeoo"]	

def solution(babbling):
    pro = ["aya", "ye", "woo", "ma"]
    answer = 0
    for j in pro:
        if pro in babbling:
            print(babbling)
            answer += 1
    return answer

print(solution(babbling))