import logging
# configure logging. Normally do this in your "app" script.
logging.basicConfig(level=logging.INFO,
                   format="%(levelname)s %(funcName)8s: %(message)s"
                   )

class MyMeta(type):
   """Custom metaclass extends 'type'."""

   def __call__(cls, *args, **kwargs):
       logging.info("performing __call__")
       # Perform object creation ourself:
       instance = cls.__new__(cls)
       instance.__init__(*args, *kwargs)
       return instance

class Person(metaclass = MyMeta):
   """Person with a name."""

   def __init__(self, name):
       logging.info(f"initialize Person('{name}')")
       self.name = name

   def __new__(cls, *args, **kwargs):
       logging.info(f"allocate a new Person")
       return super().__new__(cls)
   
   def __del__(self):
       logging.info(f"destroying {self}")
       del self.name

   def __str__(self):
       return f"{type(self).__name__}('{self.name}')"
   
if __name__ == '__main__':
   for name in ["Big","Cat","Dog","Sus","Egg"]:
       p = Person(name)
       print(p)