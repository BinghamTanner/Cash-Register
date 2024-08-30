
from abc import ABC, abstractmethod


class Packaging(ABC):
     
    
    @property
    @abstractmethod
    def packaging(self):
        pass 

    @packaging.setter
    @abstractmethod
    def packaging(self, val):
        pass 
        
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Packaging:
            return True
        return False
    
    
    
    

  
    
    