tableau = [5, 2,54, 8, 1,13,23,45, 9]
taille = len(tableau)
trouve=True
while trouve :
    trouve=False
    for i in range(taille-1):
        if tableau[i] > tableau[i+1]:
            
            tableau[i], tableau[i+1] =tableau[i+1],tableau[i]
            trouve=True

print("mon tableau trier est :",tableau)