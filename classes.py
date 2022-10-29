class Card:
    type = 'Default Card'

    def __init__(self, place, name: str, owner: str, cost, bail_cost, bailed: bool):
        self.place = place
        self.name = name
        self.cost = cost
        self.owner = owner
        self.bail_cost = bail_cost
        self.bailed = bailed

    def info(self):
        print('Place: ' + str(self.place))
        print('Type: ' + str(self.type))
        print('Name: ' + str(self.name))
        print('Owner: ' + str(self.owner))
        print('Cost: ' + str(self.cost))
        print('Bail cost: ' + str(self.bail_cost))
        print('Bailed: ' + str(self.bailed))


class Building(Card):
    type = 'Building'

    def __init__(self, place, name: str, owner: str, cost, bail_cost, bailed: bool,
                 group: str, rent: list, houses, house_cost, monopolized: bool):
        super().__init__(place, name, owner, cost, bail_cost, bailed)
        self.group = group
        self.rent = rent
        self.houses = houses
        self.houses_cost = house_cost
        self.monopolized = monopolized

    def info(self):
        super().info()
        print('Group: ' + str(self.group))
        print('Rent: ' + str(self.rent))
        print('Houses: ' + str(self.houses))
        print('Houses cost: ' + str(self.houses_cost))
        print('Monopolized: ' + str(self.monopolized))


class Seaport(Card):
    type = 'Seaport'

    def __init__(self, place, name: str, owner: str, cost, bail_cost, bailed: bool, rent: list, connection):
        super().__init__(place, name, owner, cost, bail_cost, bailed)
        self.rent = rent
        self.connection = connection

    def info(self):
        super().info()
        print('Rent: ' + str(self.rent))
        print('Connection: ' + str(self.connection))


class Company(Card):
    type = 'Company'

    def __init__(self, place, name: str, owner: str, cost, bail_cost, bailed: bool, rent: list, connection):
        super().__init__(place, name, owner, cost, bail_cost, bailed)
        self.rent = rent
        self.connection = connection

    def info(self):
        super().info()
        print('Rent: ' + str(self.rent))
        print('Connection: ' + str(self.connection))


class Player:
    def __init__(self, number, name: str, place, money, own: list, moved: bool):
        self.number = number
        self.name = name
        self.place = place
        self.money = money
        self.own = own
        self.moved = moved

    def info(self):
        print('Number: ' + str(self.number))
        print('Name: ' + str(self.name))
        print('Place: ' + str(self.place))
        print('Money: ' + str(self.money))
        print('Own: ' + str(self.own))
        print('Moved: ' + str(self.moved))
