contact = {}

while True:
    action = input('Enter add contact, delete contact, check phone number or exit: ').lower()
    if action == 'add contact':
        name = input('Enter name: ').title()
        phone_number = input('Enter phone number: ')
        contact[name] = phone_number
        print(contact)
    elif action == 'delete contact':
        name_delete = input('Enter name of contact: ')
        del contact[name_delete]
        print('Contact is delete!')
        print('contact list:', contact)
    elif action == 'check phone number':
        name_search = input('Enter name of contact: ')
        print('phone number:', contact[name_search])
    elif action == 'exit':
        break
    else:
        print('Error please try again!')
