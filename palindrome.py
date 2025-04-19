n = int(input("Enter the number: "))  
rev = 0
org = n
while n > 0:
    t = n % 10                
    rev = rev*10 + t
    n = n // 10               
if org == rev:
    print("Palindrome")             
else:
    print("Not Palidrome")
