import datetime
import sys

import entry
import log

class Menu:
    DEFAULT_LOG = 'entries.CSV'

    def __init__(self):
        self.options ={"Menu":["mm", self.display_main_menu],
                       "New Entry": ["ne", self.write_entry],
                       "Search Entries": ["se", self.search_entries],
                       "Exit the program": ["e", self.exit_program]}

    def run(self):
        while True:
            self.display_main_menu()
            user_choice = input("Enter an option: ")
            if user_choice in self.options.keys():
                action = self.options.get(user_choice)
                action()
            elif user_choice in [each[0] for each in self.options.values() if user_choice == each[0]]:
                action = [each[1] for each in self.options.values() if user_choice == each[0]]
                action[0]()
            else:
                print("{} is not a valid choice".format(user_choice))


    def display_main_menu(self):
        """The main menu."""
        print("Greetings!  Here are our options.")
        for name, method in self.options.items():
            print("Type {} or {} to access {}.  {}".format(name, method[0], method[1].__name__.replace("_", " "), method[1].__doc__))

    def write_entry(self):
        """Write a single entry to file."""
        print("Please fill out the following to write an entry to file.")
        try:
            title = input("Please enter a title for this entry:")
            start_time = input("Please enter a start time for the tast in the following format {}:"
                               .format(entry.Entry.date_format
                               .replace("%", " ").replace("- ", "-").replace(": ", ":")))
            time_spent = input("Please enter a number of minutes applied to the task:")
            notes = input("Enter details:")
            new_entry = entry.Entry(title, start_time, time_spent, notes)
            log_connection = log.Log(self.DEFAULT_LOG)
            log_connection.write_new_entry(new_entry)
        except Exception as exc:
            print("One or more of your selections were invalid.  Please re-enter.")
            print(exc)
        else:
            print(str(new_entry))
            print("Entry was successful!  Heading back to the main menu.")
            self.display_main_menu()


    def search_entries(self):
        """Search all available entries based on user criterias."""
        pass

    def exit_program(self):
        """Exits the program."""
        print("Have a nice day.")
        sys.exit(0)
