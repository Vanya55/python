#def myreverse(st):                #8
    #return st[::-1]
#print(myreverse("hello world"))


#def srez(st,start,end):            #9
    #if start < len(st):
        #return st[start:end]
    #else:
        #return st

#print(srez("hello",1,5))

#def longest_words(st):       #10
    #maxx = ""
    #lenmax = 0
    #st2 = st.split()
    #for i in st2:
        #if len(i) >lenmax:
            #lenmax = len(i)
            #maxx=i
    #return maxx
#print(longest_words("hello my goodining day"))
        

#def maxelcount(st):         #11
    #maxx = 0
    #el = ""
    #for i in st:
        #if st.count(i) > maxx:
            #maxx = st.count(i)
            #el = i
    #return el
#print(maxelcount("abrakadabra"))
