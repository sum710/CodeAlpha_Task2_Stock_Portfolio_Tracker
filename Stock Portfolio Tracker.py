# Hardcoded stock prices
stock_price={
    "AAPL":110,
    "TSLA":250,
    "GOOG":2800,
    "MSFT":280
}
#Dictionary to store stock and quantity
portfolio={}
while True:
    stock=input("Enter stock symbol or Done to finish:  ").upper()
    if stock=='DONE':
        break
    quantity=int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    
# Display the portfolio
total_investment=0
for stock, quantity in portfolio.items():
    if stock in stock_price:
        total_investment+=stock_price[stock]*quantity
    else:
        print(f"Stock {stock} not found in stock prices.")        
print(f"Total Investment in Portfolio: $ {total_investment:.2f}")   
save=input("Do you want to save the portfolio? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment in Portfolio: $ {total_investment:.2f}\n")
        file.write("Portfolio details:\n")
        for stock, quantity in portfolio.items():
            file.write(f"{stock}: {quantity}\n")
            file.write(f"Value: $ {stock_price.get(stock, 0) * quantity:.2f}\n")
# Read and display the saved portfolio
if save == 'yes':
    with open("portfolio.txt", "r") as file:
     print(file.read())