import requests

def get_exchange_rates(base_currency):
    api_url = f"https://api.exchangeratesapi.io/latest?base={base_currency}"
    response = requests.get(api_url)
    data = response.json()

    if 'rates' in data:
        return data['rates']
    else:
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == 'EUR':
        from_rate = 1
    else:
        from_rate = rates[from_currency]

    if to_currency == 'EUR':
        to_rate = 1
    else:
        to_rate = 1 / rates[to_currency]

    converted_amount = amount * (from_rate / to_rate)
    return converted_amount

def main():
    base_currency = input("Enter the base currency (e.g., USD, EUR, GBP): ").upper()
    rates = get_exchange_rates(base_currency)

    if rates is None:
        print("Failed to retrieve exchange rates.")
        return

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency, rates)
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()