# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Weapon :
    def __init__(self, ammunitions: int, rang: int ):
        self._ammunitions = ammunitions
        self._rang = rang

    def fire_at(self, x: int, y: int, z: int):
        print(f"x: {self._x}, y: {self._y}, z: {self._z}")



class missiles_antisurface (Weapon):
    def __int__(self,ammunitions: int, rang: int, x: int,y: int,z: int):
        super().__int__(ammunitions, rang )
        self.__x = x
        self.__y = y
        self.__z = z

    def fire_at(self, ammunitions: int, x: int, y: int, z: int):
        self.__ammunitions = ammunitions
        self.__x = x
        self.__y = y
        self.__z = z
        if ammunitions ==0 :
            print( "NoAmmunitionError")
        if z !=0 :
            print("OutOfRangeError")
            self.__ammunitions = self.__ammunition -1

class Missile_anti_air(Weapon):
    def __int__(self,ammunitions: int, rang: int, x: int,y: int,z: int):
        super().__int__(ammunitions, rang )
        self.__x = x
        self.__y = y
        self.__z = z

    def fire_at(self,ammunitions: int, x: int, y: int, z: int):
        self.__ammunitions = ammunitions
        self.__x = x
        self.__y = y
        self.__z = z
        if ammunitions ==0 :
            print( "NoAmmunitionError")
        if z>0 :
            print("OutOfRangeError")
            self.__ammunitions = self.__ammunition -1

class Tropille(Weapon):
    def __int__(self,ammunitions: int, rang: int, x: int,y: int,z: int):
        super().__int__(ammunitions, rang )
        self.__x = x
        self.__y = y
        self.__z = z

    def fire_at(self,ammunitions: int, x: int, y: int, z: int):
        self.__ammunitions = ammunitions
        self.__x = x
        self.__y = y
        self.__z = z
        if ammunitions ==0 :
            print( "NoAmmunitionError")
        if z<=0 :
            print("OutOfRangeError")
            self.__ammunitions = self.__ammunition -1


class Vessel :
    def __init__(self, coordinates: tuple, max_hits: int, weapon: Weapon ):
        self._coordinates = coordinates
        self._max_hits = max_hits
        self._weapon = Weapon

