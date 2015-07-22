class Bicycle(object):
  """ Bicycles have a model name, a weight, a cost to produce """
  def __init__(self, model_name, weight, cost_to_produce):
    self.model_name = model_name
    self.weight = weight
    self.cost_to_produce = cost_to_produce
    
  def __repr__(self):
    template = "{0} --> Weight: {1} lbs, Costs: ${2}"
    return template.format(self.model_name, self.weight, self.cost_to_produce)
      
class BikeShop(object):
  """ Bike Shops have a name, an inventory and are profitable """
  def __init__(self, shop_name, margin, shop_inventory):
    self.shop_name = shop_name
    self.shop_inventory = {}
    self.margin = margin
    self.profit = 0
    
    for bike in shop_inventory:
      bike.markup = int((bike.cost_to_produce / 100.0) * self.margin)
      bike.price = bike.cost_to_produce + bike.markup
      self.shop_inventory[bike.model_name] = bike

  def filter(self, budget):
    bikes = self.shop_inventory.values()
    return [ bike for bike in bikes if bike.cost_to_produce <= budget ]
    
  """ Sell bicycles with a margin over their cost """
  def sell(self, bike, customer):
    customer.bike = bike
    customer.budget -= bike.cost_to_produce
    self.profit += self.margin
    del self.shop_inventory[bike.model_name]
    
  """ Can see how much profit they have made from selling bikes """
  def __repr__(self):
    template = "\n{0} (${1} profit)\n\n{2}\n"
    bikes = "\n".join( str(bike) for bike in self.shop_inventory.values() )
    return template.format(self.shop_name, self.profit, bikes)
    
class Customer(object):
  """ Customers have a name and a bike budget """
  def __init__(self, customer_name, budget):
    self.customer_name = customer_name
    self.budget = budget
    self.bike = None