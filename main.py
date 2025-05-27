# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def calculate_interest(years, interestRate, savingRate):
    actualSaldo = savingRate * 12
    interestPA  = (interestRate - 1) * 100


    for year in range(1, int(years)+1):
        actualSaldo = (actualSaldo + savingRate * 12) * interestRate
        print(f"Jahr {year}: {savingRate} €/Monat gespart, {interestPA:.2f} % Zins, Gesamtsaldo: {actualSaldo:.2f}€")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hallo, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    years = int(input("Wie viele Jahre soll der Zins berechnet werden? \n"))
    interestRate = int(input("Wie hoch ist der Zins in Prozent? \n"))
    savingRate = int(input("Wie viel Geld soll pro Monat in € gespart werden? \n"))


    print_hi('Nutzer')

    calculate_interest(years, 1+interestRate/100, savingRate)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#76669.50€
#95836.87€