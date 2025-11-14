# Class for Chef
class Chef:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def cook(self, dish):
        print(f"Chef {self.name} is preparing {dish} (Specialty: {self.specialty})")


# Class for Customer
class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, chef, dish):
        print(f"{self.name} orders {dish} from Chef {chef.name}")
        chef.cook(dish)


# ----- Creating Two Chefs -----
chef1 = Chef("Arjun", "Italian")
chef2 = Chef("Meera", "Indian")

# ----- Creating Two Customers -----
customer1 = Customer("Rohan")
customer2 = Customer("Priya")

# ----- Order Interaction -----
customer1.order(chef1, "Pasta")
customer2.order(chef2, "Butter Chicken")
