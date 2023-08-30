def longest_increasing_subsequence(lst):
    current= []
    longest= []

    for i in range(len(lst) - 1):
        current.append(lst[i])
        if lst[i] >= lst[i + 1]:
            if len(current) > len(longest):
                longest = current
            current = []

    if current and lst[-2] < lst[-1]:
        current.append(lst[-1])
        if len(current) > len(longest):
            longest = current

    return longest

ml = [12, 1, 2, 3, 4, 25, 13, 15, 16]
result = longest_increasing_subsequence(ml)
print(result)
