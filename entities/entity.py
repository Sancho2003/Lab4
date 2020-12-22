class Entity:
    name = ""
    standard_power = 0
    equipment = None

    def equip(self, resource):
        self.equipment = resource

    def __repr__(self):
        return "Entity: {}, Equipped: {}".format(
            self.name, self.equipment)
