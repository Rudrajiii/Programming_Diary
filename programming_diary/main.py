from typing import  Optional
import time
from database import create_table , add_entry,get_entries
menu : str = """ Please Select One Of The Following Option
1) Add New Entry For Today.
2) View Entries.
3) Exit.
Your Selected Option: """
welcome:str = "Welcome To The Programming Diary"
def Prompt_new_entry():
    entry_content = input("What You Have Learned Today?\n")
    entry_date = input("Enter The Date: ")
    add_entry(entry_content,entry_date)
def View_entry(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")
print(welcome)
create_table()
while (user_input := input(menu)) != "3":
    if user_input == "1":
        Prompt_new_entry()
        print("Adding Your Entries...")
        time.sleep(3)
    elif user_input == "2":
        print("Showing Your Entries...")
        time.sleep(3)
        print("-"*10)
        View_entry(get_entries())
        print("-"*10)
    else:
        print("Invalid User Input")
