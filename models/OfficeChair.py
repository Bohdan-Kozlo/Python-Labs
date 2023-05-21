from models.Chair import Chair


class OfficeChair(Chair):
    """
    The Office Chair class represents an office chair and inherits from the Chair class
    """

    def __init__(self, id=2, material="wood", max_weight="150", owner="Bob", chair_type="type",
                 material_of_upholstery="material", current_incline_back="50"):
        super().__init__(id, material, max_weight, owner)
        self.chair_type = chair_type
        self.material_of_upholstery = material_of_upholstery
        self.current_incline_back = current_incline_back

    def adjust_position(self, value):
        """
        Method that increases the angle of inclination for an office chair
        """
        self.current_incline_back += value

    def __str__(self):
        return super().__str__(), f"Chair type={self.chair_type}, \
                Material of upholstery={self.material_of_upholstery}, \
                Current incline back={self.current_incline_back}"