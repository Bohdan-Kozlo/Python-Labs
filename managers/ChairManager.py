
class ChairManager:
    """

    """

    def __init__(self, chairs):
        self.chairs = chairs

    def add_chair(self, chair):
        self.chairs.append(chair)

    def search_by_material(self, material):
        return list(filter(lambda chair: chair.material == material, self.chairs))

    def search_by_max_weight(self, max_weight):
        return list(filter(lambda chair: chair.max_weight >= max_weight, self.chairs))
    