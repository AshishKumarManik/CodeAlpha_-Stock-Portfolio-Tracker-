from stock_data import stock_prices

user_portfolio = {}

print("Enter your stock holdings (type 'done' to finish):")
while True:
    stock = input("Stock symbol: ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in the price list. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        user_portfolio[stock] = user_portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number for quantity.")

total_investment = 0
print("\nYour Portfolio Summary:")
for stock, quantity in user_portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

save_option = input("Do you want to save the result? (yes/no): ").lower()
if save_option == 'yes':
    filename = input("Enter filename (with .txt or .csv extension): ")
    with open(filename, 'w') as file:
        file.write("Stock,Quantity,Price,Investment\n")
        for stock, quantity in user_portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock},{quantity},{price},{investment}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(f"Data saved to {filename}")
