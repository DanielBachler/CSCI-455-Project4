import sys
import robotDriver
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage

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
    def __init__(self):
        super().__init__()
        
    def init_UI(self):
        # File bar menu

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Widgets within central widget

        # Buttons for commands
        # Button Size controller
        btn_size = QSize(100,100)
        # Motors
        motors = QPushButton()
        motors.setIcon(QIcon("images/motors.png"))
        motors.setIconSize(btn_size)
        motors.setFixedSize(btn_size)
        motors.clicked.connect(self.test)

        # Headtilt
        headtilt = QPushButton()
        headtilt.setIcon(QIcon("images/headtilt.png"))
        headtilt.setIconSize(btn_size)
        headtilt.setFixedSize(btn_size)

        # Headturn
        headturn = QPushButton()
        headturn.setIcon(QIcon("images/headturn.png"))
        headturn.setIconSize(btn_size)
        headturn.setFixedSize(btn_size)

        # Bodyturn
        bodyturn = QPushButton()
        bodyturn.setIcon(QIcon("images/bodyturn.png"))
        bodyturn.setIconSize(btn_size)
        bodyturn.setFixedSize(btn_size)

        # Pause
        pause = QPushButton()
        pause.setIcon(QIcon("images/pause.png"))
        pause.setIconSize(btn_size)
        pause.setFixedSize(btn_size)

        # 8 Instruction boxes, use image sized buttons for it, each gets its own configure button
        # Use an array of buttons
        instructions = []
        # Array of config buttons
        config_buttons = []
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
            instruction.setIconSize(btn_size)
            # Set button size
            instruction.setFixedSize(btn_size)
            # Add to array
            instructions.append(instruction)

            # Make config button
            config_button = QPushButton("Configure\nCommand")
            c_name = "config_btn" + str(i)
            config_button.setObjectName(c_name)
            config_button.setFixedWidth(100)
            config_buttons.append(config_button)


        # Play and stop button
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_robot)

        stop_button = QPushButton("Stop")
        stop_button.clicked.connect(self.stop_robot)

        # Buttons?
        # Configure button (Under QListWidget)
        configure_button = QPushButton("Configure\nCommand")
        configure_button.setFixedWidth(100)
        configure_button.clicked.connect(self.configure_command)

        # Add to layouts
        # Main HBox
        main_hbox = QHBoxLayout()

        # Box for images in middle
        image_grid = QGridLayout()
        for i in range(0,8):
            # Add command to layout
            image_grid.addWidget(instructions[i], 0, i)
            image_grid.addWidget(config_buttons[i], 1, i)

        # VBox for start and stop
        start_stop_box = QVBoxLayout()
        start_stop_box.addWidget(start_button)
        start_stop_box.addWidget(stop_button)

        # VBox for QList and configure button
        command_box = QVBoxLayout()
        command_box.addWidget(motors)
        command_box.addWidget(headtilt)
        command_box.addWidget(headturn)
        command_box.addWidget(bodyturn)
        command_box.addWidget(pause)

        # Add to main box
        main_hbox.addLayout(command_box)
        main_hbox.addLayout(image_grid)
        main_hbox.addLayout(start_stop_box)

        # Set layout on central widget
        central_widget.setLayout(main_hbox)

        # Finalize geometry
        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Robot Control UI')
        self.show()

    # start_robot: Starts the robot on the programmed sequence
    # ARGS: None
    # RETURNS: None
    def start_robot(self):
        pass

    # stop_robot: Stops the robot executing the current sequence
    # ARGS: None
    # RETURNS: None
    def stop_robot(self):
        pass

    # configure_command: Gives pop up where current command can be configured
    # ARGS: None?
    # RETURNS: None
    def configure_command(self):
        pass

    def test(self):
        print("Clicked")
   
main()
    