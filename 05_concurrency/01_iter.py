"""
- Iterable 객체 : iter 함수에 인자로 전달이 가능한 객체 -> tuple, list, dictionary, set, ...
- Iterator 객체 : iter 함수가 생성해서 반환하는 객체
- Iterable 객체를 대상으로 iter 함수를 호출해서 Iterator 객체를 만든다.
- Iterable 객체와 Iterator 객체 모두 for 루프의 반복 대상이 될 수 있다.
- Iterable 객체가 와야하는 위치에는 Iterator 객체가 올 수 있다.
"""

my_list = [1, 2, 3, 4]  # iterable 객체
ir = iter(my_list)  # iterator 객체 ( my_list.__iter__() )
print(type(ir))

print(next(ir))  # ir.__next__()
print(next(ir))  # ir.__next__()

## for loop의 동작원리
for i in my_list:
    print(i, end=" ")

print()

ir = iter(my_list)
while True:
    try:
        i = next(ir)
        print(i, end=" ")
    except StopIteration:
        break

print()


class WordSplitIter:
    def __init__(self, text):
        if not (" " in text):
            self.text = []
        else:
            self.text = text.split(" ")
        self.idx = 0

    def __next__(self):  # 객체가 iterator 객체가 된다
        print("Called __next__")
        try:
            word = self.text[self.idx]
        except IndexError:
            raise StopIteration
        self.idx += 1
        return word

    def __iter__(self):
        print("Called __iter__")
        return self

    def __repr__(self):
        return self.text


word_iterator = WordSplitIter("I love you")

print(next(word_iterator))
print(next(word_iterator))