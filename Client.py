import socket
# the client server is much easier to go through
# tester is just to run this as an echo server in order to
byteStr = bytes(input("please enter a short message\n"), "utf-8")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # here, the client connects to the server application, at the values in that application
    # the server should be running already.
    # run this from a separate terminal for testing
    s.connect(('127.0.0.1', 56821))
    # sends the input. remember the maximum byte size for testing, as this may cause problems during testing
    # all that actually needs to be done here is to send some form of signal,
    # so it may be enough to even further simplify this file by simply using connect
    # and having that connection cause the subprocess to run,
    # as mentioned in the comments of the server file

    s.sendall(byteStr)
    receiver = s.recv(4096).decode("utf-8")
print('echo', repr(str(receiver)))
