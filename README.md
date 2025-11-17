# Pico Board Remote Controller

The **Pico Board Remote Controller** is a Python-based library for controlling the Raspberry Pi Pico W board via serial or Wi-Fi communication. It provides functionality for managing GPIO, PWM, and other hardware components through an easy-to-use interface. The controller can send commands to the board for configuring, controlling, and retrieving hardware settings, making it ideal for embedded projects.

## Features

- **Wi-Fi and Serial Communication**: Supports communication via both Wi-Fi and serial interfaces for flexible use cases.
- **GPIO Control**: Create, start, and control GPIO hardware like LEDs, buttons, and more.
- **PWM Management**: Send commands to control PWM pins for hardware such as motors or servos.
- **Double Pulse Generation**: Configure the PIO-based double pulse trigger used for HDSoC deadtime measurements with nanosecond-scale spacing.
- **Configuration Management**: Save, load, and apply configuration settings for easy setup and replication.
- **Cross-Platform**: Works across different platforms where Python and the necessary dependencies are available.

## Installation

### Board Files
Upload the board files to your pico following the README on the [board files github page](https://github.com/jaca230/RP_pico_W_board_interface)

### Dependencies
To use the Pico Board Remote Controller, you need to install the following Python dependencies:

- **requests**: For HTTP communication when using Wi-Fi mode.
- **pyserial**: For serial communication when using the serial mode.

You can install them using `pip`:

```bash
pip install requirements.txt
```

## Usage
See [Example Jupyter Notebooks](https://github.com/jaca230/RP_pico_W_board_remote_controller/tree/main/examples).

### Double Pulse Generator
Use `examples/double_pulse_generator.ipynb` to interactively create and tune the pulse pair that drives the deadtime measurements. The notebook walks through:

- Connecting to the Pico over serial (or Wi-Fi by swapping in `WebCommandSender`).
- Creating a `double_pulse` hardware block with the desired pin, repetition rate, pulse width, and separation.
- Applying live updates to the separation or rate to sweep the HDSoC under test.
- Stopping and deleting the hardware once the measurement is complete.

The remote commands mirror the firmware interface:

```python
settings = {
    'pin_number': 15,
    'repetition_rate_hz': 5000,
    'pulse_width_ns': 500,
    'separation_ns': 2000
}
command_sender.send_command('create', 'double_pulse', settings, 'double_pulse_gen')
command_sender.send_command('start', 'double_pulse_gen')
command_sender.send_command('apply_hardware_settings', 'double_pulse_gen', {'separation_ns': 800})
```

Note that the `WebCommandSender` and `SerialCommandSender` examples are interchangable. I.e. `WebCommandSender.send_command(args*)` and `SerialCommandSender.send_command(args*)` perform the exact same functionality on the board, the only difference is how the information gets communciated to the board.


## Configuration

You can save and load the configuration at any time to preserve your hardware setup between sessions. Commands like `save_config` and `load_config` allow for persistent hardware configurations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links
- [Raspberry Pi Pico Documentation](https://www.raspberrypi.org/documentation/pico/)
- [PySerial Documentation](https://pythonhosted.org/pyserial/)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)

