import sys
import os

# Add the "source" directory to the path
script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the script
source_dir = os.path.join(script_dir, 'source')  # Assuming "source" is in the same directory as the script
sys.path.append(source_dir)  # Add source directory to sys.path

from serial_controller import SerialController
from serial_command_sender import SerialCommandSender
from web_controller import WebController
from web_command_sender import WebCommandSender
import time

# Global variable to select between WiFi or Serial communication
USE_WIFI = False  # Set to False for Serial communication, True for WiFi
BASE_URL = "http://192.168.50.199:8080" # Change to the appropriate IP address and port

def main():
    if USE_WIFI:
        # Initialize the web controller with the base URL of the webserver
        web_controller = WebController(base_url=BASE_URL, debug=True)
        # Initialize the command sender
        command_sender = WebCommandSender(web_controller)
    else:
        # Initialize the serial controller with the appropriate port
        serial_controller = SerialController(port="COM6", debug=True)  # Adjust port as needed
        serial_controller.connect()
        # Initialize the command sender
        command_sender = SerialCommandSender(serial_controller)

    try:
        # List available commands
        print("Available commands:")
        response = command_sender.send_command('list_commands')
        print(response)

        # Get the entire configuration
        print("Current configuration:")
        response = command_sender.send_command('get_all_config')
        print(response)

        # Create a GPIO hardware (like an LED)
        settings = {
            'pin_number': "LED",
            'mode': 'OUT',
            'value': 0,
            'start_on_init': True
        }
        print(command_sender.send_command('create', 'gpio', settings, "test_gpio"))

        # Start the GPIO hardware
        print(command_sender.send_command('start', 'test_gpio'))

        # Set GPIO value to 1 (turn on LED)
        print(command_sender.send_command('apply_hardware_settings', 'test_gpio', {'value': 1}))

        # Get the updated configuration
        print("Updated configuration (after turning LED on):")
        print(command_sender.send_command('get_all_config'))

        time.sleep(1)  # Wait for 1 second

        # Set GPIO value back to 0 (turn off LED)
        print(command_sender.send_command('apply_hardware_settings', 'test_gpio', {'value': 0}))

        # Get the updated configuration
        print("Updated configuration (after turning LED off):")
        print(command_sender.send_command('get_all_config'))

                # Set GPIO value back to 0 (turn off LED)
        print(command_sender.send_command('apply_hardware_settings', 'test_gpio', {'value': 1}))

        # Save the current configuration
        print("Saving current configuration...")
        print(command_sender.send_command('save_config'))

        # Delete the test GPIO hardware
        print(command_sender.send_command('delete', 'test_gpio'))

        # Get the entire configuration
        print("Updated configuration (after deleting test GPIO):")
        print(command_sender.send_command('get_all_config'))

        time.sleep(1)  # Wait for 1 second

        # Load the saved configuration
        print("Loading saved configuration...")
        print(command_sender.send_command('load_config'))

        # Get the entire configuration
        print("Updated configuration (after loading saved config):")
        print(command_sender.send_command('get_all_config'))

        # Optionally, apply the saved configuration again
        print(command_sender.send_command('apply_config'))

    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the serial connection if using Serial
        if not USE_WIFI:
            serial_controller.close()

if __name__ == "__main__":
    main()
