def add_file(content):
    file = open("result.txt", "a")
    file.write(content + "\n")
    file.close()

def count_worlds(st):
    md = {}
    for el in st:
        if el in md:
            md[el] += 1 
        else:
            md[el] = 1
    return str(md)

def lon_words(ml):
    a = ml.split()
    maxx = 0
    n = ""
    for i in a:
        if len(i) > maxx:
            maxx = len(i)
            n = i
    return n 
    
    

def count_st(st):
    count = 0
    for i in st:
        if i == ".":
            count += 1
    return str(count)

def reverse(lis):
    a = lis.split()
    ml = []
    for i in a:
        ml.append(i[::-1])
    return " ".join(ml)

def add_file_mesege(message,rezult):
    add_file(message)
    add_file(rezult)
    print(rezult)

def main():
    file = open("data.txt", "r")
    line = file.readlines()
    file.close()
    line1 = "".join(line)
    print(line1)
    add_file(line1)
    
    worlds_count = count_worlds(line1)
    add_file_mesege("Count of words:",worlds_count)
    
    
    longest_word = lon_words(line1)
    add_file_mesege("Longest word:",longest_word)
    
    
    sentences_count = count_st(line1)
    add_file_mesege("Count of sentences:",sentences_count)
    
    reversed_text = reverse(line1)
    add_file_mesege("Reversed text:",reversed_text)
    

main()
