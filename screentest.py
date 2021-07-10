#answer 1

def LEL(n = []):
    print("largest  elements in the list is:-  "+ str(max(n)) )

LEL(n = [21,45,99,78,56])

# answer 2
def LtEL(n=[]):
    L1 = max(n)
    list1 = n
    list1.remove(max(list1))
    L2 = max(list1)

    print("largest 2 elements in the list are: "+str(L1)+" and "+str(L2))


LtEL(n=[21,45,99,78,56])

#answer 3

def Nmaxelements(M, N):
    final_list = []
  
    for i in range(0, N): 
        max1 = 0
          
        for j in range(len(M)):     
            if M[j] > max1:
                max1 = M[j]
                  
        M.remove(max1)
        final_list.append(max1)
          
    print(final_list)
  
# Driver code
M = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

# Calling the function
Nmaxelements(M, N)

