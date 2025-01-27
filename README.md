# Pico Board Remote Controller

The **Pico Board Remote Controller** is a Python-based library for controlling the Raspberry Pi Pico W board via serial or Wi-Fi communication. It provides functionality for managing GPIO, PWM, and other hardware components through an easy-to-use interface. The controller can send commands to the board for configuring, controlling, and retrieving hardware settings, making it ideal for embedded projects.

## Features

- **Wi-Fi and Serial Communication**: Supports communication via both Wi-Fi and serial interfaces for flexible use cases.
- **GPIO Control**: Create, start, and control GPIO hardware like LEDs, buttons, and more.
- **PWM Management**: Send commands to control PWM pins for hardware such as motors or servos.
- **Configuration Management**: Save, load, and apply configuration settings for easy setup and replication.
- **Cross-Platform**: Works across different platforms where Python and the necessary dependencies are available.

## Installation

To use the Pico Board Remote Controller, you need to install the following Python dependencies:

### Dependencies

- **requests**: For HTTP communication when using Wi-Fi mode.
- **pyserial**: For serial communication when using the serial mode.

You can install them using `pip`:

```bash
pip install requirements.txt
```

## Usage
See [Example Jupyter Notebooks](https://github.com/jaca230/RP_pico_W_board_remote_controller/tree/main/examples).


## Configuration

You can save and load the configuration at any time to preserve your hardware setup between sessions. Commands like `save_config` and `load_config` allow for persistent hardware configurations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links
- [Raspberry Pi Pico Documentation](https://www.raspberrypi.org/documentation/pico/)
- [PySerial Documentation](https://pythonhosted.org/pyserial/)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)