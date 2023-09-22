from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, number_array):
      self.number_array = number_array

    def needs_service(self):
       if sum(self.number_array) >= 3:
            return True
            return False
