# SIPp GUI

A simple graphical user interface (GUI) for SIPp, allowing users to easily configure and execute SIP tests as either a client or server.

## Features

- **Mode Selection**: Choose between Client and Server modes.
- **Scenario File Selection**: Load SIP scenario files (XML format).
- **SIPp Executable Path**: Browse and set the path to the SIPp executable, which is saved for future use.
- **Dynamic Interface**: Automatically adjusts the interface based on the selected mode.
- **Quality of Service (QoS)**: Specify QoS values using a dropdown for DSCP options.
- **Call Configuration**: Set the number of calls and duration for the test.

## Requirements

- Python 3.x
- PyQt5
- SIPp (download from [SIPp GitHub](https://github.com/SIPp/sipp))

## Installation

1. **Clone the repository:**

   ```
   bash
   git clone https://github.com/yourusername/sipp-gui.git
   cd sipp-gui
   ```

2. Install the required Python package:

    ```
    pip install PyQt5
    ```

3. Ensure SIPp is installed on your system.

## Usage

1. Run the application:

    ```
    python sipp_gui.py
    ```

2. Set the SIPp executable:

    - Click on the "Browse" button next to "SIPp Executable" to select the SIPp executable. This path will be saved for future runs.

3. Select a mode:

    - Choose either **Client** or **Server** mode. The interface will dynamically adjust to show relevant fields.

4. Fill in the necessary fields:

### Client Mode Fields

| Field                     | Description                              |
|---------------------------|------------------------------------------|
| **Target SIP Server IP**  | The IP address of the SIP server         |
| **Number of Calls**       | Total calls to initiate (default: 1)     |
| **Test Duration**         |                                          |
| &nbsp;&nbsp;**Hours**     | Hours for test duration (0-24)           |
| &nbsp;&nbsp;**Minutes**   | Minutes for test duration (0-59)         |
| &nbsp;&nbsp;**Seconds**   | Seconds for test duration (0-59)         |
| **QoS Value**             | DSCP options (e.g., EF, AF1, etc.)       |
| **Additional Options**    | Any extra parameters for SIPp            |

### Server Mode Fields

| Field                   | Description                                |
|-------------------------|--------------------------------------------|
| **Monitoring Sessions** | Details for monitoring incoming SIP calls  |

## Contributing

Contributions are welcome! Please submit pull requests or open issues to improve the SIPp GUI.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/asylvestro34/SIPp_GUI/blob/main/LICENSE) file for details.


























