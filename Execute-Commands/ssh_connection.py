import paramiko
import sys
import time
import re
import os.path

#Check whether the user credentials file is present

#Prompt for the path of the user file

cred_file = input("Please enter the complete path of the credentials file: ")

#Check whether the file exists

if os.path.isfile(cred_file) == True:
    print("The file exists")
else:
    print("Please check the path and try again")
    sys.exit()

#Check whether the command file exists

#Prompt for the path of the command file

cmd_file = input("Please enter the complete path of the commands file: ")

#Check whether the file exists

if os.path.isfile(cmd_file) == True:
    print("The file exists")
else:
    print("Please check the path and try again")

#Define SSH Function

def ssh_func(ip):

    global cred_file
    global cmd_file
    global result

    try:
        #Read the user credential file
        cred = open(cred_file, 'r')

        #Move the cursor to the beginning of the file
        cred.seek(0)

        #List the lines
        cred_list = cred.readlines()
        #print(cred_list)

        #Separate the username from the line
        username = cred_list[0].split(",")[0]
        #print(username)

        #Separate the password from the line
        password = cred_list[0].split(",")[1].rstrip("\n")

        #Open SSH connection
        conn = paramiko.SSHClient()

        #Store the unknown SSH Key
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Login to the device
        conn.connect(ip, username = username, password = password)

        #Open the shell to run commands
        session = conn.invoke_shell()

        #Set terminal settings
        session.send('ena\n')
        session.send('terminal length 0\n')
        time.sleep(1)

        #Execute commands from the file
        cmd_read = open(cmd_file, 'r')
        cmd_read.seek(0)
        cmd_list = cmd_read.readlines()

        for cmd in cmd_list:
            session.send(cmd)
            time.sleep(3)

        #Close the credentials file
        cred.close()

        #Close the commands file
        cmd_read.close()

        #Save the output
        output = session.recv(65535)

        #Convert the output from byte to ascii
        output = output.decode('ascii')

        #Check for errors in commands
        if re.search('% Invalid input detected', output):
            print("There was an error in the command provided")
        else:
            print("Commands have been run successfully")

        #Store the output in global a variable
        result = output

    except paramiko.AuthenticationException:
        print("The authentication failed, try again")
    print(output)
    return (output)
