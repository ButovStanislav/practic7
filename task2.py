class Validator():
    def __init__(self, obj):
        self.obj = obj
    def is_valid(self):
        return None
    
class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self.obj, (int, float))
print(issubclass(NumberValidator, Validator))

validator1 = Validator('beegeek') 
validator2 = Validator(1) 
validator3 = Validator(1.1) 
print(validator1.is_valid()) 
print(validator2.is_valid()) 
print(validator3.is_valid())

validator4 = NumberValidator('beegeek') 
validator5 = NumberValidator(1) 
validator6 = NumberValidator(1.1) 
print(validator4.is_valid()) 
print(validator5.is_valid()) 
print(validator6.is_valid())