class Franchise:
#initialize variables
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

#print address
  def __repr__(self):
    return "{}".format(self.address)

#return list of available menus at given time
  def available_menus(self, time):
    available = []
    for menu in self.menus:
        if time >= menu.start_time and time <= menu.end_time:
          available.append(menu)
    return available

class Menu:
#initialize variables
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

#print string of daily menu and times
  def __repr__(self):
    return "{} menu is available from {} to {}".format(self.name, self.start_time, self.end_time)

#calculate bill and check if purchased_item is on menu
  def calculate_bill(self, purchased_items):
    total = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        total += self.items[purchased_item]
    return total

#brunch
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu("brunch", brunch_items, 1100, 1600)
#print(brunch_menu)
#print(brunch_menu.calculate_bill(['pancakes', 'coffee', 'home fries']))

#early_bird 
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu("early_bird", early_bird_items, 1500, 1800)
#print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#dinner
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("dinner", dinner_items, 1700, 2300)

#kids
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu("kids", kids_items, 1100, 2100)

#combine all menus into one variable for reusability
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

#create Franchises
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store)
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))
