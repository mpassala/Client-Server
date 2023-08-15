import socket

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr((ord(char) - key) % 256)
    return decrypted_message

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address
server_address = ('localhost', 5000)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    while True:
        # Receive the encrypted message from the client
        encrypted_message = client_socket.recv(1024).decode()

        if not encrypted_message:
            break

        # Decrypt the message
        key = 3  # Yes very bad ceaser cipher
        decrypted_message = decrypt(encrypted_message, key)

        # Display the encrypted and decrypted messages
        print("Received encrypted message:", encrypted_message)
        print("Decrypted message:", decrypted_message)

    # Close the client connection
    client_socket.close()
