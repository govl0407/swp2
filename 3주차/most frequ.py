def solution(lst):
    ls = set(lst)
    l = list(ls)
    z = []
    m=[]
    n=[]
    for i in range(len(l)):
        z.append(0)
    for i in range(len(l)):
        for j in range(len(lst)):
            if l[i] == lst[j]:
                z[i]= z[i]+1
    
    k=sorted(z)
    k.reverse()
    """
    print("lst ="+str(lst))
    print("l ="+str(l))
    print("z ="+str(z))
    print("k = " +str(k))
    """
    for i in range(len(z)):
        if z[i] == k[0]:
            m.append(i)
    #print("m ="+str(m))
    for i in m:
        n.append(l[i])
    n.sort()
    return n    
        
   
    
        

print(solution([1, 2, 3, 4, 5, 5])) 
print(solution([12, 17, 19, 17, 23])) 
print(solution([26, 37, 26, 37, 91])) 
print(solution([28, 30, 32, 34, 144])) 
