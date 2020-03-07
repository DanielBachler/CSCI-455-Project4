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
        if(inPercentage < 0): #Forward range
            return (50*inPercentage) #Returns a negative
        if(inPercentage >= 0):
            return (20*inPercentage)  

    def accelerate(self,inValue): #assumes we know the controller type. 
        
        print("inValue:", inValue)
        if(self.controller_type == "motor" and self.turning == False):
            if(inValue < 0):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(98)  
            if(inValue > 0):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(104)
        if(self.controller_type == "motor" and self.turning == True):
            if(inValue < 0):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(102)  
            if(inValue > 0):
                for i in range(int(round(abs(inValue)/100, 0))):
                    time.sleep(0.01)
                    self.driver.control(100)                                                      
        if(self.controller_type == "body_turn"):
            if(inValue < 0):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(40)  
            if(inValue > 0):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(38)
        if(self.controller_type == "head_tilt"):
            if(inValue < 0):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(52)  
            if(inValue > 0):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(54) 
        if(self.controller_type == "head_turn"):
            if(inValue < 0):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(24)  
            if(inValue > 0):
                for i in range(int(round(abs(inValue)/200, 0))):
                    time.sleep(0.01)
                    self.driver.control(26)                                                           
    def stop(self):
        self.driver.control(65)

    def run(self):
        print("Power:", self.power)
        try:
            self.accelerate(self.parsePercentage(self.power))
        except:
            print("Missing Commmand.") 
        time.sleep(self.duration)
        self.stop()