from exemplo_18 import Cheese
import weakref
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))