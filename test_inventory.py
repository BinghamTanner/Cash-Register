# ds1 
from inventory import Candy, Cookie, IceCream, Sundae, Order, PayType



 
def test_dessi():
    
    dess = Candy()
    assert dess.name == ""
    assert dess.tax_percent == 7.25
    
    dess = Candy("tt")
    assert dess.name == "tt"
    assert dess.tax_percent == 7.25
    
    dess = Candy()
    dess.name = "rrr"
    assert dess.name == "rrr"
    dess.tax_percent = 3.00
    assert dess.tax_percent == 3.00
    
    dess = Candy("tt")
    dess.name = "llll"
    assert dess.name == "llll"
    dess.tax_percent = 3.00
    assert dess.tax_percent == 3.00
    
  
def test_cand():
    cand = Candy()
    assert cand.name == ""
    assert cand.candy_weight == 0.00
    assert cand.price_per_pound == 0.00
    assert cand.calculate_cost() == 0.00
    assert cand.calculate_tax() == 0.00
    assert cand.tax_percent == 7.25
    assert cand.packaging == "Bag"
    
    cand = Candy("skittles", 1.2, 3)
    assert cand.name == "skittles"
    assert cand.candy_weight == 1.2
    assert cand.price_per_pound == 3
    assert cand.calculate_cost() == 3.5999999999999996
    assert cand.calculate_tax() == 0.26099999999999995
    assert cand.tax_percent == 7.25
    assert cand.packaging == "Bag"
    
    cand = Candy()
    cand.name = "pie"
    assert cand.name == "pie"
    cand.candy_weight = 1.2
    assert cand.candy_weight == 1.2
    cand.price_per_pound = 3.00
    assert cand.price_per_pound == 3.00
    assert cand.calculate_cost() == 3.5999999999999996
    assert cand.calculate_tax() == 0.26099999999999995
    assert cand.tax_percent == 7.25
    cand.packaging = "skittles"
    assert cand.packaging == "skittles"
    
    cand = Candy("skittles", 1, 3)
    cand.name = "pie"
    assert cand.name == "pie"
    cand.candy_weight = 1.2
    assert cand.candy_weight == 1.2
    cand.price_per_pound = 3.00
    assert cand.price_per_pound == 3.00
    assert cand.calculate_cost() == 3.5999999999999996
    assert cand.calculate_tax() == 0.26099999999999995
    assert cand.tax_percent == 7.25
    cand.packaging = "smores"
    assert cand.packaging == "smores"
        
         
def test_cook():
    
    cook = Cookie()
    assert cook.name == ""
    assert cook.cookie_quantity == 0
    assert cook.price_per_dozen == 0.00
    assert cook.calculate_cost() == 0.00
    assert cook.calculate_tax() == 0.00
    assert cook.packaging == "Box"
        
    cook = Cookie("sugar", 1, 12)
    assert cook.name == "sugar"
    assert cook.cookie_quantity == 1
    assert cook.price_per_dozen == 12
    assert cook.calculate_cost() == 1.00
    assert cook.calculate_tax() == 0.0725
    assert cook.packaging == "Box"
        
    cook = Cookie()
    cook.name = "chocolate"
    assert cook.name == "chocolate"
    cook.cookie_quantity = 1
    assert cook.cookie_quantity == 1
    cook.price_per_dozen = 12
    assert cook.price_per_dozen == 12
    assert cook.calculate_cost() == 1.00
    assert cook.calculate_tax() == 0.0725
    cook.packaging = "boxy"
    assert cook.packaging == "boxy"
       
    cook = Cookie("sugar", 1, 12)
    cook.name = "chocolate"
    assert cook.name == "chocolate"
    cook.cookie_quantity = 1
    assert cook.cookie_quantity == 1
    cook.price_per_dozen = 12
    assert cook.price_per_dozen == 12
    assert cook.calculate_cost() == 1.00
    assert cook.calculate_tax() == 0.0725
    cook.packaging = "boxy"
    assert cook.packaging == "boxy"
       

