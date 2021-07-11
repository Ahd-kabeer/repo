
def FileAndString(fname,s):
    with open(fname,"r") as F:
        for line in F.readlines():
            if s in line:
                print('String', s, 'Found In Line', line)
                return True
                
            else:
                print("string", s, "not found")
                return False
                
    




    
FileAndString("repo/fname.txt",'goal')