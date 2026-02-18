from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIRequestHandler(BaseHTTPRequestHandler):
    """
    Custom handler for a simple HTTP API.
    """
    def do_GET(self):
        """
        Handles GET requests by routing to specific endpoints.
        """
        # Endpoint: Root /
        # path is a string with everything that comes after /
        if self.path == '/':
            self.send_response(200)
            # Define simple text format
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Send the message in bytes ("b")
            self.wfile.write(b"Hello, this is a simple API!")
        # Endpoint: /data
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            # application/json tells the browser that are structed data
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Convert dictionary to JSON string and then to bytes
            # json.dumps(data) converts the dict in a JSON string
            # encode transforms the str into bytes
            self.wfile.write(json.dumps(data).encode("utf-8"))
        # Endpoint: /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        # Endpoint: /info (Requirement for Expected Output)
        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))
        # Error Handling: 404 Not Found
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIRequestHandler, port=8000):
    """
    Initializes and starts the HTTP server.
    """
    # '': Tells the server to hear every interface in the machine (localhost, private IP, etc)
    # port: Specific channel, 8000
    server_address = ('', port)
    # server_class: It's the constructor blueprint (HTTPServer)
    # hanlder_class: The manual (SimpleAPIRequestHandler)
    # httpd: The object with the server built and ready
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    try:
        # Start an infinite bucle that blocks the terminal
        # The program waits for a do_GET, then answers and waits
        httpd.serve_forever()
    # Detects when the users press "Ctrl + C"
    except KeyboardInterrupt:
        # We close the program, otherwise the port 8000 might be blocked
        httpd.server_close()
        print("\nServer stopped.")


if __name__ == "__main__":
    run()
