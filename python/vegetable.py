class Vegetable:
    def __init__(self):
        self.sale_price = 5
        self.growth_max = 7
        self.growth = 0
    
    def  grow(self):
        self.growth += 1

vegetable = Vegetable()
vegetable.grow()