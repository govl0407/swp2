def solution(num):
    answer = 0
    while num != 0:
        answer = answer + num % 10
        num = num // 10
    return answer

a = int(input())
print(solution(a))
