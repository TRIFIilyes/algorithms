def mintab(tab, n):
    if n == 1 : 
        return tab[n-1]
    else: 
        return min(tab[n-1],mintab(tab,n-1))
    

tab = [-214122,3,4,5,-11]
n = len(tab)
print(mintab(tab,n))
