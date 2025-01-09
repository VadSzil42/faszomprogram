def isSzokoev(ev:int):
    if ev % 4 != 0:
        return False
    elif ev % 400 == 0:
        return True
    elif ev % 100 == 0:
        return False
    else:
        return True
    
ev_i = int(input("ev: "))
if isSzokoev(ev_i):
    print(ev_i, "szokoev.")
else:
    print(ev_i, "nem szokoev.")