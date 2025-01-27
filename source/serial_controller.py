import serial
import re  # Regular expression module

class SerialController:
    def __init__(self, port, baudrate=115200, timeout=1, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, debug=False):
        """Initialize the serial connection with given parameters."""
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.parity = parity
        self.stopbits = stopbits
        self.serial_conn = None
        self.debug = debug  # Debug flag to enable additional output

    def connect(self):
        """Connect to the serial port."""
        self.serial_conn = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout,
            parity=self.parity,
            stopbits=self.stopbits
        )
        print(f"Connected to {self.port}")

    def send_command(self, command):
        """Send a command to the Pico and return the response."""
        if not self.serial_conn:
            print("Not connected to the serial port.")
            return

        # Send the command with proper line termination
        self.serial_conn.flush()
        self.serial_conn.write(f"{command}\r".encode())

        # Read the response until ">>>"
        response = self.serial_conn.read_until(b'>>>').decode()  # Using byte string to specify the delimiter

        # Strip leading and trailing whitespace
        response = response.strip()

        # Use regex to find "RESPONSE: [==>message<==]"
        match = re.search(r"RESPONSE:\s?\[\==>(.*?)<==\]", response, re.DOTALL)

        if match:
            # Extract the message within the delimiters
            response_message = match.group(1)
            return response_message
        else:
            # Append the raw response to the error message if debug is enabled
            if self.debug:
                return f"No valid response found or invalid format. Raw response: {response}"
            else:
                return "No valid response found or invalid format."

    def close(self):
        """Close the serial connection."""
        if self.serial_conn:
            self.serial_conn.close()
            print(f"Connection to {self.port} closed.")
