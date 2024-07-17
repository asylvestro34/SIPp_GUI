import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox, QRadioButton,
                             QGroupBox, QComboBox, QSpinBox)


class SIPpUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the layout
        grid = QGridLayout()
        grid.setSpacing(10)

        # Radio buttons for server/client selection
        self.modeGroup = QGroupBox("Mode")
        self.clientButton = QRadioButton("Client")
        self.serverButton = QRadioButton("Server")
        self.clientButton.setChecked(True)

        modeLayout = QHBoxLayout()
        modeLayout.addWidget(self.clientButton)
        modeLayout.addWidget(self.serverButton)
        self.modeGroup.setLayout(modeLayout)

        self.serverButton.toggled.connect(self.toggleMode)

        grid.addWidget(self.modeGroup, 0, 0, 1, 3)

        # Labels and input fields
        self.sippLabel = QLabel('SIPp Executable:')
        self.sippPath = QLineEdit()
        self.sippBrowse = QPushButton('Browse')
        self.sippBrowse.clicked.connect(self.browseSIPP)

        self.scenarioLabel = QLabel('Scenario File:')
        self.scenarioPath = QLineEdit()
        self.scenarioBrowse = QPushButton('Browse')
        self.scenarioBrowse.clicked.connect(self.browseScenario)

        self.serverLabel = QLabel('Target SIP Server IP:')
        self.serverIP = QLineEdit()

        self.callsLabel = QLabel('Number of Calls:')
        self.numCalls = QSpinBox()
        self.numCalls.setValue(1)
        self.numCalls.setMinimum(1)

        self.durationLabel = QLabel('Test Duration:')
        self.hoursLabel = QLabel('Hours:')
        self.hoursInput = QSpinBox()
        self.hoursInput.setRange(0, 24)
        self.minutesLabel = QLabel('Minutes:')
        self.minutesInput = QSpinBox()
        self.minutesInput.setRange(0, 59)
        self.secondsLabel = QLabel('Seconds:')
        self.secondsInput = QSpinBox()
        self.secondsInput.setRange(0, 59)

        self.qosLabel = QLabel('QoS Value:')
        self.qosDropdown = QComboBox()
        self.qosDropdown.addItems(["DSCP - BE",
                                   "DSCP - CS1",
                                   "DSCP - AF11",
                                   "DSCP - AF12",
                                   "DSCP - AF13",
                                   "DSCP - CS2",
                                   "DSCP - AF21",
                                   "DSCP - AF22",
                                   "DSCP - AF23",
                                   "DSCP - CS3",
                                   "DSCP - AF31",
                                   "DSCP - AF32",
                                   "DSCP - AF33",
                                   "DSCP - CS4",
                                   "DSCP - AF41",
                                   "DSCP - AF42",
                                   "DSCP - AF43",
                                   "DSCP - CS5",
                                   "DSCP - EF",
                                   "DSCP - CS6",
                                   "DSCP - CS7"])

        self.optionsLabel = QLabel('Additional Options:')
        self.options = QLineEdit()

        self.monitorLabel = QLabel('Monitoring Sessions:')
        self.monitorLabel.setVisible(False)

        self.monitorSession = QLineEdit()
        self.monitorSession.setVisible(False)

        # Run button
        self.runButton = QPushButton('Run SIPp')
        self.runButton.clicked.connect(self.runSIPP)

        # Layout positioning
        grid.addWidget(self.sippLabel, 1, 0)
        grid.addWidget(self.sippPath, 1, 1)
        grid.addWidget(self.sippBrowse, 1, 2)

        grid.addWidget(self.scenarioLabel, 2, 0)
        grid.addWidget(self.scenarioPath, 2, 1)
        grid.addWidget(self.scenarioBrowse, 2, 2)

        grid.addWidget(self.serverLabel, 3, 0)
        grid.addWidget(self.serverIP, 3, 1, 1, 2)

        grid.addWidget(self.callsLabel, 4, 0)
        grid.addWidget(self.numCalls, 4, 1, 1, 2)

        grid.addWidget(self.durationLabel, 5, 0)
        grid.addWidget(self.hoursLabel, 6, 0)
        grid.addWidget(self.hoursInput, 6, 1)
        grid.addWidget(self.minutesLabel, 7, 0)
        grid.addWidget(self.minutesInput, 7, 1)
        grid.addWidget(self.secondsLabel, 8, 0)
        grid.addWidget(self.secondsInput, 8, 1)

        grid.addWidget(self.qosLabel, 9, 0)
        grid.addWidget(self.qosDropdown, 9, 1, 1, 2)

        grid.addWidget(self.optionsLabel, 10, 0)
        grid.addWidget(self.options, 10, 1, 1, 2)

        grid.addWidget(self.monitorLabel, 11, 0)
        grid.addWidget(self.monitorSession, 11, 1, 1, 2)

        grid.addWidget(self.runButton, 12, 0, 1, 3)

        self.setLayout(grid)

        self.setWindowTitle('SIPp GUI')
        self.show()

    def toggleMode(self):
        if self.serverButton.isChecked():
            self.serverLabel.setVisible(False)
            self.serverIP.setVisible(False)
            self.callsLabel.setVisible(False)
            self.numCalls.setVisible(False)
            self.durationLabel.setVisible(False)
            self.hoursLabel.setVisible(False)
            self.hoursInput.setVisible(False)
            self.minutesLabel.setVisible(False)
            self.minutesInput.setVisible(False)
            self.secondsLabel.setVisible(False)
            self.secondsInput.setVisible(False)
            self.qosLabel.setVisible(False)
            self.qosDropdown.setVisible(False)
            self.optionsLabel.setVisible(False)
            self.options.setVisible(False)
            self.monitorLabel.setVisible(True)
            self.monitorSession.setVisible(True)
        else:
            self.serverLabel.setVisible(True)
            self.serverIP.setVisible(True)
            self.callsLabel.setVisible(True)
            self.numCalls.setVisible(True)
            self.durationLabel.setVisible(True)
            self.hoursLabel.setVisible(True)
            self.hoursInput.setVisible(True)
            self.minutesLabel.setVisible(True)
            self.minutesInput.setVisible(True)
            self.secondsLabel.setVisible(True)
            self.secondsInput.setVisible(True)
            self.qosLabel.setVisible(True)
            self.qosDropdown.setVisible(True)
            self.optionsLabel.setVisible(True)
            self.options.setVisible(True)
            self.monitorLabel.setVisible(False)
            self.monitorSession.setVisible(False)

        # Adjust the size of the window dynamically
        self.adjustSize()

    def browseSIPP(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select SIPp Executable", "",
                                                  "Executables (*.exe);;All Files (*)", options=options)
        if fileName:
            self.sippPath.setText(fileName)

    def browseScenario(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Scenario File", "", "XML Files (*.xml);;All Files (*)",
                                                  options=options)
        if fileName:
            self.scenarioPath.setText(fileName)

    def runSIPP(self):
        sipp_executable = self.sippPath.text()
        scenario_file = self.scenarioPath.text()
        server_ip = self.serverIP.text()
        num_calls = self.numCalls.value()
        duration = f"{self.hoursInput.value()}h{self.minutesInput.value()}m{self.secondsInput.value()}s"
        qos_value = self.qosDropdown.currentText()
        additional_options = self.options.text()
        monitoring_session = self.monitorSession.text()

        if not sipp_executable or not scenario_file:
            QMessageBox.warning(self, 'Input Error', 'Please fill in the required fields.')
            return

        if self.serverButton.isChecked():
            command = f'{sipp_executable} -sn {scenario_file} {monitoring_session}'
        else:
            if not server_ip or not num_calls or not duration:
                QMessageBox.warning(self, 'Input Error', 'Please fill in the required fields.')
                return
            command = f'{sipp_executable} -sf {scenario_file} {server_ip} -m {num_calls} -d {duration} -q {qos_value} {additional_options}'

        print(f'Executing: {command}')
        # Execute the command here
        # os.system(command)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SIPpUI()
    sys.exit(app.exec_())
