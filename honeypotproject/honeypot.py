import socket
import logging

# Configure logging to capture the events
logging.basicConfig(
    filename="honeypot.log",  # Log will be saved as honeypot.log
    level=logging.INFO,       # Log level set to INFO
    format="%(asctime)s - %(message)s"  # Format for the log entries
)

def fake_login(client_socket, client_address):
    """ Simulates a fake login prompt. """
    client_socket.send("Username: ".encode())  # Send username prompt
    username = receive_full_input(client_socket)  # Get complete username input
    client_socket.send("Password: ".encode())  # Send password prompt
    password = receive_full_input(client_socket)  # Get complete password input
    logging.info(f"Credentials from {client_address}: {username}/{password}")  # Log credentials

def receive_full_input(client_socket):
    """ Helper function to receive unlimited input from the client. """
    data = ""
    while True:
        chunk = client_socket.recv(1024).decode()  # Read in chunks of 1024 bytes
        data += chunk
        if len(chunk) < 1024:  # Break the loop when no more data is available
            break
    return data.strip()

def handle_command(client_socket, client_address, data):
    """ Simulates the handling of commands received from the attacker. """
    if "ls" in data:  # Fake 'ls' output
        logging.info(f"Sending fake 'ls' output to {client_address}")
        client_socket.send("file1.txt file2.txt file3.txt\r\n".encode())
    elif "cat" in data:  # Fake 'cat' output
        logging.info(f"Sending fake 'cat' output to {client_address}")
        client_socket.send("This is a fake /etc/passwd content.\r\n".encode())
    else:
        logging.info(f"Unknown command received: {data}")  # For unrecognized commands

def start_honeypot():
    """ Starts the honeypot server and listens for incoming connections. """
    host = "0.0.0.0"  # Listen on all available network interfaces
    port = 2222  # Mimicking SSH service

    # Create a socket object for the honeypot
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))  # Bind to the specified host and port
    server_socket.listen(5)  # Allow a maximum of 5 pending connections
    print(f"Honeypot running on {host}:{port}")
    logging.info(f"Honeypot listening on {host}:{port}")

    while True:
        # Wait for a client to connect
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        logging.info(f"Connection attempt from {client_address}")

        # Call the fake login function
        fake_login(client_socket, client_address)

        # Send a fake SSH banner to the attacker
        client_socket.send("SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n".encode())

        try:
            # Receive data from the attacker
            data = client_socket.recv(1024).decode()
            if data:
                logging.info(f"Data received from {client_address}: {data}")  # Log the received data
                handle_command(client_socket, client_address, data)  # Handle the command
        except Exception as e:
            logging.error(f"Error: {e}")  # Log any errors
        finally:
            client_socket.close()  # Close the client connection

if __name__ == "__main__":
    try:
        start_honeypot()  # Start the honeypot server
    except KeyboardInterrupt:
        print("\nHoneypot stopped.")  # Handle interruption (Ctrl+C)
        logging.info("Honeypot stopped.")  # Log the stoppage
