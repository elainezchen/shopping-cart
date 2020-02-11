# shopping_cart.py

from pprint import pprint
from datetime import datetime
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# creating a variable to establish the current date and time
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


# TODO: write some Python code here to produce the desired output

total_price = 0
tax = 0
shopping_list = []

# ensures the user inputs the correct product identifiers
while True:
    x = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if (x.lower() == "done"):
        break
    elif ([p for p in products if str(p["id"]) == str(x)]):
        shopping_list.append(int(x))
    else:
        print("Are you sure that product identifier was correct? Please try again!")

# prints receipt with a list of all products purchased and the total prices
print("---------------------------------\nTRADER CHEN'S\nWWW.TRADER-CHEN'S-GROCERY.COM\n---------------------------------")
print("CHECKOUT AT: " + dt)
print("---------------------------------\nSELECTED PRODUCTS:")

receipt_list = []

# locates the associated name and price of the products 
for x in shopping_list:
    matching_products = [p for p in products if str(p["id"]) == str(x)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    price_usd = " (${0:.2f})".format(matching_product["price"])
    print(" + " + matching_product["name"] + str(price_usd))
    receipt_list.append(matching_product["name"])
 
# calculates subtotal before tax
print("---------------------------------")
print("SUBTOTAL: " + str(("${0:.2f}").format(total_price)))

# calculates tax
tax = total_price*0.0875
print("SALES TAX (8.75%): " + str(("${0:.2f}").format(tax)))

# calculates total price (including tax)
grand_total = total_price + tax
print("TOTAL: " + str(("${0:.2f}").format(grand_total)))
print("---------------------------------\nTHANKS, SEE YOU AGAIN!\n---------------------------------")

# email receipt

while True:
    checkout = input("\nWould the customer like to receive the receipt by email? [Y/N] ")
    if (checkout.lower() == "y"):
        email = input("What is the customer's email address? ")

        load_dotenv()

        SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")

        client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
        print("CLIENT:", type(client))

        subject = "Your Receipt from Trader Chen's Grocery"

        html_subtotal=("${0:.2f}").format(total_price)
        html_tax=("${0:.2f}").format(tax)
        html_grand_total=("${0:.2f}").format(grand_total)
        html_content = f"""
        <h3>Trader Chen's Grocery</h3>
        <strong>Hello, this is your receipt.</strong>
        <p>Date and time of checkout: {dt} </p>
        You ordered:
        <ol>
            {receipt_list}
        </ol>
        <p>Subtotal: {html_subtotal}</p>
        <p>Tax: {html_tax} </p>
        <p>Total: {html_grand_total}</p>
        <p>Thank you for shopping at Trader Chen's! See you again!</p>
        """

        print("HTML:", html_content)

        message = Mail(from_email=email, to_emails=email, subject=subject, html_content=html_content)

        try:
            response = client.send(message)

            print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
            print(response.status_code) #> 202 indicates SUCCESS
            print(response.body)
            print(response.headers)

        except Exception as e:
            print("OOPS", e.message)

        print("The receipt has been sent to the customer's email.\nThank you for shopping at Trader Chen's!\n")
        exit()

    elif(checkout.lower() == "n"):
        print("\nThank you for shopping at Trader Chen's!\n")
        exit()
        
    else:
        print("\nPlease enter a valid input.")




