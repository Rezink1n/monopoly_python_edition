class Card:

    type = 'Default Card'

    def __init__(self, place, name, cost, owner, bail_cost, bailed):
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
        print('Cost: ' + str(self.cost))
        print('Owner: ' + str(self.owner))
        print('Bail cost: ' + str(self.bail_cost))
        print('Bailed: ' + str(self.bailed))


class Building(Card):

    type = 'Building'

    def __init__(self, place, name, cost, owner, bail_cost, bailed, group, rent, houses, house_cost, monopolized):
        super().__init__(place, name, cost, owner, bail_cost, bailed)
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

    def __init__(self, place, name, cost, owner, bail_cost, bailed, rent, connection):
        super().__init__(place, name, cost, owner, bail_cost, bailed)
        self.rent = rent
        self.connection = connection

    def info(self):
        super().info()
        print('Rent: ' + str(self.rent))
        print('Connection: ' + str(self.connection))


class Company(Card):

    type = 'Company'

    def __init__(self, place, name, cost, owner, bail_cost, bailed, rent, connection):
        super().__init__(place, name, cost, owner, bail_cost, bailed)
        self.rent = rent
        self.connection = connection

    def info(self):
        super().info()
        print('Rent: ' + str(self.rent))
        print('Connection: ' + str(self.connection))

#
#
