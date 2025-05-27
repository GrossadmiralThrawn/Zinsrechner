# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculate_interest(years, interest_rate, saving_rate):
    actual_saldo = saving_rate * 12
    interest_pa = (interest_rate - 1) * 100

    for year in range(1, int(years) + 1):
        actual_saldo = (actual_saldo + saving_rate * 12) * interest_rate
        print(f"Jahr {year}: {saving_rate} €/Monat gespart, {interest_pa:.2f} % Zins, Gesamtsaldo: {actual_saldo:.2f}€")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hallo, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_Years = int(input("Wie viele Jahre soll der Zins berechnet werden? \n"))
    input_interestRate = int(input("Wie hoch ist der Zins in Prozent? \n"))
    input_savingRate = int(input("Wie viel Geld soll pro Monat in € gespart werden? \n"))

    print_hi('Nutzer')

    calculate_interest(input_Years, 1 + input_interestRate / 100, input_savingRate)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#76669.50€
#95836.87€
