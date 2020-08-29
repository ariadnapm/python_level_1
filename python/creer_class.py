class Calculator:
    def __init__(self):
        self.result = 5
    
    def add(self, value):
        self.result += value
        return self.result

    def sub(self, value_sub):
        self.result -= value_sub
        return self.result
    
    def mult(self, value_mult):
        self.result *= value_mult
        return self.result
    
    def div(self, value_div):
        self.result /= value_div
        return self.result
    
    def reset(self):
        self.result = 0
        return self.result

calc = Calculator()
print(calc.result)
calc.add(2)
print(calc.result)
calc.sub(3)
print(calc.result)
calc.mult(5)
print(calc.result)
calc.div(10)
print(calc.result)
calc.reset()
print(calc.result)