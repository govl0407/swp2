import time
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    seq = [1,1]
    if n<= 1:
        return n
    
    else :
        for i in range(2,n):
            seq.append(seq[i-1] + seq[i-2])
        return seq[len(seq)-1]
    

    
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break

    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

