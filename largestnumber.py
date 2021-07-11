def LargestInList(n=[]):
    max = 0
    for data in n:
        if data > max:
            max = data
    print('The largest number in list is', max)   



LargestInList(n = [21,45,99,78,56])