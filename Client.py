#Socket allows messages to be sent across 
import socket

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        encrypted_message += chr((ord(char) + key) % 256)
    return encrypted_message

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address
server_address = ('localhost', 5000)

try:
    # Connect to the server
    client_socket.connect(server_address)

    while True:
        # Get the message from the user
        message = input("Enter Message To Send ('q' to quit): ")

        if message.lower() == 'q':
            break

        # Encrypt the message
        key = 3  # Yes, Ceaser cipher is trash, but ssl, rsa, aes would not work
        encrypted_message = encrypt(message, key)

        # Send encrypted message to the server
        client_socket.sendall(encrypted_message.encode())

# Last minute add I looked up. Error handling for connection and socket error
except (ConnectionRefusedError, ConnectionResetError) as e:
    print("Connection error:", e)
except socket.error as e:
    print("Socket error:", e)
finally:
    # Close connection
    client_socket.close()
