# shopping_cart.py

from pprint import pprint
from datetime import datetime

d = datetime.now()
dt = d.strftime("%m/%d/%Y %H:%M")

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

# capturing user inputs
# input function, while loop (store as long as user does not input DONE), exit() function if user inputs DONE, store (add) in list and
# print list

total_price = 0
tax = 0
shopping_list = []

#x = "0" #idk if this is right
while True:
    x = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if (x.lower() == "done"):
        break
    elif (int(x) < 1 or int(x) > 20):
        print("That is not a valid item identifier.")
    else:
        shopping_list.append(int(x))

#shopping_list = [p for p in products if str(p["id"]) == str(x)]



#print(matching_products)

#how to get it to add the price and name
#def search_item(any_product):
    #return any_product["name"]

#for j in matching_products:
    #price_usd = " (${0:.2f})".format(j["price"])
    #print(" + " + j["name"] + price_usd)


# receipt
print("---------------------------------\nTRADER CHEN'S\nWWW.TRADER-CHEN'S-GROCERY.COM\n---------------------------------")
print("CHECKOUT AT: " + dt)
print("---------------------------------\nSELECTED PRODUCTS:")

for x in shopping_list:
    matching_products = [p for p in products if str(p["id"]) == str(x)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    price_usd = " (${0:.2f})".format(matching_product["price"])
    print(" + " + matching_product["name"] + str(price_usd))
 
print("---------------------------------")
print("SUBTOTAL: " + str(("${0:.2f}").format(total_price)))

tax = total_price*0.0875

print("TAX: " + str(("${0:.2f}").format(tax)))

grand_total = total_price + tax

print("TOTAL: " + str(("${0:.2f}").format(grand_total)))
print("---------------------------------\nTHANKS, SEE YOU AGAIN SOON!\n---------------------------------")
