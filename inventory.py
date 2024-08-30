
from abc import ABC, abstractmethod
from packaging import Packaging
from payment import Payment, PayType
from functools import total_ordering


@total_ordering        
class DessertItem(Packaging, ABC): 
    
    
    def __init__(self, name: str ="", tax_percent: float =7.25): 
        self.name = name
        self.tax_percent = tax_percent
        self.__packaging = None
        
        super().__init__()
    
    
    @property   
    def packaging(self):
        return self.__packaging
    
    @packaging.setter
    def packaging(self, new):
        self.__packaging = new
    
    @abstractmethod   
    def calculate_cost(self): 
        pass
    
    def calculate_tax(self): 
        
        return self.calculate_cost() * (self.tax_percent / 100)
    
    def _is_valid_operand(self, other):
            return other
        
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.calculate_cost() == other.calculate_cost())
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.calculate_cost() < other.calculate_cost())

    
class Candy(DessertItem):

    
    def __init__(self, name= "", candy_weight: float =0.00, price_per_pound: float =0.00):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"
        
    def calculate_cost(self):
        return self.price_per_pound * self.candy_weight
    
    def __str__(self):
        return f"{self.name} - Candy  ({self.packaging})".ljust(50) + "\n" + f"  {self.candy_weight:>5} lbs @ ${self.price_per_pound} /lb:".ljust(35) +  f"${self.calculate_cost():.2f}".ljust(15) + f"[Tax: ${self.calculate_tax():.2f}]"

           
class Cookie(DessertItem):

    
     
    def __init__(self, name= "", cookie_quantity=0, price_per_dozen=0.00):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"
    
    def calculate_cost(self):
        return self.cookie_quantity * self.price_per_dozen / 12
    
    def __str__(self):
        return f"{self.name} - Cookies  ({self.packaging})".ljust(50) + "\n" + f"  {self.cookie_quantity:>5} cookies @ ${self.price_per_dozen} /dozen:".ljust(35) +  f"${self.calculate_cost():.2f}".ljust(15) + f"[Tax: ${self.calculate_tax():.2f}]"

        
class IceCream(DessertItem):
    scoop_count: int
    price_per_scoop: float
    
    def __init__(self, name= "", scoop_count: int =0, price_per_scoop: float =0.00):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"
        
    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop
    
    def __str__(self):
        return f"{self.name} - Ice Cream  ({self.packaging})".ljust(50) + "\n" + f"  {self.scoop_count:>5} scoops @ ${self.price_per_scoop}/scoop:".ljust(35) +  f"${self.calculate_cost():.2f}".ljust(15) + f"[Tax: ${self.calculate_tax():.2f}]"

class Sundae(IceCream):
    topping_name: str
    topping_price: float
    
    def __init__(self, name= "", scoop_count=0, price_per_scoop=0.00, topping_name="", topping_price=0.00):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"
        
    def calculate_cost(self):
        return (self.scoop_count * self.price_per_scoop) + self.topping_price
        
    def __str__(self):
        return f"{self.topping_name} {self.name} - Sundae  ({self.packaging})".ljust(50) + "\n" + f"  {self.scoop_count:>5}scoops @ ${self.price_per_scoop}/scoop" + "\n" + f"    {self.topping_name} topping @ ${self.topping_price}:".ljust(35) + f"${self.calculate_cost():.2f}".ljust(15) + f"[Tax: ${self.calculate_tax():.2f}]"


class Order(Payment):
    
    def __init__(self, pay_method=PayType.CASH):
        self.in_order = []
        self.pay_method = pay_method
    
    @property
    def pay_type(self):
        return self.pay_method 

    @pay_type.setter
    def pay_type(self, new_val):
            self.pay_method = new_val
           
            
    def add(self, order): 
        if  order == False:
            return
        elif order == None:
            return True
        else:
            self.item = order        
            self.in_order.append(self.item)
            return self.in_order
    
    def item_count(self):
        '''retuns the length of the list of items'''
        self.order_num = len(self.in_order)
        return self.order_num
    
    
    def order_cost(self):
        self.order_price = 0
        for i in self.in_order:
            self.order_price += i.calculate_cost()
        return self.order_price  
        
    
    def order_tax(self):
        self.tax = 0 
        for i in self.in_order:
            self.tax += i.calculate_tax()
        return self.tax

    
    def __str__(self):
        return f"Order Subtotals:".ljust(35) + f"${self.order_cost():.2f}".ljust(15)  +  f"[Tax: ${self.order_tax():.2f}]" + "\n" + \
            f"Order total:".ljust(35) +  f"${self.order_cost() + self.order_tax():.2f}".ljust(15) + "\n" + \
                f"Total number of items in order: {self.item_count(): >5}" + "\n" \
                    "-----------------------------------------------------------" + "\n" \
                    f"Paid with {self.pay_method}"
                          





