from utils import TireSesnorArray

from Carrigan_tires import CarriganTire



#Shows the Sensor Array & then Gives accordingly if it needs Service or not

sensorArray = TireSesnorArray()

tire = CarriganTire(sensorArray)
        
print(tire.needs_service());
print(sensorArray)

   
        
       
