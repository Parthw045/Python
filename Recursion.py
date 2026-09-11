#to print sum first n no.
n = int(input("Enter n :"))
result =0
def sum(n):
    if n<=0 :
        break
result = result + n
sum(n-1)

