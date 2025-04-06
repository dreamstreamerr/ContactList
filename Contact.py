from os import remove


class Contact:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
    def __str__(self):
        return f"""\
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Email: {self.email}
        Phone: {self.phone}
        """

number_of_contacts = int(input("How many contacts do you want to create? "))
contact_list=[]
for i in range(number_of_contacts):
    print(f'{Contact.__name__}({i+1})')
    first_name=input('Enter Contacts Fist Name: ')
    last_name=input('Enter Contacts Last Name: ')
    email=input('Enter Contacts Email: ')
    phone=input('Enter Contacts Phone: ')
    contact_list.append(Contact(first_name=first_name, last_name=last_name, email=email,phone=phone))


for contact in contact_list:
    print(contact)

for i in contact_list:
    line=f'{i.first_name} {i.last_name} {i.email} {i.phone}\n'
    print(line)
    with open(f'contacts.txt','a') as file:
        file.write(line)
with open("contacts.txt", "r") as file:
    data = file.read()
    print("Saved Contacts:\n", data)
