class Menu:
    def __init__(self,items):
        if items is None:
            items = []
        self.items = items
        
    def add(self,item):
        if item not in self.items:
            self.items.append(item)
            
    def remove(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found")
            
    def check(self,item):
        return item in self.items
    
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
menu = Menu(initial_menu)
print("Initial Menu:", menu.items)

menu.add("Tacos")
print("Menu after adding Tacos:", menu.items)
menu.remove("Salad")
print("Menu after removing Salad:", menu.items)
cheak = menu.check("Pizza")

if cheak:
    print("Pizza is available")
else:
    print("Pizza is not available")