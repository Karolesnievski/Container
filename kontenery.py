# 1
"""stworzono kontener z kolorami"""
colors = ["nebieski", "szary", "czerwony"]
"""guess ma być zmienną do użytku w funkcji if """
guess = input("zgadnij kolor ")
"""stosujemy in, aby sprawdzić zwartość w tablicy """
if guess in colors:
    print("zgadłeś!")
else: 
    print("niestety :C, spórbuj jeszcze raz !")

# 2 Krotki
rhymes = {
    "1": "niebem",
    "2": "kwas kwas",
    "3": "śnić",
    "4": "odjazd",
}

n = input("Wpisz cyfrę: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Nie znaleziono"
    )