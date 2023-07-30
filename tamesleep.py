import random
import time
import math
countries={
"Japan":"Tokyo",
"Armenia":"Yerevan",
"Spain":"Madrid",
"USA":"Washington",
"Russia":"Moscow",
}
l = list(countries.items())
random.shuffle(l)
wrong_answers = 0
correct_answers= 0
timelimit = 10
flag = False
for i in l:
    if wrong_answers == 3:
        break
    start = time.time()
    print("Вопрос :",i[0])
    user_input = input("your answer :").title()
    end = time.time()
    elapsed_time = math.floor(end - start)
    if elapsed_time <= timelimit:
        if user_input == i[1]:
            correct_answers += 1
        else:
            wrong_answers += 1
    else:
        print("Время вышло")
        break
            
print("Правильных ответов:", correct_answers)
print("Проигрышей:", wrong_answers)
            
            

