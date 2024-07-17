# SIPp GUI

A graphical user interface (GUI) for the SIPp performance testing tool, developed using Python and PyQt5. This tool aims to simplify the use of SIPp by providing a user-friendly interface for configuring and running SIP performance tests.

## Features

- Easy selection of SIPp executable and scenario files
- Input fields for target SIP server IP, number of calls, and call rate
- Additional options for custom SIPp command-line parameters
- One-click execution of SIPp tests

## Prerequisites

### Install SIPp

SIPp is a performance testing tool for the SIP protocol. You need to install SIPp on your system before using the GUI. Follow the instructions on the [SIPp Sourceforge page](https://sipp.sourceforge.net/).

## Installation

1. Clone this repository:

```
git clone https://github.com/asylvestro34/SIPp_GUI.git
cd SIPp_GUI
```

2. Install the required Python package:

```
pip install PyQt5
```

## Usage

1. Run the 'sipp_gui.py' script:

```
python sipp_gui.py
```

2. The GUI will open, and you can configure your SIPp test by filling in the required fields:

- SIPp Executable: Path to the SIPp executable file.
- Scenario File: Path to the XML scenario file.
- Target SIP Server IP: IP address of the target SIP server.
- Number of Calls: Total number of SIP calls to generate.
- Call Rate: Rate of calls per second.
- Additional Options: Any additional SIPp command-line options.

3. Click the "Run SIPp" button to execute the SIPp test. The constructed SIPp command will be displayed in the console.

## Example

Here's an example of how to use the SIPp GUI:

1. Click the "Browse" button next to "SIPp Executable" and select the SIPp executable file.
2. Click the "Browse" button next to "Scenario File" and select your SIP scenario XML file.
3. Enter the IP address of your target SIP server in the "Target SIP Server IP" field.
4. Enter the total number of calls in the "Number of Calls" field.
5. Enter the call rate (calls per second) in the "Call Rate" field.
6. (Optional) Enter any additional SIPp command-line options in the "Additional Options" field.
7. Click the "Run SIPp" button to start the test.

## Contributing

Contributions are welcome! Please submit pull requests or open issues to improve the SIPp GUI.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


























