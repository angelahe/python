class Math():

    def __init__(self, num1, num2):
        self.real = num1
        self.unreal = num2

    def make_square(self):
        real = self.real**2 - self.unreal**2
        unreal = 2*self.real*self.unreal
        return (Math(real, unreal))

    def __repr__(self):

    #    self.unreal < 0 if return str(self.real) + '-' + str(self.unreal) + 'i' 
    #       else return str(self.real) + '+' + str(self.unreal) + 'i'
    #    return str(self.real) + '-' + str(self.unreal) + 'i' if self.unreal < 0 else return str(self.real) + '+' + str(self.unreal) + 'i'
        if self.real==0 and self.unreal==0:
            return "0"
        if self.real==0:
            return f"{self.unreal}i"
        if self.unreal==0:
            return f"{self.real}"

        return f"{self.real}{self.unreal}i" if self.unreal < 0 else f"{self.real}+{self.unreal}i"