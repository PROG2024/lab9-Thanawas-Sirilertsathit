"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""

class Counter:

    _instance = None

    def __init__(self):
        """Construct an attribute"""
        self.__count = 0

    def __new__(cls,*args,**kwargs):
        """Allocating memory"""
        if cls._instance is not None:
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def __str__(self):
        """Representative of this object"""
        return f"{self.__count}"
    
    @property
    def count(self):
        """Getter in property version"""
        return self.__count
    
    def increment(self):
        """Increase value of __count by 1"""
        self.__count += 1

    