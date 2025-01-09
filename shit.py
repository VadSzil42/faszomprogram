def isSzokoev(ev:int):
    if ev % 4 == 0:
        return True
    else:
        return False
    
ev_i = input("ev: ")
match isSzokoev(ev_i):
    case True:
        print("{0} szokoev.".format(ev_i))

    case False:
        print("{0} nem szokoev.".format(ev_i))