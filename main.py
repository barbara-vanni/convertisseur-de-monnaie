from forex_python.converter import *

# demander quelle devise ? # montrer liste des différentes devises
# montrer liste des autres devises possible ? (taux de change ou pas)
# demander en quelle devise ils veulent convertir 
# Quel montant ils veulent convertir 

c = CurrencyRates()

def devise_actuelle():
    pass

def main():
    while True:
        print("Voici la liste des différentes devises disponibles:","\n" *2 ,*c.get_rates(''),"\n")
        
        devise_actuel = str(input("Entrez votre devise actuelle: "))
        devise_voulue = str(input("Entrez la devise que vous voulez: "))
        amount = float(input("Quel montant voulez-vous convertir ? : "))
        break
main()