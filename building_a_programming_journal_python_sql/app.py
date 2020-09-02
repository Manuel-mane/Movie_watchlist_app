# importing functions
from database import add_entry, create_table, get_entries

menu = """ Please select one of the following options:
1) Add new entry for today
2) View entries
3) Exit

Your selection:

"""

welcome = "Welcome to the programming diary!"
create_table()

# Creating functions to deal with the entrance and display of the data
def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:  # it is a tuple
            print(f"{entry['date']}\n{entry['content']}\n\n")



print(welcome)

while (user_input := input(menu)) != "3": # new feature of Python 3.8
    # We deal with user input here
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
        
        
    else:
        print("Invalid option, please try again!")

   