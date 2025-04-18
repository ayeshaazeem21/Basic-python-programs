n=int(input("num:"))
print("Divisors are:",end=" ")
s=0
for i in range(1,n):
    if n%i==0:
        print(i,end=" ")
        s=s+i

