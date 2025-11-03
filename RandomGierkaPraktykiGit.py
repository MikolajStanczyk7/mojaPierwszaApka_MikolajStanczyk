import random

print("Witaj w grze 'Zgadnij liczbę'!")
liczba = random.randint(1, 100)
proba = 0
pokazano = False

while True:
    proba += 1
    strzal = input("Podaj liczbę od 1 do 100: ")
    try:
        strzal = int(strzal)
    except ValueError:
        print("To nie jest liczba! Spróbuj jeszcze raz.")
        continue

    if strzal < liczba:
        print("Za mało!")
    elif strzal > liczba:
        print("Za dużo!")
    else:
        if proba == 1:
            print("Jesteś super! Powinieneś zostać snajperem!")
        else:
            print(f"Brawo! Odgadłeś liczbę w {proba} próbach.")
        break

    if proba == 3 and not pokazano:
        decyzja = input("Czy chcesz zobaczyć wylosowaną liczbę? (t/n): ").lower()
        if decyzja == 't':
            print(f"Wylosowana liczba to: {liczba}")
        pokazano = True

#komentarz od kolaboranta

#komentarzzzzzzzzzzzzzzzzzzzzzz