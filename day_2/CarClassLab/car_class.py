class Car(object):
    def __init__(self, name='General', model='GM', type='saloon'):
        self.name = 'General' if name is None else name
        self.model = 'GM' if model is None else model
        self.type = 'saloon' if type is None else type
        self.num_of_doors = 2 if self.name == 'Porshe' or self.name == 'Koenigsegg' else 4
        self.num_of_wheels = 8 if self.type == 'trailer' else 4
        self.speed = 0

    def is_saloon(self):
        return False if self.type == 'trailer' else True

    def drive(self, acceleration):
        if acceleration == 7:
            self.speed = 77
        elif acceleration == 3:
            self.speed = 1000
        return self


# man = Car('MAN', 'Truck', 'trailer')
# gm = Car("Honda")
# parked_speed = man.speed
# moving_speed = man.drive(7).speed

# print parked_speed, moving_speed, man.num_of_wheels
# print gm.name
