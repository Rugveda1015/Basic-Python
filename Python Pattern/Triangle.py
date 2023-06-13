n = int(input("enter the number\n"))
k = 2*n -2 

for i in range(65,n): 
        for j in range(65,k):
            print(end=" ")
        k = k-1
        for j in range(65,i+1): 
            print(chr(j), end =" ")  
        
        print(" ")
    