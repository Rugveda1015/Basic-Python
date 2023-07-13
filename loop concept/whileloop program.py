#Print i as long as i is less than 6:
i = 1
#we are taking the value of i as 1
while i < 6:
#we are using the while loop for printing the from 1 to 6    
  print(i)
  #we are printing the fnal value of the i
  i += 1
  #in this step we are incrementing the value of i by 1 and we can also write it as i=i+1

#Exit the loop when i is 3:  
  i = 1
  while i < 6:
    print(i)
    if i == 3:
        #here we are taking the another value value of i as 3 
      break
  #we are using the break just to stop the loop till 3
    i += 1
    #we are incrementing the value of i
    
#Continue to the next iteration if i is 3:
i = 0
#we are taking the value of i as 0
while i < 6:
    #we are using the while loop for printing the from 1 to 6 
  i += 1
  #we are incrementing the value of i
  if i == 3: 
      #here we are taking the another value value of i as 3 
    continue
#we taking continue to skip the another value of i complete the loop till 6
  print(i)
  #printing the value of i
  
  #Print a message once the condition is false:
  i = 1
  #we are taking the value of i as 1
  while i < 6:
 #we are using the while loop for printing the from 1 to 6       
    print(i)
    #printing the value of the i
    i += 1
    #incrementing the value of i
  else:
      #we are using the else condition to ensure that loop is getting completed
    print("i is no longer less than 6")
    #printing the statment after the else statment