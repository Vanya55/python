import random
from inputimeout import inputimeout,TimeoutOccurred
countries={
"Japan":"Tokyo",
"Armenia":"Yerevan",
"Spain":"Madrid",
"USA":"Washington",
"Russia":"Moscow",
}
l = list(countries.items())
random.shuffle(l)
dic = dict(l)
count = 0
for k,v in dic.items():
    print("Вопрос :",k)
    try:
        user_input=inputimeout(prompt="Ответ :",timeout=10)
        if user_input==v.lower():
            count+=1
    except Exception:
        print("Время Вышло!")
        break
print("Верные ответи",count)

            
            

