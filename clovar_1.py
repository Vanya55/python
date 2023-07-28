l= [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
  ]
c={}
s=0
for i in l:
    if i['item']== 'item1': 
        s+=i['amount']
    else:
        c['item2']=i['amount']
    c['item1']=s
    
print(c)
