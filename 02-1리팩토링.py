
score = int(input("enter score: "))
k = [[100,"A"],[90,"A"],[80,"B"],[70,"C"]]
n = 0
if not 0<=score<=100:
    print("wrong input")
else: 
    for i in k:
        if i[0] <= score < i[0]+10:
            print("Your score is ", score, ", Grade is ",i[1])
            n = 1
    if n==0:
        print("Your score is ", score, ", Grade is F")

