def selection_sort(lis):        
    for i in range(len(lis)):
        minn = i
        
        for j in range(i + 1, len(lis)):
            if lis[j] < lis[minn]:
                minn = j

        lis[minn], lis[i] = lis[i], lis[minn]
            
    return lis
print(selection_sort([-2, 45, 0, 11, -9,88,-97,-202,747]))
