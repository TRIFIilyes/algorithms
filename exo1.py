
# using a sorted array 
def find_mod_sorted():
    tab  = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,4,4,4,4,5,5,5,5,5]
    mod = tab[0]
    flag = tab[0]
    rep= 1 
    c = 1
    for i in range(0,len(tab)-1): 
        if tab[i] == flag :
            c +=1
        else:
            flag = tab[i]
            c = 1

        if c > rep :
            mod = tab[i]
            rep = c
        
    print(mod)
        
def find_mod_dict():
    pass 
def find_mod_nrml():
    pass
if __name__ == "__main__":
    print("using a sorted array : ")
    find_mod_sorted()
    print("using dictionary:")
    find_mod_dict()
    print("normal way : ")
    find_mod_nrml()

