from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, number_array):
     self.number_array = number_array

    def needs_service(self):
       for num in self.number_array:
            if num >= 0.9:
                return True
                return False