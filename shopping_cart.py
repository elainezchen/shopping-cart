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


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 1000.2342
    Example: to_usd(1000.2342)
    Returns: $1,000.23
    """
    return "${0:,.2f}".format(my_price)

def find_product(products):
    """
    Returns a dictionary containing products that have matching ids to the ones the user inputted.
    Param: products (dictionary)
    """
    return [p for p in products if str(p["id"]) == str(x)]

def find_tax(total_price):
    """
    Returns a float that multiplies the price with a predetermined tax rate.
    Param: total_price (int or float) like 10.882
    Example: find_tax(10.882)
    Returns: 0.952175
    """
    return total_price*0.0875

def find_total(total_price, tax):
    """
    Returns a float or int that finds the total price of some items including tax.
    Param: total_price (int or float) like 10.882, tax (float) like 0.952175
    Example: find_tax(10.882, 0.952175)
    Returns: 11.834175
    """
    return total_price + tax

if __name__ == "__main__":
        
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

    def print_message(message):
        """
        Returns a string value with a line of dashes on top.
        Param: message (string) like "hello"
        Example: message("hello")
        Returns:
        -------------------------
        hello
        """
        print("-------------------------")
        print(message)

    # prints receipt with a list of all products purchased and the total prices
    print_message("TRADER CHEN'S\nWWW.TRADER-CHEN'S-GROCERY.COM")
    print_message("CHECKOUT AT: " + dt)
    print_message("SELECTED PRODUCTS:")

    receipt_list = []

    # locates the associated name and price of the products 
    for x in shopping_list:
        matching_products = find_product(products)
        matching_product = matching_products[0]
        total_price = total_price + matching_product["price"]
        price_usd = to_usd(matching_product["price"])
        print(" + " + matching_product["name"] + " " + str(price_usd))
        receipt_list.append(matching_product["name"])
    
    # calculates subtotal before tax
    print_message("SUBTOTAL: " + to_usd(total_price))

    # calculates tax
    tax = find_tax(total_price)
    print("SALES TAX (8.75%): " + to_usd(tax))

    # calculates total price (including tax)
    grand_total = find_total(total_price, tax)
    print("TOTAL: " + to_usd(grand_total))
    print_message("THANKS, SEE YOU AGAIN!\n-------------------------")

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
            html_content = f"""
            <h3>Trader Chen's Grocery</h3>
            <strong>Hello, this is your receipt.</strong>
            <p>Date and time of checkout: {dt} </p>
            You ordered:
            <ol>
                {receipt_list}
            </ol>
            <p>Subtotal: {to_usd(total_price)}</p>
            <p>Tax: {to_usd(tax)} </p>
            <p>Total: {to_usd(grand_total)}</p>
            <p>Thank you for shopping at Trader Chen's! See you again!</p>
            """

            print("HTML:", html_content)
            message = Mail(from_email=email, to_emails=email, subject=subject, html_content=html_content)

            try:
                response = client.send(message)
                print(response.status_code) #> 202 indicates SUCCESS
            except Exception as e:
                print("OOPS", e.message)

            print("The receipt has been sent to the customer's email.\nThank you for shopping at Trader Chen's!\n")
            exit()

        elif(checkout.lower() == "n"):
            print("\nThank you for shopping at Trader Chen's!\n")
            exit()
            
        else:
            print("\nPlease enter a valid input.")




