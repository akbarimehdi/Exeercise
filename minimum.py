# Ce programme permet de déterminer lequel de deux nombres flottants entrés
# par l’utilisatrice ou l’utilisateur est le plus petit

# akbarimehdi 20210926


_val1=int(input("Veuillez entrer le premier nombre: "));
_val2=int(input("Veuillez entrer le second nombre: "));
if(_val1>_val2):
    print("Le plus petit nombre est ",_val2);
elif(_val2>_val1):
    print("Le plus petit nombre est ",_val1);
else:
    print("Les nombres sont egaux");
