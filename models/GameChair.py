from models.Chair import Chair


class GameChair(Chair):
    """
    The GameChair class represents a gaming chair and inherits from the Chair class
    """

    def adjust_position(self, value):
        pass

    def __init__(self, id=2, material="wood", max_weight="150", owner="Bob", height_of_armrests=30, max_height=50,
                 weight_of_chair=30):
        super().__init__(id, material, max_weight, owner)
        self.height_of_armrests = height_of_armrests
        self.max_height = max_height
        self.weight_of_chair = weight_of_chair

    def __str__(self):
        return super().__str__(), f"Height of armrests={self.height_of_armrests}, \
                Max height={self.max_height}, \
                Weight of chair={self.weight_of_chair}"