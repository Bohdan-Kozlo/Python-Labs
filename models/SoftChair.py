from models.Chair import Chair


class SoftChair(Chair):
    """
    The SoftChair class represents a soft chair and is inherited from Chair
    """

    def adjust_position(self, value):
        pass

    def __init__(self, id=2, material="wood", max_weight="150", owner="Bob", filler="foller", depth="depth",
                 cushioning=True):
        super().__init__(id, material, max_weight, owner)
        self.filler = filler
        self.depth = depth
        self.cushioning = cushioning

    def __str__(self):
        return super().__str__(), f"Filler={self.filler}, \
                Depth={self.depth},\
                Cushioning={self.cushioning}"
