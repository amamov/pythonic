import random
import time
import sqlite3
import datetime
import pygame

pygame.init()
pygame.mixer.init()
bad_sound = pygame.mixer.Sound("./assets/bad.wav")
good_sound = pygame.mixer.Sound("./assets/good.wav")


connect = sqlite3.connect()


words = []  # 단어 리스트
count = 1  # 게임 시도 횟수
number_of_successes = 0  # 정답 수

with open("./assets/word.txt", "r") as file:
    for word in file:
        word = word.strip()
        words.append(word)

# print(words)
input("Ready? Press Enter Key.")

start = time.time()

while count <= 5:
    random.shuffle(words)
    question = random.choice(words)
    print(f"\nQuestions # {count}")
    print(question)
    answer = input(">").strip()
    print()
    if answer == question:
        print("Pass!")
        number_of_successes += 1
    else:
        print("Wrong!")

    count += 1

end = time.time()

timer = end - start
timer = format(timer, ".3f")

if number_of_successes >= 3:
    print("Good!")
else:
    print("Fuck!")

print("Time :", timer, "초  success :", number_of_successes)
