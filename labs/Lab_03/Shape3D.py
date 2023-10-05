import math

class Shape3D:

    def __init__(self, radius, volume, area):
        raise NotImplementedError("Abstract class cannot be instantiated")

    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        raise NotImplementedError("Not implemented for apibstract class")

    def print_info(self):
        print(f"Area: {self.area} Volume: {self.volume}")


class Cylinder(Shape3D):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height
    
    def cylinder_volume(self) -> float:
        return 3.145*(self.radius^2)*self.height

    def cylinder_area(self) -> float:
        return 2 * 3.1415 * self.radius^2 + 2 * 3.1415 * self.radius * self.height

class Cuboid(Shape3D):
    def __init__(self, width: float, length: float, height: float):
        self.width = width
        self.length = length
        self.height = height
    
    def cuboid_area(self) -> float:
        return 2* (self.width + self.length) + 2*(self.width + self.height) + 2*(self.length * self.height)
    
    def cuboid_volume(self) -> float:
        return self.length*self.width*self.height

class Cube(Cuboid):
    
    def cube_area(self) -> float:
        area = self.cuboid_area()
        return area

    def cube_volume(self) -> float:
        volume = sellf.cuboid_volume()
        return volume

    

#Area: 54  Volume: 27
#Area: 150.79644737231007  Volume: 141.3716694115407
#Area: 228  Volume: 216





    
