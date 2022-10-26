mini = 0
def min(index, taille,tab,mini):
    if index == 0 : 
        mini = tab[0]
        return min(1,taille,tab,mini)
    else:
        if index == taille :
            return mini
        else:
            if tab[index] <= mini:
                mini = tab[index]
                return min(index+1,taille, tab,mini)
            else: 
                return min(index+1,taille,tab,mini)


tab = [2,3,4,0,12,12,13,123,21,-1,12,3,-44,90909]
print(min(0,len(tab),tab,mini))
