def lnko(a:int,b:int):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

def lkkt(a,b):
    o=lnko(a,b)
    return a*b//o

a = int(input("Adj egy szamot: "))
b = int(input("Adj meg egy szamot: "))
print(lnko(a, b))