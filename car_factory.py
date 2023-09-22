from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.Octoprime_tires import OctoprimeTire
from tires.Carrigan_tires import CarriganTire

from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from utils import TireSesnorArray


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_type):
        
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        
        if tire_type == "CarriganTire":
            tire = CarriganTire(TireSesnorArray())
        elif tire_type == "OctoprimeTire":
            tire = OctoprimeTire(TireSesnorArray())
        else:
            raise ValueError("Invalid tire type. Choose between 'CarriganTire' and 'OctoprimeTire'.")

        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_type):
        
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        
        if tire_type == "CarriganTire":
            tire = CarriganTire(TireSesnorArray())
        elif tire_type == "OctoprimeTire":
            tire = OctoprimeTire(TireSesnorArray())
        else:
            raise ValueError("Invalid tire type. Choose between 'CarriganTire' and 'OctoprimeTire'.")

        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_type):
        
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        
        if tire_type == "CarriganTire":
            tire = CarriganTire(TireSesnorArray())
        elif tire_type == "OctoprimeTire":
            tire = OctoprimeTire(TireSesnorArray())
        else:
            raise ValueError("Invalid tire type. Choose between 'CarriganTire' and 'OctoprimeTire'.")

        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_type):
        
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        
        if tire_type == "CarriganTire":
            tire = CarriganTire(TireSesnorArray())
        elif tire_type == "OctoprimeTire":
            tire = OctoprimeTire(TireSesnorArray())
        else:
            raise ValueError("Invalid tire type. Choose between 'CarriganTire' and 'OctoprimeTire'.")

        car = Car(engine, battery, tire)
        return car


   @staticmethod
   def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_type):
    
       engine = CapuletEngine(current_mileage, last_service_mileage)
       battery = NubbinBattery(current_date, last_service_date)
    
    if tire_type == "CarriganTire":
        tire = CarriganTire(TireSesnorArray())
    elif tire_type == "OctoprimeTire":
        tire = OctoprimeTire(TireSesnorArray())
    else:
        raise ValueError("Invalid tire type. Choose between 'CarriganTire' and 'OctoprimeTire'.")

    
    car = Car(engine, battery, tire)
    return car


