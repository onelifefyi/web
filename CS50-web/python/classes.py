class Point():
    def __init__(self, x, y): # This is the constructor in python, automatically called
        self.x = x            # Argument: self, all functions that operate on themselves (hence called methods) take self
        self.y = y            # Self represents the object in call

p = Point(2,8)
print(f"x: {p.x}, y: {p.y}")