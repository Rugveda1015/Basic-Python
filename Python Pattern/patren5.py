n = int(input("Enter the number for pattern"))
k = 2*n -2
for i in range(n,0,-1):
    for j in range(0,k): 
        print(end="\n")
        
    k = k-1
    
    for j in range(0,i-1):
        
        print("7", end =" ")
    print("\n")
