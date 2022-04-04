#!/usr/bin/python3

class square():
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        size = 0
        i = 0
        for key, value in kwargs.items():
            if i == 0:
                size = value
                i += 1
            else:
                if value != size:
                    raise ValueError
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
