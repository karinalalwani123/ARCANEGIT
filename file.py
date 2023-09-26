import os

def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of '{filename}':")
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Content written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_file(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    print("\nOptions:")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Write to a file")
    print("4. Delete a file")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        filename = input("Enter the file name: ")
        create_file(filename)
    elif choice == "2":
        filename = input("Enter the file name to read: ")
        read_file(filename)
    elif choice == "3":
        filename = input("Enter the file name to write to: ")
        content = input("Enter the content to write: ")
        write_file(filename, content)
    elif choice == "4":
        filename = input("Enter the file name to delete: ")
        delete_file(filename)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
