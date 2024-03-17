# cafe.py - Task 7 - Practical Task 2

# list - menu 4 items
# dic - stock - stock value for the 4 items
# dic - price - price 4 items
# calc total_stock value of stock

# define the stock
menu = {"Lasigne","Pizza","Burger","Toastie"}
stock = {"Lasigne": 6,
         "Pizza": 6,
         "Burger": 5,
         "Toastie": 3
        }
price = {"Lasigne": 8.99,
         "Pizza": 12.99,
         "Burger": 8.99,
         "Toastie": 6.99
        }

# function to go through the list/dict's to do the calculations
def total_stock(menu, stock, price):
 
    # do the maths 
    total_stock = sum(stock[item] * price [item] for item in menu)
    return(total_stock)

# run the function
total_stock(menu, stock, price)
# output the results
print(f"Your total stock is worth £{total_stock(menu,stock,price)}")