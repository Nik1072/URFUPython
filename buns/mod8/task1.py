class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        if isinstance(value, list) and len(value) == 4:
            if isinstance(value[0], int) and isinstance(value[1], int) and isinstance(value[2], int) and isinstance(value[3], int):
                if value[0] >= 0 and value[1] >= 0 and value[2] >= 0 and value[3] >= 0:
                    self._coordinates = value
                else:
                    raise Exception('Invalid coordinates value Argument. Координаты задаются списком из четырёх int значений (pos_x, pos_y, length, width), больше 0')
            else:
                raise Exception('Invalid coordinates value Argument. Координаты задаются списком из четырёх int значений (pos_x, pos_y, length, width), больше 0')
        else:
            raise Exception('Invalid coordinates value Argument. Координаты задаются списком из четырёх int значений (pos_x, pos_y, length, width), больше 0')

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if isinstance(value, int) and value >= 0:
            self._speed = value
        else:
            raise Exception('Invalid speed value Argument. Скорость задаётся int значением не менее 0')

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise Exception('Invalid brand value Argument. Название бренда задаётся str')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int) and 0 <= value < 2024:
            self._year = value
        else:
            raise Exception('Invalid year value Argument. Год задаётся int значением от 0 (включительно) до 2023 (включительно)')

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if isinstance(value, int) and 0 < value <= 9999999:
            self._number = value
        else:
            raise Exception('Invalid number value Argument. Номер задаётся int значением от 0 до 9999999 (включительно)')

    def __str__(self):
        return f"Transport: coordinates: x: {self.coordinates[0]} y: {self.coordinates[1]} length: {self.coordinates[2]} width: {self.coordinates[3]}, speed: {self.speed}mph, brand: {self.brand}, year: {self.year}, number: {self.number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return self._coordinates[0] == pos_x and self._coordinates[1] == pos_y and self._coordinates[2] == length and self._coordinates[3] == width

class Passenger():
    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, value):
        if isinstance(value, int) and value > 0:
            self._passengers_capacity = value
        else:
            raise Exception('Invalid passengers capacity value Argument. Значение вместимости пассажиров задаётся значением int большим нуля')

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        if isinstance(value, int) and value >= 0:
            self._number_of_passengers = value
        else:
            raise Exception('Invalid number of passengers value Argument. Значение кол-ва пассажиров задаётся значением int большим или равным нулю')

    def __str__(self):
        return f"Passenger: passengers capacity: {self.passengers_capacity}, number of passengers: {self.number_of_passengers}"

class Cargo():
    def __init__(self, carrying):
        self.carrying = carrying

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, value):
        if isinstance(value, int) and value > 0:
            self._carrying = value
        else:
            raise Exception('Invalid carrying value Argument. Значение грузоподъёмности задаётся int значением большим нуля')


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value >= 0:
            self._height = value
        else:
            raise Exception('Invalid port value Argument. Значение высоты задаётся int значением большим или равным нулю')

class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number, license_plate):
        super().__init__(coordinates, speed, brand, year, number)
        self.license_plate = license_plate

    @property
    def license_plate(self):
        return self._license_plate

    @license_plate.setter
    def license_plate(self, value):
        if isinstance(value, str) and len(value) == 6:
            self._license_plate = value
        else:
            raise Exception(
                'Invalid port value Argument. Значение номера авто задаётся str длинной в 6 элементов')

class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if isinstance(value, str):
            self._port = value
        else:
            raise Exception('Invalid port value Argument. Значение порта (название порта) задаётся str')



class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number, license_plate):
        super().__init__(coordinates, speed, brand, year, number, license_plate)

class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, license_plate, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number, license_plate)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, license_plate, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number, license_plate)
        Cargo.__init__(self, carrying)

class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)

class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)

class Biplane(Plane):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number, height)

class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

class CargoPlane(Plane, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, height, carrying):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Cargo.__init__(self, carrying)

# Как я не пытался, гибрид классов (Plane и Ship) не хотел работать, теряя в себе аргумент port
# class Seaplane(Plane, Ship):
#     def __init__(self, coordinates, speed, brand, year, number, height, port):
#         Plane.__init__(self, coordinates, speed, brand, year, number, height)
#         Ship.__init__(self, coordinates, speed, brand, year, number, port)