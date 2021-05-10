import smbus
import time
bus = smbus.SMBus(1)
address = 0x70


#SRF08 REQUIRES 5V
time.sleep(1)

def lightlevel():
        light = bus.read_byte_data(address, 1)
        return light
    
    
def brightness(light):
    if light <50:
        print("Too Dark")
    if light >50 and light <100:
        print("Dark")
    if light >100 and light <150:
        print("Medium")
    if light >150 and light <200:
        print("Bright")   
    if light >200 and light <250:
        print("Too Bright")  

while True:
       
        time.sleep(0.7)
        lightlvl = lightlevel()
        
        print(brightness(lightlvl))
       