def test_ice():
     
    ice = IceCream()
    assert ice.name == ""
    assert ice.scoop_count == 0
    assert ice.price_per_scoop == 0.00
    assert ice.calculate_cost() == 0.00
    assert ice.calculate_tax() == 0.00
    assert ice.packaging == "Bowl"
    
    ice = IceCream("vanilla", 3, 1.00)
    assert ice.name == "vanilla"
    assert ice.scoop_count == 3
    assert ice.price_per_scoop == 1.00
    assert ice.calculate_cost() == 3.00
    assert ice.calculate_tax() == 0.21749999999999997
    assert ice.packaging == "Bowl"
    
    ice = IceCream()
    ice.name = "rice"
    assert ice.name == "rice"
    ice.scoop_count = 4
    assert ice.scoop_count == 4
    ice.price_per_scoop = 1.00
    assert ice.price_per_scoop == 1.00
    assert ice.calculate_cost() == 4.0
    assert ice.calculate_tax() == 0.29
    ice.packaging = "bowls"
    assert ice.packaging == "bowls"
    
    ice = IceCream("vanilla", 3, 1.00)
    ice.name = "rice"
    assert ice.name == "rice"
    ice.scoop_count = 5
    assert ice.scoop_count == 5
    ice.price_per_scoop = 4.00
    assert ice.price_per_scoop == 4.00 
    assert ice.calculate_cost() == 20.0
    assert ice.calculate_tax() == 1.45 
    ice.packaging = "bowls"
    assert ice.packaging == "bowls"
     
     
def test_sun():
       
    sun = Sundae()
    assert sun.name == ''
    assert sun.scoop_count == 0
    assert sun.price_per_scoop == 0.00
    assert sun.topping_name == ""
    assert sun.topping_price == 0.00
    assert sun.calculate_cost() == 0.00
    assert sun.calculate_tax() == 0.00
    assert sun.packaging == "Boat"
    
    sun = Sundae("banana sundae", 2, 3.00, "sprinkles", 1.00)
    assert sun.name == "banana sundae"
    assert sun.scoop_count == 2
    assert sun.price_per_scoop == 3.00
    assert sun.topping_name == "sprinkles"
    assert sun.topping_price == 1.00
    assert sun.calculate_cost() == 7.00
    assert sun.calculate_tax() == 0.5075
    assert sun.packaging == "Boat"
    
    sun = Sundae()
    sun.name = "banana sundae"
    assert sun.name == "banana sundae"
    sun.scoop_count = 2
    assert sun.scoop_count == 2
    sun.price_per_scoop = 3.00
    assert sun.price_per_scoop == 3.00
    sun.topping_name = "sprinkles" 
    assert sun.topping_name == "sprinkles" 
    sun.topping_price = 6.00
    assert sun.topping_price == 6.00  
    assert sun.calculate_cost() == 12.0
    assert sun.calculate_tax() == 0.8699999999999999
    sun.packaging = "boats"
    assert sun.packaging == "boats"
        
    sun = Sundae("banana sundae", 2, 3.00, "sprinkles", 1.00)
    sun.name = "banana"
    assert sun.name == "banana"
    sun.scoop_count = 8
    assert sun.scoop_count == 8
    sun.price_per_scoop = 7.00
    assert sun.price_per_scoop == 7.00
    sun.topping_name = "spr" 
    assert sun.topping_name == "spr"  
    sun.topping_price = 6.00
    assert sun.topping_price == 6.00  
    assert sun.calculate_cost() == 62.0
    assert sun.calculate_tax() == 4.495
    sun.packaging = "boats"
    assert sun.packaging == "boats"
        
             
def test_order():
    ord = Order(PayType.CASH)  
    ord.add(Candy("skittles", 1, 3))    
    ord.add(Cookie("sugar", 1, 12))
    ord.add(IceCream("vanilla", 3, 1.00))
    ord.add(Sundae("banana sundae", 2, 3.00, "sprinkles", 1.00))
    ord.pay_type = PayType.CASH
    assert ord.pay_type == PayType.CASH
    ord.pay_type = PayType.CARD
    assert ord.pay_type == PayType.CARD
    ord.pay_type = PayType.PHONE
    assert ord.pay_type == PayType.PHONE
    
       
def test_valid_operand():
    h = Candy("", 3, 2)
    p = IceCream()
    assert p.__lt__(h) == True
    assert h.__lt__(p) == False
    assert p.__le__(h) == True
    assert h.__le__(p) == False
    assert p.__ge__(h) == False
    assert h.__ge__(p) == True
    assert p.__eq__(h) == False
    assert h.__eq__(p) == False
    assert p.__gt__(h) == False
    assert h.__gt__(p) == True


        
        
