d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300,'b':200,'d':400}
c={}
for i in d1:
    if i in d2:
        c[i]=d1[i]+d2[i]
    else:
        c[i]=d1[i]
for i in d2:
    if i not in c:
        c[i]=d2[i]
        
print(c)
        

