print("💰 Simple Currency Converter 💰\n")

# Exchange rates relative to 1 USD
exchange_rates = {
    'USD': 1,       # 1 USD = 1 USD
    'PKR': 280,     # 1 USD = 280 PKR
    'EUR': 0.92,    # 1 USD = 0.92 EUR
    'GBP': 0.80,    # 1 USD = 0.80 GBP
    'INR': 83       # 1 USD = 83 INR
}

print("Available currencies:", ', '.join(exchange_rates.keys()))

# Input from user
from_currency = input("Convert from (currency code, e.g., PKR): ").upper()
to_currency = input("Convert to (currency code, e.g., USD): ").upper()

if from_currency not in exchange_rates or to_currency not in exchange_rates:
    print("❌ Sorry, one of the currencies is not supported.")
else:
    amount = input(f"Enter the amount in {from_currency}: ")
    
    if amount.replace('.', '', 1).isdigit():  # check if valid number
        amount = float(amount)
        # Convert to USD first
        amount_in_usd = amount / exchange_rates[from_currency]
        # Then convert USD to target currency
        converted_amount = amount_in_usd * exchange_rates[to_currency]
        print(f"\n💱 {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("❌ Invalid amount entered. Please enter a number.")
