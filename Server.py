import socket
import subprocess
# Step One: declare a socket. AF_INET and SOCK_STREAM are standard arguments here
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Step Two: bind the socket to the correct IP_Address and port number.
    # when the Pi is set up, these arguments, seen in bind(), will need to be changed
    # Current values are common for echo servers, seen in class
    s.bind(('127.0.0.1', 56821))

    # Step 3, begin listening for a connection from the client
    # the argument of 0 signifies the "backlog" of connections which can exist.
    # 0 means that if the server is already connected to the client, it will not connect with
    # a second instance of the client. This way, if the arm is already moving it will not
    # continue looping through the arm's code because someone pressed the button 5 times
    print("listening")
    s.listen(0)

    # when listen activates, the accept method is called, and the return value is
    # stored in a pair of variables.
    connection, address = s.accept()

    # with is just python's equivalent to try-finally (not try catch), specifically for connections
    with connection:

        print('Connected by', address)
        # Here, before the infinite loop, would be the place to run the script/subprocess of the arm
        # this can be done simply by importing "subprocess" and adding the line
        # subprocess.call("./a.out")

        while True:
            # this is just some basic example code for an echo server like we saw in class.
            # 1024 is the number of bytes that can be received. this is the highest
            # value within the recommended limit of the documentation
            data = connection.recv(4096)
            # subprocess.call("./a.out")
            ###take commands
            # if there is some crazy problem with the input, it will break the loop
            if not data:
                break
            print("recevied " + str(data))
            connection.sendall(data)
