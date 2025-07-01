#My name is Jacob Baker and this is Chapter 6 Lab 1 and I am completing this on June 30
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
sales = []

for day in days:
    amount = float(input(f"Enter the sales amount for {day}       : "))
    sales.append (amount)
total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sales = max(sales)
highest_day = max(days)
lowest_sales = min(sales)
lowest_day =min(days)

print(f"Total weekly sales     : ${total_sales:.2f}") 
print (f"Average weekly sales  : ${average_sales:.2f}")
print (f"The highest sales were ${highest_sales:.2f} on {highest_day}")
print (f"The lowest sales were ${lowest_sales:.2f} on {lowest_day}")
