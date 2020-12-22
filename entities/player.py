from entities import entity


class Player(entity.Entity):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.standard_power = 5

    def __repr__(self):
        return "Player: {}, Equipped: {}".format(
            self.name, self.equipment)
