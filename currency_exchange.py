# This is a currency converter program. A text file contains the daily exchange rate.
# It converts the value of a foreign currency into Hungarian forints.

# reading file and creating dictionary for data
with open("exchange.txt", 'r', encoding='utf-8') as txt:
    infile = txt.read().splitlines()
list = []
for line in infile:
    currency, currency_sign, rate = line.split("-")
    list.append(
        {"currency": currency, "currency_sign": currency_sign, "rate": float(rate)})

# selecting currency
print(f"Please select the desired currency from the list by entering its 3-letter code.")
for a in list:
    print(a["currency"], " - ", a["currency_sign"])


def find_sign():
    for line in list:
        if line["currency_sign"] == input_sign:
            return 1
        

while True:
    input_sign = input().upper()
    if find_sign() == 1:
        break
    else:
        print("\nThere is no such currency found. Please choose from the list.")


# giving the amount of money to be converted
for a in list:
    if a["currency_sign"] == input_sign:
        print(
            f"\nThe exchange rate for {a["currency"]} today is: 1 {a["currency_sign"]} = {a["rate"]} HUF")
        chos_amo = float(input(
            f"\nPlease give the amount of {a["currency"]} to be echanged to Hungarian Forints\n"))
        print(f"This is {round(chos_amo*a["rate"])} HUF.")
