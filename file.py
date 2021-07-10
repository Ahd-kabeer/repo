
def FileAndString():
    s ='goal'
    fname=  open("fname.txt", "r")
    flag = 0
    index = 0
    for line in fname:
        index += 1
        if s in line:
            flag = 1
            break
    if flag == 0:
        print("string", s, "not found")
    else:
        print('String', s, 'Found In Line', index)
FileAndString()