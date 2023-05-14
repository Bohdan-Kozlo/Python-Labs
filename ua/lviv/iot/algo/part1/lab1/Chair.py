class Chair:
    """
    The chair class has such fields as ID, material, maximum weight, and owner.
    Similarly, the class has methods: occupy, release, is_occupied and the static method get_instance
    """

    instance = None

    def __init__(self, id=1, material="wood", max_weight="150", owner="Bob"):
        self.__id = id
        self.__material = material
        self.__max_weight = max_weight
        self.__owner = owner

    def __str__(self):
        return f"Id={self.__id}, Material={self.__material}," \
               f" Max weight={self.__max_weight}, Owner={self.__owner}"

    def occupy(self, owner):
        self.__owner = owner

    def release(self):
        self.__owner = None

    def is_occupied(self):
        return self.__owner is not None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value):
        self.__material = value

    @property
    def max_weight(self):
        return self.__max_weight

    @max_weight.setter
    def max_weight(self, value):
        self.__max_weight = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @staticmethod
    def get_instance():
        if Chair.instance is None:
            Chair.instance = Chair()
        return Chair.instance
