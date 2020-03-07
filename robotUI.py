import sys
import robotDriver
import controls
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QFont

app = None

def main():
    app = QApplication(sys.argv)
    main_window = UI()
    main_window.init_UI()
    sys.exit(app.exec_())

# Have QList with commands (objects?)
# 8 empty boxes that can be clicked to fill with commands
# configure button for selected command
# 
class UI(QMainWindow):
    # Class vars
    # List of commands to be executed
    command_list = [None] * 8

    # List of control objects
    controllers = [None] * 8

    # Current head position
    head_pos = 0

    # List of config buttons
    config_buttons = []

    # List of images
    instructions = []

    # Button Size controller
    btn_size = QSize(80,80)

    # Blank config window
    config_window = ""

    def __init__(self):
        super().__init__()

    # init_UI: Initializes the UI for the UI class
    # ARGS: None
    # RETURNS: None
    def init_UI(self):
        # File bar menu

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Widgets within central widget

        # Buttons for commands
        
        # Motors
        motors = QPushButton()
        motors.setIcon(QIcon("images/motors.png"))
        motors.setIconSize(self.btn_size)
        motors.setFixedSize(self.btn_size)
        motors.clicked.connect(lambda: self.add_command("motor"))

        # Headtilt
        headtilt = QPushButton()
        headtilt.setIcon(QIcon("images/headtilt.png"))
        headtilt.setIconSize(self.btn_size)
        headtilt.setFixedSize(self.btn_size)
        headtilt.clicked.connect(lambda: self.add_command("head_tilt"))

        # Headturn
        headturn = QPushButton()
        headturn.setIcon(QIcon("images/headturn.png"))
        headturn.setIconSize(self.btn_size)
        headturn.setFixedSize(self.btn_size)
        headturn.clicked.connect(lambda: self.add_command("head_turn"))

        # Bodyturn
        bodyturn = QPushButton()
        bodyturn.setIcon(QIcon("images/bodyturn.png"))
        bodyturn.setIconSize(self.btn_size)
        bodyturn.setFixedSize(self.btn_size)
        bodyturn.clicked.connect(lambda: self.add_command("body_turn"))

        # Pause
        pause = QPushButton()
        pause.setIcon(QIcon("images/pause.png"))
        pause.setIconSize(self.btn_size)
        pause.setFixedSize(self.btn_size)
        pause.clicked.connect(lambda: self.add_command("pause"))

        # 8 Instruction boxes, use image sized buttons for it, each gets its own configure button
        # Default icon
        default_icon = QIcon("images/blank.png")
        # Create 8 boxes
        for i in range(0, 8):
            # Make button
            instruction = QPushButton()
            # Get unique name in order
            name = "instruction" + str(i)
            # Set name
            instruction.setObjectName(name)
            # Set icon
            instruction.setIcon(default_icon)
            # Set icon size
            instruction.setIconSize(self.btn_size)
            # Set button size
            instruction.setFixedSize(self.btn_size)
            # Add to array
            self.instructions.append(instruction)

            # Make config button
            config_button = QPushButton("Configure\nCommand")
            c_name = "config_btn" + str(i)
            config_button.setObjectName(c_name)
            config_button.setFixedWidth(80)
            self.config_buttons.append(config_button)

        # Set up config buttons clicked commands
        self.config_buttons[0].clicked.connect(lambda: self.configure_command(self.config_buttons[0].objectName()))
        self.config_buttons[1].clicked.connect(lambda: self.configure_command(self.config_buttons[1].objectName()))
        self.config_buttons[2].clicked.connect(lambda: self.configure_command(self.config_buttons[2].objectName()))
        self.config_buttons[3].clicked.connect(lambda: self.configure_command(self.config_buttons[3].objectName()))
        self.config_buttons[4].clicked.connect(lambda: self.configure_command(self.config_buttons[4].objectName()))
        self.config_buttons[5].clicked.connect(lambda: self.configure_command(self.config_buttons[5].objectName()))
        self.config_buttons[6].clicked.connect(lambda: self.configure_command(self.config_buttons[6].objectName()))
        self.config_buttons[7].clicked.connect(lambda: self.configure_command(self.config_buttons[7].objectName()))

        # Play and stop button
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_robot)

        stop_button = QPushButton("Stop")
        stop_button.clicked.connect(self.stop_robot)

        # Remove last added item button
        remove_last_added = QPushButton("Remove")
        remove_last_added.setToolTip("Removes the last added command from the list")
        remove_last_added.clicked.connect(self.remove)

        # Buttons?

        # Add to layouts
        # Main HBox
        main_hbox = QHBoxLayout()

        # Box for images in middle
        image_grid = QGridLayout()
        for i in range(0,8):
            # Add command to layout
            image_grid.addWidget(self.instructions[i], 0, i)
            image_grid.addWidget(self.config_buttons[i], 1, i)

        # HBox for start and stop
        start_stop_box = QHBoxLayout()
        start_stop_box.addWidget(start_button)
        start_stop_box.addWidget(remove_last_added)
        start_stop_box.addWidget(stop_button)

        # Vbox for buttons and command images
        button_command_box = QVBoxLayout()
        button_command_box.addLayout(start_stop_box)
        button_command_box.addLayout(image_grid)

        # VBox for QList and configure button
        command_box = QVBoxLayout()
        command_box.addWidget(motors)
        command_box.addWidget(headtilt)
        command_box.addWidget(headturn)
        command_box.addWidget(bodyturn)
        command_box.addWidget(pause)

        # Add to main box
        main_hbox.addLayout(command_box)
        main_hbox.addLayout(button_command_box)
        #main_hbox.addLayout(image_grid)
        #main_hbox.addLayout(start_stop_box)

        # Set layout on central widget
        central_widget.setLayout(main_hbox)

        # Finalize geometry
        self.setGeometry(0, 0, 480, 200)
        self.setWindowTitle('Robot Control UI')
        self.show()

    # start_robot: Starts the robot on the programmed sequence
    # ARGS: None
    # RETURNS: None
    def start_robot(self):
        print("---------")
        for command in self.command_list:
            print(command)

    # stop_robot: Stops the robot executing the current sequence
    # ARGS: None
    # RETURNS: None
    def stop_robot(self):
        pass

    # configure_command: Gives pop up where current command can be configured
    # ARGS: None?
    # RETURNS: None
    def configure_command(self, button):
        index = int(button[-1])
        # Error checking to ensure you cant configure a command that doesnt exist
        if self.command_list[index] is not None:
            control_object = self.controllers[index]
            # Make config window
            self.edit_window = ConfigUI(self, control_object, index)
            self.edit_window.init_UI()
        else:
            QMessageBox.question(self, "Error", "No command to configure", QMessageBox.Close, QMessageBox.Close)

    # remove: Removes the last added command
    # ARGS: None
    # RETURNS: None
    def remove(self):
        if self.head_pos > 0:
            self.head_pos -= 1
            self.command_list[self.head_pos] = None
            self.controllers[self.head_pos] = None
            self.update_commands()
        else:
            QMessageBox.question(self, "Error", "Cannot remove more commands", QMessageBox.Close, QMessageBox.Close)

    # add_commands: Refactored version of command adding functions, pass in args with lambda function
    # ARGS: command (String)
    # RETURNS: None
    def add_command(self, command):
        if self.head_pos < 8:
            self.command_list[self.head_pos] = command
            temp_controller = controls.Controller(command)
            self.controllers[self.head_pos] = temp_controller
            self.head_pos += 1
            self.update_commands()
        else:
            QMessageBox.question(self, "Error", "Cannot add more commands", QMessageBox.Close, QMessageBox.Close)

    def update_commands(self):
        for i in range(0,8):
            icon = QIcon("images/blank.png")
            cur_command = self.command_list[i]
            cur_instruction = self.instructions[i]

            if cur_command == "motor":
                icon = QIcon("images/motors.png")
            elif cur_command == "head_turn":
                icon = QIcon("images/headturn.png")
            elif cur_command == "head_tilt":
                icon = QIcon("images/headtilt.png")
            elif cur_command == "body_turn":
                icon = QIcon("images/bodyturn.png")
            elif cur_command == "pause":
                icon = QIcon("images/pause.png")

            cur_instruction.setIcon(icon)
            cur_instruction.setFixedSize(self.btn_size)
            cur_instruction.setIconSize(self.btn_size)

