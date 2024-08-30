from abc import ABC, abstractmethod
from enum import Enum

class Payment(ABC):
    
    
    @property
    @abstractmethod
    def pay_type(self):
        pass 

    @pay_type.setter
    @abstractmethod
    def pay_type(self, val):
        pass 
        
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Payment:
            return True
        return False

class PayType(Enum):
    CASH = 1
    CARD = 2
    PHONE = 3







    