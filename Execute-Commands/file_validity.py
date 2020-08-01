import os.path
import sys

#Check validity of the file

def file_validity():
        #Prompt user for the path of the file
        ip_file = input("Enter the absolute path of the file containing IP addresses: ")

        #Validate if the file exists
        if os.path.isfile(ip_file) == True:
                print("The entered file exists")
        else:
                print("Please confirm location of the file and try again")
                sys.exit()

        #Open the input file
        input_file = open(ip_file, 'r')
        input_file.seek(0)
        ip_list = input_file.readlines()
        input_file.close()

        #Remove new line characters from the list
        ip_final_list = [item.rstrip() for item in ip_list]

        #Return the list
        return ip_final_list
