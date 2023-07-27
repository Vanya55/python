import random
quest=[{"harc":"What is capital of Armenia:?","patasxan":"Yerevan,Pekin,Gyumri,Buenos Aires","chisht":"Yerevan"},
        {"harc":"What is capital of France:?","patasxan":"Paris,Erevan,Gyumri,London","chisht":"Paris"},
        {"harc":"What is capital of China:?","patasxan":"Pekin,Paris,Pokin,Tbilisi","chisht":"Pekin"},
        {"harc":"What is capital of USA:?","patasxan":"Washington,Paris,Pekin,London","chisht":"Washington"},
        {"harc":"What is capital of Brazil:?","patasxan":"Brazil,Washington,Pekin,Brezil","chisht":"Brazil"},
        {"harc":"What is capital of Georgia:?","patasxan":"Tbilisi,Washington,Lisbon,Brazil","chisht":"Tbilisi"},
        {"harc":"What is capital of Germany:?","patasxan":"Berlin,Erevan,Lisbon,Roma","chisht":"Berlin"},
        {"harc":"What is capital of Austria:?","patasxan":"Vienna,Erevan,Lisbon,Roma","chisht":"Vienna"},
        {"harc":"What is capital of Italy:?","patasxan":"Roma,Washington,Lisbon,Brazil","chisht":"Roma"},
        {"harc":"What is capital of Spain:?","patasxan":"Madrid,Paris,Barselona,London","chisht":"Madrid"},   
        {"harc":"What is capital of United Kingdom:?","patasxan":"London,Erevan,Madrid,Lisbon","chisht":"London"},
        {"harc":"What is capital of Russian:?","patasxan":"Belgorod,Tula,Peterburg,Moscow","chisht":"Moscow"},
        {"harc":"What is capital of UAE:?","patasxan":"Abu Dhabi,Washington,Gyumri,Tbilisi","chisht":"Abu Dhabi"},
        {"harc":"What is capital of Portugaly:?","patasxan":"Lisabon,Washington,Gyumri,Buenos Aires","chisht":"Lisabon"},
        {"harc":"What is capital of Argentina:?","patasxan":"Buenos Aires,Washington,Gyumri,Minsk","chisht":"Buenos Aires"},
]
random.shuffle(quest);
count=0
for i in quest:
    print(i['harc'])
    newAnsers=i['patasxan'].split(",")
    correct_answer=i["chisht"]
    random.shuffle(newAnsers);
    for el in newAnsers:
        print(el)
    inputAnser=input('mutqagreq patasxany:').title()
    if inputAnser==correct_answer:
        count+=1
    print("\n" *2)
    
print("Correctly answered to :",count,"times")   
