from ua.lviv.iot.algo.part1.lab1.Chair import Chair

chair_list = [
    Chair(),
    Chair.get_instance(),
    Chair(2, "Plastic", 100, "Bob")
]

for object in chair_list:
    print(object)
