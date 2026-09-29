stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 120,
    "MSFT": 300,
    "AMZN": 185,
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = quantity * price

        print(f"{stock}: {quantity} shares × ${price} = ${investment}")

        total_investment += investment

    except ValueError:
        print("Please enter a valid number.")

print("\nHere the Portfolio Summary")
print(f"Total Investment: ${total_investment}")


with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write(f"Total Investment: ${total_investment}\n")
print("Result saved to portfolio.txt")