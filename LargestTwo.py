def LargestInList(n=[]):
    
    max = 0
    for data in n:
        if data > max:
            max = data
    L1 = max
    list1 = n
    list1.remove(max)
    max1 = 0
    for elements in list1:
        if elements > max1:
            max1 = elements
    print('The largest 2 elements in list are', max,'&',max1)
    


LargestInList(n=[21,45,99,78,56])