def solution(T: int, l: list) -> list:
    answer = []

    for idx in range(T):
        rank = 1
        for jdx in range(T):
            if l[idx][0] < l[jdx][0] and l[idx][1] < l[jdx][1]:
                rank += 1
        answer.append(rank)
    return " ".join([str(i) for i in answer])


T = int(input())
l = []
for i in range(T):
    x, y = map(int, input().split(" "))
    l.append((x, y))

print(solution(T, l))