import random
from bicycles import Bicycle, BikeShop, Customer

if __name__ == '__main__':
  """ Create 6 different bicycle models """
  first_bike = Bicycle("Road", 20, 200)
  second_bike = Bicycle("Mountain", 40, 300)
  third_bike = Bicycle("Touring", 35, 650)
  fourth_bike = Bicycle("Hybrid", 20, 720)
  fifth_bike = Bicycle("Triathlon", 45, 475)
  sixth_bike = Bicycle("Track", 30, 250)

  """ Create a bicycle shop that has 6 different bicycle models in stock """
  inventory_list = [ first_bike, second_bike, third_bike, fourth_bike, fifth_bike, sixth_bike ]
  bike_shop = BikeShop("Ryan's Shop", 20, inventory_list)
  
  """ 
    Print the initial inventory of the bike shop for each bike it carries.
  """
  print bike_shop
    
  """ Create three customers """
  customer_list = [ Customer("Ryan", 200), Customer("Audrey", 500), Customer("Amy", 1000) ]
  
  """ 
  Print the name of each customer
  """
  print "\nCustomers"
  print "-" * 20

  for customer in customer_list:
    template = "{0}, Budget: ${1}"
    print template.format(customer.customer_name, customer.budget)
    
  """ 
    List of the bikes offered by the bike shop that they can afford given their budget
    NOTE:  Make sure you price the bikes in such a way that each customer can afford at least one.
  """
  print "\nWhich bikes can they afford?"
  for customer in customer_list:
    print '-' * 20
    bikes = ", ".join( bike.model_name for bike in bike_shop.filter(customer.budget) )
    print customer.customer_name, "-->", bikes

  """ 
    Have each of the three customers purchase a bike
      - Print the name of the bike the customer purchased
      - The cost
      - How much money they have left over in their bicycle fund
  """
  print "\nWhich bike did the customers buy?"
  print '-' * 20
  
  template = "{0} bought the {1} at ${2}, and they have ${3} left over."
  for customer in customer_list:
    affordables = bike_shop.filter(customer.budget)
    bike_shop.sell(random.choice(affordables), customer)
    
    print template.format(
      customer.customer_name, customer.bike.model_name, 
      customer.bike.cost_to_produce, customer.budget
    )
  
  """
    After each customer has purchased their bike
      - Bicycle shop's remaining inventory for each bike
      - How much profit they have made selling the three bikes.
  """
  print bike_shop