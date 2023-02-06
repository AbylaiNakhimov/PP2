class TriangleChecker: 
    def __init__(self, a, b, c): 
        self.a = a 
        self.b = b 
        self.c = c 
 
    def is_triangle(self): 
        if any(val <= 0 for val in [self.a, self.b, self.c]): 
            return "Nothing will work with negative numbers!" 
        if any(val is None for val in [self.a, self.b, self.c]): 
            return "You only need to enter numbers!" 
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b): 
            return "You can build a triangle!" 
        return "It's a pity, but you can't make a triangle out of this." 