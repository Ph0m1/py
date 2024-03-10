def swap(c1,c2):
    nc1 = c1.lower()
    nc2 = c2.upper()
    return nc1,nc2
c1,c2=input().split()
nc1,nc2=swap(c1,c2)
print(nc1+','+nc2)