class Parent():
   def __init__(self, last_name, eye_color):
       print("Parent constructor called!")
       self.last_name = last_name
       self.eye_color = eye_color

   def show_info(self):
      print("Last Name - " + self.last_name)
      print("Eye Color - " + self.eye_color)
      
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called!")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("last name: " + self.last_name)
        print("eye color: " + self.eye_color)
        print("number of toys: " + str(self.number_of_toys))

billy_cyrus = Parent("Cyrus", "Blue")

#print(billy_cyrus)
#print(billy_cyrus.last_name)

bob_cyrus = Child("Cyrus", "Blue", 5)

#print(bob_cyrus)
#print(bob_cyrus.number_of_toys)

billy_cyrus.show_info()
bob_cyrus.show_info()
