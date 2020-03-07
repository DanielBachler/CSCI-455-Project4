# Add objects that control the robot here
class Controller:
    # Has the 5 types with different functions based on type
    controller_type = ""

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
