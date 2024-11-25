from collections import Counter

def solution(array):
    count = Counter(array)  # 각 숫자의 등장 횟수를 세줌
    modes = count.most_common()  # 등장 횟수가 많은 순으로 정렬
    
    # 최빈값이 하나인지 확인
    if len(modes) > 1 and modes[0][1] == modes[1][1]:
        return -1  # 최빈값이 여러 개면 -1 반환
    
    return modes[0][0]  # 최빈값 반환
