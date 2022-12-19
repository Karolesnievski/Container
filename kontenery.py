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
