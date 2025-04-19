n = int(input("Enter the number: "))  
rev = 0
org = n
while n > 0:
    t = n % 10                
    rev = rev + t * 3
    n = n // 10               
if org == rev:
    print("It is an Armstrong number")             
else:
    print("It is not an Armstrong number")
