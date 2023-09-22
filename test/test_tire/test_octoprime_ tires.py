from utils import TireSesnorArray

from octoprime import OctoprimeTire



#Prints out the Sensor Array & then Gives accordingly if it needs Service or not

sensorArray = TireSesnorArray()

tire = OctoprimeTire(sensorArray)
        
print(tire.needs_service());

print(sum(sensorArray));

   
        
       
