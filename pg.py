"""
    nodemon pg.py
"""

# 리스트 반대로 바꾸기
# string 반대로 바꾸기


def bulls_and_cows(problem, answer):
    strike, ball = 0, 0

    for pr_e in problem:  # 5
        for as_e in answer:  # 1
            if pr_e == as_e:
                strike += 1  # 1
                answer.remove(as_e)
                break
            elif as_e in problem:  #
                ball += 1
                break

    return [(strike), (ball)]


print(bulls_and_cows([1, 5, 8], [1, 8, 9]))