# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish.\n")

# Input loop
while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available.\n")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    portfolio[stock_name] = quantity
    print(f"✅ Added {stock_name} worth ${investment}\n")

# Display result
print("\n📌 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock} → {qty} shares × ${price} = ${qty * price}")

print("\n💰 Total Investment Value: $", total_investment)

# Optional: Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            file.write(f"{stock},{qty},{price},{qty * price}\n")
        file.write(f"Total Investment: ${total_investment}")

    print("📁 Portfolio saved to portfolio.txt")
