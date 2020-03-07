# Add objects that control the robot here
import time
import robotDriver
class Controller:
    # Has the 5 types with different functions based on type
    controller_type = ""
    driver = robotDriver.RobotControl() 
    # Temp data for testing
    duration = 0
    # Use percentage of total speed (more user friendly)
    power = 0 
    # Turning, only for motor type
    turning = False

    def __init__(self, controller_type):
        self.controller_type = controller_type

    def update(self, duration, power, turning=False):
        self.duration = duration
        self.power = power
        self.turning = turning
        print("Updated command")

    def parsePercentage(self, inPercentage):
        if(self.controller_type == "motor"):
            if(inPercentage < 0): #Forward range
                return (-50*inPercentage) #Returns a negative
            if(inPercentage >= 0):
                return (20*inPercentage)  

    def accelerate(self,inValue): #assumes we know the controller type. 
        print("inValue:", inValue)
        if(self.controller_type == "motor"):
            if(inValue < 6000):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(98)  
            if(inValue > 6000):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(98)                                

    def stop(self):
        if(self.controller_type == "motor"):
            # YEET
            self.driver.control(65)

    def run(self):
        print("Power:", self.power)
        self.accelerate(self.parsePercentage(self.power)) 
        time.sleep(self.duration)
        self.stop()