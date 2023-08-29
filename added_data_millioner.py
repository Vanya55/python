filename = 'milioner.txt'
def get_file_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    data_list = []
    for line in lines:
        data_dict = eval(line)
        data_list.append(data_dict)

    return data_list[0]
        


def added_data(data_list):
    newList=data_list
    flag = True
    while flag :
        new_dict = {}
        data = input("added data/ yes or no :")
        if data == "yes":
            harc = input("Add a question :")
            if proverka(newList,harc)== False:
                new_dict["harc"]=harc
                patasxan= input("Add answers :").split()
                patasxan = ",".join(patasxan)
                new_dict["patasxan"]=patasxan
                chisht = input("Add the correct answer :")
                new_dict["chisht"]=chisht
                newList.append(new_dict)
            
        else:
            flag=False
        with open(filename, 'w') as file:
            file.write(str(data_list) + '\n')

def proverka(data_list,quest):
    flag = False
    for i in data_list:
        if i["harc"]== quest:
            flag = True
            break
    return flag
            
        
            
    


def main():
    data_list=get_file_data(filename)
    added_data(data_list)
main()
