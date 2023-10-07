class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I'm a teacher!")

class Customer(User):
    print("I'm a Customer!")
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def update_membership(self, new_membership):
        print('Calculating costs')
        self.membership_type = new_membership

    #def read_customer():
     #   print('Reading customer from DB')
    
    def __str__(self):
        #print('converting to string')
        return self.name + ' ' +  self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    __hash__ = None

    __repr__ = __str__     

users = [Customer('fahd', 'Gold'),
            Customer('mohd', 'Silver'),
            Teacher()]

for user in users:
    user.log()

#print(customers)

#print(customers[1])
#customers[1].update_membership('Gold')
#print(customers[1]) 

#Customer.read_customer()