N,M = input("Enetr the value of N and 3 times the Value of M to that of N:").split()
N =int(N)
M =int(M)
lineprint = (M - 3)//2
belowprint = 3
for i in range(N//2):
    for j in range(0,lineprint):
        print("-",end="")
    for k in range(0,2*(i+1)-1):
        print(".|.",end="")
    for l in range(0,lineprint):
        print("-",end="")
    print()    
    lineprint = lineprint - 3
for m in range(0,(M-7)//2):
    print("-",end="")
print("WELCOME",end="")
for o in range(0,(M-7)//2):
    print("-",end="")
print()
for a in range(N//2,0,-1):
    for b in range(0,belowprint):
        print("-",end="")
    for c in range(0,2*(a)-1):
        print(".|.",end="")
    for d in range(0,belowprint):
        print("-",end="")
    print()    
    belowprint = belowprint + 3
