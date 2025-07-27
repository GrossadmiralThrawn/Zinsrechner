def calculate_interest(years, interest_rate, saving_rate):
    actual_saldo = 0
    interest_pa = (interest_rate - 1) * 100

    for year in range(1, int(years) + 1):
        actual_saldo = (actual_saldo + saving_rate * 12) * interest_rate
        print(f"Jahr {year}: {saving_rate} €/Monat gespart, {interest_pa:.2f} % Zins, Gesamtsaldo: {actual_saldo:.2f}€")


def calculate_interest_one_time(years, interest_rate, one_time_amount):
    actual_saldo = one_time_amount
    for year in range(1, int(years) + 1):
        actual_saldo *= interest_rate
        print(f"Jahr {year}: Einmalig {one_time_amount} € angelegt, {interest_rate * 100 - 100:.2f} % Zins, "
              f"Gesamtsaldo: {actual_saldo:.2f}€")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hallo, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Nutzer')

    while True:
        input_Years = int(input("Wie viele Jahre soll der Zins berechnet werden? \n"))
        input_interestRate = int(input("Wie hoch ist der Zins in Prozent? \n"))
        input_rate_or_one_time = input("Soll nur einmal oder mehrfach Geld eingezahlt werden? e/m\n")

        if input_rate_or_one_time == "e":
            input_savingRate = int(input("Wie viel Geld soll gezahlt werden? \n"))
            calculate_interest_one_time(input_Years, 1 + input_interestRate / 100, input_savingRate)
        else:
            input_savingRate = int(input("Wie viel Geld soll pro Monat in € gespart werden? \n"))
            calculate_interest(input_Years, 1 + input_interestRate / 100, input_savingRate)

        print("------------------------------------------------------------------")

        print("Willst du eine weitere Variante berechnen?")
        response = input("ja/nein \n").lower().strip()

        if (response == "ja" or response == "Ja" or
                response == "JA" or response == "j" or response == "y" or response == "yes"):
            continue
        else:
            break

