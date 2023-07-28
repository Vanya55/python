import random
import time
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
for i in l:
        if wrong_answers == 3:
            break
        start = time.time()
        print("Вопрос :",i[0])
        user_input = input().title()
        end = time.time()
        elapsed_time = end - start

        if elapsed_time > 10:
            print("Время вышло!")
            wrong_answers += 1
        elif user_input == i[1]:
            correct_answers += 1
        else:
            wrong_answers += 1
            
print("Правильных ответов:", correct_answers)
print("Проигрышей:", wrong_answers)
            
            

