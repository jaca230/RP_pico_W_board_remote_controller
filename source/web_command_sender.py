class WebCommandSender:
    def __init__(self, web_controller):
        """
        Initialize the command sender with the web controller.
        :param web_controller: An instance of WebController to handle HTTP communication.
        """
        self.web_controller = web_controller

    def _format_args(self, *args):
        """
        Private method to format arguments: handle strings, numbers, and dictionaries.
        """
        formatted_args = []
        for arg in args:
            if isinstance(arg, dict):
                formatted_args.append(arg)  # Directly append dictionary without string formatting
            elif isinstance(arg, str):
                formatted_args.append(arg)  # Strings don't need explicit quoting
            elif isinstance(arg, bool):
                formatted_args.append(arg)  # Booleans remain as is (True/False)
            else:
                formatted_args.append(arg)  # Numbers are handled as they are
        return formatted_args

    def send_command(self, command_name, *args):
        """
        Send a command to the webserver with the given command name and arguments.
        """
        # Prepare the payload
        data = {"command": command_name}
        if args:
            formatted_args = self._format_args(*args)
            data["args"] = formatted_args

        # Send the command using WebController
        return self.web_controller.send_command("run_command", data)
