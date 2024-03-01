# Simple Python Client-Server Project

This is a simple client-server project implemented in Python. The project facilitates communication between a client and a server, allowing the client to send commands to the server for execution and receive the output.

## Project Structure

- **client.py**: Client-side script responsible for connecting to the server and sending commands.
- **server.py**: Server-side script responsible for listening to client connections, executing commands, and sending back the output.
- **README.md**: Documentation file providing information about the project, its usage, and setup.

## Usage

1. **Setting Up the Server**:
   - Run `server.py` to start the server.
   - The server will start listening for incoming client connections.

2. **Connecting with the Client**:
   - Execute `client.py` to initiate the client-side interaction.
   - The client will establish a connection with the server.

3. **Sending Commands**:
   - Once the connection is established, you can input commands in the client terminal.
   - Type `exit` to terminate the connection and close the client.

## Requirements

- Python 3.x installed on your system.

## Notes

- By default, the server listens on port 8888. You can modify the port in `server.py` if required.
- This project is intended for educational purposes and may require additional security measures for production use.
- Ensure both the client and server scripts are executed on the same machine for testing purposes.

## Contributing

Contributions to the project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

