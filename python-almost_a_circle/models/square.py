#!/usr/bin/python3
"""Create Square class"""
from models.rectangle import Rectangle


class Square (Rectangle):
    """Square Class"""

    def __init__(self, size,  x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )

    @property
    def size(self) -> int:
        """get size"""
        return self.width

    @size.setter
    def size(self, value) -> None:
        """Set size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")
        self.width = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value > 0:
            raise ValueError("height must be > 0")
        self.height = value

    def update(self, *args, **kwargs):
        """Update elements"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self) -> str:
        """Make class dictionary"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
