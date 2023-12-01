from forex_python.converter import *
import json

# demander quelle devise ? # montrer liste des différentes devises
# montrer liste des autres devises possible ? (taux de change ou pas)
# demander en quelle devise ils veulent convertir 
# Quel montant ils veulent convertir 

c = CurrencyRates()
history= []


def convert_currency(amount, from_currency, to_currency):
    try:
        if from_currency in get_favorite_currencies():
            # get_favorite_currencies = from_currency
            print(f"Utilisation de la devise préférée: {from_currency}")
        else:
            print(f"La devise {from_currency} n'est pas une devise préférée.")

        rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        conversion_result = {
            'amount': amount,
            'from_currency': from_currency,
            'to_currency': to_currency,
            'converted_amount': converted_amount
        }
        history.append(conversion_result)
        return converted_amount
    except:
        print("La conversion est impossible. Veuillez vérifier les devises fournies.")
        return None


def add_currency(currency, rate):
    new_currency = {'currency': currency, 'rate': rate}
    
    try:
        with open('new_currencies.json', 'r') as file:
            currencies = json.load(file)
    except FileNotFoundError:
        currencies = []

    currencies.append(new_currency)

    with open('new_currencies.json', 'w') as file:
        json.dump(currencies, file)

    return currencies

    


def add_favorite_currency(currency):

    favorites = get_favorite_currencies()
    favorites.append(currency)
    with open('favorite_currencies.json', 'w') as file:
        json.dump(favorites, file)

def get_favorite_currencies():
    try:
        with open('favorite_currencies.json', 'r') as file:
            favorites = json.load(file)
        return favorites
    except FileNotFoundError:
        return []
    



def print_conversion_history():
    print("Historique des conversions:")
    for entry in history:
        print(f"{entry['amount']} {entry['from_currency']} => {entry['converted_amount']} {entry['to_currency']}")

def main():
    while True:
        print("Voici la liste des différentes devises disponibles:","\n" *2 ,*c.get_rates(''),"\n")
        
        print("\nMenu:")
        print("1. Convertir une somme")
        print("2. Ajouter une devise")
        print("3. Ajouter une devise préférée")
        print("4. Afficher mes devises préférées")
        print("5. Afficher l'historique des conversions")
        print("6. Quitter")

        choice = input("Choisissez une option (1-6): ")

        if choice == '1':
            amount = float(input("Entrez le montant à convertir : "))
            from_currency = input("Entrez la devise d'origine: ")

            use_favorite = input("Voulez-vous utiliser une devise préférée ? (Oui/Non): ").lower()
            if use_favorite == 'oui':
                favorite_currencies_list = get_favorite_currencies()
                if favorite_currencies_list:
                    print("Devises préférées disponibles:", favorite_currencies_list)
                    to_currency = input("Choisissez la devise de destination parmi les devises préférées : ")
                    # marche pas :(, prend que le premier index
                else:
                    print("Aucune devise préférée disponible. Veuillez en ajouter d'abord.")
                    continue
            else:
                to_currency = input("Entrez la devise de destination: ")

            converted_amount = convert_currency(amount, from_currency, to_currency)
            if converted_amount is not None:
                print(f"{amount} {from_currency} équivaut à {converted_amount} {to_currency}")


        elif choice == '2':
            currency = input("Entrez le code de la nouvelle devise : ")
            rate = float(input(f"Entrez le taux de conversion de votre devise {currency} : "))
            add_currency(currency, rate)
            print(f"{currency} a été ajouté avec succès.")
            new_favorite = input("Voulez-vous ajouter la nouvelle devise à vos devises préférées ?(Oui/Non)").lower() 
            if new_favorite == 'oui':
                add_favorite_currency(add_currency)
                print(f"{currency} a été ajouté à vos favories.")
                # marche pas :(

        elif choice == '3':
            currency = input("Entrez le code de la devise préférée à ajouter : ")
            add_favorite_currency(currency)
            print(f"{currency} a été ajouté aux devises préférées.")

        elif choice == '4':
            print(*get_favorite_currencies())

        elif choice == '5':
            print_conversion_history()

        elif choice == '6':
            print("Au revoir!")
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")
main()