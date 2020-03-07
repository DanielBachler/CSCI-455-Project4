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

    def __init__(self, controller_type):
        self.controller_type = controller_type

    def update(self, duration, power):
        self.duration = duration
        self.power = power
        print("Updated command")

    def parsePercentage(self, inPercentage):
        if(self.controller_type == "motor"):
            if(inPercentage < 0): #Forward range
                return (-50*inPercentage) #Returns a negative
            if(inPercentage >= 0):
                return (50*inPercentage)  

    def accelerate(self,inValue): #assumes we know the controller type. 
        print("inValue:", inValue)
        if(self.controller_type == "motor"):
            if(inValue < 6000):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.2)
                    self.driver.control(98)             

    def stop(self):
        if(self.controller_type == "motor"):
            self.driver.control(65)

    def motor(self, duration, power):
        # start_time = time.time()
        # for i in range(duration):
        #     accelerate(parsePercentage(20))
        #     time.sleep(start_time + i*duration - time.time())
        # self.stop()
        print("Power:", power)
        self.accelerate(self.parsePercentage(power)) 
        time.sleep(self.duration)
        self.stop()

    def run(self):
        self.motor(self.duration, self.power)