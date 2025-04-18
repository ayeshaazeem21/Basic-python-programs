n = int(input("Enter the number: "))  
rev = 0
org = n
while n > 0:
    t = n % 10                
    rev = rev + t * 3
    n = n // 10               
if org == rev:
    print("Equal")             
else:
    print("Not equal")
