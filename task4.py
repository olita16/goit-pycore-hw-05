def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."
        except Exception as e:
            return f"An error occurred: {e}"
    return inner

class ContactBook:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, args):
        name, phone = args
        self.contacts[name] = phone
        return "Contact added."

    @input_error
    def show_phone(self, args):
        name = args[0]
        return self.contacts[name]

    @input_error
    def show_all_contacts(self, args):
        if not self.contacts:
            return "No contacts found."
        return '\n'.join([f"{name}: {phone}" for name, phone in self.contacts.items()])

def handle_input(contact_book):
    command = input("Enter a command: ").strip().lower()
    if command == 'add':
        args = input("Enter name and phone: ").split()
        return contact_book.add_contact(args)
    elif command == 'phone':
        name = input("Enter name to get the phone number: ").strip()
        return contact_book.show_phone([name])
    elif command == 'all':
        return contact_book.show_all_contacts([])
    elif command == 'exit':
        return "Goodbye!"
    else:
        return "Unknown command. Try again."

def main():
    contact_book = ContactBook()
    while True:
        result = handle_input(contact_book)
        print(result)
        if result == "Goodbye!":
            break

if __name__ == "__main__":
    main()
