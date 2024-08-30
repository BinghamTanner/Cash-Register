from enum import Enum
import inventory
from payment import Payment, PayType

def payment_prompt():
    p_prompt = """Payment Type: 
    1: CASH
    2: CARD
    3: PHONE"""

    print()
    print(p_prompt)
    print() 
    
    try: 
        pay_in = int(input("Enter payment method: "))        
        if pay_in == 1:
            return PayType.CASH.name
        if pay_in == 2:
            return PayType.CARD.name
        elif pay_in == 3:
            return PayType.PHONE.name
        
        else: 
            print("Enter one of the payment types. ")
            return 
            
    except ValueError:
            print("Enter one of the payment types. ")
            return 


def user_prompt_candy():
    try:
        cand_in = str(input("Enter the type of candy: "))
        quant_in = float(input("Enter the quantity purchased(per pound): "))
        price_in = float(input("Enter the price per pound: "))

    except ValueError:
        print("Hey, not cool!")
        return
    

    candy_order = inventory.Candy(cand_in, quant_in, price_in)

    return candy_order


def user_prompt_cookie():
    try:
        cook_in = str(input("Enter the type of cookie: "))
        quant_in = float(input("Enter the number of cookies purchased: "))
        price_in = float(input("Enter the price per dozen: "))

    except ValueError:
        print("Hey, not cool!")
        return
    

    cookie_order = inventory.Cookie(cook_in, quant_in, price_in)
    return cookie_order 
    

def user_prompt_icecream():
    try:
        ice_in = str(input("Enter the type of icecream: "))
        quant_in = float(input("Enter the number of scoops: "))
        price_in = float(input("Enter the price per scoop: "))

    except ValueError:
        print("Hey, not cool!")
        return
    

    icecream_order = inventory.IceCream(ice_in, quant_in, price_in)
    return icecream_order 


def user_prompt_sundae():
    try:
        sun_in = str(input("Enter the type of icecream: "))
        quant_in = float(input("Enter the number of scoops: "))
        price_in = float(input("Enter the price per scoop: "))
        topping_in = str(input("Enter the topping: "))
        topp_price_in = float(input("Enter the price for the toppng: "))

    except ValueError:
        print("Hey, not cool!")
        return


    sundae_order = inventory.Sundae(sun_in, quant_in, price_in, topping_in, topp_price_in) 
    return sundae_order 


def main_menu(): 
    ordenar = inventory.Order() 
    menu = '''MENU:
    1. Candy
    2. Cookies
    3. Ice Cream
    4. Sundae'''
    print()
    print(menu)
    print() 
    try: 
        
        user_in = input("What would you like to add to the order?(1-4, Enter for done): ")
        if user_in == '':
            

            return False
            
        user_in = int(user_in)
        
        if user_in < 1 or user_in > 4:
            print("Enter number between 1 and 4.")
            return 
            
    except ValueError:
            print("Enter number between 1 and 4.")
            return 
        
    if user_in == 1:
        return user_prompt_candy()
    elif user_in == 2:
        return user_prompt_cookie()
    elif user_in == 3:
        return user_prompt_icecream()
    elif user_in == 4:
        return user_prompt_sundae()
    else:
        pass
    
    
def main():
    
    ordenar = inventory.Order()   

    while ordenar.add(main_menu()):
        pass

    ordenar.pay_method = payment_prompt() 
    
    
        

    print("-----------------------RECEIPT-----------------------------")
    ordenar.in_order.sort()
    for i in range(len(ordenar.in_order)):
        print(ordenar.in_order[i])
    print("-----------------------------------------------------------")
    print(ordenar)   
    
    

main()
