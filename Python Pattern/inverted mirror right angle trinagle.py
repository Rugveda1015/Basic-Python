#code for inverted mirror right angle triangle
n=int(input("Enter the value for the pattern\n"))
#in a bove step we are taking the value from user for input, and we are writing (\n) for the 
#next line.
k = 2 * n - 2
#in this step we initialization of the k
for i in range(n,0,-1): 
    #in this step we are using the for loop for the no. 0 to n 
    for j in range(0,k): 
        #in this step we are using the nested for loop for the j
        print(end=" ")
        #here we using the print for the space
    k = k + 2
        # here we are initialization k
    for j in range(0,i-1):
            #here again we are using the nested for loop for the j 
        print(j,end= " ")
    print("\n")

