def isSzokoev(ev:int)
    if ev % 4 == 0:
        return True
    else:
        return False
    
ev_i = input("Év: ")
match isSzokoev(ev_i):
    case True:
        print("{0} szökőév.".format(ev_i))

    case False:
        print("{0} nem szökőév.".format(ev_i))