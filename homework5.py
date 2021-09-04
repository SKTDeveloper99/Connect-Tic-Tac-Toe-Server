
# Tic Tac Toe Client v2.1
# Supported by Python v3.0 or higher


import socket

print("\nWelcome to Tic Tac Toe Client v2.1 written by Khoa tran!")
print("This client is supported by Python v3.0.0 or higher.")

host_ip = "64.183.98.170"
server_port = 3800

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to Tic Tac Toe Server at " + host_ip + ":" + str(server_port) + " ...\n")

try:
    # Establish connection to TCP server
    tcp_client.connect((host_ip, server_port))

    # contains logic for server and client responses
    while True:
        
        # prints server messages until server expects a response
        while True:

            # get server message
            serverOut = tcp_client.recv(1024).decode()
			
			# check for ttt board
            printBoard = False
            if(serverOut[0:1] == "1" or (serverOut[0:1] == "X" and serverOut[0:2] != "X/") or serverOut[0:1] == "O"):
                print(" " + serverOut[0:1] + " | " + serverOut[1:2] + " | " + serverOut[2:3])
                print("---+---+---")
                print(" " + serverOut[3:4] + " | " + serverOut[4:5] + " | " + serverOut[5:6])
                print("---+---+---")
                print(" " + serverOut[6:7] + " | " + serverOut[7:8] + " | " + serverOut[8:9])
                print(serverOut[9:])
                printBoard = True

            # print server message if it has not already been printed
            if(printBoard == False):
                print(serverOut)
		
            # check if server is disconnecting
            if(serverOut.find("isconnect") > -1):
                break

            # check if server is asking for user move
            if(serverOut.find("move?") > -1):
                break

            # check if server is asking for X/O
            if(serverOut.find("X/O?") > -1):
                break

        # follow up break if server is disconnecting
        if(serverOut.find("isconnect") > -1):
            break

        # prompt for user input and send
        message = input(" -> ")
        tcp_client.send(message.encode())

finally:
    tcp_client.close()
    print("Disconnecting from server...")

print("Done!\n")

# end of file