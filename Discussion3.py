import math

class Rectangle():
    # Represents a rectangle with a given width and height

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Initializes the Rectangle object with width and height

    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}"
    
    # Returns a string representation of the Rectangle object

    def area_calculator(self):
        return self.width * self.height
    
    # Returns the area of the rectangle 

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.width == other.wideth and self.height == other.height 
    
    # Compares two Rectangle objects for equality; returns True if both rectangles have the same width and height, False otherwise

def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    pass

if __name__ == "__main__":
    main()