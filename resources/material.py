from resources import resource


class Material(resource.Resource):
    ID = ""
    hardness = 0
    blastproof = 0

    def breaking(self, entity):
        if self.status == "Unbroken":
            if entity.equipment is not None:
                power = entity.equipment.power
            else:
                power = entity.standard_power
            self.hardness -= power
            self.check()

    def check(self):
        if self.hardness <= 0:
            self.hardness = 0
            self.status = "Broken"

    def __init__(self):
        super().__init__()
        self.type = "building_material"

    def __repr__(self):
        return "{0}: Hardness: {1}, Status: {2}".format(" ".join([self.name]),
                                                        self.hardness,
                                                        self.status)

    def getting_text(self):
        return (f"Material: {0} {1}, Hardness: {2}, Blastproof: {3}", self.ID,
                self.name, self.hardness, self.blastproof)


class Concrete(Material):
    def __init__(self):
        super().__init__()
        self.name = "Concrete"
        self.ID = 251
        self.hardness = 1.8
        self.blastproof = 9


class Bricks(Material):
    def __init__(self):
        super().__init__()
        self.name = "Bricks"
        self.ID = 45
        self.hardness = 2
        self.blastproof = 30


class Iron(Material):
    def __init__(self):
        super().__init__()
        self.name = "Iron"
        self.ID = 42
        self.hardness = 5
        self.blastproof = 30


class Stone(Material):
    def __init__(self):
        super().__init__()
        self.name = "Stone"
        self.ID = 1
        self.hardness = 1.5
        self.blastproof = 6
