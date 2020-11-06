"""
    nodemon pg.py
"""


def check_group_word(word: str) -> bool:
    is_group_word = True
    _word = []
    for idx in range(len(word)):
        if word[idx] in _word:
            is_group_word = False
        if idx + 1 < len(word) and word[idx] != word[idx + 1]:
            _word.append(word[idx])
    return is_group_word


T = int(input())
words = []
count = 0
for i in range(T):
    word = input()
    words.append(word)
for word in words:
    if check_group_word(word):
        count += 1
print(count)

assert check_group_word("happy") == True
assert check_group_word("new") == True
assert check_group_word("aba") == False
assert check_group_word("abcabc") == False
