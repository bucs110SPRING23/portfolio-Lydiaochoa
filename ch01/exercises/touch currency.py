amount = input("input the amount")
amount = float(amount)
rate = input("Enter the exchange rate")
rate = float(rate)
new_amount = amount * rate 
minus_fees = (new_amount - 3)
print("your result minus a convinience fee",minus_fees)

