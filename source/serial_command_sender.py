import json

class SerialCommandSender:
    def __init__(self, serial_controller):
        """Initialize the PWM remote controller with serial interface."""
        self.serial_controller = serial_controller

    def _capitalize_booleans_in_json(self, json_str):
        """Fix the capitalization of booleans in a JSON string (True/False instead of true/false)."""
        # Replace lowercase true/false with capitalized True/False
        return json_str.replace('true', 'True').replace('false', 'False')

    def _format_args(self, *args):
        """Private method to format arguments: handle strings, numbers, and dictionaries."""
        formatted_args = []
        for arg in args:
            if isinstance(arg, dict):
                # Convert dictionary to a JSON string representation
                json_str = json.dumps(arg)
                # Perform a second pass to capitalize booleans
                formatted_args.append(self._capitalize_booleans_in_json(json_str))
            elif isinstance(arg, str):
                # Keep quotes around strings
                formatted_args.append(f"\"{arg}\"")
            elif isinstance(arg, bool):
                # Convert boolean to proper capitalized string representation
                formatted_args.append("True" if arg else "False")
            else:
                # Convert non-strings to string
                formatted_args.append(str(arg))
        return formatted_args

    def send_command(self, command_name, *args):
        """Send a command to the Pico (PWM-related or list commands)."""
        # Start the command string
        command_string = f"run_command(\"{command_name}\""
        
        # If there are arguments, format them correctly
        if args:
            formatted_args = self._format_args(*args)
            # Join arguments with commas and append to the command string
            command_string += f",{', '.join(formatted_args)}"
        
        # Close the command string and send
        command_string += ")"
        
        return self.serial_controller.send_command(command_string)
