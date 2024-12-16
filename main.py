class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color if color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS] else 'undefined'

    def get_model(self):
        return f"Model: {self.__model}"

    def get_horsepower(self):
        return f"Engine power: {self.__engine_power} hp"

    def get_color(self):
        return f"Color: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Owner: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"You cant park there! {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()





