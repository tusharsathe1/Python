import json

#Prompt for option
selected_option = input("\n1. Create New Contact" + "\n2. Search Existing Contact" + "\n3. Delete Contact" + "\n4. Exit" + "\n\nEnter the number for your option: ")

#User database
user_database = {}
db_file = open('Contacts.json', 'r')
db_file.seek(0)
user_database = json.load(db_file)
db_file.close()

#Function to create new contact
def new_contact():
    global user_database

    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    phone_number = input("Enter the phone number: ")
    email_addr = input("Enter the email address: ")
    search_name = input("Enter a friendly name for search: ")

    #Add the user input to the database
    user_database[search_name] = {'First Name' : first_name, 'Last Name' : last_name, 'Phone Number' : phone_number, 'Email' : email_addr}

    #Write the entry to the file
    read_file = open('Contacts.json', 'w')
    json.dump(user_database, read_file)

#Function to search existing contact
def existing_contact():
    global user_database

    search_name = input("\nEnter the friendly name of the contact: ")

    if search_name in user_database:
        print("\nFirst Name: " + str(user_database[search_name]['First Name']))
        print("\nLast Name: " + str(user_database[search_name]['Last Name']))
        print("\nPhone Number: " + str(user_database[search_name]['Phone Number']))
        print("\nEmail: " + str(user_database[search_name]['Email']) + "\n")
    else:
        print("\nThe contact doesn't exist\n")

#Function to delete a contact
def delete_contact():
    global user_database

    del_name = input("\nEnter the friendly name of the contact: ")

    #Delete the contact
    del user_database[del_name]

    #Update the file
    read_file = open('Contacts.json', 'w')
    json.dump(user_database, read_file)

#Decision based on user input
if int(selected_option) == 1:
    new_contact()
elif int(selected_option) == 2:
    existing_contact()
elif int(selected_option) == 3:
    delete_contact()
