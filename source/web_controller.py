import requests
import json

class WebController:
    def __init__(self, base_url, debug=False):
        """
        Initialize the web controller with the base URL of the webserver.
        :param base_url: The base URL of the webserver (e.g., 'http://192.168.1.100:8080').
        :param debug: Enable debug mode for verbose output.
        """
        self.base_url = base_url
        self.debug = debug

    def send_command(self, endpoint, data):
        """
        Send a POST request to the webserver with the given endpoint and JSON data.
        :param endpoint: The specific API endpoint (e.g., 'run_command').
        :param data: The JSON data to send in the POST request.
        :return: The server's response as a JSON object.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            if self.debug:
                print(f"Sending POST request to {url} with data: {json.dumps(data, indent=4)}")
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
            return response.json()  # Parse and return the JSON response
        except requests.RequestException as e:
            if self.debug:
                print(f"Error sending request to {url}: {e}")
            return {"error": str(e)}
