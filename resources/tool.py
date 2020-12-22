from resources import resource


class Tool(resource.Resource):
    power = 0
    durability = 0

    def __init__(self):
        super().__init__()
        self.type = "breaking_tool"

    def __repr__(self):
        return "{0}, power: {1}".format(" ".join([self.name]),
                                        self.power, self.durability)

    def getting_text(self):
        return (f"Tool: {0} {1}, Power: {2}, Durability: {3}", self.name,
                self.power, self.durability)


class WoodenPickaxe(Tool):
    def __init__(self):
        super().__init__()
        self.name = "Wooden Pickaxe"
        self.power = 2
        self.durability = 60


class IronPickaxe(Tool):
    def __init__(self):
        super().__init__()
        self.name = "Iron Pickaxe"
        self.power = 4
        self.durability = 250