class ConfigUI(QWidget):
    # The parent window
    parent_window = QMainWindow

    # Object of control type
    control_object = controls.Controller

    # Spot var
    spot = None

    # Global font for object
    font = QFont("Comic Sans", 20)

    def __init__(self, parent_window, control_object, spot):
        super().__init__()
        self.parent_window = parent_window
        self.control_object = control_object
        self.spot = spot

    def init_UI(self):
        # Add edit forms here
        # Time duration field (QDoubleSpinBox)
        time_duration_label = QLabel("Duration:")
        time_duration_label.setFont(self.font)
        time_duration = QDoubleSpinBox()
        time_duration.setObjectName("time_duration")
        # Set properties for box
            # Max and min values
        time_duration.setMaximum(50.0)
        time_duration.setMinimum(0.0)
            # Step
        time_duration.setSingleStep(0.1)
            # Precision
        time_duration.setDecimals(1)
            # init value
        time_duration.setValue(self.control_object.duration)
        time_duration.setMinimumHeight(50)
        time_duration.setFont(self.font)

            # Box for time duration
        time_duration_box = QHBoxLayout()
        time_duration_box.addWidget(time_duration_label)
        time_duration_box.addWidget(time_duration)

        # Power input box (QSpinBox)
        power_label = QLabel("Power:")
        power_label.setFont(self.font)
        power = QSpinBox()
        power.setObjectName("power")
        # Set properties
            # Max and min values
        power.setMinimum(-100)
        power.setMaximum(100)
            # Interval
        power.setSingleStep(5)
        power.setSuffix("%")
        power.setValue(self.control_object.power)
        power.setMinimumHeight(50)
        power.setFont(self.font)

            # Box for power
        power_box = QHBoxLayout()
        power_box.addWidget(power_label)
        power_box.addWidget(power)

        # Update and close button
        update_button = QPushButton("Update")
        update_button.clicked.connect(self.update)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)

        # Button box
        button_box = QHBoxLayout()
        button_box.addWidget(update_button)
        button_box.addWidget(cancel_button)

        # Main Box
        main_box = QVBoxLayout()
        main_box.addLayout(time_duration_box)
        main_box.addLayout(power_box)
        main_box.addLayout(button_box)

        # Set main_box as main layout
        self.setLayout(main_box)

        # Finalize window
        self.setGeometry(200, 50, 400, 300)
        self.setWindowTitle('Configure %s at spot %d' % (self.control_object.controller_type, self.spot))
        self.show()

    def update(self):
        # Get input fields
        time_duration = self.findChild(QDoubleSpinBox, "time_duration")
        power = self.findChild(QSpinBox, "power")
        self.control_object.update(time_duration.value(), power.value())
        self.close()

main()
    