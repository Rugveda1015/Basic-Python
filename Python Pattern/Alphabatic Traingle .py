n = int(input("enter the number\n"))
k = 2*n -2

if n >65: 
    for i in range(65,n): 
        
        for j in range(65,k):
            print(end=" ")
        k = k-2
        for j in range(0,i+1): 
            print(str(j), end =" ")  
        print("\r")
    

else:
    print("enter the num ber greater than 67\n")
    