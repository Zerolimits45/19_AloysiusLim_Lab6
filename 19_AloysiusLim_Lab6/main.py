class Computer:
    def __init__(self, computer_type, computer_model, computer_system, computer_storage):
        self.computer_type = computer_type
        self.computer_model = computer_model
        self.computer_system = computer_system
        self.computer_storage = computer_storage

    def playGame(self, game):
        print("(%s) %s is playing %s" %(self.computer_type, self.computer_model, game))

hp = Computer('HP','Desktop','Windows','1TB SSD')
print(hp.computer_type)
print(hp.computer_model)
print(hp.computer_system)
print(hp.computer_storage)
hp.playGame("Pac-man")
print("---------------")

class Desktop(Computer): #the computer refers to the parent class and this desktop is a child class
    def __init__(self, computer_model, computer_system, computer_storage):
        Computer.__init__(self, 'Desktop', computer_model, computer_system, computer_storage)
asus = Desktop('Asus', 'Windows', '1TB HDD')
print(asus.computer_type)
print(asus.computer_model)
print(asus.computer_system)
print(asus.computer_storage)
asus.playGame("Valorant")
print("---------------")

class Laptop(Computer):
    def __init__(self, computer_model, computer_system, computer_storage):
        Computer.__init__(self, 'Laptop', computer_model, computer_system, computer_storage)
apple = Laptop('Apple', 'MacOSx', '512GB SSD')
print(apple.computer_type)
print(apple.computer_model)
print(apple.computer_system)
print(apple.computer_storage)
apple.playGame("Genshin Impact")




